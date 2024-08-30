"""This is the client code"""

from tree_builder import TreeBuilder
from tree_director import TreeDirector

if __name__ == '__main__':
    builder: TreeBuilder = TreeBuilder()
    director: TreeDirector = TreeDirector(builder)

    # build a 4 sized tree with no difficulty
    print("Building an easy tree")
    director.build(4, 0)
    builder.result().display()
    builder.reset()

    # build a 10 sized tree with medium difficulty
    print("Building an medium level tree")
    director.build(10, 0.5)
    builder.result().display()
    builder.reset()

    # build a 100 sized tree with maximum difficulty
    print("Building an maximum level tree")
    director.build(15, 1)
    builder.result().display()
    builder.reset()
