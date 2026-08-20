class MiniHeap:
    def __init__(self):
        self.heap = [None]
        self.size = 0
    
    def insert(self, data):
        self.heap.append(data)
        self.size += 1
        self.arrange()

    def show(self):
        for i in self.heap:
            print(i)
    
    def arrange(self):
        current = self.size

        while current // 2:
            parent = current // 2

            if self.heap[current] < self.heap[parent]:
                self.heap[current], self.heap[parent] = self.heap[parent], self.heap[current]
                
                current = parent
            else:
                break

    def delete_a_root(self):
        if self.size == 0:
            return None

        root = self.heap[1]

        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1

        if self.size > 0:
            self.sink_bottom()

        return root

    def sink_bottom(self):
        current = 1

        while True:
            child = self.min_child(current)

            if child is None:
                break

            if self.heap[current] > self.heap[child]:
                self.heap[current], self.heap[child] = (
                    self.heap[child],
                    self.heap[current]
                )
                current = child
            else:
                break

    def min_child(self, current):
        left = current * 2
        right = left + 1

        if left > self.size:
            return None

        if right > self.size:
            return left

        if self.heap[left] < self.heap[right]:
            return left
        else:
            return right
    
    def heapsort():
        print("sin sortear: ")
        heap.show()
        
        sortlist = []

        while self.size > 0:
            sortlist.append(self.delete_a_root())
        
        self.heap = sortlist

        print("sorteado: ")
        for i in sortlist: 
            print(i)
def main():
    heap = MiniHeap()

    heap.insert(5)
    heap.insert(6)
    heap.insert(7)
    heap.insert(321)
    heap.insert(-1)
    heap.insert(3)

main()