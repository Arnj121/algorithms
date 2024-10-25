class Queue:

    def __int__(self, values=None):
        if values is None:
            values = []
        self.values=values

    def push(self,value):
        self.values.append(value)
        return True

    def pop(self):
        if len(self.values):
            self.values.pop(0)
            return True
        return False

    def find(self,value):
        try:
            return self.values.index(value)
        except ValueError:
            return False

    def seek(self):
        if len(self.values):
            return self.values[0]
        return False

    def tail(self):
        if len(self.values):
            return self.values[-1]
        return False

    def parse(self):
        return self.values

    def size(self):
        return len(self.values)

class Stack:
    def __int__(self,values=None):
        if values is None:
            values=[]
        self.values=values

    def push(self,value):
        self.values.append(value)
        return True

    def pop(self):
        if len(self.values):
            del self.values[-1]
            return True
        return False

    def seek(self):
        if len(self.values):
            return self.values[-1]
        return False

    def size(self):
        return len(self.values)

    def find(self,value):
        try:
            return self.values.index(value)
        except ValueError:
            return False
