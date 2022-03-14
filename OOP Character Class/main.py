# Task 1
class Properties:
    def __init__(self, name, phrase1, phrase2):
        self.name = name
        self.phrase1 = phrase1
        self.phrase2 = phrase2
        self.level = 0
    def speak(self, phraseNum):
        if phraseNum ==1:
           print (self.phrase1)
        elif phraseNum ==2:
           print(self.phrase2)

    def setLevel(self, newLevel):
        self.level = newLevel


character1 = Properties("Kung Fu Panda", "Skadooosh", "You've been blinded by pure awesomness")
character2 = Properties("Spiderman", "My Spider-Sense is tingling", "Your friendly neighbourhood spiderman")
#Task 2
character1.speak(1)
character1.setLevel(2)
character2.speak(2)
