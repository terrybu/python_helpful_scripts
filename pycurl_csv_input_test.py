import pycurl
import urllib
import csv
import os
from datetime import datetime

phoneNumberColumnHeader = 'PhoneNumber'

logFile = None
startTime = datetime.now()
formattedStartTime = startTime.strftime("%Y%m%d%H%M")

def logInfo( logMessage ):
    """Logs data to the log file."""
    global logFile
    if ( logFile == None ):
        logFile = open("Logs/pycurl_%s.txt"%formattedStartTime,"w")
    logFile.write(str(logMessage))
    logFile.write('\n')
    logFile.flush()

def printLog(str):
	print(str)
	logInfo(str)

def openCsvFile( csvFileName ):
    """Opens a CSV Reader and returns it and the file handle for later closing."""
    csvfile = open(csvFileName, 'rb')
    fileReader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    return (csvfile,fileReader)

def openCsvWriter( csvFileName, fieldNames ):
    """Opens a CSV Writer and returns it and the file handle for later closing."""
    csvfile = open(csvFileName, 'wb')
    fileWriter = csv.DictWriter(csvfile, delimiter=',', quotechar='"', fieldnames=fieldNames)
    return (csvfile,fileWriter)

def getFieldNames( fileReader ):
    """Given a CSV file dictionary reader, returns the header field names from the CSV file."""
    return fileReader.fieldnames            

def fileToList( fileReader ):
    """Given a CSV file, this method returns an array composed of all the rows in that file."""
    rows = []
    for rowDictionary in fileReader:
        rows.append(rowDictionary)
    return rows

def pycurlWithParam(phoneNumber):
	c = pycurl.Curl()
	url = 'https://www.terrybu.com'
	post_params = [
	('AccountHolderPhoneNumber', phoneNumber),
	]
	resp_data = urllib.urlencode(post_params)
	c.setopt(pycurl.POSTFIELDS, resp_data)
	c.setopt(c.URL, url)
	c.perform()
	printLog("\n\nPhone Number: " + str(phoneNumber))
	printLog("\nRESPONSE CODE: " + str(c.getinfo(pycurl.HTTP_CODE)))
	printLog("\n" + c.getinfo(pycurl.EFFECTIVE_URL))
	printLog("******************************************************")
	c.close()

def readPhoneNumberColumn(rows):
	printLog("There are %d rows in the input csv file"%len(rows))
	for row in rows:
		if row[phoneNumberColumnHeader]:
			phoneNum = row[phoneNumberColumnHeader]
			pycurlVData(phoneNum)




def main( argv ):
    """Main entry point for processing the file."""
    if ( len(argv) > 1 ):
        csvInputFileName = argv[1]
        if ( os.path.exists(csvInputFileName) and os.path.isfile(csvInputFileName) ):
            print("Opening file...")
            (fileHandle,fileReader) = openCsvFile( csvInputFileName )
            print("Processing ...")
            allRows = fileToList( fileReader )
            readPhoneNumberColumn(allRows)
            #TODO: Need to WRITE to a CSV with the API OUTPUT RESULTS

        else:	
            exit()
    else: 	 
        print("Insufficient parameters!")
        exit()

if __name__ == '__main__':
    import sys
    sys.exit(main( sys.argv ))

