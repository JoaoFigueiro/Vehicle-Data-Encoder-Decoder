import json
import operator 

class Vehicle:
    def __init__(self, reg_number, year, passenger, mass): 
        self.registration_number = reg_number
        self.year_of_production = year 
        self.passenger = passenger
        self.vehicle_mass = mass

    @property
    def registration_number(self):
        return self._registration_number

    @registration_number.setter
    def registration_number(self, reg_number): 
        if not reg_number: 
            raise ValueError("Registration number must not be empty!")
        self._registration_number = reg_number

    @property
    def year_of_production(self):
        return self._year_of_production

    @year_of_production.setter
    def year_of_production(self, year): 
        try: 
            year = int(year) 
        except: 
            raise ValueError("Year of production must be an integer!")
        self._year_of_production = year

    @property
    def passenger(self):
        return self._passenger

    @passenger.setter
    def passenger(self, passenger): 
        str_values = ['y', 'n']

        if isinstance(passenger, str) and passenger not in str_values:
            raise ValueError("Passenger must be 'n' or 'y'!")
        
        self._passenger = True if passenger in ['y', True] else False   

    @property
    def vehicle_mass(self):
        return self._vehicle_mass

    @vehicle_mass.setter
    def vehicle_mass(self, mass): 
        try: 
            mass = float(mass) 
        except: 
            raise ValueError("Vehicle mass must be an integer or float!")
        self._vehicle_mass = mass

    def to_dict(self):
        return {
            'registration_number': self.registration_number,
            'year_of_production': self.year_of_production,
            'passenger': self.passenger,
            'mass': self.vehicle_mass
        }

def encode_vehicle(vehicle):
    if isinstance(vehicle, Vehicle):
        return vehicle.to_dict()
    else:
        err = vehicle.__class__.__name__ + ' is not JSON serializable'
        raise TypeError(err)

def decode_vehicle(vehicle_dict): 
    return Vehicle( 
        vehicle_dict['registration_number'],
        vehicle_dict['year_of_production'],
        vehicle_dict['passenger'],
        vehicle_dict['mass'],
    )

init_message = """
What can I do for you?
1 - produce a JSON string describing a vehicle
2 - decode a JSON string into vehicle data
"""

print(init_message)
option = 0 

while option not in [1, 2]: 
    option = input("Your option: ")
    option = int(option)

if option == 1: 
    registration_number = input("Registration number: ")
    year_of_production = input("Year of production: ")
    passenger = input("Passenger [y/n]: ")
    vehicle_mass = input("Vehicle mass: ")

    vehicle = Vehicle(
        reg_number=registration_number,
        year=year_of_production,
        passenger=passenger,
        mass=vehicle_mass
    )

    print(f"Resulting json string is: {json.dumps(vehicle, default=encode_vehicle)}")

elif option == 2:
    json_str = input("Enter vehicle JSON string: ")
    vehicle = json.loads(json_str, object_hook=decode_vehicle)
    print(json.dumps(vehicle, default=encode_vehicle))

print("Done")
