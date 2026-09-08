#1. Første program
print("Hello World!")


#%% # 2. Personlig hilsen

my_name = "Viktoriia"
favorite_language = "Python"
print("Hello,",my_name +"!", "Your favorite language is", favorite_language +"!")


#%% # 3. Navnehilsen med input

# noinspection DuplicatedCode
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name + "!"
print("Hello,",full_name)

hours = float(input("Enter your hours: "))
rate = float(input("Enter your rate: "))
pay = hours * rate
print("Pay:",pay)


#%% # 4. Favorittfarge

farge = input("Please enter your favorittfargen:")
print(f"Din favorittfarge er{farge}.")

