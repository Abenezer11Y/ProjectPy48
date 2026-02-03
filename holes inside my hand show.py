class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity
    
    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare()
        maintenance_charge = base_fare * 0.10
        final_fare = base_fare + maintenance_charge
        print(final_fare)

capaciy_input = int(input("Enter the amount of seats the bus will have: "))
bus = Bus(capaciy_input)
total_fare = bus.fare()