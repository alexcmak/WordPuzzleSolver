import os
import pytesseract
from PIL import Image

# this program reads a png file and use Python Tesseract to read words and try to create a word puzzle
#
# You will need to install pytesseract, have that in your PATH
#
# Alex Mak

def ocr_image(png_file):

	try:
		image = Image.open(png_file)

		text = pytesseract.image_to_string(image)

		print('--------- [ OCR ] --------------')
		print(text)
		return text

	except:
		print(f'failed to open {png_file}')
		return ''


def clean_up_text_from_ocr(text):

	print('--------- [ clean up ] --------------')
	# if there are spaces, remove them.

	text = text.replace(' ' ,'')
	text = text.replace('\n\n' ,'\n')

	print(f'{text}')

	return text

# find difference of each number in a list
def diff_consecutive(nums):
	return [nums[i+1] - nums[i] for i in range(len(nums)-1)]

# check if entire list is the same by
# convert list to set and see if only 1 item in set
def all_equal(lst):
  return len(set(lst)) == 1


def determine_rectangle(text):
	#print(text)
	# determine if it is a rectangle by checking distance between each carriage return
	series = [pos for pos, char in enumerate(text) if char == '\n']

	lengths = diff_consecutive(series)

	return (all_equal(lengths))

# insert a separator
# this function is AI generated
def insert_char_between(string, char_to_insert, char_to_exclude):
	result = []
	for c in string:
		if c != char_to_exclude:
			result.append(c)
			result.append(char_to_insert)
		else:
			result.append(c)
	return ''.join(result[:-1])



def convert_image_to_text(png_file):

	text = ocr_image(png_file)
	text = clean_up_text_from_ocr(text)


	file_name, extension = os.path.splitext(png_file)
	text_file = file_name + '.txt'
	with open(text_file, "w") as f:

		text = insert_char_between(text, '\t', '\n')

		f.write(text)
		print(f'{text_file} created')

	if determine_rectangle(text) == True:
		print("yes rectangle puzzle")
	else:
		print("sorry ocr did not read a rectangle")
		return False

	return True

def main():
	filename = input("Enter a file name to convert to text: ");

	convert_image_to_text(filename)


if __name__ == "__main__":
	main()
