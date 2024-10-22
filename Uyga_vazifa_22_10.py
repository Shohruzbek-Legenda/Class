class Odam:
    def __init__(self,ism):
        self.ism = ism
    def salomlashish(self):
        print(f'Salom {self.ism}')

odam = Odam(input())
odam.salomlashish()