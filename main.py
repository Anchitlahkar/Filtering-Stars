import pandas as pd
import csv


rows = []
with open("Star_Data.csv", "r") as f:
    csv_reader = csv.reader(f)

    for row in csv_reader:
        rows.append(row)


star_data = rows[1:]

count = 0

temp_data = list(star_data)
print('Total Stars: ', len(star_data))

for data in temp_data:
    try:
        if float(data[2]) <= 100.00 and float(data[5]) >= 150.00 or float(data[2]) <= 100.00 and float(data[5]) <= 350.00:
            count += 1
        else:
            star_data.remove(data)
    except:
        star_data.remove(data)
        pass


print('Filtered Stars:', len(star_data))


name = []
radius = []
mass = []
distance = []
gravity= []

for i in range(len(star_data)):
    name.append(star_data[i][1])
    distance.append(star_data[i][2])
    mass.append(star_data[i][3])
    radius.append(star_data[i][4])
    gravity.append(star_data[i][5])


print(count)

df = pd.DataFrame(list(zip(name, distance, mass, radius, gravity)), columns=['Star_Name', 'Distance', 'Mass', 'Radius', 'Gravity'])
df.to_csv('Filtered_Data.csv')