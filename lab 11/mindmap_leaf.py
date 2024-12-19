class MindMapLeaf:
    def __init__(self, name, shape):
        self.name = name
        self.shape = shape

    def display(self, indent=0):
        spaces = " " * indent
        print(f"{spaces}{self.name}")