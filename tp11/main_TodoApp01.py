#!/usr/bin/env python
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from TodoDAO2 import TodoDAO2

class TodoApp(QMainWindow):

    def __init__(self, dao):
        super(TodoApp, self).__init__()
        self.dao = dao

        # Initialisation de la fenêtre
        self.setWindowTitle("Liste des Todos")
        self.setGeometry(300, 100, 600, 400)

        # Création du widget central
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout(self.central_widget)

        # Création de la table
        self.table_widget = QTableWidget()
        layout.addWidget(self.table_widget)
        
        # Configuration de la table
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(["ID", "UserID", "Title", "Completed"])
        self.load_data()

    def load_data(self):
        todos = list(self.dao.find_all())
        self.table_widget.setRowCount(len(todos))

        for row, todo in enumerate(todos):
            self.table_widget.setItem(row, 0, QTableWidgetItem(str(todo.id)))
            self.table_widget.setItem(row, 1, QTableWidgetItem(str(todo.userId)))
            self.table_widget.setItem(row, 2, QTableWidgetItem(todo.title))
            self.table_widget.setItem(row, 3, QTableWidgetItem(str(todo.completed)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dao = TodoDAO2('todos_db.db')
    window = TodoApp(dao)
    window.show()
    sys.exit(app.exec())
