

"""
Code by Ezechukwu Emmanuel
Extra Creativity
----------------
the code displays a customized print statement based on the user's choice of Celsius or Fahrenheit and 
"""

def wind_chill(temperature, wind_speed):
    wind_chill_val = 35.74 + 0.6215 * temperature - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16)
    return wind_chill_val


def celsius_to_fahrenheit(t_celsius):
    t_fahrenheit = t_celsius * (9/5) + 32
    return t_fahrenheit


temperature = float(input("What's the current temperature? "))
unit_choice = input("Enter 'C' for Celsius or 'F' for Fahrenheit: ")

if unit_choice.lower() == 'c':
    converted_temperature = celsius_to_fahrenheit(temperature)
    print(f"The wind chill for the temperature in Celsius {temperature}°C is as follows:")
else:
    converted_temperature = temperature
    print(f"The wind chill for the temperature in Fahrenheit {temperature}°F is as follows:")

print("Speed (mph)\tWind Chill")

for speed in range(5, 61, 5):
    wind_chill_val = wind_chill(converted_temperature, speed)
    print(f"{speed}\t\t{wind_chill_val:.2f}")
