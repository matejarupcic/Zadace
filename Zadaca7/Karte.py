#imamo karte od keca do kralja s 4 boje
#računalo izvlači jednu kartu i izvukli ste recimo 5 i (1) vi
#kazete visa ili manja,(2) racunalo izvlaci slj kartu,
#(3) radi se uspordba karata te ako ste vi recimo
#rekli visa i racunalo je izvuklo kartu 6 dobijete poruku
#točno, a a ko ste vi rekli niža,  a računalo je izvuklo 
#kartu broj 6, dobijete poruku netočno i zaustavlja se igra.

import random
class Karte:
    def __init__(self):
        self.ranks = ["Kec", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Decko", "Dama", "Kralj"] #[0,1,2,...]
        self.suits = ["Tref", "Srce", "Karo", "Pik"]
        self.deck = []
        value = 1 
        for rank in self.ranks: #ovo rank moze biti i 
            for suit in self.suits:
                self.deck.append ([rank + "iz" + suit + "boja", value])
            value = value + 1
        random.shuffle(self.deck) #mijesanje karata
        self.score = 0
        self.card1 = self.deck.pop(0)

    def display_title_bar(self):
        print ("\t**********************************")
        print ("\t*** Kartaška igra - izvlačenje ***")
        print ("\t**********************************")

    def get_user_choice(self):
        print ("\n[1] Pokreni kartašku igru")
        print ("\n[x] Izlaz")
        return input ("Što želite napraviti?")

    def start_game (self):
        while True:
            print ("Vaš trenutni rezultat je {}".format(self.score))
            print ("\nVaša trenutna karta je {}".format(self.card1[0]))
            while True:
                choice = input ("(v)viša ili (n)niža karta?")
                if choice[0].lower() in ["v", "n"]: #ako je prvo slovo v ili n izlazi iz ove while petlje 
                    break
            
            self.card2 = self.deck.pop(0)
            print("Sljedeća odabrana karta je {}".format(self.card2))
            #vi sad trebate vidjeti je li je korisnik upisao v ili n
            #te ovisno o upisu v ili n usporediti karte i ispisati pogodak
            # te nastaviti, ako je pogodak igra se nastavlja i rezultat pogodenih
            #karata se kumulativno povecava u varijabli score,
            # #a ako nije pogodak izaci iz petlje i zavrsiti igru

            if choice [0].lower () == "v" and self.card2[1] > self.card1[1]:
                print("Točno! Pogodak!")
                self.score = self.score + 1
            elif choice[0].lower ()== "v" and self.card2[1]< self.card1[1]:
                print ("Krivo! Kraj igre. Vaš završni rezultat je {}".format(self.score))
                break
            elif choice[0].lower () == "n" and self.card2[1] < self.card1[1]:
                print ("Točno! Pogodak!")
                self.score = self.score + 1
            elif choice[0].lower() == "n" and self.card2[1] > self.card1[1]:
                print ("Krivo! Kraj igre. Vaš završni rezultat je {}".format(self.score))
                break
            elif choice[0].lower() == "n" and self.card2[1] == self.card1[1]:
                print ("Karte su jednake vrijednosti. Vaš završni rezultat je {}".format(self.score))
                 
            elif choice[0].lower() == "v" and self.card2[1] == self.card1[1]:
                print ("Karte su jednake vrijednosti. Vaš završni rezultat je {}".format(self.score))
                 
            self.card1 = self.card2


            

    def play(self):
        choice = ''
        self.display_title_bar()
        while choice != 'x':
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == '1':
                self.start_game()
            elif choice == 'x':
                print("\n Hvala na igri. Pozdrav!")
            else:
                print ("Hvatanje izuzetaka")

if __name__ == "main ":
    game= Karte ()
    game.play ()


        