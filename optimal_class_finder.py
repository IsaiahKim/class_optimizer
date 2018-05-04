from tabula import read_pdf
from os import path
from glob import glob 

class_count = 100
CLASS_LENGTH = 8 # For CU Boulder, tags are of the format ANTH1000, 4 letters and 4 digits

requirements = glob(path.join('.',"*.{}".format('pdf')))

def scrape_pdf(req):  
	catalog = read_pdf(req, pages="all", multiple_tables=True, lattice=True) # Lattice required to read boundries
	for page in range(len(catalog)):
		for i in range(len(catalog[page])):
			try:
				tag = catalog[page][0][i] + catalog[page][1][i] # Class tag
				if (type(tag) is str) and (len(tag) == CLASS_LENGTH): #
					new_tag = tag + "-" + catalog[page][2][i] # Actual Class Name
					if new_tag not in class_dict:
						class_dict[new_tag] = req[:-4] # Removes the .pdf
					else:
						class_dict[new_tag] = class_dict.get(new_tag) + ", " + req[:-4]
			except: # Skips header rows and empty rows
				continue
			
class_dict = {}
for req in requirements:
	scrape_pdf(req[2:])

listed = 0
for course in sorted(class_dict, key=lambda course:len(class_dict[course].split()), reverse=True):
	if listed < class_count:
		print("Class: " + course + " | Requirements Met: " + class_dict[course])
		listed += 1
	else:
		break