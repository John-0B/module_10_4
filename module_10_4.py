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
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for guest in guests[0]:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{table.guest.name} сел(-а) за стол номер {table.number}')
                    break
                if all([table.guest for table in self.tables]):
                    self.queue.put(guest)
                    print(guest.name, 'в очереди')
                    break

    def discuss_guests(self):
        while not self.queue.empty() or any([table.guest for table in self.tables]):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла) и '
                          f'Стол номер {table.number} свободен')
                    table.guest = None
                if not self.queue.empty() and table.guest is None:
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.start()


tables = [Table(number) for number in range(1, 6)]
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman', 'Vitoria', 'Nikita', 'Galina',
                'Pavel', 'Ilya', 'Alexandra']
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(guests)
cafe.discuss_guests()
