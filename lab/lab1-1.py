class FIFO:
    def __init__(self):
        self.queue = []
    def input(self, item):
        self.queue.append(item)
        self.queue.pop(0)
    def output(self):
        return self.queue

fifo = FIFO()
fifo.input("kek")
print(fifo.output())
fifo.input("kek2")
print(fifo.output())