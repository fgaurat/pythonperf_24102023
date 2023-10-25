import sqlite3
from Todo import Todo

class TodoDAO:

    def __init__(self,db_file) -> None:
        self.__conn = sqlite3.connect(db_file)

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

    def __del__(self):
        self.__conn.close()