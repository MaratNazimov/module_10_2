from threading import Thread, Lock
from time import sleep

lock = Lock()

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        quantity = 100
        day = 0
        print(f"{self.name}, на нас напали!")
        while quantity >= 0:
            sleep(1)
            day += 1
            quantity -= self.power
            with lock:
                print(f"{self.name} сражается {day} дней, осталось {quantity} вражеских воинов.")
                if quantity == 0:
                    print(f"{self.name} одержал победу спустя {day} дней(дня)!")
                    break

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
