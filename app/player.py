class PLAYER:
    def __init__(self, uid, name):
        self.uid = uid
        self.name = name

    def uid(self):
        return self.uid

    def name(self):
        return self.name

    def __str__(self):
        return "I am Player"
