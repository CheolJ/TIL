class Marine:
    
    def __init__(self):
        self.health = 40
        self.attack_pow = 5
    
    
    def attack(self, unit):
        unit.health -= self.attack_pow
        if unit.health <= 0:
            unit.health = 0

class Marine2(Marine):
    
    def __init__(self):
        super(Marine, self).__init__()
        self.max_health = 40


marine = Marine2()
