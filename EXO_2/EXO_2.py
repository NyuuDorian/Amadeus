#path for the bookings file
pathToBookingFile = "../Data/bookings.csv"

#Going through the first file
bookingFile = open(pathToBookingFile, 'r')
bookingFile.seek(0) #we read the file through the beginning

#reading the first line in order to get the different header
header = bookingFile.readline()

#In order to have a clean header
cleanHeader = header.strip().replace(" ", "").split('^')
print(cleanHeader)

#initialize the different columns that are useful
arr_port_column = 0
IATA_column = 0
pax_column = 0
#arr_city_column = 0

#Find the real number for those columns.
i = 0
for x in cleanHeader:
    #print(x, i)
    if x == 'arr_port':
        arr_port_column = i
    elif x == 'pax':
        pax_column = i
    elif x == 'pos_iata':
        IATA_column = i
    i += 1

breaker = 0
known_arr_port = []
counter = []
for line in bookingFile:
    cleanLine = line.strip().replace(" ", "").split('^')
    #print(cleanLine)
    if cleanLine[arr_port_column] in known_arr_port:
        counter[known_arr_port.index(cleanLine[arr_port_column])] += int(cleanLine[pax_column])
    else:
        known_arr_port.append(cleanLine[arr_port_column])
        counter.append(int(cleanLine[pax_column]))
    #print(known_arr_port)
    #print(counter)
    #print(len(known_arr_port), len(counter))
    #print(known_arr_port, known_arr_port.index(cleanLine[arr_port_column]), counter)
    #breaker += 1
    #if breaker == 15:
    #    break;
    
    #SINCE too big for a line try to get through a file ?

print(counter)
    
#print(arr_port_column, pax_column, IATA_column)

#closing file
bookingFile.close()