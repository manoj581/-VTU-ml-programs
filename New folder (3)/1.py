import csv
def loadCsv(filename):
	lines = csv.reader(open(filename, "rt"))
	dataset = list(lines)
	for i in range(len(dataset)):
		dataset[i] = dataset[i]
	return dataset

attributes = ['Sky','Temp','Humidity','Wind','Water','Forecast']
print(attributes)
n = len(attributes)
dataset = loadCsv("1.csv")
print(dataset)
h=['0'] * n
print("Intial hypothesis")
print(h)
print("The hypothesis are")

for i in range(len(dataset)):
    target = dataset[i][-1]
    if(target == 'Yes'):
        for j in range(n):
            if(h[j]=='0'):
                h[j] = dataset[i][j]
            if(h[j]!= dataset[i][j]):
                h[j]='?'
    print(i+1,'=',h)

print("Final hypothesis")
print(h)
