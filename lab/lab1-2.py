class LIFO:
    def __init__(self):
        self.queue = []
    def input(self, item):
        self.queue.append(item)
        if len(self.queue) > 1:
            self.queue.pop(0)
        else:
            return None
    def output(self):
        return self.queue

lifo = LIFO()
lifo.input("kek")
print(lifo.output())
lifo.input("kek2")
print(lifo.__repr__())