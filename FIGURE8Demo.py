'''
  This file is part of a simple example of how the FIGURE8 system works.
	https://github.com/cheri/FIGURE8-demo

  Copyright (c) 2015 Sarah Harmon
  	This source code is free to use under the GNU General Public License (GPL) with author attribution.

  OVERVIEW
	The complete FIGURE8 system writes creative metaphors and similes by:
		- Selecting a tenor.
		- Finding an appropriate vehicle (least semantically similar, with
			few properties in common).
		- Generating a sentence by using imaginative recall on fixed, valid
			grammar constructions.
		- Ranking its generations to decide which one is its "favorite".

	Commonly associated properties for words (e.g. "queen" having a common
		association with "royal") are derived via a JavaScript web scraper on
		online databases (e.g. http://wordassociations.net/).

	Creatively associated words are found with a separate module that learns
		from input literary texts (stored in input.txt).  For an example of how
		these words are discovered, refer to FindAssocs.py.

  USAGE
	From the command line, type "python FIGURE8Demo.py"
  	The demo presented here will:
  		- Select a tenor from NounMetadata.py.
  		- Find three potential vehicles for that tenor.
  		- Generate a fixed simile for each tenor-vehicle pairing.
  		- Rank its comparison based on a few miscellaneous statistics about the pair.

  SAMPLE GENERATION
  	As an example, this demo may generate
  		(1) "The music is curtsying like a princess."
  		(2) "The music is like a shuffling dance."

  	Notably, "music" and "dance" share a higher value of semantic similarity
  	than "music" and "princess".  The complete FIGURE8 system would likely
  	favor the former simile and reject the latter.
'''

import random
from requests import get
import en
import FindAssocs
from NounMetadata import getObjects
import difflib

all_obj = getObjects()

def find_intersection(item1,item2):
	return list(set(item1["assoc"]+item1["color"]) & set(item2["assoc"]+item2["color"]))

def find_num_in_common(item1,item2):
	return len(find_intersection(item1,item2))

def find_perc_in_common(item1,item2):
	return 100*len(find_intersection(item1,item2))/ (len(item1["assoc"])+len(item1["color"])+len(item2["assoc"])+len(item2["color"])-len(find_intersection(item1,item2)))

def get_singular(tenor):
  # Manage exceptions that Nodebox handles poorly.
  # e.g., singular words ending in "ss" are changed to end in "s"
  if tenor!="princess":
    return en.noun.singular(tenor)
  else:
   return tenor

# Makes a simple simile based on fixed grammar constructions.
def make_simile(tenor, vehicle, adj, verb):
  # Obtain singular form of tenor.
  sing_tenor = get_singular(tenor)

  simile = ""
  fixed_forms = [
			"The "+sing_tenor+" is like " + en.noun.article(adj) + " " + vehicle,
			"The "+sing_tenor+" is " + adj + ", like " + en.noun.article(vehicle)
	]

	# Sometimes, the verbs are able to be conjugated by the available NodeBox Linguistics database.
  try:
		fixed_forms.extend([
			"The "+sing_tenor+" is " + en.verb.present_participle(verb) + " like " +  en.noun.article(vehicle),
			"The "+tenor+" " + en.verb.past(verb,person=1) + " like " + en.noun.article(adj) + " " + vehicle,
			"The "+tenor+", like " + en.noun.article(adj) + " " + vehicle + ", " +  en.verb.past(verb,person=1)
		])
		simile = random.choice(fixed_forms)

  except KeyError, e:
		print "(KeyError: Verb unavailable for NodeBox conjugation.)\n"
		simile = random.choice(fixed_forms)

  return simile

# Finds a vehicle associated with a tenor.
def find_vehicle(tenor):
	a = tenor["assoc"]
	vehicle = tenor
	b = []
	while (set(a).isdisjoint(b) or tenor["name"]==vehicle["name"]):
		vehicle = random.choice(all_obj)
		b = vehicle["assoc"]
	return vehicle

# Returns the semantic similarity between two words.
def sss(s1, s2, type='concept', corpus='webbase'):
    sss_url = "http://swoogle.umbc.edu/SimService/GetSimilarity"
    try:
        response = get(sss_url, params={'operation':'api','phrase1':s1,'phrase2':s2,'type':type,'corpus':corpus})
        return float(response.text.strip())
    except:
        print("Error in getting semantic similarity.")
        return 0.0

# Returns a value indicating the degree of similarity between two input strings, or an input
# string and an array of strings.
def similarity(str1, str2):
	return difflib.SequenceMatcher(None,str1, str2).ratio()

# Prints a simple ranking of the comparison between a tenor and vehicle.
def rank_comparison(tenor, vehicle, metaphor):
	# Semantic similarity.
	sem_sim = sss(tenor["name"], vehicle["name"])
	str_sim = similarity(tenor["name"], vehicle["name"])

	# Conceptual (Semantic) similarity.
	print("SemSim("+ tenor["name"] + ", " + vehicle["name"] + "): " + str(sem_sim))

	# String similarity.
	print("DiffLibSeqSim("+ tenor["name"] + ", " + vehicle["name"] + "): " + str(str_sim))

	# Number of properties in common.
	print("Properties in Common: " + str(find_intersection(tenor,vehicle)))
	print("Percentage of Common Properties: " + str(find_perc_in_common(tenor,vehicle)))
	print("Shares major category? ") + str(tenor["type"]==vehicle["type"])

def main():
	# Choose a tenor at random from NounMetaData.py.
	tenor = random.choice(all_obj)

	print "*********************************"
	print "THE TENOR IS: " + tenor["name"]

	# Find three vehicles for the tenor.
	for y in range(0, 3):
		print "*********************************"
		vehicle = find_vehicle(tenor)

		print "The #" + str(y+1) + " VEHICLE is " + vehicle["name"]

		# Find associated creative words to construct a simile.
		adj=random.choice(vehicle["adj"])
		verb=random.choice(vehicle["verb"])

		if (verb != "[VERB]" and adj != "[ADJ]"):
			print "THE VERB IS " + verb
			print "THE ADJ IS " + adj

			simile = make_simile(tenor["name"], vehicle["name"], adj, verb)

			print("SIMILE: '" + simile + ".'")

			### RANK GENERATION ###
			print "\nRANKING STATISTICS"
			rank_comparison(tenor,vehicle,simile)

	print "*********************************"

if __name__ == '__main__':
	main()
