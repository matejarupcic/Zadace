# prvo pretvorimo stringove (tekst) u brojeve i rješavanje s modulom, a to znači (igrač_1 - računalo_igrač_2)%5...ostatak 1 ili 2 - Win igrač_1...3, 4 Win računalo_igrač_2..0 neriješeno
# "rock", "Spock", "paper", "lizard", "scissors" pretvoriti u sljedeće brojeve:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random
from KPSError import KPSError
class Kps:
    def __init__(self):
        self.player_input = None
        self.player_number = -1
        self.computer_number = -1
        self.computer_choice_name = None
        
    def broj_u_string(self):
        
        if self.computer_number == 0:
            self.computer_choice_name = "kamen"
        elif self.computer_number == 1:
            self.computer_choice_name = "papir"
        elif self.computer_number == 2:
            self.computer_choice_name = "skare"
        else:
            self.computer_choice_name = None
            raise KPSError(103)
        return self.computer_choice_name
    
       
    def string_u_broj(self):
    
        if self.player_input == "kamen":
            self.player_number = 0
        elif self.player_input == "papir":
            self.player_number = 1
        elif self.player_input == "skare":
            self.player_number = 2

        else:
            self.player_number = -1
            raise KPSError(102)
        return self.player_number

    def play(self):
        """
        Glavna logika.
        Prvo, radi se korisnikov input, zatim pretvara korisnikov input u broj (metoda string_u_broj), utvrđuje pobjednika i
        na kraju pretvara odabrani broj računalo_igrač_2-a u tekst (metoda broj_u_string), odabir pobjednika s ostatkom i ispisuje pobjednika (Winner-a) 
        """
        # unos korisnikovog tekst
        self.player_input = input("Odaberite kamen, papir ili skare ").lower()
        # pretvorba korisnikovog tekst u broj
        self.player_number = self.string_u_broj()
        # racunalo odabire pomocu random metode
        self.computer_number = random.randrange(0,3)
        ostatak = (self.player_number - self.computer_number)%3
        if(self.player_number == -1):
            winner = "Greška"
            raise KPSError(101)
        else:
            if ostatak == 0:
                winner = "Neriješeno"
            elif ostatak == 1 or ostatak == 2:
                winner = "Vi (čovjek) pobjeđujete"
            elif ostatak == 3 or ostatak == 4:
                winner = "Računalo pobjeđuje"
        self.computer_choice_name = self.broj_u_string()
        print("Vi (čovjek) ste odabrali: {}".format(self.player_input.title()))
        print("Računalo je odabralo: {}".format(self.computer_choice_name.title()))
        print(winner)
        
if __name__ == "__main__":
    game = Kps()
    game.play()
        
        
            

        
        
        