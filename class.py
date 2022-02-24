
# name = "마린"
# hp = 40
# damage = 5

# print("{0} 유닛이 생성 되었습니다 ".format(name))
# print(" 체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 탱크
# tank_name = "탱크"
# tank_hp = 40
# tank_damage = 5

# print("{0} 유닛이 생성 되었습니다 ".format(tank_name))
# print(" 체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군이 공격 합니다. [공격력 {2}]".format(name, location, damage))


# attack(name, "1시", 40)


class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

        print("{0} 유닛이 생성 되었습니다 ".format(self.name))
        print(" 체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))


# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 20, 3)
tank = Unit("탱크", 100, 35)
tank.speedup = True

print("유닛이름: {0}, 공격력: {1} \n".format(tank.name, tank.damage))
if tank.speedup == True:
    print("{0} 는 속업 했습니다.".format(tank.name))
    
