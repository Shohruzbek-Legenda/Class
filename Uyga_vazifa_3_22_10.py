import time

class Odam:
    def __init__(self,ism):
        self.ism = ism
    def yugurish(self):
        print(f'{self.ism} siz yugurishni boshladingiz')
    def yiqilish(self):
        time.sleep(5)
        print(f"{self.ism} siz yeqilib tushdingiz! :(")


odam = Odam(input('Ismini kiriting: '))
odam.yugurish()
odam.yiqilish()