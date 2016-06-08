#!/usr/bin/python
import os,csv,sys
#value = raw_input("sample ?")
#print( "Value is : "+value)
#os.system("echo "+value+" | festival --tts")
fo = open("hindiCounting.csv", "r")
#print "Name of the file: ", fo.name
try:
    reader = csv.reader(fo)
    for row in reader:
        print row
except:
	print "Unable to read the csv file"
finally:
    fo.close()
