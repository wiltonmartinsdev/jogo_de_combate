import random

class Personage:
    def __init__(self, name, life, level):
        self.__name = name
        self.__life = life
        self.__level = level

    def get_name(self):
        return self.__name
    
    def get_life(self):
        return self.__life
        
    
    def get_level(self):
        return self.__level
    
    def show_details(self):
        return f"Nome: {self.get_name()}\nVida: {self.get_life()}\nNível: {self.get_level()}"
    
    def receive_attack(self, damage):
        self.__life -= damage

        if self.__life < 0:
            self.__life = 0

    def attack(self, target):
        damage = random.randint(self.get_level() * 2, self.get_level() * 4) # Baseado no nível
        target.receive_attack(damage)
        print(f"{self.get_name()} atacou {target.get_name()} e causou {damage} de dano!")

# Classe responsável pela gestão do game.
class Game:
    """ Classe orquestradora do game """

    def __init__(self) -> None:
        self.hero = Hero(name="Herói", life=100, level=5, ability="Super Força")
        self.enemy = Enemy(name="Morcego", life=80, level=5, type="Voador")

    def start_battle(self):
        """ Fazer a gestão da batalha em turnos """
        print("Iniciando Batalha")

        while self.hero.get_life() > 0 and self.enemy.get_life() > 0:
            print("\nDetalhes dos Personagens:\n")
            print(self.hero.show_details())
            print(self.enemy.show_details())

            input("Pressione Enter para atacar...")

            choice = input("Escolha (1 - Ataque Normal, 2 - Ataque Especial): ")

            if choice == "1":
                self.hero.attack(self.enemy)

            elif choice == "2":
                self.hero.special_attack(self.enemy)
            
            else:
                print("Escolha inválida! Tente novamente.")

            if self.hero.get_life() > 0:
                # Inimigo ataca herói.
                self.enemy.attack(self.hero)

        if self.hero.get_life() > 0:
            print("\nParabéns, você venceu a batalha!")
        else:
            print("\nVocê foi derrotado!")
    
class Hero(Personage):
    def __init__(self, name, life, level, ability):
        super().__init__(name, life, level)
        self.__ability = ability

    def get_ability(self):
        return self.__ability
    
    def show_details(self):
        return f"{super().show_details()}\nHabilidade: {self.get_ability()}\n"
    
    def special_attack(self, target):
        damage = random.randint(self.get_level() * 5, self.get_level() * 8) # Dano aumentado
        target.receive_attack(damage)
        print(f"{self.get_name()} usou a habilidade especial, {self.get_ability()}, em {target.get_name()} e causou {damage} de dano!")    
    
class Enemy(Personage):
    def __init__(self, name, life, level, type):
        super().__init__(name, life, level)
        self.__type = type
    
    def get_type(self):
        return self.__type
    
    def show_details(self):
        return f"{super().show_details()}\ntipo: {self.get_type()}\n"

# Instância do game e inicar batalha.  
game = Game()
game.start_battle()

