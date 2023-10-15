import click
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin 
from sqlalchemy import orm
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.sqlite'

db = SQLAlchemy()
db.init_app(app)

class User(db.Model, UserMixin): 
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150))
    password = db.Column(db.String(150))
    todos = db.relationship('Todo', backref='user', lazy=True)
    lists = db.relationship('List', backref='user', lazy=True)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    complete = db.Column(db.Boolean, default=False)
    description = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    lists = db.relationship('List', secondary='todo_list', back_populates='todos')

    def populate_lists(self, list_ids):
        lists = []
        for id in list_ids:
            if id > 0: lists.append(db.session.get(List, id))
        self.lists = lists

class List(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    todos = db.relationship(Todo, secondary='todo_list', back_populates='lists')
    complete = False
    
    @orm.reconstructor
    def check_complete(self):
        self.complete = all([todo.complete for todo in self.todos])

todo_list = db.Table(
    'todo_list',
    db.Column('todo_id', db.Integer, db.ForeignKey('todo.id'), primary_key=True),
    db.Column('list_id', db.Integer, db.ForeignKey('list.id'), primary_key=True)
)

with app.app_context():
    db.create_all()

@click.command('init-db')
def init():  # (1.)
    with app.app_context():
        db.drop_all()
        db.create_all()
    click.echo('Database has been initialized.')

app.cli.add_command(init)  # (2.)