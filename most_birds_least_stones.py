from tabula import read_pdf
from os import path
from glob import glob 

class_count = 100
class_dict = {}

birds = glob(path.join('.',"*.{}".format('pdf')))

def scrape_pdf(req):
	catalog = read_pdf(req, pages="1")
	for i in range(2, len(catalog)):
		tag = catalog['Unnamed: 0'][i] + catalog['Unnamed: 1'][i]
		if tag not in class_dict:
			class_dict[tag] = req[:-4]
		else:
			class_dict[tag] = class_dict.get(tag) + ", " + req[:-4]
			
for bird in birds:
	scrape_pdf(bird[2:])

listed = 0
for stone in sorted(class_dict, key=lambda stone:len(class_dict[stone].split()), reverse=True):
	if listed < class_count:
		print("Class: " + stone + " | Requirements Met: " + class_dict[stone])
		listed += 1
	else:
		break