
#A
cars=[{'make':'Toyota','model':'Corolla' ,'price':35500,'year':2018},
{'make':'BMW','model':'X3', 'price':62000,'year':2020},
{'make':'Ford', 'model':'Edge','price':42100,'year':2017},
{'make':'Lexus', 'price':53000,'year':2021,'model':'PhEV'},
{'make':'Hyundai', 'price':33100,'year':2019,'model':'Elantra'},
{'make':'Land Rover', 'price':86000,'year':2022,'model':'Range Rover'},
{'make':'Hyundai', 'price':33100,'year':2019,'model':'Sonata'}
]

soted_cars = list()

#B
def sort_by_price():
    sorted_cars = sorted(cars, key = lambda car: car['price'])
    print(sorted_cars)
    
    
car_same_year = list()
#C #D
def find_car_made_by_same_year(cars:str, year:int):
    car_same_year = filter(lambda car: car['year'] == year, cars)
    return car_same_year

#E
print(">>E<<__________________________________________________________")
print()
print(f'Cars from 2017: {list(find_car_made_by_same_year(cars, 2017))}')
print()
print(f'Cars from 2019: {list(find_car_made_by_same_year(cars, 2019))}')
