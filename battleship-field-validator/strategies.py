from abc import ABC, abstractmethod
from collections import deque


class Stack(list):
    @property
    def empty(self) -> bool:
        return not self
    
    def push(self, item):
        self.append(item)

class BFSStrategy(ABC):

    container: None

    @abstractmethod
    def put(self, value):...

    @abstractmethod
    def get(self):...

    def __len__(self):
        return(len(self.container))
    
    def __repr__(self):
        return repr(self.container)

class Lifo(BFSStrategy):

    def __init__(self) -> None:
        super().__init__()
        self.container = Stack()
    
    def put(self, value):
        self.container.push(value)

    def get(self):
        return self.container.pop()

class Fifo(BFSStrategy):

    def __init__(self) -> None:
        super().__init__()
        self.container = deque()
    
    def put(self, value):
        self.container.appendleft(value)

    def get(self):
        return self.container.pop()
    