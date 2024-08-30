from typing import List

class Tree:
    def __init__(self):
        self.parts = []

    def display(self):
        # generate top of the tree
        print('        _____   ')
        print('       /     \\ ')
        print('      /       \\')

        # display parts
        for part in self.parts:
            part.display()


class TreePart:
    def __init__(self, variant: int):
        """
        - variant (int): this parameter defines the type of the tree part. It can be:
            0: for simple part
            1: for left branch
            2: for right branch
        """
        self.variant = variant

    def display(self):
        if self.option == 0:
            content  = '      |       |'
            content += '      |       |'
            content += '      |       |'
            print(content)

        elif self.option == 1:
            content  = '  0   |       |'
            content += ' 0 0  |       |'
            content += '  ----|       |'
            print(content)

        else:
            content  = '      |       |   0  '
            content += '      |       |  0 0 '
            content += '      |       |----  '
            print(content)