import os

def main( argv ):
    """Main entry point for processing the file."""
    if ( len(argv) > 1 ):
    	text_filename = argv[1]
    	if ( os.path.exists(text_filename) and os.path.isfile(text_filename) ):
    		print("Opening file...")
    		file_object = open(text_filename, 'r')
    		lines = file_object.readlines()
    		new_list = list(map(lambda x: x.strip('\n'),lines))
    		# print(new_list)

    		comma_separated_string_list = list(map(lambda x: x.replace(' ', ','),new_list))
    		print(comma_separated_string_list)

    		#final output should be comma separated with new line for each row
    		for item in comma_separated_string_list:
    			print(item)





    	else:	
    		exit()
    else: 	 
        print("Insufficient parameters!")
        exit()

if __name__ == '__main__':
    import sys
    sys.exit(main( sys.argv ))