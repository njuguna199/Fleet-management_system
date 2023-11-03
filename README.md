# Fleet-management_system
This is a new system coded initially in python being created to monitor and track the behavioural patterns of 10 buses and two lorries for Yaya Altar, to be able to track their maintenance spending habits and overall performance


Vehicle Class:

This class serves as a blueprint for all types of vehicles in your fleet. It has attributes like name (the vehicle's name), mileage_limit (the maximum mileage before service is required), mileage (current mileage), service_count (number of services performed), error_count (number of reported errors), repair_history (a list of error descriptions), and total_repair_cost (the cumulative cost of repairs).

It has several methods:

run(self, distance): Simulates the vehicle running a certain distance. If the mileage exceeds the mileage limit, it triggers a service and resets the mileage to zero.
add_error(self, error_description): Records an error in the vehicle's history and increments the error count.
add_repair_cost(self, cost): Adds the cost of a repair to the total repair cost.
get_monthly_report(self): Returns a report with various statistics about the vehicle.
Bus and Lorry Classes:

These are subclasses of the Vehicle class, specializing in buses and lorries. They set the mileage_limit for buses to 5000 and for lorries to 10000. They inherit all the attributes and methods from the Vehicle class.
FleetManagementSystem Class:

This class represents the fleet management system. It has attributes like vehicles (a list to store all the vehicles in the fleet), best_vehicle (a reference to the vehicle with the fewest errors), and min_error_count (the minimum number of errors among all vehicles).

It has methods:

add_vehicle(self, vehicle): Adds a vehicle to the fleet.
run_fleet(self, distance): Simulates all vehicles in the fleet running a certain distance.
With this code, you can create vehicles (either buses or lorries), add them to the fleet, and simulate running them for a specific distance. The system keeps track of various statistics for each vehicle, such as mileage, service count, error count, and repair costs. The FleetManagementSystem class also keeps track of the vehicle with the fewest errors, which is stored in the best_vehicle attribute. This system allows you to manage and monitor your fleet of vehicles.

