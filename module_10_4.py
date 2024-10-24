import queue
from threading import Thread
import random
from queue import Queue
from time import sleep


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name


    def run(self):
        sleep(random.randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.table = tables

    def guest_arrival(self, *guests):
        g_list = guests[0]
        for j in range(len(g_list)):
            for i in range(len(tables)):
                if tables[i].guest is None:
                    tables[i].guest = g_list[j].name
                    g_list[j].start()
                    print(f'{g_list[j].name} сел(-а) за стол номер {tables[i].number}')
                    break

                if i == len(tables) - 1 and tables[i].guest != g_list[j].name:
                    Queue.put(q, g_list[j])
                    print(g_list[j].name, 'в очереди')

    def discuss_guests(self):
        if Queue.empty(q) is False:
            print('Не пустая')
        if [Guest.is_alive(name) for name in guests] is False:
            print('Ушёл')


q = queue.Queue()
tables = [Table(number) for number in range(1, 6)]
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman', 'Vitoria', 'Nikita', 'Galina',
                'Pavel', 'Ilya', 'Alexandra']
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(guests)
cafe.discuss_guests()
