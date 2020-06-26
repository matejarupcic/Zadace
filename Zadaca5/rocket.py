import math
class Rocket():
    #Klasa raketa radi simulaciju kretanja rakete tenka u igri,
    # kao fizička simulacija na polju kad tenk ispali raketu
    def __init__(self, x=0, y=0):
        # svaka raketa ima svoje x i y pozicije
        self.x = x
        self.y = y
    
    def get_distance(self, other_rocket):
        # računa udaljenost od vaše rakete do druge rakete
        # vraća vrijednost udaljenosti
        distance = math.sqrt((self.x-other_rocket.x)**2+(self.y-other_rocket.y)**2)
        return distance