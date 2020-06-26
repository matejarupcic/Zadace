from random import randrange
from RpslsError import RpslsError

class Rpsls:

    def display_title_bar(self):
        print("\t******************************")  
        print("\t*******Igra Rpsls *********")  
        print("\t******************************")  

    def get_user_choice(self):
        print("\n[1]Igraj igru Rpsls.")
        print("[x] Izlaz.")
        return input("Odaberite što želite napraviti? ")
    def __init__(self):
        self.player_input = None
        self.player_number = -1
        self.computer_number = -1
        self.computer_choice_name = None
    def broj_u_string(self):
         
        if self.computer_number == 0:
            self.computer_choice_name = "rock"
        elif self.computer_number == 1:
            self.computer_choice_name = "Spock"
        elif self.computer_number == 2:
            self.computer_choice_name = "paper"
        elif self.computer_number == 3:
            self.computer_choice_name = "lizard"
        elif self.computer_number == 4:
            self.computer_choice_name = "scissors"
        else:
            self.computer_choice_name = None
            raise RpslsError(103)
        return self.computer_choice_name
    def string_u_broj(self):
        
        if self.player_input == "rock":
            self.player_number = 0
        elif self.player_input == "spock":
            self.player_number = 1
        elif self.player_input == "paper":
            self.player_number = 2
        elif self.player_input == "lizard":
            self.player_number = 3
        elif self.player_input == "scissors":
            self.player_number = 4
        else:
            self.player_number = -1
            raise RpslsError(102)
        return self.player_number

    def start_game(self):
        
        self.player_number = self.string_u_broj()
        
        self.computer_number = random.randrange(0,5)
        ostatak = (self.player_number - self.computer_number)%5 
                 
        while True:
            i=0
            j=0 
            if(self.player_number == -1):
                winner = "Greška"
                raise RpslsError(101)
        else:
            if ostatak == 0:
                winner = "Neriješeno"

            elif ostatak == 1 or ostatak == 2:
                winner = "Vi (čovjek) pobjeđujete"
                i+=1
                print ('\nTrenutni rezultat je igrač ima ',i,'pobjeda, a kompjuter ima',j,'pobjeda\n')
            elif ostatak == 3 or ostatak == 4:
                winner = "Računalo pobjeđuje"
                j+=1
                print ('\nTrenutni rezultat je igrač ima ',i,'pobjeda, a kompjuter ima',j,'pobjeda\n')
            else:
                break
            if i==3 or j==3:
                if i==3:
                    print('\n\nVi ste ukupan pobjetnik!!')
                else:
                    print('\n\nKompjuter je ukupan pobjetnik!!')
                break
        
    def play(self):
        choice = ''
        self.display_title_bar()
        self.start_game()
        while choice != 'x':
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == '1':# u ovoj situaciji choice ima vrijednost '1' što je string (tekst), uspoređuje se s brojem 1
                self.start_game()
            elif choice == 'x':
                print("\nHvala na igranju. Pozdrav!")
            else:
                raise RpslsError(000)
        
if __name__ == '__main__':
    game = Rpsls()
    game.play()