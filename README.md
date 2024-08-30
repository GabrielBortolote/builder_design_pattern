# Builder

This project implements a use case for a Design Pattern, the Builder. To know more about this pattern you can access [this website](https://refactoring.guru/design-patterns/builder).

## What it is?

The **Builder**  is a creational design pattern that that can be used to create complex objects. If you have an object that has too many attributes consider to use a Builder instead of passing all the attributes as parameters to the constructor.

## Project

Do you remember the lumberjack game?

![game image](/images/game.jpg)

This game was very simple, there is a ruge tree, with branches. The lumberjack can be to the left or to the right of the tree, there are just too buttons, left and right, if the player press left the lumberjack hit the tree with an axe and go to the left, else, if the right button is pressed the same hit is done but lumberjack goes to the right. Every lumberjack's hit decrease the size of the tree, all the remaining parts of the tree goes down one position.

The tree is composed by parts, the parts can be a simple wood:

![simple wood](/images/simple-wood.png)

A left branch:

![left branch](/images/left-branch.png)

Or a right branch:

![right-branch](/images/right-branch.png)

The purpose of the game is to hit the entire tree without letting lumberjack being hit by a branch. So let's build the tree using the Builder Design Pattern. First of all we know that the client code (in this case, the game engine), is going to create the tree at some point, so we need a class tree.

main.py

```python
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

```

tree.py

```python
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
```

Now we need to create the TreeBuilder, with the necessary methods to create a tree:

tree_builder.py

```python
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
```

Now we are going to create the Director, an object that can command a builder to create different trees:

tree_director.py

```python
from tree_builder import TreeBuilder
import random

class TreeDirector:
    def __init__(self, builder: TreeBuilder):
        self.builder = builder

    def build(self, tree_size: int, game_difficulty: int):
        """
        - size (int): defines how many parts will the tree have
        - difficulty (int): a number between 0 and 1 representing the
          percentage of tree parts that is going to have branches. Eg.:
            - difficulty = 0, means that the tree will have no branches
            - difficulty = 1, means that all the tree parts have branches
        """
        # define where the branches are
        number_of_branches = int(tree_size * game_difficulty)
        branches = random.sample(range(0, tree_size), number_of_branches)

        # add all parts
        for i in range(0, tree_size):
            if i in branches:
                if random.choice([True, False]):
                    self.builder.add_left_branch()
                else:
                    self.builder.add_right_branch()
            else:
                self.builder.add_simple()
```

Note that the director receive the parameter *size* that defines how many parts will the tree have and the parameter difficulty, a number between 0 and 1 representing the percentage of tree parts that is going to have branches.

- difficulty = 0, means that the tree will have no branches
- difficulty = 1, means that all the tree parts have branches

The logic about creating branches accordingly with the difficult is all on Director's responsibilities while building the tree is on the Builder responsibilities. The Director doesn't even know what's a Tree. Now let's build create some trees to see the result:

```bash
python main.py 
Building an easy tree
        _____   
       /     \ 
      /       \
      |       |
      |       |
      |       |
      |       |  
      |       |
      |       |
      |       |
      |       |  
      |       |
      |       |
      |       |
      |       |  
      |       |
      |       |
      |       |
      |       |  
      |_______|


Building an medium level tree
        _____   
       /     \ 
      /       \
      |       |
      |       |
      |       |
      |       |  
      |       |      
      |       |   0  
      |       |  0 0 
      |       |----    
      |       |
      |       |
      |       |
      |       |  
      |       |      
      |       |   0  
      |       |  0 0 
      |       |----    
      |       |      
      |       |   0  
      |       |  0 0 
      |       |----    
      |       |
      |       |
      |       |
      |       |  
      |       |
      |       |
      |       |
      |       |  
      |       |
  0   |       |
 0 0  |       |
  ----|       |  
      |       |
      |       |
      |       |
      |       |  
      |       |      
      |       |   0  
      |       |  0 0 
      |       |----    
      |_______|


Building an maximum level tree
        _____   
       /     \ 
      /       \
      |       |      
      |       |   0  
      |       |  0 0 
      |       |----    
      |       |      
      |       |   0  
      |       |  0 0 
      |       |----    
      |       |
  0   |       |
 0 0  |       |
  ----|       |  
      |       |
  0   |       |
 0 0  |       |
  ----|       |  
      |       |
  0   |       |
 0 0  |       |
  ----|       |  
      |       |      
      |       |   0  
      |       |  0 0 
      |       |----    
      |       |      
      |       |   0  
      |       |  0 0 
      |       |----    
      |       |      
      |       |   0  
      |       |  0 0 
      |       |----    
      |       |      
      |       |   0  
      |       |  0 0 
      |       |----    
      |       |      
      |       |   0  
      |       |  0 0 
      |       |----    
      |       |
  0   |       |
 0 0  |       |
  ----|       |  
      |       |
  0   |       |
 0 0  |       |
  ----|       |  
      |       |
  0   |       |
 0 0  |       |
  ----|       |  
      |       |      
      |       |   0  
      |       |  0 0 
      |       |----    
      |       |      
      |       |   0  
      |       |  0 0 
      |       |----    
      |_______|

```

Thanks for reading, feel free to fork this and implement the rest of the game.
