from flask import Flask, render_template, request, redirect
app = Flask(__name__)


from vehicles import Car, Boat, Plane
from rentals import RentalLog, RentVehicle
from inventory import VehicleInventory


@app.route('/healthcheck')
def health_check():
    return 'We are running!'


@app.route('/')
def main():
    return render_template('index.html', vehicle_inventory=VehicleInventory \
                                            .ALL_VEHICLES, \
                                         rental_log=RentalLog
                                            .CURRENT_RENTALS)
                                        

@app.route("/add_vehicle_to_inventory", methods=["GET", "POST"])
def add_vehicle_to_inventory():
    
    if request.method == "POST":

        req = request.form

        print(req)

        vehicle_type = req.get("vehicle_type").title()
        vehicle_colour = req.get("colour")
        vehicle_weight = req.get("weight")
        vehicle_brand = req.get("brand")
        vehicle_motor_type = req.get("motor_type")

        if vehicle_type.title() == 'Car':
            new_car = Car(vehicle_colour,
                        vehicle_weight,
                        vehicle_brand)
        
            print(new_car)

            VehicleInventory.ALL_VEHICLES.append(new_car)
        
        if vehicle_type.title() == 'Boat':
            new_boat = Boat(vehicle_colour,
                        vehicle_weight,
                        vehicle_brand,
                        vehicle_motor_type)
        
            print(new_boat)

            VehicleInventory.ALL_VEHICLES.append(new_boat)

        
        if vehicle_type.title() == 'Plane':
            new_plane = Plane(vehicle_colour,
                              vehicle_weight,
                              vehicle_brand)
        
            print(new_plane)

            VehicleInventory.ALL_VEHICLES.append(new_plane)

 
        return redirect('/')

    return render_template("index.html")


@app.route("/remove_vehicle_from_inventory", methods=["GET", "POST"])
def remove_vehicle_to_inventory():

    if request.method == "POST":

        req = request.form

        vehicle_number = req.get("vehicle_number") # E.g. VV1

        for (i, item) in enumerate(VehicleInventory.ALL_VEHICLES, start=1):
            if item.vehicle_number == vehicle_number:
                VehicleInventory.ALL_VEHICLES.remove(item)

        return redirect('/')


@app.route("/rent_vehicle", methods=["GET", "POST"])
def rent_vehicle():

    if request.method == "POST":
        
        req = request.form

        vehicle_number = req.get("rent_a_vehicle") # E.g. VV1
        
        print(vehicle_number)

        for (i, item) in enumerate(VehicleInventory.ALL_VEHICLES, start=1):
            if item.vehicle_number == vehicle_number:
                RentVehicle(int(i) -1)

        return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)