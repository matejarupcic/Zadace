import random

class Pogadanjebroja:
    def __init__(self):
        self.player_input = None
        self.player_number = -1
        self.computer_number = -1
        self.computer_choice_name = None
        self.izvlacenje_number = -1
        self.izvlacenje_choice_name = None
    def display_title_bar(self):
        print("\t**********************************")  
        print("\t****** Igra pogađanje broja ******")  
        print("\t**********************************")  

    def get_user_choice(self):
        print("\n[1]Igraj igru.")
        print("[x] Izlaz.")
        return input("Odaberite što želite napraviti? ")

    def start_game(self):
        
        self.player_input = int(input("Odaberite broj 1-200: "))
        
        # racunalo odabire pomocu random metode
        self.computer_number = random.randrange(0,200)
        self.izvlacenje_number = random.randrange(0,200)
        while True:
            if self.player_input == self.computer_choice_name:
                print ('\n\nČestitam pogodili ste broj')
            
            elif self.computer_number == self.izvlacenje_number:
                print ('\nKompjuter je pogodio broj, izgubili ste')
            elif self.player_input > self.izvlacenje_number:
                print ('\n\nČestitam prešli ste broj')
            elif self.computer_number > self.izvlacenje_number:
                print ('\nKompjuter je prešao broj, izgubili ste')
            elif self.player_input == self.computer_number:
                print ('\nNeriješeno')

        print("Vi (čovjek) ste odabrali: {}").format(self.player_input)
        print("Računalo je odabralo: {}").format(self.computer_choice_name.title())
        #print(winner)


    def play(self):
        choice = ''
        self.display_title_bar()
        self.start_game()
        while choice != 'x':
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == '1':
                self.start_game()
            elif choice == 'x':
                print("\nHvala na igranju. Pozdrav!")
              
if __name__ == "__main__":
    game = Pogadanjebroja()
    game.play()
        
        
            

        
        
        