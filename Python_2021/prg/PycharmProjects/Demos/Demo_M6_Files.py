# open a file: filevar = open('<filename>', '<mode>'), mode = r, w, a
# open a file in a path: filevar = open(r'<path>', '<mode>')
# the first form is recommended for this course, but only works if the file is located in the project folder

# write a string to a file: <filevar>.write(<var> + '\n')     NOTE: newline is NOT added automatically
# close a file: <filevar>.close
# read entire file: <infile>.read()
# read one line from a file: <infile>.readline()

# use .rstrip('\n') to strip newline from input
# read/write to a .txt file always uses strings


# using a while loop to read input from a file
def while_loop_read():
	print("====== Use a while loop to read and display the file ======")
	infile = open('names.txt')
	name = infile.readline()

	# when the end of the file has been reached, readline() returns the empty string
	while name != '':
		print(name, end="")
		name = infile.readline()

	infile.close()
	print("")


# using a for loop to read the same input file
# must close it first in order to reset the file pointer (read position)
# this loop should give the same result as the previous one
def for_loop_read():
	print("====== Use a for loop to read the same file ======")
	infile = open('names.txt')

	for line in infile:
		# .strip() removes all whitespace from both sides (spaces, tabs, newlines)
		# you can also use .rstrip() to strip from right, .lstrip() to strip from left
		# you can specify specific text to strip with the argument: .strip("\n")
		print(line.strip())
		print("wobble")

	infile.close()
	print("")


# using read() to read the entire file (including newlines) into one long string
# if you do it this way, you must be prepared to break apart the string
# and strip newlines to get to the data
def read_file_as_one_string():
	print("====== Use read() to read the entire file as one string ======")
	infile = open('names.txt')

	all_file = infile.read()
	print(all_file, end="*")
	print(type(all_file))           # show the data type of all_file

	infile.close()
	print("")


# writing a new file, use mode 'w'   NOTE: any existing file of the same name will be replaced
def write_new_file():
	print("====== Create the file test.txt ======")
	out_file = open('test.txt', 'w')
	for n in range(0, 100, 10):
		out_file.write(format(n, '3d') + '\n')       # format 3 columns width and newline

	out_file.close()


# append to an existing file, use mode 'a'
def append_to_file():
	print("====== Append data to the file test.txt ======")
	out_file = open('test.txt', 'a')
	for n in range(100, 200, 10):
		out_file.write(format(n, '3d') + '\n')       # same format as before

	out_file.close()


# to copy and modify a file, use two file variables: one for reading, one for writing
# for this example, I am using a copy of the original names file
def copy_infile_to_outfile():
	infile = open('test.txt', 'r')
	out_file = open('test.tmp', 'w')

	for line in infile:
		out_file.write(line)

	infile.close()
	out_file.close()


# all import statements should appear at the top of the file
# for the purposes of the demo, I am putting it with the related code
def system_file_functions():
	import os
	# now we can delete the old file
	os.remove('test.txt')
	# and rename the new file to the original name
	os.rename('test.tmp', 'test.txt')


def main():
	while_loop_read()
	for_loop_read()
	read_file_as_one_string()
	write_new_file()
	append_to_file()
	copy_infile_to_outfile()
	system_file_functions()


# call the main function
main()
