__author__ = 'oscartaracena'
#Version 1.0 - this is just the reading and parsing of the file. Next major
#part will be passing command line arguements from the command line.
#just some code


file1 = open('LG_YPCST_Data.txt', 'r')
str1 = raw_input("please enter the what you are searching for>")

#print file.readlines()
counter = 0
for i in file1:
    if str1 in i:
        counter += 1
file1.close()

print counter
