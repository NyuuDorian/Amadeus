import os

#path for the bookings file
path1 = "../Data/bookings.csv"
#path for the searches file
path2 = "../Data/searches.csv"

#The file to write in
fileToWriteIn = open('answer_file.txt', 'w+')

#Going through the first file
file1 = open(path1, 'r')
file1.seek(0)

NumberOfLinesOfPath1 = 0
for line in file1:
    NumberOfLinesOfPath1 += 1
    
#closing the file because we do not need it anymore
file1.close()

print('Number of lines of the bookings file: ',NumberOfLinesOfPath1)
fileToWriteIn.write('Number of lines of the bookings file: ' + str(NumberOfLinesOfPath1) + '\n')


#Going through the second file
file2 = open(path2, 'r')
file2.seek(0)

NumberOfLinesOfPath2 = 0
for line in file2:
    NumberOfLinesOfPath2 += 1

#closing the file because we do not need it anymore
file2.close()
    
print('Number of lines of the searches file: ',NumberOfLinesOfPath2)
fileToWriteIn.write('Number of lines of the searches file: ' + str(NumberOfLinesOfPath2) + '\n')


#Total number of lines.
TotalNumberOfLines = NumberOfLinesOfPath1 + NumberOfLinesOfPath2
print('Total number of lines of the 2 files: ',TotalNumberOfLines)
fileToWriteIn.write('Total number of lines of the 2 files: ' + str(TotalNumberOfLines) + '\n')

fileToWriteIn.close()