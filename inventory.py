"""Vehicle Inventory
"""


class VehicleInventory:  # pylint: disable=too-few-public-methods
    """Holds a list of all vehicles"""
    ALL_VEHICLES = []

    def __init__(self, new_vehicle):

        VehicleInventory.ALL_VEHICLES.append(new_vehicle)


