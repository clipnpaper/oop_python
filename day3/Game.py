class GameObject:
    def __init__(self, name, x=0, y=0):
        self.name = name
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def info(self):
       return f"{self.name} ({self.x}, {self.y})"

class HP:
    def __init__(self, max_hp):
        self.max_hp = max_hp
        self.current = max_hp

    def damage(self, amount):
        self.current -= amount

    def is_alive(self):
        return self.current > 0

class Weapon:
    def __init__(self, name, power):
        self.name = name
        self.power = power

class Skill:
    def __init__(self, name, multiplier):
        self.name = name
        self.multiplier = multiplier

class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

class Character(GameObject):
    def __init__(self, name, x=0, y=0):
        super().__init__(name, x, y)
        self.hp = None
        self.weapon = None
        self.skill = None
        self.armor = None

    def attack(self):
        return self.weapon.power

    def use_skill(self):
        return (int)(self.attack() * self.skill.multiplier)

    def take_damage(self, amount):
        actual_amount = max(amount - self.armor.defense, 0)
        self.hp.damage(actual_amount)
        return actual_amount

    def change_weapon(self, weapon:Weapon):
        self.weapon = weapon


class Monster(GameObject):
    def __init__(self, name, power, x=0, y=0):
        super().__init__(name)
        self.power = power

class Warrior(Character):
    def __init__(self, name, x=0, y=0):
        super().__init__(name, x, y)
        self.hp = HP(150)
        self.weapon = Weapon("롱소드", 20)
        self.skill = Skill("강타", 1.5)
        self.armor = Armor("판금갑옷", 10)

class Wizard(Character):
    def __init__(self, name, x=0, y=0):
        super().__init__(name, x, y)
        self.hp = HP(90)
        self.weapon = Weapon("지팡이", 8)
        self.skill = Skill("파이어볼", 4.0)
        self.armor = Armor("로브", 2)

class Dragon(Monster):
    pass

class Slime(Monster):
    pass


if __name__ == "__main__":
    w = Warrior("아서")
    z = Wizard("멀린")

    print(w.attack(), w.use_skill(), z.use_skill())

    print(w.take_damage(25), w.hp.current)

    print(z.take_damage(25), z.hp.current)
    w.change_weapon(Weapon("전투도끼", 30))

    print(w.attack(), w.use_skill())