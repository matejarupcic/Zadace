class Napaderror (Exception):
    
    def __init__(self, code):
        self.error_message = ''
        self.error_message = '~'*50+'\n'
        self.error_dict = {
            000: 'ERROR-000: Nespecificirana pogreška',
            101: 'ERROR-101: Greška povezana s korisnikovim unosom!',
            102: 'ERROR-102: Greška povezana s neispravnim unosom teksta!',
            103: 'ERROR-103: Greška povezana s neispravnom pretvorbom broja u tekst!'
        }
        try:
            self.error_message += self.error_dict[code] 
        except KeyError:
            self.error_message += self.error_dict[000]
        self.error_message += '\n'

    class Zdravometar(NapadOrkovaerror):
        def __init__(self, msg=''):
            self.error_message = self.znakovi + 'ERROR-101: Problem sa zdravometrom' +'\n'
            print("Opis greške: {}".format(self.error_message))