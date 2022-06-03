import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
	print("we've called main")

	line = language_file.readline()
	
	if line:
		print_line(line, encoding, errors)
		print("we're about to call main again")
		return main(language_file, encoding, errors)
	else:
		print("no line found, we're not calling main again")
		

def print_line(line, encoding, errors):
	next_lang = line.strip()
	raw_bytes = next_lang.encode(encoding, errors=errors)
	cooked_string = raw_bytes.decode(encoding, errors=errors)
	
	print(raw_bytes, "<===>", cooked_string)
	

languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)
