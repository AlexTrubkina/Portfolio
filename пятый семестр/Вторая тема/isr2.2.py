class Fibonacci():
    def __init__(self, max_num):
        self.check = 0
        self.max_num = max_num
        self.num  = 0
        self.next_num = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.check > self.max_num:
           raise StopIteration

        self.check = self.num + self.next_num

        buff = self.num + self.next_num
        self.num   = self.next_num
        self.next_num  = buff
        
        return self.num
