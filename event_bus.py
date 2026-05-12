import queue

class MessageBus:
    def __init__(self):
        self.queue = queue.Queue()

    def publish(self, event):
        self.queue.put(event)

    def consume(self):
        return self.queue.get()