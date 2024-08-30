"""This is the client code"""

from 

if __name__ == '__main__':
    builder: TreeBuilder = TreeBuilder()
    director: TreeDirector = TreeDirector(builder)

    # build a 4 sized tree with no difficulty
    director.build(4, 0)
    builder.result.display()

    # build a 10 sized tree with medium difficulty
    director.build(10, 0.5)
    builder.result.display()

    # build a 100 sized tree with maximum difficulty
    director.build(10, 1)
    builder.result.display()
