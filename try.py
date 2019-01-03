import PyPDF2
import xlwt
import xlrd
import csv
import itertools
import os.path

opened_pdf=PyPDF2.PdfFileReader('pune.pdf','rb')

with open('mytxtfile.txt', 'w') as f:
    for i in range(0,100):
        p=opened_pdf.getPage(i);
        p_text=p.extractText()
        P_lines=p_text.splitlines()
        print (P_lines)
        for item in P_lines:
            f.write("%s\n" % item)

with open('mytxtfile.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)                        #for whitespace removing
    #lines = (line.split(",") for line in stripped if line)
    #mystring = ', '.join(lines)
    with open('final1.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        #writer.writerow(('title', 'intro'))
        writer.writerows(stripped)

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







'''''
text_file = open("2.txt", "r") # Multi is name of my file and Name_of_File.txt must be in the same folder otherwise you have to write the direction of specific file.
lines = text_file.readlines()
my_iter=iter(lines)
#print (type(lines))
#b = bytes(lines, 'utf-8')

#print len(lines)

mystring =', '.join(lines)
text_file.close()
with open("OutPut.csv", 'wb')as f:
    writer = csv.writer(f)
    writer.writerow([mystring])
    #writer.writerows(map(lambda x: [x], (bytes(mystring,'utf-8')))


    
with open("output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(a)
n = 0
for line in lines:
    n = n + 1
    if "2016" in line:
        if "[" in line:
            date_time = line.split("[")[0]
            year = date_time.split(" ")[0]
            month = date_time.split(" ")[1]
            day = date_time.split("  ")[1]
            time = date_time.split("  ")[2]
            hour = time.split(":")[0]
            minute = time.split(":")[1]
            second = time.split(":")[2]

       
file=open("2.txt")
lines=[line.strip() for line in file if file.strip()]
for i,line in enumerate(lines):
    csv.set(i%3,line)
#========================================================================================================================

save_path = "F:/New folder/New folder/"

completeName_in = os.path.join(save_path, '2' + '.txt')
completeName_out = os.path.join(save_path, 'Output22_file_csv' + '.csv')

file1 = open(completeName_in)
In_text = csv.reader(file1, delimiter=',')

file2 = open(completeName_out, 'w')
out_csv = csv.writer(file2)

file3 = out_csv.writerows(In_text)

file1.close()
file2.close()

csvfile = "F\\New folder\\New folder\\2.csv"
with open('2.csv') as csvfile:
#Assuming res is a flat list
    with open(csvfile, "w") as output:
     writer = csv.writer(output, lineterminator='\n')
     for val in P_lines:
        writer.writerow([val])

#Assuming res is a list of lists
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(res)

with open('2.txt','r') as csv_file:
myFile = open('po.csv', 'w')
with pc_csv:
   writer = csv.writer(myFile)
   writer.writerows(P_lines)


with open('2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')

with open('2.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('8.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('title', 'intro'))
        writer.writerows(lines)

with open('2.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line for line in stripped if line)
    grouped = itertools.izip(*[lines] * 3)
    with open('log.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('title', 'intro'))
        writer.writerows(grouped)
book=xlwt.Workbook
f1=open('2.txt','r+')
boook.save('Excelfile'+'.xls')


file=file.writelines(["%s\n" % item  for item in P_lines])
file1=open("1.txt","w")
file1.write(file)

file = open("E:\\marks.txt","r")
file.readline() #line 1
file.readline() #line 2
file.readline() #line 3
file.readline() #line 4
file.readline() #line 5
#-----------------------------------------------------------------student1
roll_no = file.read(10) #read roll no from line 6
#print(roll_no)
file.readline() #line 6
file.readline() #line 7
file.readline() #line 8
file.readline() #line 9
file.readline() #line 10
#-----------------------sub1 sem 1
sub1 = file.read(6)
file.read(2)
oesub1 =  file.read(2)
file.read(6)
thsub1 = file.read(2)
file.readline()
#-----------------------sub2
sub2 = file.read(6)
file.read(2)
oesub2 =  file.read(2)
file.read(6)
thsub2 = file.read(2)
file.readline()
#-----------------------sub3
sub3 = file.read(6)
file.read(2)
oesub3 =  file.read(2)
file.read(6)
thsub3 = file.read(2)
file.readline()
#-----------------------sub4
sub4 = file.read(6)
file.read(2)
oesub4 =  file.read(2)
file.read(6)
thsub4 = file.read(2)
file.readline()
#-----------------------sub5
sub5 = file.read(6)
file.read(2)
oesub5 =  file.read(2)
file.read(6)
thsub5 = file.read(2)
file.readline()
#-----------------------sub6
sub6 = file.read(6)
file.read(26)
twsub6 =  file.read(2)
file.read(6)
prsub6 = file.read(2)
file.readline()
#----------------------sub7
sub7 = file.read(6)
file.read(26)
twsub7 =  file.read(2)
file.read(6)
prsub7 = file.read(2)
file.readline()
#-----------------------sub8
sub8 = file.read(6)
file.read(26)
twsub8 =  file.read(2)
file.read(6)
prsub8 = file.read(2)
file.readline()
#------------------------sub9
sub9 = file.read(6)
file.read(2)
tesub9 =  file.read(2)
file.readline()#auditcourse
#------------------sem 2
file.readline()
#-----------------------sub10
sub10 = file.read(6)
file.read(2)
oesub10 =  file.read(2)
file.read(6)
thsub10 = file.read(2)
file.readline()
#-----------------------sub11
sub11 = file.read(6)
file.read(26)
twsub11 =  file.read(2)
file.readline()
#-----------------------sub12
sub12 = file.read(6)
file.read(2)
oesub12 =  file.read(2)
file.read(6)
thsub12 = file.read(2)
file.readline()
#-----------------------sub13
sub13 = file.read(6)
file.read(2)
oesub13 =  file.read(2)
file.read(6)
thsub13 = file.read(2)
file.readline()
#-----------------------sub14
sub14 = file.read(6)
file.read(2)
oesub14 =  file.read(2)
file.read(6)
thsub14 = file.read(2)
file.readline()
#-----------------------sub15
sub15 = file.read(6)
file.read(26)
twsub15 =  file.read(2)
file.read(6)
prsub15 = file.read(2)
file.readline()
#----------------------sub16
sub16 = file.read(6)
file.read(26)
twsub16 =  file.read(2)
file.read(6)
prsub16 = file.read(2)
file.readline()
#-----------------------sub17
sub17 = file.read(6)
file.read(26)
twsub17 =  file.read(2)
file.read(6)
prsub17 = file.read(2)
file.readline()
#------------------------sub18
sub18 = file.read(6)
file.read(26)
twsub18 =  file.read(2)
file.read(6)
prsub18 = file.read(2)

file.readline()
file.read(19)
sgpa = file.read(4)
#----------------------------------------------



'''