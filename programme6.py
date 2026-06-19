#creation of temperature converter
user = input("what do you want to convert to? (Celsius or Fahrenheit or Kelvin): ")
temperature =float(input("Enter the temperature value: "))
if user == "Celsius":
    fahrenheit = (temperature * 9/5) + 32
    kelvin = temperature + 273.15
    print(f'the given temperature in fahrenheit  {fahrenheit}')
    print(f'the given temperature in kelvin  {kelvin}')
elif user == 'fahrenheit':
    celsius = (temperature - 32) * 5/9
    kelvin = (temperature - 32) * 5/9 + 273.15
    print(f'the given temperature in celsius{celsius}')
    print(f'the given temperature in kelvin{kelvin}')
elif user == 'kelvin':
    celsius = temperature - 273.15
    fahrenheit = (temperature - 273.15) * 9/5 + 32
    print(f'the given temperature in celsius {celsius}')
    print(f'the given temperature in fahrenheit {fahrenheit}')
else:
    print("Invalid input. Please enter 'Celsius', 'Fahrenheit', or 'Kelvin'.")     

     