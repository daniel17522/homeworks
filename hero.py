class SuperHero:
    people='people'
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.hp = health_points*2
        self.nickname = nickname
        self.superpower = superpower
        self.catchphrase = catchphrase
    def info(self):
        print(f' name: {self.name} catchphrase: {self.catchphrase}')
    def __str__(self):
        return f' nickname: {self.nickname} superpower: {self.superpower} health points: {self.hp}'
    def __len__(self):
        return len(self.catchphrase)
Deadpool = SuperHero(' Wade\n','Deadpool\n', 'regenerating\n', 150, "Well, I May Be Super, But Im not hero" )
Deadpool.info()
print(Deadpool)
print(' длинна коронной фразы:', len(Deadpool), 'символов')