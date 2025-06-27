class Player:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position
    def __str__(self):
        return f"{self.name}, {self.age} лет, {self.position}"

class Team:
    def __init__(self, name, coach):
        self.name = name
        self.coach = coach
        self.players = []
    def add(self, player):
        self.players.append(player)
    def remove(self, player_name):
        self.players = [p for p in self.players if p.name != player_name]
    def show(self):
        print(f"Команда: {self.name}, тренер: {self.coach}")
        for player in self.players:
            print(f"- {player}")

# Пример использования
if __name__ == "__main__":
    # Создаем игроков
    p1 = Player("Иванов", 25, "нападающий")
    p2 = Player("Петров", 30, "полузащитник")
    p3 = Player("Сидоров", 28, "защитник")

    # Создаем команды
    red = Team("Красные", "Краснов")
    blue = Team("Синие", "Синёв")

    # Добавляем игроков
    red.add(p1)
    red.add(p2)
    blue.add(p3)

    # Показываем состав
    red.show()
    blue.show()

    # Удаляем игрока
    red.remove("Петров")
    red.show()