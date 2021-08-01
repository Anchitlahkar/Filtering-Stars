import pandas as pd
import csv


rows = []
with open("Star_Data.csv", "r") as f:
    csv_reader = csv.reader(f)

    for row in csv_reader:
        rows.append(row)


star_data = rows[1:]

count = 0



name = []
radius = []
mass = []
distance = []
gravity= []


temp_data = list(star_data)
print('Total Stars: ', len(star_data))

for data in temp_data:
    try:
        if float(data[2]) <= 100.00:
            if float(data[5]) >=150.00 and float(data[5]) <=350.00:
                count += 1
                distance.append(data[2])
                gravity.append(data[5])
                name.append(data[1])
                mass.append(data[3])
                radius.append(data[4])

    except:
        star_data.remove(data)
        pass

print(distance,'\n\n\n\n\n',gravity)

print(count)

df = pd.DataFrame(list(zip(name, distance, mass, radius, gravity)), columns=['Star_Name', 'Distance', 'Mass', 'Radius', 'Gravity'])
df.to_csv('Filtered_Data.csv')
