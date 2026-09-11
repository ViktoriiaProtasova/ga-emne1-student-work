#%% Tillegg: Hopp over verdier med continue

counter = 0

for i in range(1, 31):
    if i % 4 == 0:
        continue
    else:
        print(i)
        counter += 1
print(f"Total amount: {counter}")