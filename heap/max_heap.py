class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        #bubble up:
        # if inserted left child
        if len(self.storage) % 2 == 0:
            # replace with head if it's bigger than head 
            if self.storage[len(self.storage) - 1] > self.storage[(len(self.storage) - 1) / 2 - 1]:
                self.storage[len(self.storage) - 1], self.storage[(len(self.storage) - 1) / 2 - 1] = self.storage[(len(self.storage) - 1) / 2 - 1], self.storage[len(self.storage) - 1]
        # if inserted right child:
        if len(self.storage) % 2 == 1:
            if self.storage[len(self.storage) - 1] > self.storage[((len(self.storage) - 1) - 1) / 2 - 1]:
                self.storage[len(self.storage) - 1], self.storage[((len(self.storage) - 1) - 1)/ 2 - 1] = self.storage[(len(self.storage) - 1) / 2 - 1], self.storage[len(self.storage) - 1]

    def delete(self):
        pass

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        if len(self.storage) % 2 == 0:
            # replace with head if it's bigger than head 
            if self.storage[len(self.storage) - 1] > self.storage[(len(self.storage) - 1) / 2 - 1]:
                self.storage[len(self.storage) - 1], self.storage[(len(self.storage) - 1) / 2 - 1] = self.storage[(len(self.storage) - 1) / 2 - 1], self.storage[len(self.storage) - 1]
        # if inserted right child:
        if len(self.storage) % 2 == 1:
            if self.storage[len(self.storage) - 1] > self.storage[((len(self.storage) - 1) - 1) / 2 - 1]:
                self.storage[len(self.storage) - 1], self.storage[((len(self.storage) - 1) - 1)/ 2 - 1] = self.storage[(len(self.storage) - 1) / 2 - 1], self.storage[len(self.storage) - 1]
    def _sift_down(self, index):
        pass


