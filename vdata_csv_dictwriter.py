import os
from datetime import datetime
from customtools import headerstrings
from customtools import logfile
from customtools import csvhandler
from apimanager import vdata

def main( argv ):
    """Main entry point for processing the file."""

    if ( len(argv) > 1 ):
        csv_input_file_name = argv[1]
        log = logfile.LogFile( os.path.basename(__file__), logfile.LogLevel.DEBUG )
        csv_handler = csvhandler.CsvFileHandler(csv_input_file_name)
        header_strings = headerstrings.HeaderStrings()
        if ( os.path.exists(csv_input_file_name) and os.path.isfile(csv_input_file_name) ):
            log.infoLog("Opening CSV file...")
            (file_handle,csv_file_reader) = csv_handler.open_csv_file_reader()
            log.infoLog("Processing ...")
            response_array = vdata.pycurl_vData_radarScore_v2( csv_file_reader, log)
            field_names = [header_strings.get_phone_number_header(), header_strings.get_last_seen_date_header(), header_strings.get_response_header(), header_strings.get_http_code_header(), header_strings.get_prepostpaid_header()]
            (out_handle, csv_file_writer) = csv_handler.open_csv_writer( field_names )
            csv_handler.write_response_to_csv_with_last_seen(csv_file_writer, response_array)
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

