''' 
  This file is part of a simple example of how the FIGURE8 system works.
	https://github.com/cheri/FIGURE8-demo

  Copyright (c) 2015 Sarah Harmon
  	This source code is free to use under the GNU General Public License (GPL) with author attribution. 

  FUNCTION
    The FIGURE8 system generates a file like this containing metadata for 
    generating figurative language.  

    The metadata in this example includes basic properties about each noun in the 
    knowledge base.  These properties are:
     - object name
     - object type (major category)
     - commonly-associated properties 	(collected via web scraper)
     - commonly-associated colors 		(collected via web scraper)
     - creatively-associated adjectives (found with FindAssocs.py)
     - creatively-associated verbs 		(found with FindAssocs.py)
'''

objects = [
	# Food-related nouns.
	{"name":"apple", "assoc":["round","sour","sweet","juicy","edible","crunch","crisp","fresh","fruit"],
				     "color":["green","red"],
				     "type":"food",
					 "adj":['gilded', 'wild', 'little', 'big','spiced','rotten','withered','fragrant','gnarled'],
					 "verb":['blossom','bloom','ferment','shrivel','bite']
	},
	
	{"name":"grape", "assoc":["round","sour","sweet","juicy","edible","fresh","fruit"],
				     "color":["purple","blue","green","white"],
				     "type":"food",
					 "adj":['white', 'French', 'perfumed', 'nourishing','luscious','sour','ripened','juicy','wild','pickled','spiced'],
					 "verb":['hang','fell']
	},

	{"name":"water","assoc":["pure","sweet","wet","fresh","edible"],
				     "color":["blue","transparent"],
				     "type":"drink",
					  "adj":['bright', 'blue', 'smooth', 'great', 'clear', 'pure', 'deep', 'open', 'stagnant', 'cold', 'placid', 'dark', 'moonlit', 'quiet', 'fine', 'sour', 'last', 'little', 'muddy', 'sweet', 'scented', 'cool', 'big', 'sure', 'futile', 'subterranean', 'perfumed', 'stormy', 'iced', 'sugared', 'high', 'silvery', 'yellow', 'strong'],
					  "verb":['closed', 'swimming', 'close', 'crackled', 'flowed', 'seized', 'became', 'trickled', 'ran', 'thundering', 'flanked', 'tumbled', 'glimmering', 'grasping', 'soaked', 'beating', 'raised', 'existed', 'cried', 'began', 'hold', 'did', 'left', 'welled', 'revived', 'narrowed', 'covered', 'jarred', 'gone', 'waving', 'passed', 'kept', 'rushes', 'tinged', 'sunk', 'drown', 'rolling', 'sprouted', 'shone', 'thickened', 'surrounded', 'being']
	},

	# Nouns that represents kinds of animals.
	{"name":"turtle", "assoc":["slow","quiet","natural","round","animal"],
						"color":["green"],
						"type":"animal",
						"adj":["armored","sandy","striped"],
						"verb":['swarming','eat']
	},
	
	{"name":"cat", "assoc":["stealthy","quiet","quick","selfish","agile","graceful","alert","sensual","intelligent","natural","soft"],
				   "color":["black","white","brown","orange"],
				   "type":"animal",
				   "adj":['great', 'lesser', 'yellowish', 'dead'],
				   "verb":['fell', 'flattened', 'screaming', 'believed', 'looks', 'reposed', 'obtruded']
	},
	
	{"name":"serpent", "assoc":["stealthy","dangerous","quiet","intelligent","natural"],
					   "color":["black","white","green","red"],
					   "type":"animal",
					   "adj":["fiery","fascinating"],
					   "verb":["entwined"]	
	},
	
	{"name":"bird","assoc":["beautiful","free","happy","natural","sweet","musical"],
				   "color":["red","orange","yellow","green","blue","purple","white","black"],
				   "type":"animal",
				   "adj":['wooden', 'proud', 'latest', 'little', 'beautiful', 'happy', 'other', 'young', 'royal', 'poor', 'dark-gray', 'dead', 'perfect', 'wild', 'large', 'white', 'foreign', 'strange', 'voracious', 'Large', 'estimable', 'wide-winged', 'monstrous', 'rare'],
				   "verb":['building', 'sing', 'jumped', 'cried', 'felt', 'painted', 'lay', 'are', 'took', 'began', 'sang', 'flew', 'fell', 'flying', 'flies', 'frightened', 'rose', 'whistled', 'beating', 'falling', 'retaining', 'skimming', 'drying']
	},

	# Nouns that represents kinds of people.	
	{"name":"king", "assoc":["old","royal","powerful"],
					   "color":[],
					   "type":"person",
					   "adj":['new', 'modern', 'chief', 'late', 'first', 'unfortunate', 'great', 'peace-loving', 'good', 'free', 'shadowy', 'French'],
					   "verb":['explained', 'thinking', 'awaits', 'stood', 're-entered', 'entered', 'mumbled', 'looked', 'replied', 'defies', 'lunged','pales', 'seeking', 'listen', 'began', 'answered', 'knew', 'fell',  'consented', 'advancing', 'taking', 'looking', 'waved', 'commanded', 'watched', 'abandons', 'excited', 'flew', 'wished', 'feared', 'signed', 'nothing', 'turned', 'employs', 'took', 'make', 'asked', 'attacked', 'perceived', 'retiring', 'speaks', 'accustomed', 'desired', 'appeared', 'made', 'returned', 'opened', 'trembled', 'advanced', 'danced', 'counted', 'called', 'entertained', 'holding', 'held', 'halted', 'judged', 'granted', 'thanked', 'exchanged', 'inviting', 'continuing', 'laughed', 'betraying', 'addressing', 'inspired', 'driven', 'issued', 'remained', 'meet']
	},
	
	{"name":"princess", "assoc":["royal","powerful","beautiful"],
					   "color":[],
					   "type":"person",
					   "adj":['splendid', 'old', 'gallant', 'poor','fairy','widowed','young','gracious','Egyptian','winsome'],
					   "verb":['curtsy','sleeping']
	},	

	{"name":"prince", "assoc":["royal","powerful","beautiful"],
					   "color":[],
					   "type":"person",
					   "adj":['little', 'handsome', 'real', 'young', 'gracious', 'Italian', 'dear', 'worthy', 'unhappy', 'idle'],
					   "verb":['acting', 'travelling','entered', 'returned', 'looked', 'offering']
	},	

	{"name":"queen", "assoc":["royal","powerful","beautiful"],
					   "color":[],
					   "type":"person",
					   "adj":['poor', 'beautiful', 'unfortunate', 'true', 'young', 'noble', 'little', 'Austrian','imprisoned'],
					   "verb":['kissed', 'leaving', 'cried', 'thought', 'begging', 'blushing', 'murmured', 'remain', 'looked', 'conspires', 'laid', 'sank', 'pressed', 'loves', 'felt', 'turned', 'uttered', 'took', 'ran', 'speaking', 'concealed', 'wants', 'speak', 'protect', 'gave', 'requires', 'entered', 'remained', 'bent', 'affecting', 'resumed', 'appeared', 'send', 'saving', 'charged', 'followed', 'fallen']
	},	

	# Nouns that represent buildings.
	{"name":"castle", "assoc":["old","strong","royal"],
					   "color":[],
					   "type":"building",
					   "adj":['royal', 'high', 'several', 'strong', 'lofty', 'old', 'fabulous','feudal', 'impregnable', 'medieval', 'fortified', 'enchanted', 'gothic', 'norman', 'mediaeval', 'moorish', 'ruined', 'rebuilt', 'ancestral', 'doubting', 'ducal', 'steep', 'defended', 'stately', 'ruinous', 'situated', 'walled', 'defensible', 'airy', 'dangerous', 'tin', 'crumbling', 'towered', 'nameless', 'princely', 'precipitous', 'sequestered', 'picturesque', 'welsh', 'lodged', 'perched', 'guarded', 'scottish', 'quartered', 'architectural', 'crowned', 'inaccessible', 'massy', 'neighbouring', 'twelfth', 'dilapidated', 'wooded', 'scots', 'craggy', 'inhabited', 'haunted', 'sumptuous'],
					   "verb":['rose', 'stood', 'telling', 'built']
	},

	# Nouns that are associated with music.
	{"name":"song", "assoc":["musical","beautiful"],
					   "color":[],
					   "type":"music",
					   "adj":['beautiful', 'old', 'religious', 'more', 'cheerful', 'dreadful', 'comic', 'melodious', 'plaintive', 'musical', 'sweet', 'rhythmical', 'favorite', 'gaelic', 'joyous', 'discordant', 'rapturous', 'spring', 'popular', 'composing', 'convivial', 'mournful', 'blithe', 'patriotic', 'operatic', 'glad', 'slavic', 'monotonous', 'jubilant', 'lugubrious', 'sentimental', 'battle', 'metrical', 'sonorous', 'composed', 'scottish', 'exultant', 'doleful', 'elizabethan', 'licentious', 'war', 'merry', 'funeral', 'joyful', 'immortal', 'wailing', 'devotional', 'festive', 'satirical', 'rowdy', 'cheery', 'wandering', 'amorous', 'lively', 'obscene', 'pastoral', 'nonsensical', 'magic', 'triumphal', 'ceaseless', 'auld', 'wood', 'lusty', 'deathless', 'gay', 'drear', 'jovial', 'balmy', 'harmonious', 'poetical', 'enchanting', 'exquisite', 'poetic', 'wordless', 'thrilling'],
					   "verb":['came', 'mingled', 'disturb', 'delighted', 'accompanied']
	},

	{"name":"dance", "assoc":["musical","happy"],
					   "color":[],
					   "type":"music",
					   "adj":['wild', 'merry','graceful', 'nimble', 'singing', 'joyous', 'stately', 'tribal', 'pretty', 'lascivious', 'macabre', 'weirdly', 'piped', 'performing', 'festive', 'rhythmical', 'lewd', 'lively', 'footed', 'shuffling', 'informal', 'doleful', 'decorous', 'ravishing', 'gay', 'wayward', 'unholy', 'improvised', 'quivered', 'frenzied', 'fantastic', 'obscene', 'lyrical', 'courtly', 'scenic', 'sports', 'coordinated', 'naked', 'licentious', 'monotonous', 'molten', 'wood', 'plaintive', 'fairy', 'nee', 'harmonious', 'interminable', 'dainty', 'joyful', 'unbecoming', 'impassioned', 'musical', 'playful', 'masked', 'ended', 'moonlit'],
					   "verb":['according','ending','daring']
	},

	{"name":"music", "assoc":["musical","beautiful"],
					   "color":[],
					   "type":"music",
					   "adj":['deep', 'beautiful', 'merry', 'chamber', 'operatic', 'tinny', 'classical', 'melodious', 'discordant', 'rhythmical', 'rock', 'plaintive', 'sweet', 'ravishing', 'harmonious', 'lyrical', 'singing', 'martial', 'heavenly', 'enchanting', 'raucous', 'sensuous', 'voluptuous', 'exquisite', 'church', 'secular', 'soft', 'devotional', 'loud', 'sonorous', 'unearthly', 'poetic', 'jubilant', 'soothing', 'celestial', 'gay', 'triumphal', 'tuned', 'festive', 'fond', 'mournful', 'dramatic', 'muted', 'monotonous', 'concerted', 'mim', 'glad', 'scenic', 'lively', 'weird', 'artistic', 'joyous', 'magic', 'barbaric', 'inaudible', 'thrilling', 'resounding', 'toned', 'dreamy', 'descriptive', 'reedy', 'composed', 'italian', 'melancholy', 'blended'],
					   "verb":['went', 'dancing', 'produced', 'seemed']
	},

	# Parts of the body.
	{"name":"eye", "assoc":["round","beautiful"],
					   "color":["amber","blue","brown","grey","green","hazel","red","violet"],
					   "type":"body part",
					   "adj":['blue', 'thine', 'old', 'envious', 'bright', 'clear', 'clever', 'own', 'sparkling', 'mild', 'yellow-green', 'black', 'beady', 'keen', 'fierce', 'other', 'wary', 'weak', 'little', 'reptilian', 'cunning', 'hollow', 'gray', 'careful', 'fishy', 'wide-open', 'sharp', 'haggard', 'fine', 'great', 'curious', 'angry', 'big', 'haughty', 'quick', 'beautiful', 'vigilant', 'dark', 'jealous', 'greedy', 'eager', 'intelligent', 'favorable', 'large', 'inflamed', 'ardent', 'brilliant', 'glassy', 'sad', 'luminous', 'weary', 'haunting', 'wonderful', 'dark-blue', 'alert', 'speculative', 'somber', 'human', 'photographic', 'gloomy', 'naked', 'unbelieving', 'thoughtful', 'magnificent', 'inscrutable', 'prominent', 'shrewd', 'glad', 'amber', 'strange', 'animated', 'penetrating', 'perforated', 'vacant', 'open', 'deep-set', 'dim', 'calm', 'red', 'downcast', 'fiery', 'prying', 'lustrous', 'dear', 'eloquent', 'dull', 'bold', 'enormous', 'expressive', 'bloodshot', 'indiscreet', 'immortal', 'moistened', 'fascinating', 'implacable', 'glaring', 'feeble', 'languid', 'brown', 'sunken', 'yellow', 'pale', 'lazy', 'sharpest', 'small', 'malicious', 'feverish', 'liquid', 'gentle', 'fevered', 'restless', 'Fierce', 'paternal', 'grave', 'flaming', 'hazel', 'sombre', 'critical', 'wistful', 'fearful', 'troubled', 'intense'],
					   "verb":['fixed', 'glared', 'think', 'sparkled', 'snapped', 'opened', 'straining', 'glittering', 'scanned', 'filled', 'turned', 'glancing', 'loomed', 'looked', 'wandered', 'resulting', 'followed', 'widened', 'registered', 'reflected', 'seen', 'narrowed', 'dropped', 'fell', 'staring', 'raised', 'peering', 'gazed', 'glistening', 'dishevelled', 'resumed', 'glistened', 'interpreted', 'fastened', 'brightened', 'lost', 'donated', 'embraced', 'laughed', 'plunged', 'took', 'reading', 'dazzled', 'asked', 'shone', 'crammed', 'flashed', 'remember', 'reddened', 'cried', 'repeated', 'began', 'shut', 'darkened', 'became', 'spoke', 'emitted', 'seemed', 'gazing', 'gleamed', 'searching', 'watching', 'caught', 'saw', 'beamed', 'met', 'snapping', 'remained', 'searched', 'roved', 'swept', 'follow', 'unclosed', 'held', 'dilating', 'flashing', 'sought', 'reminded', 'are', 'made', 'burned', 'peeled', 'brimming', 'beginning', 'streaming', 'blazing', 'narrowing', 'stick', 'surveyed', 'cleared', 'watched', 'glowing', 'darted', 'covered', 'see', 'started', 'pierce', 'injected', 'remaining', 'lighted', 'complained', 'habituated', 'hooked', 'bathed', 'gave', 'bandaged', 'closed', 'entered', 'blindfolded', 'veiled', 'glanced', 'resembled', 'been', 'swam', 'retired', 'consists', 'dilated', 'runs', 'sufficed', 'shaded', 'bade', 'beaming', 'passed', 'rested', 'starting', 'expressing', 'placed', 'interrogated', 'endeavoring', 'evinced', 'continued', 'accustomed', 'demanded', 'suffused', 'ordered', 'appeared', 'suppose', 'heaving', 'expanded', 'reaching', 'expressed', 'supplying', 'stood', 'rolled', 'ran', 'felt', 'acquired', 'endeavored', 'twinkled', 'streamed', 'glowed', 'glittered', 'softened', 'dancing', 'aching', 'circled', 'peered', 'twisting', 'be', 'straying', 'grew', 'screwed', 'betrayed', 'regaled', 'devouring', 'kept', 'eluded', 'blazed', 'conned', 'mouldered', 'buried', 'observed', 'regarding', 'announced', 'set', 'kindled', 'questioned', 'hesitating', 'scanning', 'stared', 'rolling', 'forgot']},

	{"name":"mouth",   "plural":False,
					   "assoc":["round","red","tight"],
					   "color":["red"],
					   "type":"body part",	
					   "adj":['thin-lipped', 'wide-open', 'dark', 'charming', 'perfect', 'own', 'mobile', 'childlike', 'sad', 'strong', 'curved', 'wide', 'menacing', 'long'],
					   "verb":['became', 'passing', 'seemed', 'constituted', 'watered', 'reflected', 'affords', 'repeated', 'gave', 'bewildered', 'do', 'shut', 'hesitated', 'turned', 'pressed', 'chiselled', 'contracted', 'stood', 'hardened', 'gagged', 'growing', 'twisted', 'stretched', 'fell']
						},

	{"name":"ears",    "plural":True,
					   "assoc":["round","slender"],
					   "color":["brown","orange"],
					   "type":"body part",
					   "adj":['long', 'human', 'deaf', 'keen', 'willing', 'quick', 'own', 'menacing', 'mortal', 'sensitive'],
					   "verb":['rang', 'detected', 'warned', 'bore', 'caught', 'began', 'stretching', 'chafed', 'whispering', 'took', 'ringing', 'pleading', 'hear', 'mingled', 'kept', 'attuned']
						},
	
	# Celestial.
	{"name":"moon", "assoc":["round","big","space","natural","dry"], 
				       "color":["grey","white","silver"],
				       "type":"celestial",
					   "adj":['African', 'slender', 'weary', 'huge', 'misshapen', 'burned-out', 'desolate', 'pale', 'fitful', 'bright', 'inflamed'],
					   "verb":['shone', 'rose', 'voiced', 'broke', 'lessened', 'soared', 'afforded', 'climbed', 'slanted', 'haunted', 'lighted', 'strove', 'hidden', 'shedding', 'resembled', 'shining', 'showed', 'looked', 'sailed']},

	{"name":"sun", "assoc": ["round","big","space","natural","hot"], 
				       "color":["yellow","red"],
				       "type":"celestial",
					   "adj":['warm', 'beautiful', 'bright', 'brilliant', 'hot', 'western', 'new', 'tropical', 'fierce', 'red', 'white', 'rosy', 'sub-tropical', 'northern', 'ardent', 'autumnal','cloudless', 'bleached', 'slanting', 'shining', 'mid', 'dappled', 'vernal', 'solar', 'tropical', 'fleecy', 'blazing', 'tanned', 'autumnal', 'resplendent', 'balmy', 'bright', 'hot', 'gravitational', 'molten', 'sultry', 'dewy', 'shaded', 'dried', 'sparkling', 'glittering', 'nebulous', 'cloudy', 'tops', 'topmost', 'diffused', 'rosy', 'luminous', 'reflecting', 'fiery', 'watery', 'broiling', 'baked', 'declining', 'western', 'up', 'blistered', 'parched', 'down', 'gilded', 'hazy', 'tinted', 'eastern', 'wintry', 'pitiless', 'peeping', 'gaseous', 'fervid', 'glaring', 'revolving', 'sunk', 'descending', 'crested', 'flaming', 'stellar', 'still', 'terrestrial', 'planetary', 'incandescent', 'misty', 'ethereal', 'burnt', 'leafy', 'verdant', 'refreshing', 'exposed', 'shady', 'sheltered', 'reflected', 'streaked', 'milky', 'coppery', 'clear', 'lurid', 'radiant', 'genial', 'bareheaded', 'blue', 'glorious'],
					   "verb":['shone', 'shines', 'rose', 'shining', 'warmed', 'dispelled', 'dropped', 'topped', 'stands', 'descended', 'pass', 'penetrated', 'lost', 'burned', 'turn', 'set', 'cleared', 'blazed', 'sloped', 'grew', 'began', 'soared', 'beating', 'hidden', 'climbed', 'passed', 'greeted', 'glowed', 'hung', 'tinged', 'seemed', 'disappears', 'advanced', 'done', 'shed', 'disappeared', 'rises', 'sank', 'hanging']},

	{"name":"world", "assoc":["round","natural","big","space"],
					   "color":[],
				       "type":"celestial",
					   "adj":['wide', 'great', 'whole', 'stupid', 'outer', 'dead', 'savage', 'little', 'entire', 'silent', 'desolate', 'strange', 'scientific', 'terrible', 'burned-out', 'particular', 'grateful', 'visionary', 'fashionable', 'many', 'political', 'literary', 'cosmopolitan', 'real', 'glorious', 'mad', 'beautiful', 'inconceivable'],
					   "verb":['thought', 'appeared', 'differed', 'took', 'grown', 'completed', 'knows', 'humiliated', 'replied', 'stands', 'leave', 'belongs', 'dies', 'counting', 'filled', 'deceived', 'called', 'grows', 'traverse', 'returned', 'did', 'aided', 'are', 'calls', 'shaking', 'displayed', 'contains', 'nothing', 'obeyed', 'stood', 'knew', 'allowing']},

	# Items.
	{"name":"clock", "assoc":['round','artificial'], 
				       "color":[],
				       "type":"item",
					   "adj":['old', 'electric', 'ponderous', 'astronomical', 'big', 'Italian'], 
					   "verb":['talked', 'struck', 'directed', 'indicated', 'pointed', 'shows', 'rose', 'counting', 'gave']},

	# Natural entities. 
	{"name":"rain", "assoc":["cold","wet","pure","clean","natural","fresh"], 
					  "color":["blue"],
					  "type":"of-earth",
					  "adj":['steady', 'golden', 'heavy', 'incessant'],
					  "verb":['beating', 'continued', 'pouring', 'touched', 'concluded', 'extinguished']},
	
	{"name":"snow", "assoc":["cold","wet","pure","clean","natural","fresh"], 
					  "color":["blue"],
					  "type":"of-earth",
					  "adj":['cold', 'eternal', 'powdered', 'feathery','slippery'],
					  "verb":['lay', 'covers', 'crackled', 'began', 'beat', 'fell', 'covered', 'blown', 'marked']},					  

    # Valuables.
	{"name":"pearl", "assoc":["round","rare","pure","beautiful","natural"],
					   "color":['white','silver'],
					   "type":"valuable",
					   "adj":["inlaid","iridescent","studded","priceless","garnished","jewelled","lustrous","costly","bombed","plaited","strung","decked","hued","handled","peerless","gold",'false', 'loveliest', 'liquid', 'richest'],
					   "verb":['lying', 'fell']},

	# Electronics. 
	{"name":"wire", "assoc":["slender","artificial"],
					   "color":[],
					   "type":"electronics",
					   "adj":['telegraphic', 'magnetic'],
					   "verb":["grating"]}, 	    

    # Plants.
	{"name":"tree", "assoc":["tall","natural","heavy"],
					  "color":["green","brown"],
					  "type":"plant",
					  "adj":["luxuriant","planted","feathery","shaded","tropical","dense","leafless",'other', 'tallest', 'noble', 'young', 'poor', 'dark', 'elder', 'little', 'old', 'large', 'blue', 'beautiful', 'great', 'cherry', 'second', 'gnarled', 'nearest', 'leafy', 'nearby', 'own', 'single', 'tall', 'Tall', 'genealogical', 'olive', 'fine', 'same', 'big', 'rare', 'secular'],
					  "verb":['was', 'did', 'grew', 'wished', 'trembling', 'fell', 'trembled', 'presented', 'tried', 'remained', 'became', 'told', 'thought', 'related', 'sighed', 'rejoicing', 'saw', 'overlooking', 'bent', 'clustering', 'rose', 'stood', 'rustled', 'talked', 'nodded', 'covered', 'sat', 'smelled', 'sent', 'decked', 'sloping', 'sprouted', 'continued', 'spreading', 'Spring', 'waving', 'brought', 'made', 'exposed', 'seeking', 'waved', 'carrying', 'having', 'waiting', 'blocked', 'touched', 'overarched', 'seemed', 'loomed', 'deepened', 'appeared', 'detached', 'profiled', 'contained', 'lined', 'seen', 'flashed', 'watching', 'lighted', 'growing', 'consists', 'forsakes', 'betrayed', 'found', 'reclining', 'concealed', 'situated', 'shaken', 'leaning', 'lashed', 'projected', 'swayed', 'looking']},

	
	{"name":"flower", "assoc":["clean","natural","light","weak","beautiful","pure","slender"],
						"color":["red","orange","yellow","green","blue","purple","pink"],
						"type":"plant",
						"adj":['planted', 'sweet', 'lovely', 'bloomed', 'fragrant', 'decked', 'perfumed', 'wilted', 'scented', 'odorous', 'leaved', 'starred', 'floral', 'showy', 'variegated', 'luxuriant', 'withered', 'balmy', 'choice', 'decorated', 'potted', 'twining','purplish', 'damask', 'vernal', 'dewy', 'redolent', 'sunny', 'hued', 'alpine', 'pansy', 'garnished', 'bordered', 'verdant', 'flaunting', 'crowned', 'tropical','spangled', 'leafless', 'patterned', 'creamy', 'gorgeous', 'plucked', 'waxy', 'waxen', 'velvety', 'tubular', 'purple', 'autumnal', 'scarlet', 'shady', 'artificial', 'leafy', 'feathery', 'starry', 'tasteful', 'dainty', 'fair', 'decorative','colorful', 'tinted', 'honeyed', 'flowery', 'laden', 'gaudy', 'gauzy', 'limpid','symbolical', 'inlaid', 'shaded', 'inconspicuous', 'overgrown', 'bright', 'poor', 'prettiest', 'single', 'empty', 'sick', 'other', 'happy', 'dead', 'handsome', 'beautiful', 'red', 'white', 'elder', 'real', 'yellow', 'few', 'artificial', 'little', 'golden', 'withered', 'humble'],
						"verb":['adorn', 'seed', 'leaf', 'blossom', 'bloom', 'bunch', 'wither', 'wreathe', 'strew', 'festoon', 'sprig', 'decorate', 'weed', 'transplant', 'twine', 'deck', 'embroider', 'ripen', 'ornament', 'color', 'bud', 'carpet', 'pluck', 'beautify', 'sow', 'distil', 'droop', 'mow', 'landscape', 'fringe', 'scent', 'turf', 'soil', 'waft', 'entwine', 'fashion', 'sprinkle', 'plant', 'grow', 'mingle']},					  
	
	# Related to the air.
	{"name":"breeze", "assoc":["clean","natural","light","fresh"],
						"color":[],
						"type":"air",
						"adj":["balmy","refreshing","fitful","sprung","gusty","salty","scented","cloudless","sultry","vernal","fragrant","cloudy","eastward","cool","perfumed","spicy","humid","redolent","gauzy","fresh","leafy","choppy","fleecy","stiff","inconstant","downwind","laden","odorous","pungent","autumnal","tropical","exhilarating","blown","faint","delicious","tops","heeled","nearby","wispy","filmy","oppressive","caressing","silken","loving","acrid","glassy","languid","sluggish","favourable","sparkling","hazy","airy","chilled","stifling","prevailing",'gentle', 'brisk', 'capricious', 'fragrant', 'languid', 'fresh', 'fair', 'autumnal'],
						"verb":['arose', 'subsided', 'fanning', 'sighed', 'whispering', 'ceased']},
	
	# Geographical features.
	{"name":"mountain", "assoc":["tall","immobile","big","strong","powerful","pure"],
						"color":["green","white"],
						"type":"landscape",
						  "adj":['rocky', 'capped', 'steep', 'precipitous', 'rugged', 'craggy', 'purple', 'alpine', 'inaccessible', 'snowy', 'delectable', 'blue', 'barren', 'volcanic', 'tops','copper', 'polar', 'towering', 'desolate', 'terraced', 'wooded', 'lofty', 'impassable', 'surrounding', 'trackless', 'alluvial', 'jagged', 'riven', 'misty', 'towered', 'western', 'bleak', 'ghost', 'fertile', 'coastal', 'timbered','highest', 'lofty', 'numerous', 'towering', 'distant', 'little', 'inaccessible', 'high', 'dim', 'black', 'bold', 'mysterious', 'Distant', 'wild', 'low', 'inverted', 'nameless', 'mighty', 'small'],
						  "verb":['covered', 'glowing', 'well-watered',  'blocked', 'replied', 'emptied', 'brought', 'clothed', 'turns',  'lining', 'cried', 'bounded', 'hemmed', 'loomed', 'changed', 'showed', 'dulled', 'spiring', 'hung', 'appeared', 'began', 'beholds']},

	{"name":"garden", "assoc":["clean","natural","light","beautiful","pure"],
						"color":[],
						"type":"landscape",
						"adj":['large', 'Botanical', 'beautiful', 'little', 'tasteful', 'charming', 'green', 'shady', 'magnificent', 'fine', 'small', 'old'],
						"verb":['lived', 'begins', 'stood', 'deserted', 'bordered', 'connected', 'consisting', 'planted', 'isolated', 'built', 'laid', 'plucking', 'shut', 'being', 'sent', 'ornamented', 'assumed', 'became', 'belonged', 'bathed', 'looked', 'inviting', 'denuded', 'considered', 'sauntered', 'taking', 'came']},

	{"name":"cliff", "assoc":["tall","natural","dangerous"],
					   "color":[],
					   "type":"landscape",
					   "adj":['precipitous', 'overhanging', 'overhung', 'towering', 'chalky', 'craggy', 'rocky', 'rugged', 'towered', 'inaccessible', 'riven', 'jagged', 'crumbling', 'grassy', 'steep', 'sloping', 'impassable', 'wooded', 'sheltered', 'hewn', 'layered', 'walled', 'perched', 'cornish', 'volcanic', 'tops', 'weathered', 'stupendous', 'inland', 'eroded', 'lofty', 'forbidding', 'alluvial', 'tumbled', 'stony', 'bounded', 'ascending', 'stunted', 'crashing', 'mossy', 'reverberating', 'bordered', 'coastal', 'alpine', 'precarious', 'holed', 'flinty', 'sandy', 'abrupt', 'crowned', 'clinging', 'reddish', 'rock', 'descending', 'crested', 'frowning','low', 'towering', 'great', 'opposite', 'natural', 'white', 'miniature', 'sheer', 'steep', 'dark', 'red', 'rugged', 'stony', 'rocky', 'tall'],
					   "verb":['taking', 'searching', 'examining', 'looming', 'stepped', 'rising', 'saluted', 'echoed', 'keep', 'frowned', 'appeared']},

	{"name":"lake", "assoc":["wet","natural","calm","fresh","clean","beautiful","pure","cold"],
					  "color":["blue","green","silver"],
					  "type":"landscape",
					  "adj":['salt', 'brackish', 'shallow', 'marshy', 'navigable', 'inland', 'glacial', 'swampy', 'alpine', 'reedy', 'placid', 'limpid', 'wooded', 'stagnant', 'unruffled','dry', 'blue', 'caspian', 'upper', 'crystal', 'glassy', 'alluvial', 'dotted', 'overhung', 'situated', 'indented', 'underground', 'fishing', 'precipitous', 'volcanic', 'grassy', 'trackless', 'eastward', 'molten', 'bordered', 'frozen', 'arctic', 'picturesque', 'mountainous', 'northern', 'rocky', 'verdant', 'still', 'pine', 'swiss', 'fertile', 'scenic', 'fore', 'silver', 'canadian', 'diversified','deep', 'transparent', 'blue', 'dark', 'large', 'largest', 'second', 'great', 'sacred', 'beautiful', 'narrow', 'dusty', 'white', 'immense'],
					  "verb":['broken', 'sat', 'lay', 'called', 'extending']},

	{"name":"forest", "assoc":["natural","dangerous","beautiful","dark","green"],
						"color":["green"],
						"type":"landscape",
						"adj":['hilly', 'rugged', 'rocky', 'primeval', 'coastal', 'trackless', 'dense', 'leafy', 'swampy', 'tropical', 'impenetrable', 'leafless', 'scrubby', 'enchanted', 'verdant', 'marshy', 'timbered', 'felled', 'luxuriant', 'green', 'grassy', 'dappled', 'wooded', 'leaved', 'fore', 'stunted', 'unbroken', 'mossy', 'tangled', 'untamed', 'unexplored', 'gigantic', 'arable', 'uncultivated', 'bordered', 'sombre', 'moonlit', 'wild', 'autumnal', 'gnarled', 'sparse', 'petrified', 'dotted', 'mountainous', 'tops', 'woody', 'blanketed', 'boundless', 'tilled', 'sunlit', 'drear','shady', 'fertile', 'diversified', 'wood', 'thick', 'overgrown', 'starlit', 'illimitable', 'impassable', 'uninhabited', 'savage', 'interminable', 'precipitous', 'towering', 'stringy', 'majestic', 'alluvial', 'peopled', 'gloomy', 'siberian', 'decaying', 'steep', 'cultivated', 'encircling', 'accursed', 'clad', 'giant','fragrant','wide', 'green', 'perfect', 'whole', 'thick', 'great', 'dense', 'dark', 'ancient', 'miniature', 'nearby', 'verdant', 'Indian', 'Vast', 'small', 'primeval', 'virgin', 'impenetrable'],
						"verb":['turned', 'called', 'glowed', 'searching', 'circling', 'penetrated', 'followed', 'inhabited', 'pausing', 'declare', 'expecting', 'stood', 'surrounded']},

	{"name":"desert", "assoc":["natural","dangerous","dry"],
						"color":["orange"],
						"type":"landscape",
						"adj":['rocky', 'arid', 'trackless', 'arabian', 'nomadic', 'inhospitable', 'stranded','deserted', 'parched', 'mongolian', 'syrian', 'illimitable', 'arab', 'uninhabited', 'barren', 'fertile', 'sandy', 'sterile', 'stony', 'caspian', 'forlorn', 'impassable', 'parthian', 'limitless', 'mountainous', 'featureless', 'thirsty', 'coastal', 'egyptian', 'swampy', 'populous', 'reclaimed', 'enlisted', 'boundless', 'salt', 'abandoned', 'inhabited', 'pitiless', 'alluvial', 'sparse', 'deserted', 'mined', 'baked', 'tawny', 'mediterranean', 'prickly', 'australian', 'dreary', 'peopled', 'stark', 'eastward', 'dry', 'asiatic', 'habitable', 'unending', 'tropical', 'uncultivated', 'untamed', 'desolate', 'uncivilized', 'martian', 'gravelly', 'travelled', 'treacherous', 'dotted', 'wild', 'lonely', 'ethiopian', 'tartar','perished','terrible', 'strange', 'such', 'luminous', 'forlorn', 'God-forsaken', 'mountainous', 'unknown', 'open', 'fragrant', 'black-and-white', 'many', 'wild', 'whole', 'contorted', 'flat', 'other', 'arboreal', 'somber', 'fearful', 'short', 'old', 'mysterious', 'dreary'],
						"verb":['magnify', 'driven', 'surrounded', 'began', 'underwent', 'reaching', 'trotting', 'seemed', 'stretched', 'rose', 'covered', 'steed', 'developed', 'leaving', 'changed', 'resembled', 'leading', 'opened', 'dominated', 'returned', 'setting', 'became', 'fighting', 'gather', 'makes']},

	{"name":"ocean", "assoc":["wet","natural","dangerous","fresh","clean","beautiful","pure","cold"],
					   "color":["blue","green","purple"],
					   "type":"landscape",
					   "adj":['wild', 'best', 'Indian', 'boundless', 'blue', 'old', 'human'],
					   "verb":['beat',"darkening",'called']},
	
	{"name":"swamp", "assoc":["natural","ugly","dirty","foul"],
					   "color":["green","grey","brown","black"],
					   "type":"landscape",
					   "adj":["great","frozen","thick","misty","ghostly","sandy","sickly","wild","dense","tangled","sluggish","noxious","poisonous","wooded","entangled","treacherous","grassy","stinking","coastal","humid","flooded","arid","sterile"],
					   "verb":["rot","bubble"]},	
]

def getObjects():
	return objects
	
def main():
	print "This file is used to store object representations."

if __name__ == '__main__':
	main()
