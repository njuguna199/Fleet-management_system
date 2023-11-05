from flask import Flask, render_template
from fleet_management import FleetManagementSystem  # Import your Fleet Management System script

app = Flask(__name__)

# Create a FleetManagementSystem instance and customize it with vehicles
fleet_manager = FleetManagementSystem()

from fleet_management import Bus
bus1 = Bus("City Express", "John Doe")
# Customize bus1 and add it to fleet_manager
# ...

@app.route('/')
def fleet_info():
    # Initialize your FleetManagementSystem here
    fleet_manager = FleetManagementSystem()

    # Add vehicles, customize them, and simulate operations as needed
    # ...

    # Calculate reliability and spending
    fleet_manager.calculate_reliability()
    total_monthly_spending = fleet_manager.calculate_monthly_spending()

    # Calculate overall monthly spending
    total_monthly_spending = fleet_manager.calculate_monthly_spending()

    # Return a template with the fleet information
    return render_template('fleet_info.html', fleet=fleet_manager, total_spending=total_monthly_spending)
    
if __name__ == '__main__':
    app.run(debug=True)
    
