import csv
with open('speedtest.log', 'r') as csvfile:
    reader = csv.reader(csvfile)
    a = []
    for row in reader:
        a.append(row)

for line in a[1:]:
    down = float(line[6])/1000.0 / 1000.0
    up = float(line[7])/1000.0 / 1000.0
    print("{} down: {:.2f} Mb/s up: {:.2f} Mb/s".format(line[3], down, up))
