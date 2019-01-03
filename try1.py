file = open("C:\\Users\\Pratik\\Desktop\\PDF _TO_EXCEL\\marks.txt","r")

count = 0

for x in range(1,118):

    for i in range(1,32):
        file.readline()
    file.read(19)
    var1 = file.read(1)
    if var1 == '-':
        count = count + 1
    for i in range(1,29):
        file.readline()
    file.read(19)
    var2 = file.read(1)
    if var2 == '-':
        count  = count + 1
    file.readline()
    file.readline()

PerFailed = (count/237) * 100
PerPassed = ((237-count)/237)*100

print ('Total students  = 237 ')
print ('Total students passed :',(237-count))
print ('Total students failed :',count)
print ('Percentage of students Passed',PerPassed)
print ('Percentagge of students failed',PerFailed)






