'''  
  This file is part of a simple example of how the FIGURE8 system works.
	https://github.com/cheri/FIGURE8-demo

  Copyright (c) 2015 Sarah Harmon
  	This source code is free to use under the GNU General Public License (GPL) with author attribution. 

  FUNCTION
  	This file reads in an input text file and searches for a given noun.  	
	Verbs and adjectives that are used in the same context as the 
	provided noun are retrieved using the Nodebox English Linguistics 
	library (available at https://www.nodebox.net/code/index.php/Linguistics).
	
  USAGE
  	From the command line, type "python FindAssocs.py [YOUR NOUN HERE]"
  	The program will return two lists:
  		(1) A list of ADJECTIVES associated by other authors with the noun parameter
  		(2) A list of VERBS associated by other authors with the noun parameter

  INPUT FILE
  	The provided input file of literary text is included as an example, 
  	and contains an eclectic smattering of open source texts from Project 
  	Gutenberg (https://www.gutenberg.org/).    

  	Selected literary texts for this demo include: 
  	 - Fairy Tales (Hans Christian Andersen, as edited by J.H. Stickney): 
  	 	* The Fir Tree
  	 	* Little Tuk   	 	  	 	
  	 	* Little Thumbelina
  	 	* ...and more, from: http://www.gutenberg.org/files/32571/32571-h/32571-h.htm
  	 - Tarzan the Terrible
  	 - Around the World in Eighty Days
  	 - The Three Musketeers
  	 - Desert Gold
  	 - The Count of MonteCristo
  	 - The Scarlet Pimpernel
  	 - Scaramouche
  	 - Heart of Darkness
'''	

import re
import en
import sys
import random

# Looks for whole word w in a sentence, regardless of case.
# Helper function for find_sentences_with_word.  
def find_whole_word(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

# Looks through an input text, and finds all sentences containing a given word.
def find_sentences_with_word(word):
	sentences_with_word = []

	# Read in the file.
	with open('input.txt', 'r') as f:
	    read_data = f.read()
	read_data = read_data.replace("\n", " ")
	 
	# Identify and extract all sentences.
	read_data = read_data.replace("?", ".")
	read_data = read_data.replace("!", ".")
	sentences = read_data.split(".")
	 
	# Remove extraneous punctuation so words might be processed.		
	for idx, sentence in enumerate(sentences):
		sentences[idx] = re.sub('[\":,;]', '', sentence)
	
	# Find sentences with word in them, if any.
	for sentence in sentences:
		if (find_whole_word(word)(sentence) or find_whole_word(en.noun.plural(word))(sentence)):
			sentences_with_word.append(sentence)

	return sentences_with_word

# Example of how to obtain some associated ADJECTIVES with a noun using NodeBox 
# and source of input text.
def get_assoc_adjs(word):	
	listOfWords = []
	
	sentences_with_word = find_sentences_with_word(word)
		
	for sww in sentences_with_word:	
		singleAdjList = en.sentence.find(sww,"(JJ) " + word,chunked=False)
		pluralAdjList = en.sentence.find(sww,"(JJ) " + en.noun.plural(word),chunked=False)
		
		listOfWords = add_words_to_list(singleAdjList, word, listOfWords, True)
		listOfWords = add_words_to_list(pluralAdjList, word, listOfWords, True)

	return listOfWords

# Example of how to obtain some associated VERBS with a noun using NodeBox and 
# a source of input text.
def get_assoc_verbs(word):	
	listOfWords = []
	
	sentences_with_word = find_sentences_with_word(word)
	
	for sww in sentences_with_word:
		patterns = [word + " (VB)", word + " (VBD)", word + " (VBG)", word + " (VBN)", word + " (VBP)",word + " (VBZ)",
					en.noun.plural(word) + " (VB)", en.noun.plural(word) + " (VBD)", en.noun.plural(word) + " (VBG)", en.noun.plural(word) + " (VBN)", en.noun.plural(word) + " (VBP)",en.noun.plural(word) + " (VBZ)"]

		for patt in patterns:
			listOfWords = add_words_to_list(en.sentence.find(sww,patt,chunked=False), en.noun.plural(word), listOfWords, False)

	return listOfWords

# Adds associated words neatly to a list.
# Helper function for get_assoc_adjs and get_assoc_verbs.
def add_words_to_list(list, word, listOfWords, wordIsFirst):
	if list and len(list[0]) > len(word):
		for phrase in list:
			indexOfWord = phrase.find(word)
			if wordIsFirst:
				newWord = phrase[:indexOfWord].strip().lower()
				
				# Ensure no " " + word are in list.
				indexOfSpace = phrase.find(" ")
				if indexOfSpace != -1:
					newWord = phrase[:indexOfSpace]
			else:
				newWord = re.search(r'\\word (\w+)', phrase)
				newWord = phrase[indexOfWord+len(word):].strip().lower()				

				# Ensure plural endings + " " + verb are in list.
				indexOfSpace = phrase.find(" ")
				if indexOfSpace != -1:
					newWord = phrase[indexOfSpace+1:]

			if newWord not in listOfWords and newWord != word and newWord != "":
				listOfWords.append(newWord)
	return listOfWords

# Neatly prints the found associated words for a given noun.
def print_my_assocs(noun):	
	
	print "Process initiated with noun '" + noun + "'.  I'm thinking..."
	assoc_adjs = get_assoc_adjs(noun)
	assoc_verbs = get_assoc_verbs(noun)

	print "*********************************"
	print "I found the following ADJECTIVES associated with " + noun.upper() + ":"
	print assoc_adjs
	print "*********************************"
	print "I found the following VERBS associated with " + noun.upper() + ":"
	print assoc_verbs
	print "*********************************"

def main():
	# If given nouns as arguments, print their associations.
	if len(sys.argv) > 1:
		for arg in sys.argv[1:]:	
			print_my_assocs(arg)

	# Otherwise, print associations for a random default noun.
	else:
		default_noun = random.choice(["anger", "boy", "dreams", "eyes", "girl", "laughter", "music", "sun", "world"])
		print_my_assocs(default_noun)
	
if __name__ == '__main__':
	main()