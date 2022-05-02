

import sys, os
import argparse

def cat(myFile):

	try:
		file_content = " "
		with open(myFile, 'r') as f:
			file_content = f.read()
		print(file_content)

			
	except Exception as e:

		print(e)
		sys.exit()


def main():
	parser = argparse.ArgumentParser(description="Print or Concatenate multiple files.")
	parser.add_argument("--files", help="File name to print out.", type=str, metavar='F', nargs='+')
	args = parser.parse_args()

	if args.files:
		for file in args.files:
			file_content = cat(file)
			print(file_content)

	
		
	else:
		print('No file specified')

if __name__ == '__main__':
	main()


	

