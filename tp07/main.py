import requests
from Todo import Todo
from TodoDAO import TodoDAO

def main():
    dao = TodoDAO("todos_db.db")

    todos = dao.find_all()
    l = list(todos)
    print(len(l))
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
