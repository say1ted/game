class Creature:
    def __init__(self, name, health, attack_min, attack_max, items):
        self.attack_min = attack_min
        self.health = health
        self.attack_max = attack_max
        self.name = name
        self.items = items

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return "Name\t:\t{}\t|\tHealth\t:\t{}\t|\tAttack\t:\t{}-{}".\
            format(self.name, self.health, self.attack_min, self.attack_max)





