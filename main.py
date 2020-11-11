""" Vince's Vehicles:

This system allows the user to rent different types of vehicles
and manage inventory.

"""

import sys
from vehicles import Car, Boat, Plane
from rentals import RentalLog, RentVehicle
from inventory import VehicleInventory
from flask import Flask, render_template
app = Flask(__name__)

class Menu:
    """ A Class used to represent a Menu

    ...

    Attributes
    ----------
    ans : str
        a string to hold user choice from menu options
    vehicle_choice : str
        a string to hold the choice of vehicle
    car_colour : str
        a string to hold car colour
    car_weight : int
        a string to hold car weight in kilograms
    car_brand : str
        a string to hold a car brand i.e. Ford, Tesla etc.
    new_car : obj
        holds an object instance of a Car
    new_plane : obj
        holds an object instance of a Plane
    new_boat : obj
        holds an object instance of a Boat
    vehicle_to_remove_from_inventory : int
        an integer to hold a vehicle to remove from inventory
    index_of_vehicle_to_remove_from_inventory : int
        an integer to hold the index of the vehicle to remove from inventory

    Methods
    -------
    print_main_menu()
        Prints the main menu
    handle_input()
        Gets menu choice from user
    """

    def print_main_menu(self):
        """Print the main menu of the application."""

        print("""
            1.Add a Vehicle to Inventory
            2.Remove a Vehicle from Inventory
            3.View all Vehicles in Inventory
            4.View Rental Log
            5.Rent a Vehicle
            6.Exit/Quit
            """)

    def handle_input(self):
        """Get the user choice from the main menu"""

        self.ans = input("What would you like to do? ")

        # Enter a Vehicle
        if self.ans == "1":
            vehicle_choice = input("Enter vehicle type, choose from:\n"
                                   "1: Car\n"
                                   "2: Plane\n"
                                   "3: Boat\n"
                                   "\nChoice: ")

            # Car
            if vehicle_choice == "1":
                print('\nEnter Car details:\n')
                car_colour = input("Car Colour: ")
                car_weight = int(input("Car Weight: "))
                car_brand = input("Brand: ")

                new_car = Car(car_colour,
                              car_weight,
                              car_brand)

                # str_new_car = str(new_car).replace('\n', " ")

                VehicleInventory.ALL_VEHICLES.append(new_car)

                main_menu()

            # Plane
            elif vehicle_choice == "2":
                print('\nEnter Plane details:\n')
                plane_colour = input("Plane Colour: ")
                plane_weight = int(input("Plane Weight: "))
                plane_brand = input("Brand: ")

                new_plane = Plane(plane_colour,
                                  plane_weight,
                                  plane_brand)

                # str_new_plane = str(new_plane).replace('\n', " ")

                VehicleInventory.ALL_VEHICLES.append(new_plane)

                main_menu()

            # Boat
            elif vehicle_choice == "3":
                print('\nEnter Boat details:\n')
                boat_colour = input("Boat Colour: ")
                boat_weight = int(input("Boat Weight: "))
                boat_brand = input("Boat Brand: ")
                boat_motor_type = input("Motor Type: ")

                new_boat = Boat(boat_colour,
                                boat_weight,
                                boat_brand,
                                boat_motor_type)

                # str_new_boat = str(new_boat).replace('\n', " ")

                VehicleInventory.ALL_VEHICLES.append(new_boat)

                main_menu()

        # Remove a Vehicle
        elif self.ans == "2":
            vehicle_to_remove_from_inventory \
                = int(input('Vehicle number to be removed: '))
            index_of_vehicle_to_remove_from_inventory \
                = vehicle_to_remove_from_inventory - 1
            del VehicleInventory \
                .ALL_VEHICLES[index_of_vehicle_to_remove_from_inventory]
            main_menu()

        # Print all Vehicles
        elif self.ans == "3":
            print('\n')
            print("All vehicles in inventory...\n")
            for (i, item) in enumerate(VehicleInventory.ALL_VEHICLES, start=1):
                print(i, item)
            main_menu()

        # Current rentals
        elif self.ans == "4":
            print('\n')
            print('Currently rented vehicles...\n')
            for (i, item) in enumerate(RentalLog.CURRENT_RENTALS, start=1):
                print(i, item)
            main_menu()

        # Rent a Vehicle
        elif self.ans == "5":
            print('\n')
            print("All vehicles available to rent: \n")
            for (i, item) in enumerate(VehicleInventory.ALL_VEHICLES, start=1):
                print(i, item)
            vehicle_number_to_rent = int(input(
                '\nWhich vehicle number do you want to rent: '))
            vehicle_index = vehicle_number_to_rent - 1
            RentVehicle(vehicle_index)
            main_menu()

        # Exit system
        elif self.ans == "6":
            sys.exit()

        # Handle other inputs
        elif self.ans != "":
            print("\n Not Valid Choice Try again")
            main_menu()


def main_app():
    """Creates a Menu() object and calls appropriate methods"""
    menu = Menu()
    menu.print_main_menu()
    menu.handle_input()


if __name__ == "__main__":
    app.run(debug=True)
