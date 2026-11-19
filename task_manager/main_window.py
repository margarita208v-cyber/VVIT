from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QLabel, QLineEdit, QPushButton,
    QListWidget, QListWidgetItem, QMessageBox,
    QVBoxLayout, QHBoxLayout, QComboBox,
)
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Задание 2:
        self.setWindowTitle("Менеджер задач")
        self.resize(500, 400)

        # Задание 12: разделение логики
        self.init_ui()
        self.connect_signals()
        self.update_counter()

    # Задание 3 + 4 + 12
    def init_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        # Виджеты 
        self.label_new = QLabel("Новая задача")

        self.input_task = QLineEdit()
        self.input_task.setPlaceholderText("Название задачи")

        # Задание 13
        self.priority_box = QComboBox()
        self.priority_box.addItems(["Обычный", "Высокий", "Низкий"])

        self.btn_add = QPushButton("Добавить")
        self.btn_delete = QPushButton("Удалить")
        self.btn_clear = QPushButton("Очистить всё")

        # Задание 13
        self.btn_done = QPushButton("Выполнено")

        self.list_tasks = QListWidget()

        # Задание 11
        self.label_counter = QLabel("Количество задач: 0")

        # Задание 13
        self.statusBar().showMessage("Готово")

        #  Компоновка Задание 4 
        top_layout = QHBoxLayout()
        top_layout.addWidget(self.input_task)
        top_layout.addWidget(self.priority_box)
        top_layout.addWidget(self.btn_add)

        # Кнопки действий в другую строку
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.btn_done)
        buttons_layout.addWidget(self.btn_delete)
        buttons_layout.addWidget(self.btn_clear)

        # layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.label_new)
        main_layout.addLayout(top_layout)
        main_layout.addWidget(self.list_tasks)
        main_layout.addLayout(buttons_layout)
        main_layout.addWidget(self.label_counter)

        central.setLayout(main_layout)

    # Задание 12 подключение сигналов 
    def connect_signals(self):
        self.btn_add.clicked.connect(self.add_task)          # Задание 5
        self.input_task.returnPressed.connect(self.add_task) # Задание 7
        self.btn_delete.clicked.connect(self.delete_task)    # Задание 8
        self.btn_clear.clicked.connect(self.clear_tasks)     # Задание 10
        self.btn_done.clicked.connect(self.mark_done)        # Задание 13
        self.list_tasks.itemChanged.connect(self.update_counter)  # счётчик при чекбоксе

    # Задание 5 + 6
    def add_task(self):
        text = self.input_task.text().strip()

        # Задание 6
        if not text:
            QMessageBox.warning(self, "Ошибка", "Введите название задачи")
            return

        priority = self.priority_box.currentText()
        item = QListWidgetItem(f"[{priority}] {text}")

        # Задание 13
        item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
        item.setCheckState(Qt.CheckState.Unchecked)

        self.list_tasks.addItem(item)
        self.input_task.clear()
        self.update_counter()                                # Задание 11
        self.statusBar().showMessage(f"Добавлено: {text}")   # Задание 13

    # Задание 8 + 9 удаление задачи
    def delete_task(self):
        current = self.list_tasks.currentItem()

        # Задание 8
        if current is None:
            QMessageBox.warning(self, "Ошибка", "Выберите задачу для удаления")
            return

        # Задание 9
        answer = QMessageBox.question(
            self, "Подтверждение",
            f"Удалить задачу?\n\n{current.text()}",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )

        if answer == QMessageBox.StandardButton.Yes:
            row = self.list_tasks.row(current)
            self.list_tasks.takeItem(row)
            self.update_counter()                            # Задание 11
            self.statusBar().showMessage("Задача удалена")

    # Задание 10 очистка всего списка
    def clear_tasks(self):
        if self.list_tasks.count() == 0:
            QMessageBox.information(self, "Информация", "Список задач уже пуст")
            return

        answer = QMessageBox.question(
            self, "Подтверждение",
            "Удалить все задачи?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )

        if answer == QMessageBox.StandardButton.Yes:
            self.list_tasks.clear()
            self.update_counter()                            # Задание 11
            self.statusBar().showMessage("Все задачи удалены")

    # Задание 11
    def update_counter(self):
        total = self.list_tasks.count()
        done = sum(
            1 for i in range(total)
            if self.list_tasks.item(i).checkState() == Qt.CheckState.Checked
        )
        # Задание 13
        self.label_counter.setText(
            f"Количество задач: {total} (выполнено: {done})"
        )

        # Задание 13
        self.setWindowTitle(f"Менеджер задач — {total} задач")

    # Задание 13
    def mark_done(self):
        current = self.list_tasks.currentItem()
        if current is None:
            QMessageBox.warning(self, "Ошибка", "Выберите задачу")
            return

        current.setCheckState(Qt.CheckState.Checked) 
        self.statusBar().showMessage("Задача отмечена выполненной")