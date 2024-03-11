# Function to convert measurements based on type, value, and conversion type
def convert_measurement(measurement_type, value, conversion_type):
    # Conversion factors for various measurement types and units
    conversion_factors = {
    "Length": {
        "m": 1,  # base unit for length is meter
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.34,
        "in": 0.0254,
        "cm": 0.01,
        "km": 1000,
        "mm": 0.001,
        "mile": 1609.34,
        "yard": 0.9144,
        "rod": 5.0292,
    },
    "Volume": {
        "l": 1,  # base unit for volume is liter
        "fl oz": 0.0295735,
        "t": 0.00110231,
        "gal": 3.78541,
        "ml": 0.001,
        "cup": 0.236588,
        "pt": 0.473176,
        "qt": 0.946353,
        "gill": 0.118294,
        "m^3": 1000,
        "cm^3": 0.001,
        "barrel (oil)": 158.987,
        "US gallon": 3.78541,
        "Imperial gallon": 4.54609,
    },
    "Mass": {
        "kg": 1,  # base unit for mass is kilogram
        "oz": 0.0283495,
        "lbs": 0.453592,
        "short ton": 907.185,
        "g": 0.001,
        "stone": 6.35029,
        "ton": 907.185,
        "mg": 1e-6,
        "tonne": 1000,
        "lb troy": 0.373242,
        "grain": 0.0000647989,
        "carat": 0.0002,
        "microgram": 1e-9,
    },
    "Data": {
        "bps": 1,  # base unit for data is bits per second
        "Kbps": 1000,
        "Mbps": 1e6,
        "Gbps": 1e9,
        "Bps": 8,  # bytes per second
        "KBps": 8000,
        "MBps": 8e6,
        "GBps": 8e9,
    },
    "Pressure": {
        "Pa": 1,  # base unit for pressure is Pascal
        "kPa": 1000,
        "MPa": 1e6,
        "bar": 1e5,
        "atm": 101325,
        "psi": 6894.76,
        "mmHg": 133.322,
    },
    "Speed": {
        "m/s": 1,  # base unit for speed is meters per second
        "km/h": 0.277778,
        "mi/h": 0.44704,
        "ft/s": 0.3048,
        "knot": 0.514444,
        "mach": 343.2,
    },
    "Time": {
        "sec": 1,  # base unit for time is second
        "min": 60,
        "hr": 3600,
        "day": 86400,
        "week": 604800,
        "month": 2628000,
        "year": 31536000,
    },
    "Temperature": {
        "K": 1,  # base unit for temperature is Kelvin
        "C": lambda x: x + 273.15,
        "F": lambda x: (x + 459.67) * 5/9,
    },
}


    # Validate input for measurement type
    if measurement_type not in conversion_factors:
        print("Invalid measurement type. Please choose from (Length, Volume, Mass, Data, Pressure, Speed, Time, Temperature).")
        return

    # Validate input for conversion type
    if conversion_type not in ["Imperial", "Metric"]:
        print("Invalid conversion type. Please choose either 'Imperial' or 'Metric'.")
        return

    print(f"Enter source unit for {measurement_type} ({conversion_type}):")
    user_input_source_unit = input()

    print(f"Enter target unit for {measurement_type} ({conversion_type}):")
    user_input_target_unit = input()

    # Check if the entered units are valid
    if user_input_source_unit not in conversion_factors[measurement_type] or user_input_target_unit not in conversion_factors[measurement_type]:
        print("Invalid source or target unit. Please choose valid units from the list.")
        return

    # Calculate conversion factor and convert the value
    conversion_factor_source = conversion_factors[measurement_type][user_input_source_unit]
    conversion_factor_target = conversion_factors[measurement_type][user_input_target_unit]

    converted_value = value * (conversion_factor_source / conversion_factor_target)

    print(f"Converted {measurement_type}: {converted_value:.2f} {user_input_target_unit}")

# Main loop for user interaction
# Main loop for user interaction
while True:
    print("Choose measurement type (Length, Volume, Mass, Data, Pressure, Speed, Time, Temperature), or type 'exit' to end:")
    user_input_type = input().capitalize()

    # Exit the program if the user types 'exit'
    if user_input_type == "Exit":
        break

    # Validate input for measurement type
    if user_input_type not in ["Length", "Volume", "Mass", "Data", "Pressure", "Speed", "Time", "Temperature"]:
        print("Invalid input for measurement type. Please choose from (Length, Volume, Mass, Data, Pressure, Speed, Time).")
        continue

    print("Enter value for conversion:")
    try:
        user_input_value = float(input())
    except ValueError:
        print("Invalid input for value. Please enter a numerical value.")
        continue

    print("Choose conversion type (Imperial or Metric):")
    user_input_conversion_type = input().capitalize()

    # Call the conversion function with user inputs
    convert_measurement(user_input_type, user_input_value, user_input_conversion_type)

    # Ask the user if they want to perform another conversion
    print("Do you want to perform another conversion? (yes/no)")
    user_input_another_conversion = input().lower()

    # Exit the loop if the user doesn't want to perform another conversion
    if user_input_another_conversion != "yes":
        break

