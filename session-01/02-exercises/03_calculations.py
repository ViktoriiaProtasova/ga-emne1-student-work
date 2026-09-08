#%% #9. Minutter til timer og minutter

helt_antall_minutter = int(input("skriv inn et helt antall minutter: "))
hele_timer = helt_antall_minutter // 60
resterende_minutter = helt_antall_minutter % 60
print(f"Dette tilsvarer {hele_timer} hele timer og {resterende_minutter} minutter som blir igjen")


#%% #10. Tips og totalpris

price = float(input("Enter the price:"))
tips = price * 0.15
total_price = price + tips
print(f"The tips is {tips:.2f}")
print(f"The total price is {total_price:.2f}")


#%% #11. Centimeter til fot

height_cm = float(input("Enter height in centimeters: "))
height_feet = height_cm / 30.48
print(f"Height in feet: {height_feet:.2f}")


#%% #12. Beregn ukelønn

hourly_rate = float(input("Enter hourly rate: "))
hours_worked = int(input("Enter hours worked: "))
weekly_salary = hourly_rate * hours_worked
print(f"Weekly salary: {weekly_salary:.2f}")
