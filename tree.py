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
        for i, part in enumerate(self.parts):
            part.display(i)

        # generate the grass
        print('      |_______|\n\n')


class TreePart:
    def __init__(self, variant: int):
        """
        - variant (int): this parameter defines the type of the tree part. It can be:
            0: for simple part
            1: for left branch
            2: for right branch
        """
        self.variant = variant

    def display(self, i):
        if self.variant == 0:
            buffer  = '      |       |\n'
            buffer += '      |       |\n'
            buffer += '      |       |\n'
            buffer += '      |       |  '
            print(buffer)

        elif self.variant == 1:
            buffer  = '      |       |\n'
            buffer += '  0   |       |\n'
            buffer += ' 0 0  |       |\n'
            buffer += '  ----|       |  '
            print(buffer)

        else:
            buffer  = '      |       |      \n'
            buffer += '      |       |   0  \n'
            buffer += '      |       |  0 0 \n'
            buffer += '      |       |----    '
            print(buffer)