import random
from rocket import Rocket
from tank import Tank
class brodovi(Rocket):
    # tank simulira ratni tenk na polju, ali zapravo koristi sve metode rakete
    # pa ga možemo zvati simulacija rakete
    def __init__(self, x=0, y=0, route = 0):
        super().__init__(x, y)
        self.route = route
    
    def display_title_bar(self):
        # prikazujemo glavni naslov igre korisniku
        print("\t************************************")
        print("\t** Igra - Borba brodova i tenkova **")
        print("\t************************************")
    
    def get_user_choice(self):
        # pokazujemo korisniku meni i pitamo ga što želi napraviti te vracamo aplikaciji njegov odgovor
        print("\n[1] Pokreni borbu tenkova.")
        print("\n[2] Pokreni borbu brodova.")
        print("[x] Izlaz.")
        
        return input("Odaberite što želite napraviti u igri?")
    
    def fight1(self):
        # kreiram nekoliko tenkova i raketa s pozicijama slučajnog odabira (biblioteka random)
        # tenkovi imaju random broj odrađenih/napravljenih ruta na ratnom polju
        brodNum = int(input("Unesite broj brodova na ratnom polju:")) # upisao broj 5
        brod = []
        rockets = []
        for x in range(0,brodNum): # for petlja se vrti od 0 do 5
            x = random.randint(0,100)
            y = random.randint(1,100)
            self.route = random.randint(0,10)
            brod.append(brodovi(x,y,self.route))
        
        for x in range(0, brodNum): # for petlja se vrti od 0 do 5
            x = random.randint(0, 100)
            y = random.randint(1,100)
            rockets.append(Rocket(x, y))
        
        # prikazivanje/ispis napravljene rute svakog tenka u listi na ratnom polju
        for index, brod in enumerate(brodovi):
            print("Brod {} je napravio {} rutu/e".format(index+1, brod.route))
        
        print("\n")
        yourBrod = int(input("Od {} tenkova, vaš tenk je pod brojem:".format(brodNum)))
        
        chosenBrod = brod[yourBrod-1]
        # prikazivanje/ispis udaljenosti vašeg tenka ostalih tenkova
        for index, brod in enumerate(brodovi):
            distance = chosenBrod.get_distance(brod)
            print("Vaš tenk je udaljen {} kilometara od tenka broj {}.".format(distance, index+1))
        
        print("\n")
        # prikazivanje/ispis udaljenosti vašeg tenka od raketa u listi raketa
        for index, rocket in enumerate(rockets):
            distance = chosenBrod.get_distance(rocket)
            print("Vaš brod je udaljen {} kilometara od rakete broj {}.".format(distance, index+1))
        
    def play(self):
        choice = ''
        self.display_title_bar()
        while choice != 'x':
            choice = self.get_user_choice()
            # na temelju korisnikova odabira izvršavamo programsku logiku naše igrice ovisno o tome
            #što je korisnik odabrao
            self.display_title_bar()
            if choice == '1':
                self.fight()
            if choice == '2':
                self.fight1()
            elif choice == 'x':
                print("\nHvala na igri i poštenoj borbi :) . Pozdrav.")
            else:
                print("\nGreška.\n")
    
if __name__ == "__main__":
    game = brodovi()
    game.play() 
        
        
        
    