# Energy bill calculator program

# -------------------------
# Subprograms
# -------------------------
def energy_cost(previous_meter_reading, current_meter_reading, calorific_value):
    units_used = current_meter_reading - previous_meter_reading
    kwh_used =  units_used * 1.022 * (calorific_value / 3.6) #kilowatt hours used
    cost = int(0.0284 * kwh_used)
    return cost


# -------------------------
# Main program
# -------------------------
previous_meter_reading = int(input("Previous meter reading: "))
current_meter_reading = int(input("Current meter reading: "))
calorific_value = 39.3
cost = energy_cost(previous_meter_reading, current_meter_reading, calorific_value)
print("Cost is $", cost)