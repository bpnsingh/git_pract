class Pokemon:
    def __init__(self,name,level,type,maximum_health,current_health,KO):
        self.name=name
        self.level=level
        self.type=type
        self.maximum_health=maximum_health
        self.current_health=current_health
        self.is_knocked_out=KO
    def lose_health(self,point):
        self.current_health -= point
        print (f"{self.name} has now {self.current_health}")
    def gain_health(self,point):
        self.current_health+=point
        print(f"{self.name} has now {self.current_health}")
    def knock_out(self):
        if self.current_health == 0:
            print (f"{self.name} is knocked out")
    def revive_pokemon(self):
        print(f"{self.name} is revived")

    def attack(self,other_pokemon):
        
