#!/usr/bin/env python
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from table_app import Ui_MainWindow
from TodoDAO2 import TodoDAO2

class TodoApp(QMainWindow, Ui_MainWindow):

    def __init__(self, dao):
        super(TodoApp, self).__init__()
        self.dao = dao
        self.setupUi(self)  # Initialisation de l'interface utilisateur

        # Configuration de la table
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "UserID", "Title", "Completed"])
        self.load_data()

    def load_data(self):
        todos = list(self.dao.find_all())
        self.tableWidget.setRowCount(len(todos))

        for row, todo in enumerate(todos):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(todo.id)))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(str(todo.userId)))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(todo.title))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(str(todo.completed)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dao = TodoDAO2("todos_db.db")
    window = TodoApp(dao)
    window.show()
    sys.exit(app.exec_())
