# Fleet-management_system
This is a new system coded initially in python being created to monitor and track the behavioural patterns of 10 buses and two lorries for Yaya Altar, to be able to track their maintenance spending habits and overall performance


Vehicle Class:

Vehicle is the base class representing a generic vehicle.
It has attributes like name (vehicle name), mileage_limit (maximum mileage before service), driver_name (driver's name), mileage (current mileage), service_count (number of times serviced), error_count (number of errors), repair_history (list of repair descriptions), and total_repair_cost (total cost of repairs).
It has methods to:
run: Simulate running the vehicle for a distance, update mileage, and trigger service when the mileage limit is reached.
add_error: Record an error description and increment the error count.
add_repair_cost: Add the cost of repairs to the total repair cost.
get_monthly_report: Generate a monthly report with vehicle details.
Bus and Lorry Classes:

Bus and Lorry are subclasses of Vehicle specialized for buses and lorries, respectively.
They inherit attributes and methods from the base class but can also set their own default mileage_limit values.
FleetManagementSystem Class:

FleetManagementSystem is a class for managing a fleet of vehicles.
It has attributes like vehicles (a list to store vehicle instances), best_vehicle (the most reliable vehicle), and min_error_count (the minimum error count across vehicles).
It has methods to:
add_vehicle: Add a vehicle to the fleet.
run_fleet: Simulate running the fleet for a given distance.
calculate_reliability: Determine the most reliable vehicle based on error count.
calculate_monthly_spending: Calculate the total monthly spending on repairs for the fleet.
Creating and Customizing Vehicles:

The code creates and customizes 10 instances of the Bus class (representing 10 buses) with different details like service count, errors, repair costs, and mileage.
Simulating Fleet Operation:

The code simulates running the fleet for 2000 miles using the run_fleet method of the FleetManagementSystem.
Calculating Reliability and Spending:

It calculates the most reliable vehicle and overall monthly spending on repairs using the calculate_reliability and calculate_monthly_spending methods.
Printing Reports:

The code prints monthly reports for each vehicle, including driver, mileage, service count, errors, repair history, and repair costs.
Sorting Vehicles by Reliability:

It sorts the vehicles by error count (reliability) in ascending order, displaying the most reliable vehicle first.
Overall Monthly Spending:

It prints the total monthly spending on repairs for the entire fleet.
This code is a Python script that models a fleet management system, allowing you to manage and monitor the status of a fleet of vehicles, calculate reliability, and track monthly spending on repairs.




