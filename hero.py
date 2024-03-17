class Hero:
    def __init__(self, fighting_fitness, charm, skill):
        self._fighting_fitness = fighting_fitness
        self._charm = charm
        self._skill = skill
        self._sestertii = 0

    @property
    def fighting_fitness(self):
        return self._fighting_fitness
    @fighting_fitness.setter
    def fighting_fitness(self, value):
        self._fighting_fitness = value
    @property
    def charm(self):
        return self._charm
    @charm.setter
    def charm(self, value):
        self._charm = value
    @property
    def skill(self):
        return self._skill
    @skill.setter
    def skill(self, value):
        self._skill = value
    @property
    def sestertii(self):
        return self._sestertii
    @sestertii.setter
    def sestertii(self, value):
        self._sestertii = value
