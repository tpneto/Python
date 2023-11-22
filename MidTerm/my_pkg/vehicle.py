
class Vehicle():
    
    vin_number = ''
        
    #A
    def __init__(self, make, model, price, year):
        self.make = make
        self.model = model
        self.price = price
        self.year = year
     
    #B    
    def show_info(self):
        print()
        print('Vehicle information:\n')
        print(f'Make: {self.make}')
        print(f'Model: {self.model}')
        print(f'Price: $ {self.price}')
        print(f'Year: {self.year}')
        print(f'VIN Number: {self.get_vehicle_vin_number()}')
        print()
        
    #C
    
    def get_vehicle_vin_number(self):
        Vehicle.vin_number = f'{self.make[0]}_{self.model[0]}_{self.year}'
        return Vehicle.vin_number
    

        