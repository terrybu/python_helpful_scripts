import os
from datetime import datetime
from CustomTools import LogFile
from CustomTools import CsvFileHandler
from APIManager import VData

PHONE_NUMBER_COLUMN_HEADER = 'phone_number'
RESPONSE_COLUMN_HEADER = 'response'
HTTP_CODE_COLUMN_HEADER = 'HTTP_CODE'

def write_response_to_csv(csv_file_writer, response_array):
    csv_file_writer.writeheader()
    for response_string in response_array:
        csv_file_writer.writerows(
        [{PHONE_NUMBER_COLUMN_HEADER: response_string[PHONE_NUMBER_COLUMN_HEADER], 
        RESPONSE_COLUMN_HEADER: response_string[RESPONSE_COLUMN_HEADER],
        HTTP_CODE_COLUMN_HEADER: response_string[HTTP_CODE_COLUMN_HEADER]
        }])

def main( argv ):
    """Main entry point for processing the file."""
    if ( len(argv) > 1 ):
        csv_input_file_name = argv[1]
        log = LogFile.LogFile( os.path.basename(__file__), LogFile.LogLevel.DEBUG )
        csvHandler = CsvFileHandler.CsvFileHandler(csv_input_file_name)
        if ( os.path.exists(csv_input_file_name) and os.path.isfile(csv_input_file_name) ):
            log.infoLog("Opening CSV file...")
            (file_handle,csv_file_reader) = csvHandler.open_csv_file_reader()
            log.infoLog("Processing ...")
            response_array = VData.pycurl_vData_radarScore_v2_phoneNumberAlone( csv_file_reader, PHONE_NUMBER_COLUMN_HEADER, RESPONSE_COLUMN_HEADER, HTTP_CODE_COLUMN_HEADER, log)
            field_names = [PHONE_NUMBER_COLUMN_HEADER, RESPONSE_COLUMN_HEADER, HTTP_CODE_COLUMN_HEADER]
            (out_handle, csv_file_writer) = csvHandler.open_csv_writer( field_names )
            write_response_to_csv(csv_file_writer, response_array)
            out_handle.close()
            log.infoLog("Writing complete.")
        else:   
            exit()
    else:    
        print("Insufficient parameters!")
        exit()

if __name__ == '__main__':
    import sys
    sys.exit(main( sys.argv ))

