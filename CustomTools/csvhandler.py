import csv
from datetime import datetime
import os 
import headerstrings
import urlparse 

class CsvFileHandler:
    
	def __init__( self, csv_file_name):
		self.csv_file_name = csv_file_name

	def open_csv_file_reader(self):
		"""Opens a CSV Reader and returns it and the file handle for later closing."""
		csv_file = open(self.csv_file_name, 'rb')
		csv_file_reader = csv.DictReader(csv_file, delimiter=',', quotechar='"')
		return (csv_file,csv_file_reader)

	def open_csv_writer(self, field_names):
		start_time = datetime.now()
		formatted_start_time = start_time.strftime("%Y%m%d%H%M%S")
		if self.csv_file_name[:6] == "input/":
			csv_file = open("Output/" + formatted_start_time + "_OUTPUT_RESULT_" + self.csv_file_name[6:], 'w')
		else:
			csv_file = open("Output/" + formatted_start_time + "_OUTPUT_RESULT_" + self.csv_file_name, 'w')
		file_writer = csv.DictWriter(csv_file, delimiter=',', quotechar='"', fieldnames=field_names, extrasaction='ignore')
		return (csv_file,file_writer)

	def write_response_to_csv_no_last_seen(self, csv_file_writer, response_array):
		csv_file_writer.writeheader()
		header_strings_object = headerstrings.HeaderStrings()
		ph_header = header_strings_object.get_phone_number_header()
		response_header = header_strings_object.get_response_header()
		http_header = header_strings_object.get_http_code_header()
		for response_object in response_array:
			csv_file_writer.writerows(
				[{ph_header: response_object[ph_header], 
				response_header: response_object[response_header],
				http_header: response_object[http_header]
				}])

	def write_response_to_csv_with_last_seen(self, csv_file_writer, response_array):
		csv_file_writer.writeheader()
		header_strings_object = headerstrings.HeaderStrings()
		ph_header = header_strings_object.get_phone_number_header()
		response_header = header_strings_object.get_response_header()
		http_header = header_strings_object.get_http_code_header()
		last_seen_header = header_strings_object.get_last_seen_date_header()
		prepaid_postpaid_header = header_strings_object.get_prepostpaid_header()
		for response_object in response_array:
			prepaid_or_postpaid_string = self.determine_if_prepaid(response_object[response_header])
			csv_file_writer.writerows(
				[{ph_header: response_object[ph_header], 
				response_header: response_object[response_header],
				http_header: response_object[http_header],
				last_seen_header: response_object[last_seen_header],
				prepaid_postpaid_header: prepaid_or_postpaid_string
				}])

	def determine_if_prepaid(self, response_string):
		params = urlparse.parse_qs( response_string )
		LAST_SEEN_DATE_STATUS_RESPONSE_KEY = "LastSeenDateStatus"
		if (params.has_key(LAST_SEEN_DATE_STATUS_RESPONSE_KEY)):
			if  (params[LAST_SEEN_DATE_STATUS_RESPONSE_KEY][0] == '1'):
				return "postpaid/unknown"
			else:
				return "prepaid"
		else:
			if (params['ReputationalIndex'][0] == '2'):
				return "postpaid/unknown"
			else:
				return "prepaid"

