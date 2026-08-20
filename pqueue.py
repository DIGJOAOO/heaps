from heaps import heap

class element:
    def __init__(self, e, i):
        self.element = e
        self.i = i

class pqueue:
    def __init__(self):
        self.heap = heap

    def enqueue(self, element):
        self.heap.insert(element)

    def dequeue(self):
        if self.heap.size == 0:
            return None

        return self.heap.delete_a_root()

    def peek(self):
        if self.heap.size == 0:
            return None

        return self.heap.heap[1]

    def show(self):
        self.heap.show()

perro = element("perro", 0)
gato = element("gato", 2)
pez = element("pez", 5)
caballo = element("caballo", 1)

Queue = pqueue()

Queue.enqueue(perro)
Queue.enqueue(gato)
Queue.enqueue(pez)
Queue.enqueue(caballo)