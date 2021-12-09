class Pile :
    def __init__(self):
        self.lst = []

    def est_vide(self):
        if self.lst == [] :
            return True
        else:
            return False

    def empiler(self, e):
        self.lst.append(e)
        return self.lst

    def sommet(self):
        if self.est_vide() == True :
            return
        else:
            return self.lst[-1]

    def depiler(self):
        assert(self.lst != []),'erreur'
        self.lst.pop()

    def __str__(self): #__repr__
        self.str = ""
        for i in range(len(self.lst)):
            self.str =   str(self.str) + str('|') + str(self.lst[-1-i]) + str('|') + str('\n')
        if self.est_vide() == True:
            return str('|' + ' ' + '|')
        return str(self.str)

    def __repr__(self):
        self.str = ""
        for i in range(len(self.lst)):
            self.str =   str(self.str) + str('|') + str(self.lst[-1-i]) + str('|') + str('\n')
        return str(self.str)
