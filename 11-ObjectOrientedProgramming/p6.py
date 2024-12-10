import time
class Phone():
    def __init__(self,brand, model, year):
        self.brand = brand 
        self.model = model
        self.year = year
    
    def printDetails(self):
        print('Trapphone specifications:')
        print(f'Brand: {self.brand}')
        print(f'Model: {self.model}')
        print(f'Year of production: {self.year}')       

    def overheat(self):
        reaktor = [25,65,123,256,541]
        print("-"*30)
        print(f'Uwaga telefon sie przegrzewa!!!!!!!!')
        for i in range(5):
            print(f"Stopien reaktora wynosi {reaktor[i]}°C")
            time.sleep(0.7)
        print("BOOOM"*1231)

    def chargeBattery(self,battery):
        self.battery = battery
        print("-"*30)
        print("Twoja bateria wynosi aktualnie 0%")
        print(f'Chcesz naladować baterie do {self.battery}')
        print("Rozpoczynam ladowanie...")
        time.sleep(2)
        for i in range(self.battery):
            print(f'Twoja bateria wynosi: {i}')
            i+=1
            print('Ładowanie')
            time.sleep(0.2)
           

def main():

    phone1 = Phone("Samsung","M23","2018")
    phone1.printDetails()
    phone1.overheat()
    phone1.chargeBattery(100)


if __name__ =="__main__":
    main()
