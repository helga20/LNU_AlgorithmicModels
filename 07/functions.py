import tkinter as tk
from queue import Queue

# Функція для зафарбовування клітинки при натисканні
def draw_cell(event):
    widgets = event.widget.master.widgets
    row_num = 0
    column_num = 0
    found = False

    # Знаходимо, яку саме клітинку було натиснуто
    for row in widgets:
        for cell in row:
            if cell == event.widget:
                found = True
                break
            column_num += 1
        if found:
            break
        else:
            column_num = 0
            row_num += 1

    # Змінюємо колір клітинки і записуємо зміну у логічне поле
    event.widget.config(bg='#878787')
    event.widget.master.area[row_num][column_num] = 1


# Клас таблиці — прямокутна сітка клітинок
class Table(tk.Frame):
    def __init__(self, parent, rows, columns):
        tk.Frame.__init__(self, parent, background="black")
        self.widgets = []  # список віджетів (Label)
        self.area = []     # логічна матриця значень

        for row in range(rows):
            current_widgets_row = []
            current_fields_row = []
            for column in range(columns):
                label = tk.Label(self, borderwidth=0, width=2)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                label.bind('<Button-1>', draw_cell)
                current_widgets_row.append(label)
                current_fields_row.append(0)

            self.widgets.append(current_widgets_row)
            self.area.append(current_fields_row)

        # Розтягуємо колонки по ширині
        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)

    # Задати текстове значення клітинці
    def set_value(self, row, column, value):
        widget = self.widgets[row][column]
        widget.configure(text=value)

    # Задати колір клітинки
    def set_color(self, row, column, color):
        widget = self.widgets[row][column]
        widget.configure(bg=color)

    # Заповнити клітинки за умовою задачі 1
    def fill_area_task1(self, area):
        self.area = area
        for row in range(len(area)):
            for column in range(len(area[0])):
                if area[row][column] == 1:
                    self.set_color(row, column, '#878787')

    # Заповнити клітинки за умовою задачі 2
    def fill_area_task2(self, area):
        self.area = area
        for row in range(len(area)):
            for column in range(len(area[0])):
                if area[row][column] == -1:
                    self.set_color(row, column, '#878787')  # бар’єри
                else:
                    self.set_value(row, column, area[row][column])  # значення кроків BFS

    # Показати шлях у задачі 2
    def draw_way_task2(self, way):
        for v in way:
            self.set_color(v[0], v[1], '#FFFF00')  # шлях жовтим кольором

    # Позначити старт і фініш
    def mark_start_finish(self, start, finish):
        self.set_color(start[0], start[1], '#228B22')  # зелений — старт
        self.set_color(finish[0], finish[1], '#FF0000')  # червоний — фініш


# Клас, що описує логічну карту поля та реалізує BFS
class Area(object):
    def __init__(self, rows, columns, start, finish, barriers):
        self._rows = rows
        self._columns = columns
        self.start = start
        self.finish = finish
        self._barriers = barriers
        self.__area = None
        self._build()

    def __call__(self, *args, **kwargs):
        self._show()

    def __getitem__(self, item):
        return self.__area[item]

    # Побудова логічної карти
    def _build(self):
        self.__area = [[0 for _ in range(self._columns)] for _ in range(self._rows)]
        for b in self._barriers:
            self[b[0]][b[1]] = -1  # бар’єри
        self[self.start[0]][self.start[1]] = 1  # стартова точка

    # BFS-заповнення поля
    def fill(self):
        q = Queue()
        q.put(self.start)
        while not q.empty():
            index = q.get()

            l = (index[0]-1, index[1])
            r = (index[0]+1, index[1])
            u = (index[0], index[1]-1)
            d = (index[0], index[1]+1)

            if l[0] >= 0 and self[l[0]][l[1]] == 0:
                self[l[0]][l[1]] = self[index[0]][index[1]] + 1
                q.put(l)
            if r[0] < self._rows and self[r[0]][r[1]] == 0:
                self[r[0]][r[1]] = self[index[0]][index[1]] + 1
                q.put(r)
            if u[1] >= 0 and self[u[0]][u[1]] == 0:
                self[u[0]][u[1]] = self[index[0]][index[1]] + 1
                q.put(u)
            if d[1] < self._columns and self[d[0]][d[1]] == 0:
                self[d[0]][d[1]] = self[index[0]][index[1]] + 1
                q.put(d)

    # Відновлення шляху від фінішу до старту
    def get_path(self):
        if self[self.finish[0]][self.finish[1]] == 0 or self[self.finish[0]][self.finish[1]] == -1:
            raise Exception('Path not found')

        path = []
        item = self.finish

        while not path.append(item) and item != self.start:
            l = (item[0]-1, item[1])
            if l[0] >= 0 and self[l[0]][l[1]] == self[item[0]][item[1]] - 1:
                item = l
                continue

            r = (item[0]+1, item[1])
            if r[0] < self._rows and self[r[0]][r[1]] == self[item[0]][item[1]] - 1:
                item = r
                continue

            u = (item[0], item[1]-1)
            if u[1] >= 0 and self[u[0]][u[1]] == self[item[0]][item[1]] - 1:
                item = u
                continue

            d = (item[0], item[1]+1)
            if d[1] < self._columns and self[d[0]][d[1]] == self[item[0]][item[1]] - 1:
                item = d
                continue

        return reversed(path)

    # Повертає логічне поле
    def get_area(self):
        return self.__area
