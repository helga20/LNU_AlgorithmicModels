import tkinter as tk
from queue import Queue
from functions import Area, Table

#<--------читання матриці з файлу---------> 
def file_reading(file_path):
    area = []
    f = open(file_path, "r")
    for x in f:
        # Перетворюємо кожен рядок файлу в список цілих чисел
        area.append(list(int(i) for i in x.strip()))
    return area
#<!--------читання матриці з файлу--------->

#<-----отримання координат бар’єрів (значення 1)----->
def get_barriers(area):
    barriers = []
    for i in range(len(area)):
        for j in range(len(area[0])):
            if area[i][j] == 1:
                barriers.append((i, j))  # додаємо координати бар’єра
    return barriers
#<!-----отримання координат бар’єрів (значення 1)----->

#<-------що робити після натискання кнопки "Ок"------->
def ok_click():
    matrix = file_reading("task1.txt")  # зчитуємо матрицю з файлу
    rows = len(matrix)
    columns = len(matrix[0])
    barriers = get_barriers(matrix)  # знаходимо всі бар’єри

    # Зчитуємо координати старту з поля вводу
    startArr = startEntry.get().split(',')
    start = (int(startArr[0]), int(startArr[1]))

    # Зчитуємо координати фінішу з поля вводу
    finishArr = finishEntry.get().split(',')
    finish = (int(finishArr[0]), int(finishArr[1]))

    # Створюємо логічне поле та запускаємо BFS
    area = Area(rows=rows, columns=columns, start=start, finish=finish, barriers=barriers)
    area.fill()
    new_matrix = area.get_area()
    path = area.get_path()

    # Візуалізуємо таблицю
    table = Table(window, rows, columns)
    table.fill_area_task2(new_matrix)
    table.draw_way_task2(path)
    table.mark_start_finish(start, finish)
    table.pack(side=tk.LEFT, padx=20)
#<!-------що робити після натискання кнопки "Ок"------->

#<---------головне вікно-------> 
if __name__ == '__main__':
    window = tk.Tk()
    window.geometry('300x200')  # розміри вікна

    # Поле для вводу координат старту
    startLabel = tk.Label(window, text='Start:')
    startLabel.pack()
    startEntry = tk.Entry(window, width=20)
    startEntry.pack()

    # Поле для вводу координат фінішу
    finishLabel = tk.Label(window, text='Finish:')
    finishLabel.pack()
    finishEntry = tk.Entry(window, width=20)
    finishEntry.pack()

    # Кнопка запуску алгоритму
    okButton = tk.Button(window, text='Ok', command=ok_click)
    okButton.pack()

    window.mainloop()  # запускаємо цикл обробки подій
#<!---------головне вікно------->
