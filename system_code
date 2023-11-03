class Vehicle:
    def __init__(self, name, mileage_limit, driver_name):
        self.name = name
        self.mileage_limit = mileage_limit
        self.driver_name = driver_name
        self.mileage = 0
        self.service_count = 0
        self.error_count = 0
        self.repair_history = []
        self.total_repair_cost = 0

    def run(self, distance):
        self.mileage += distance
        if self.mileage >= self.mileage_limit:
            self.service_count += 1
            self.mileage = 0
            print(f"{self.name} has been serviced.")
    
    def add_error(self, error_description):
        self.error_count += 1
        self.repair_history.append(error_description)

    def add_repair_cost(self, cost):
        self.total_repair_cost += cost

    def get_monthly_report(self):
        remaining_mileage = self.mileage_limit - self.mileage
        report = f"{self.name}: \n"
        report += f"Driver: {self.driver_name}\n"
        report += f"Total mileage: {self.mileage}\n"
        report += f"Remaining mileage to service: {remaining_mileage}\n"
        report += f"Service count: {self.service_count}\n"
        report += f"Error count: {self.error_count}\n"
        if self.error_count > 0:
            report += f"Errors:\n"
            for error in self.repair_history:
                report += f"  - {error}\n"
        report += f"Total repair cost: {self.total_repair_cost}\n"
        return report

class Bus(Vehicle):
    def __init__(self, name, driver_name, mileage_limit=5000):
        Vehicle.__init__(self, name, mileage_limit, driver_name)

class Lorry(Vehicle):
    def __init__(self, name, driver_name, mileage_limit=10000):
        Vehicle.__init__(self, name, mileage_limit, driver_name)

class FleetManagementSystem:
    def __init__(self):
        self.vehicles = []
        self.best_vehicle = None
        self.min_error_count = float('inf')

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def run_fleet(self, distance):
        for vehicle in self.vehicles:
            vehicle.run(distance)

    def calculate_reliability(self):
        for vehicle in self.vehicles:
            if vehicle.error_count < self.min_error_count:
                self.min_error_count = vehicle.error_count
                self.best_vehicle = vehicle

    def calculate_monthly_spending(self):
        total_spending = sum(vehicle.total_repair_cost for vehicle in self.vehicles)
        return total_spending

# Create a fleet with individual vehicle names and driver names
fleet_manager = FleetManagementSystem()

# Create and customize 10 bus instances
bus1 = Bus("City Express", "John Doe")
bus1.service_count = 5
bus1.add_error("Engine trouble")
bus1.add_repair_cost(1000)
bus1.mileage = 3000

bus2 = Bus("Metro Shuttle", "Jane Smith")
bus2.service_count = 3
bus2.mileage = 1000

bus3 = Bus("Sunrise Transport", "Mike Johnson")
bus3.service_count = 4
bus3.add_error("Transmission issue")
bus3.add_repair_cost(500)
bus3.mileage = 2000

bus4 = Bus("Sunset Coaches", "Emily Davis")
bus4.service_count = 2
bus4.add_error("Tire puncture")
bus4.add_repair_cost(200)
bus4.mileage = 4000

bus5 = Bus("Morning Star", "Robert Brown")
bus5.service_count = 1
bus5.add_error("Fuel leak")
bus5.add_repair_cost(300)
bus5.mileage = 1500

bus6 = Bus("City Voyager", "Olivia Wilson")
bus6.service_count = 6
bus6.mileage = 2500

bus7 = Bus("Urban Express", "Michael Lee")
bus7.service_count = 3
bus7.add_error("Brake issue")
bus7.add_repair_cost(450)
bus7.mileage = 3500

bus8 = Bus("Metro Express", "Sophia Johnson")
bus8.service_count = 5
bus8.add_error("Engine trouble")
bus8.add_repair_cost(750)
bus8.mileage = 4200

bus9 = Bus("Sunrise Shuttle", "William Davis")
bus9.service_count = 2
bus9.mileage = 3000

bus10 = Bus("Sunrise Voyager", "Ella Martinez")
bus10.service_count = 4
bus10.add_error("Electrical problem")
bus10.add_repair_cost(600)
bus10.mileage = 4800

# Add all 10 buses to the fleet
fleet_manager.add_vehicle(bus1)
fleet_manager.add_vehicle(bus2)
fleet_manager.add_vehicle(bus3)
fleet_manager.add_vehicle(bus4)
fleet_manager.add_vehicle(bus5)
fleet_manager.add_vehicle(bus6)
fleet_manager.add_vehicle(bus7)
fleet_manager.add_vehicle(bus8)
fleet_manager.add_vehicle(bus9)
fleet_manager.add_vehicle(bus10)

# Simulate running the fleet for 2000 miles
fleet_manager.run_fleet(2000)

# Calculate vehicle reliability
fleet_manager.calculate_reliability()

# Calculate overall monthly spending
total_monthly_spending = fleet_manager.calculate_monthly_spending()

# Print monthly reports for each vehicle
for vehicle in fleet_manager.vehicles:
    print(vehicle.get_monthly_report())

 # Print the most reliable vehicle
if fleet_manager.best_vehicle:
    print(f"The best vehicle with the fewest errors is {fleet_manager.best_vehicle.name}")

# Sort the vehicles by reliability (ascending order)
sorted_vehicles = sorted(fleet_manager.vehicles, key=lambda vehicle: vehicle.error_count)

# Print vehicles in order of reliability
print("\nVehicles ordered by reliability (best to least):")
for vehicle in sorted_vehicles:
    print(f"{vehicle.name}: Error Count - {vehicle.error_count}, Total Repair Cost - KSH{vehicle.total_repair_cost}")

# Print overall monthly spending
print(f"Overall monthly spending: KSH{total_monthly_spending}")
