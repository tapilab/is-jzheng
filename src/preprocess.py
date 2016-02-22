"""
	Load mutiple lines of json file from a single file.

	return "text" line by line from each json. 
"""


import json
import glob
import codecs
import re
import string


def load_file(path):
    with codecs.open(path,encoding="utf-8") as file:
    	lines = file.readlines()
  
    res = []

    for line in lines:
    	
    	line = json.loads(line)['text'].lower()
    	
    	line = re.sub(r'\n\t', ' ', line)
    	line = line.encode('utf-8') 
    	
 
    	line = line.strip().translate(None, string.punctuation)
    
    	res.append(line)

    return res


def write_file(file , path):
	f = codecs.open(path , "w" )
	i = 0
	
	for l in file:
	
		
		f.write(l)
		f.write("\n")

	
	f.close()




if __name__ == "__main__":
	path = "../data/cmu/review/review.txt"
	path_write = "../data/cmu/review/processed_comments.json"
	comments = load_file(path)
	write_file(comments, path_write)




