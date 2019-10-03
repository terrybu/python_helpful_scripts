import csv
from datetime import datetime
import os 

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