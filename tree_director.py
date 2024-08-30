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