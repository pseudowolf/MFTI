class Dragon:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def is_alive(self) -> bool:
        return self.health > 0

    def get_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0

    def talk(self):
        print(self.name, 'health', self.health, 'Hit me!')

    def final_cry(self):
        print(self.name, 'is dead...')


def main():

    enemy_list = [Dragon('Smog'), Dragon('Hidra')]
    finished = False
    while not finished:
        enemy = enemy_list[0]
        enemy.talk()
        damage = int(input())
        enemy.get_damage(damage)
        if not enemy.is_alive():
            enemy.final_cry()
            enemy_list.pop(0)
        if not enemy_list:
            finished = True
    print('You win!')


main()
