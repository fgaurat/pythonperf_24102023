import sqlite3
from Todo import Todo

class TodoDAO2:

    def __init__(self,db_file) -> None:
        print(f"def __init__(self,{db_file}) -> None")
        self.__db_file = db_file
        
        self.__conn = sqlite3.connect(self.__db_file)

    def save(self,todo:Todo):
        cur = self.__conn.cursor()
        sql_insert = "INSERT INTO todos_tbl(userId,title,completed) VALUES(?,?,?)"
        cur.execute(sql_insert,(todo.userId,todo.title,todo.completed))
        self.__conn.commit()

    def find_all(self):
        cur = self.__conn.cursor()
        sql = "SELECT id,userId,title,completed FROM todos_tbl"
        res = cur.execute(sql)
        
        for data in res.fetchall():
            todo = Todo(*data)
            yield todo        
    
    def __enter__(self):
        print(f"def __enter__(self)")
        
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"def __exit__(self)")
        if self.__conn:
            self.__conn.close()
            self.__conn = None


    def __del__(self):
        print(f"def __del__(self)")
        if self.__conn:
            self.__conn.close()
