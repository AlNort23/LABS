class MindMapComposite:
    def __init__(self, name, shape):
        self.name = name
        self.shape = shape
        self.children = []

    def add(self, child):
        self.children.append(child)

    def display(self, indent=0):
        spaces = " " * indent
        print(f"{spaces}{self.name}")
        for child in self.children:
            child.display(indent + 2)