class Odam:
    def __init__(self, ism):
        self.ism = ism
        self.kuy = 0
    def kuylash(self):
        self.kuy = 1
        if self.kuy == 1:
            print(f'{self.ism} kuyladi.')
        else:
            print(f'{self.ism} kulamadi.')

class Odam2:
    def __init__(self, ism):
        self.ism = ism
        self.e = 0
    def eshitish(self, odam):
        self.e = 1
        if odam.kuy == 1:
            print(f'{self.ism} eshitdi.')
        else:
            print(f'{self.ism} eshitilmadi.')
    def gapirish(self, odam):
        if odam.kuy == 1 and self.e == 1:
            print('Yahshi, faqat sal balandroq kuylashiz kerak.')


odam1 = Odam(input('1-odamni ismini kiriting: '))
odam2 = Odam2(input('2-odamni ismini kiriting: '))

odam1.kuylash()
odam2.eshitish(odam1)
odam2.gapirish(odam1)

