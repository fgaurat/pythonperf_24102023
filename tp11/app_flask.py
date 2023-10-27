from flask import Flask,render_template
from TodoDAO2 import TodoDAO2

app = Flask(__name__)

# flask --app app_flask run --debug

@app.route("/hello")
def hello_world():
    return "<p>Bonjour, World!</p>"



@app.route("/old")
def index_old():


    dao = TodoDAO2("todos_db.db")
    todos = dao.find_all()

    html = ""
    for todo in todos:
        row = f"""
<tr>
    <td>{todo.id}</td>
    <td>{todo.userId}</td>
    <td>{todo.title}</td>
    <td>{todo.completed}</td>
</tr>"""
        html+=row
    html = f"<table>{html}</table>"
    return html


@app.route("/")
def index():
    #controller
    dao = TodoDAO2("todos_db.db")
    todos = list(dao.find_all())

    return render_template('todos.html',list_of_todos=todos)
