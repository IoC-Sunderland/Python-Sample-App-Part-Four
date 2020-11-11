from inventory import VehicleInventory

class RentalLog: 
   
    CURRENT_RENTALS = []


class RentVehicle: 

    def __init__(self, vehicle):
        vehicle = VehicleInventory.ALL_VEHICLES[vehicle]
        VehicleInventory.ALL_VEHICLES.remove(vehicle)
        RentalLog.CURRENT_RENTALS.append(vehicle)


class Rentee(): 
    """ A Rentee Class """
    def __init__(self):
        pass


class RentalRates(): 
    """ A Rental_Rates """
    def __init__(self):
        pass
