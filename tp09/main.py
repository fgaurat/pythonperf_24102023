from TodoDAO import TodoDAO
from TodoDAO2 import TodoDAO2
from pprint import pprint


def main():
    dao = TodoDAO2("./tp09/todos_db.db")

    pprint(next(dao.find_all()))

    print("before context")
    with TodoDAO2("./tp09/todos_db.db") as dao2:
        print("context")
        pprint(next(dao2.find_all()))
    print("after context")

if __name__ == '__main__':
    main()
