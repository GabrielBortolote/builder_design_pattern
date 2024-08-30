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
    
```

tree.py

```python

```

Now we need to create the TreeBuilder, with the necessary methods to create a tree:

```python

```

Now we are going to create the Director, an object that can command a builder to create different trees:

```python

```

Note that the director receive the parameter *size* that defines how many parts will the tree have and the parameter difficulty, a number between 0 and 1 representing the percentage tree parts that is going to have branches.

- difficulty = 0, means that the tree will have no branches
- difficulty = 1, means that all the tree parts have branches

Now let's build create some trees to see the result:

```bash

```

Thanks for reading, feel free to fork this and implement the rest of the game.
