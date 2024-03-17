class Enemy:
    def __init__(self, fighting_fitness):
        self._fighting_fitness = fighting_fitness

    @property
    def fighting_fitness(self):
        return self._fighting_fitness
    @fighting_fitness.setter
    def fighting_fitness(self, value):
        self._fighting_fitness = value