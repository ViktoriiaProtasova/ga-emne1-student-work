#%% 17. Sekunder til timer, minutter og sekunder

number_of_seconds = int(input("Please enter a whole number of seconds: "))
whole_hours = number_of_seconds // 3600
rest_seconds = number_of_seconds % 3600
whole_minutes = rest_seconds // 60
remaining_seconds = rest_seconds % 60
print(f"{number_of_seconds} seconds gave: {whole_hours} h, {whole_minutes} min and {remaining_seconds} sec")
