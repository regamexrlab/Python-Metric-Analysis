import csv


speed, hr, length, distance = 0, 0, 0, 0
speeds, hrs = [], []

with open('GOTOES_FIT-CSV_4493050655517899(1).csv', 'r') as file: 
    reader = csv.DictReader(file)
    for row in reader:
        length += 1
        
        speed += float(row["speed"])
        speeds.append(row["speed"])
        
        hr += float(row["heart_rate"])
        hrs.append(row["heart_rate"])
        
        distance = row["distance"]

    avr_speed, avr_hr = speed // length, hr // length

with open('sample_analysis.txt', 'w') as file:
    file.write("Minute, Heart Rate/Min, Speed/Min")
    file.write("\n")
    for i in range(len(speeds)):
        file.write(str(i))
        file.write(", ")
        file.write(hrs[i])
        file.write(", ")
        file.write(speeds[i])
        file.write("\n")

    file.write("Average Speed: ")
    file.write(str(avr_speed))
    file.write("\n")
    file.write("Average Heart Rate: ")
    file.write(str(avr_hr))
    file.write("\n")
    file.write("Distance: ")
    file.write(distance)

    
