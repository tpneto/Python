
from vehicle import Vehicle

cars=[{'make':'Toyota','model':'Corolla' ,'price':35500,'year':2018},
{'make':'BMW','model':'X3', 'price':62000,'year':2020},
{'make':'Ford', 'model':'Edge','price':42100,'year':2017},
{'make':'Lexus', 'price':53000,'year':2021,'model':'PhEV'},
{'make':'Hyundai', 'price':33100,'year':2019,'model':'Elantra'},
{'make':'Land Rover', 'price':86000,'year':2022,'model':'Range Rover'},
{'make':'Hyundai', 'price':33100,'year':2019,'model':'Sonata'}
]

#2.1
obj_vehicles_list = list()

for c in cars:
    vehicle = Vehicle(c['make'], c['model'], c['price'], c['year'])
    obj_vehicles_list.append(vehicle)

#2.2
for vehicle in obj_vehicles_list:
    vehicle.show_info()
    
