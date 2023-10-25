# Contents of this repository

You are on the **`sqlalchemy`** branch of this repository. It contains example code from the "[Relational databases with Flask-SQLAlchemy](https://hwrberlin.github.io/fswd/13-sqlalchemy.html)" session.

## Steps to execute the example code

**Step 1:** set up and activate a [Python Virtual Environment](https://hwrberlin.github.io/fswd/01-python-vscode.html#32-use-the-python-virtual-environment-as-default-for-this-workspace).

**Step 2:** install the required Python packages from the terminal with the command `pip install -r requirements.txt`:

```shell
(venv) C:\Users\me\projects\webapp> pip install -r requirements.txt
```

> I created the file `📄requirements.txt` with this command: `pip freeze > requirements.txt`

**Step 3:** initialize the app's SQLite database via `flask init-db`:

```shell
(venv) PS C:\Users\me\projects\webapp> flask init-db
Database has been initialized.
```

**Step 4:** start the web server via `flask run --reload`:

```shell
(venv) PS C:\Users\me\projects\webapp> flask run --reload
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
```