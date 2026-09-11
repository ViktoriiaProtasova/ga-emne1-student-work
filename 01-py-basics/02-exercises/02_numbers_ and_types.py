#%% #5. Summer to tall

tall1 = int(input("Enter a number: "))
tall2 = int(input("Enter another number: "))
summ = tall1 + tall2
print("Amount:",summ)


#%% # 6. Finn gjennomsnittet

tall1 = int(input("Enter a number: "))
tall2 = int(input("Enter another number: "))
average = (tall1 + tall2) / 2
print(f"Average: {average:.2f}")


#%% #7. Celsius til Fahrenheit

celsius = float(input("Enter a temperature in Celsius: "))
fahrenheit = round(celsius * 9 / 5 + 32)
print(f"The temperature in Fahrenheit is: {fahrenheit}°F")


#%% #8. Fahrenheit til Celsius

fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
celsius = round((fahrenheit - 32) * 5 / 9)
print(f"The temperature in Celsius is: {celsius}°C")
