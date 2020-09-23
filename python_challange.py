import numpy as np
from urllib import request

# http://www.pythonchallenge.com/pc/def/0.html
def ch1():
	print (np.power(2,38))


def char_to_char(arg):
	if arg.isalpha():
		switcher = {
			"y": "a",
			"z": "b",
		}
		return switcher.get(arg, chr(ord(arg)+2))
	else:
		return arg


# http://www.pythonchallenge.com/pc/def/map.html
def ch2():
	# page_source = open("ch2", "r")
	# string = page_source.read()
	string = "map"
	string_replace = ""
	for i in range (len(string)):
		string_replace += char_to_char(string[i])
	# print(string)
	print(string_replace)


# http://www.pythonchallenge.com/pc/def/ocr.html
def ch3():
	page_source = open("ch3", "r")
	string = page_source.read()
	string_char = ""
	for i in range(len(string)):
		if string[i].isalpha():
			string_char += string[i]

	print(string_char)
	page_source.close()


# http://www.pythonchallenge.com/pc/def/equality.html
def ch4():
	page_source = open("ch4", "r")
	string = page_source.read()
	string_char = ""
	len_string = len(string)
	for i in range(4,len_string-5):
		if (string[i]+string[i-4]+string[i+4]).islower() and string[i-4:i+5].isalpha():
			string_upper_check = string[i-3:i] + string[i+1:i+4]
			if string_upper_check.isupper():
				string_char += string[i]
				# print (string[i-4:i+5])
	print (string_char)
	page_source.close()


# http://www.pythonchallenge.com/pc/def/linkedlist.html
# http://www.pythonchallenge.com/pc/def/linkedlist.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
def ch5():
	nothing = int(16044/2)
	print(nothing)
	catch_phrase = "and the next nothing is "
	len_catch_phrase = len(catch_phrase)

	while(str(nothing).isdigit()):
		r = request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(nothing))
		bytecode = r.read()
		htmlstr = bytecode.decode()

		space_idx = -1
		temp_phrase = htmlstr[space_idx-len_catch_phrase:space_idx]

		while (temp_phrase != catch_phrase):
			space_idx = space_idx - 1
			temp_phrase = htmlstr[space_idx-len_catch_phrase:space_idx]

		nothing = htmlstr[space_idx:]
		print("\n" + htmlstr)
		print(nothing)


# http://www.pythonchallenge.com/pc/def/peak.html
# http://www.pythonchallenge.com/pc/def/pickle.html
def ch6():
	print("TBD")

if __name__ == "__main__": 
	ch5()