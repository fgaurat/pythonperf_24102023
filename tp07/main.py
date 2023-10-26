import requests
from Todo import Todo
from TodoDAO import TodoDAO
from pprint import pprint


def get_completed_todos(stream):
    for todo in stream:
        if todo.completed:
            yield todo 

def main():
    dao = TodoDAO("todos_db.db")

    todos = dao.find_all()
    # dao.find_all() | get_completed_todos
    completed_todos = list(get_completed_todos(todos))
    print(len(completed_todos))
    # for completed_todo in get_completed_todos(todos):
    #     print(completed_todo)
    
    # l = list(todos)
    # pprint(l)
    # print(len(l))
    # print(l[0].completed)
    # todo_0 = next(todos)
    # print(todo_0)
    # todo_1 = next(todos)
    # print(todo_1)
    # for todo in todos:
    #     print(todo)

def main_write():
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    data = response.json()
    dao = TodoDAO("todos_db.db")
    for t in data:
        todo = Todo(**t)
        print(todo)
        dao.save(todo)


if __name__ == '__main__':
    main()
