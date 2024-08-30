from tree import Tree, TreePart

class TreeBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self.tree = Tree()

    def add_simple(self) -> None:
        part = TreePart(0)
        self.tree.parts.append(part)

    def add_left_branch(self) -> None:
        part = TreePart(1)
        self.tree.parts.append(part)

    def add_right_branch(self) -> None:
        part = TreePart(2)
        self.tree.parts.append(part)

    def result(self) -> Tree:
        return self.tree
