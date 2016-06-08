#!/usr/bin/python
import os,csv,sys,time
#value = raw_input("sample ?")
#print( "Value is : "+value)
#os.system("echo "+value+" | festival --tts")
fo = open("hindiCounting.csv", "r")
#print "Name of the file: ", fo.name
try:
    reader = csv.reader(fo)
    for row in reader:
        print row[2]
	os.system("echo "+row[2]+" | festival --tts")
	time.sleep(1)
except:
	print "Unable to read the csv file"
finally:
    fo.close()
