class Character:
    def __init__(self,name,hp,level):
        self.name = name
        self.hp = hp
        self.level = level

class NPC(Character):
    def __init__(self,name,hp,level):
        super().__init__(name,hp,level)
    
    def speak(self):
        return f"{self.name} says: 'I heard monsters running around last night!'"
        #  return "{0} says: 'I heard monsters running around last night!'".format(self.name) - old format for Udemy

villager = NPC("Bob", 100, 12)
villager.speak()  # "I heard there were monsters running around last night!".

print(villager.speak())