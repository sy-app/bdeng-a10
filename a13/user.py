class User:
    def __init__(self, i, bought_items):
        self.id = i
        self.bought_items = bought_items
        self.similarity = None
        self.sim_label = None
