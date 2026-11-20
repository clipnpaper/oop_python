class GameObject:
    def __init__(self, name):
        self.name = name

class HP:
    def __init__(self, max_hp):
        self.max_hp = max_hp
        self.current = max_hp

    def damage(self, amount):
        self.current = max(self.current - amount, 0)

    def heal_full(self):
        self.current = self.max_hp

    def is_alive(self):
        return self.current > 0

class Element:
    def __init__(self, name):
        self.name = name

    def multiplier(self, target):
        dic = {"불" : "풀", "풀" : "물", "물" : "불"}
        if self.name == target.element.name:
            return 1.0
        elif dic[self.name] == target.element.name:
            return 2.0
        return 0.5

class Level:
    def __init__(self):
        self.level = 1
        self.exp = 0

    def need(self):
        return self.level * 100

    def gain(self, amount):
        total_exp = amount + self.exp
        up_level = 0
        while self.need() < total_exp:
            total_exp -= self.need()
            self.level += 1
            up_level += 1
        self.exp = total_exp
        return up_level

class Item:
    def __init__(self, name):
        self.name = name

class Inventory:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def add(self, item: Item):
        if len(self.items) > self.capacity:
            return False
        self.items.append(item)
        return True

    def take(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                return item
        return None

class Weapon(Item):
    def __init__(self, name, power, element: Element):
        super().__init__(name)
        self.power = power
        self.enhance = 0
        self.element = element

    def upgrade(self):
        self.power += 5
        self.enhance += 1

    def __str__(self):
        return f"+{self.enhance} {self.name}[{self.element.name}]" if self.enhance >= 1 else f"{self.name}[{self.element.name}]"

class Monster(GameObject):
    def __init__(self, name, hp:HP, element, exp_reward, drop = None):
        super().__init__(name)
        self.hp = hp
        self.element = element
        self.exp_reward = exp_reward
        self.drop = drop

class Character(GameObject):
    def __init__(self, name, hp:HP, weapon:Weapon):
        super().__init__(name)
        self.hp = hp
        self.weapon = weapon
        self.level = Level()
        self.inventory = Inventory(5)

    def attack(self, target: Monster):
        battle_log = [f"{self.name}의 {self.weapon} 공격!"]
        
        mul = self.weapon.element.multiplier(target)
        damage_amount = (int)(self.weapon.power * mul)
        target.hp.damage(damage_amount)
        battle_log.append(f"{target.name}에게 {damage_amount} 피해 (x{mul})")

        if not target.hp.is_alive():

            battle_log.append(f"{target.name} 처치! EXP +{target.exp_reward}")
            up_level = self.level.gain(target.exp_reward)

            if up_level:
                self.hp.max_hp += 20 * up_level
                self.hp.heal_full()
                battle_log.append(f"레벨 업! Lv.{self.level.level} (최대 HP {self.hp.max_hp})")

            if target.drop and self.inventory.add(target.drop):
                battle_log.append(f"'{target.drop.name}' 획득!")
        return battle_log

    def equip(self, name):
        temp_weapon = self.inventory.take(name)
        if self.inventory.add(self.weapon):
            self.weapon = temp_weapon
            return True
        return False 

    def upgrade_weapon(self):
        if self.inventory.take("강화석"):
            self.weapon.upgrade()
            return True
        return False

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, HP(150), Weapon("화염 검", 30, Element("불"))) 

class Slime(Monster):
    def __init__(self):
        super().__init__("슬라임", HP(40), Element("풀"), 60, Weapon("물의 창", 25, Element("물")))

class Golem(Monster):
    def __init__(self):
        super().__init__("골렘", HP(120),Element("풀"), 90, Item("강화석"))

class Dragon(Monster):
    def __init__(self):
        super().__init__("보스", HP(300), Element("불"), 500)

if __name__ == "__main__":
    hero = Warrior("아서")

    # 1) 슬라임 사냥
    for line in hero.attack(Slime()):
        print(line)
    print([i.name for i in hero.inventory.items])
    print("---")

    # 2) 골렘 사냥 (쓰러질 때까지 공격)
    golem = Golem()
    while golem.hp.is_alive():
        for line in hero.attack(golem):
            print(line)
    print("---")

    # 3) 보스전 준비: 무기 교체 + 강화
    print(hero.equip("물의 창"), hero.weapon, [i.name for i in hero.inventory.items])
    print(hero.upgrade_weapon(), hero.weapon, hero.weapon.power)
    print("---")

    # 4) 보스전
    boss = Dragon()
    turn = 0
    while boss.hp.is_alive():
        turn += 1
        hero.attack(boss)
    print(f"{turn}턴 만에 보스 처치! Lv.{hero.level.level}, EXP {hero.level.exp}")