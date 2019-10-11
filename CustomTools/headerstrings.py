PHONE_NUMBER_COLUMN_HEADER = 'phone_number'
LAST_SEEN_DATE_COLUMN_HEADER = 'last_seen_date'
LAST_SEEN_DATE_STATUS_RESPONSE_KEY = "LastSeenDateStatus"
RESPONSE_COLUMN_HEADER = 'response'
HTTP_CODE_COLUMN_HEADER = 'HTTP_CODE'
PREPAID_POSTPAID_COLUMN_HEADER = "Prepaid/Postpaid"

class HeaderStrings:

	def __init__( self ):
		return None

	def get_phone_number_header(self):
		return PHONE_NUMBER_COLUMN_HEADER

	def get_last_seen_date_header(self):
		return LAST_SEEN_DATE_COLUMN_HEADER

	def get_response_header(self):
		return RESPONSE_COLUMN_HEADER

	def get_http_code_header(self):
		return HTTP_CODE_COLUMN_HEADER

	def get_prepostpaid_header(self):
		return PREPAID_POSTPAID_COLUMN_HEADER