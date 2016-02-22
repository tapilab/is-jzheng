"""
	Train word2vec
"""

import logging
import os.path
import sys
import multiprocessing
#import gensim.models.word2vec

from gensim.models.word2vec import Word2Vec
from gensim.models.word2vec import LineSentence

import os


if __name__ == '__main__':
	program = os.path.basename(sys.argv[0])
	logger = logging.getLogger(program)

	logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
	logging.root.setLevel(level=logging.INFO)
	logger.info("running %s" % ' '.join(sys.argv))



	file_path = "../data/cmu/review/processed_comments.json"

	model_path = "model"
	vector_path = "vector"

	count = multiprocessing.cpu_count()
	
	model = Word2Vec(LineSentence(file_path),size=200, window=10, min_count=5, workers=count)

	model.save(model_path)
	model.save_word2vec_format(vector_path, binary=False)