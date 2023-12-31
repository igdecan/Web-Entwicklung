from flask import Flask, render_template, redirect, url_for, request, abort, flash
from flask_bootstrap import Bootstrap5
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import forms
from flask_login import LoginManager, current_user, login_required

app = Flask(__name__)
api = Api(app)

app.config.from_mapping(
    SECRET_KEY = 'secret_key_just_for_dev_environment',
    BOOTSTRAP_BOOTSWATCH_THEME = 'pulse'
)

from auth import auth
app.register_blueprint(auth, url_prefix='/')

from db import db, User, Todo, List

bootstrap = Bootstrap5(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/index')
@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('todos'))
    else:
        return render_template('home.html')

@app.route('/todos/', methods=['GET', 'POST'])
@login_required
def todos():
    form = forms.CreateTodoForm()
    if request.method == 'GET':
        todos = Todo.query.filter_by(user_id=current_user.id).order_by(Todo.id).all()  # !!
        return render_template('todos.html', todos=todos, form=form)
    else:  # request.method == 'POST'
        if form.validate():
            todo = Todo(description=form.description.data, user_id=current_user.id)  # !!
            db.session.add(todo)  # !!
            db.session.commit()  # !!
            flash('Todo has been created.', 'success')
        else:
            flash('No todo creation: validation error.', 'warning')
        return redirect(url_for('todos'))

@app.route('/todos/<int:id>', methods=['GET', 'POST'])
def todo(id):
    todo = db.session.get(Todo, id)  # !!
    form = forms.TodoForm(obj=todo)  # (2.)  # !!
    if request.method == 'GET':
        if todo:
            if todo.lists: form.list_id.data = todo.lists[0].id  # (3.)  # !!
            choices = db.session.execute(db.select(List).order_by(List.name)).scalars()  # !!
            form.list_id.choices = [(0, 'List?')] + [(c.id, c.name) for c in choices]  # !!
            return render_template('todo.html', form=form)
        else:
            abort(404)
    else:  # request.method == 'POST'
        if form.method.data == 'PATCH':
            if form.validate():
                form.populate_obj(todo)  # (4.)
                todo.populate_lists([form.list_id.data])  # (5.)  # !!
                todo.user_id = current_user.id
                db.session.add(todo)  # !!
                db.session.commit()  # !!
                flash('Todo has been updated.', 'success')
            else:
                flash('No todo update: validation error.', 'warning')
            return redirect(url_for('todo', id=id))
        elif form.method.data == 'DELETE':
            db.session.delete(todo)  # !!
            db.session.commit()  # !!
            flash('Todo has been deleted.', 'success')
            return redirect(url_for('todos'), 303)
        else:
            flash('Nothing happened.', 'info')
            return redirect(url_for('todo', id=id))

@app.route('/lists/', methods=['GET', 'POST'])
@login_required
def lists():
    form = forms.CreateListForm()
    if request.method == 'GET':
        lists = List.query.filter_by(user_id=current_user.id).order_by(List.name).all()  # (6.)  # !!
        return render_template('lists.html', lists=lists, form=form)
    else:
        if form.validate():
            list = List(name=form.name.data, user_id=current_user.id)
            db.session.add(list)
            db.session.commit()
            flash('List has been created.', 'success')
        else:
            flash('No list creation: validation error.', 'warning')
        return redirect(url_for('lists'))

@app.route('/lists/<int:id>')
def list(id):
    list = db.session.get(List, id)  # !!
    if list is not None:
        return render_template('list.html', list=list)
    else:
        return redirect(url_for('lists'))

@app.errorhandler(404)
def http_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def http_internal_server_error(e):
    return render_template('500.html'), 500

@app.get('/faq/<css>')
@app.get('/faq/', defaults={'css': 'default'})
def faq(css):
    return render_template('faq.html', css=css)

@app.get('/ex/<int:id>')
@app.get('/ex/', defaults={'id':1})
def ex(id):
    if id == 1:
        return render_template('ex1.html')
    elif id == 2:
        return render_template('ex2.html')
    else:
        abort(404)

todo_post_args = reqparse.RequestParser()
todo_post_args.add_argument("description", type=str, help="Description of the ToDo", required=True)
todo_post_args.add_argument("user_id", type=int, help="User_ID of the ToDo", required=True)

todo_patch_args = reqparse.RequestParser()
todo_patch_args.add_argument('complete', type=bool, help='ToDo completed or not')
todo_patch_args.add_argument('description', type=str, help='Description of the ToDo')
todo_patch_args.add_argument("user_id", type=int, help='User_ID of the ToDo')

resource_fields = {
    'id': fields.Integer, 
    'complete': fields.Boolean, 
    'description': fields.String, 
    'user_id': fields.Integer 
}

class AllTodos(Resource):
    @marshal_with(resource_fields)
    def get(self):
        # Retrieve all ToDo items from the database
        todos = Todo.query.all()
        return todos

api.add_resource(AllTodos, '/api/todos')

class SpecificTodo(Resource):
    @marshal_with(resource_fields)
    def get(self, todo_id):
        # Retrieve the ToDo with the given ID
        todo = Todo.query.get(todo_id)
        if not todo:
            abort(404, message="Todo not found")
        return todo
    
    @marshal_with(resource_fields)
    def post(self, todo_id):
        args = todo_post_args.parse_args()
        result = Todo.query.filter_by(id=todo_id).first()
        if result:
            abort(409, message='Todo id taken')

        todo = Todo(id=todo_id, description=args['description'], user_id=args['user_id'])
        db.session.add(todo)
        db.session.commit()
        return todo, 201
    
    @marshal_with(resource_fields)
    def patch(self, todo_id):
        args = todo_patch_args.parse_args()
        result = Todo.query.filter_by(id=todo_id).first()
        if not result:
            abort(404, message='Todo doesnt exist, connot patch')

        if args['complete'] is not None:
            result.complete = args['complete']
        if args['description'] is not None:
            result.description = args['description']
        if args['user_id'] is not None:
            result.user_id = args['user_id']

        db.session.commit()
        return result

    def delete(self, todo_id):
        todo = Todo.query.get(todo_id)
        if not todo:
            abort(404, message="Todo not found")
        db.session.delete(todo)
        db.session.commit()
        return '', 204
    
api.add_resource(SpecificTodo, '/api/todo/<int:todo_id>')