import sys, os
import tensorflow
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'code')))
import library

subset = set(['tensorflow', 'nn', 'add'])

graph = library.__create__(
	dict(),
	'tensorflow',
	tensorflow
)

fillstring, filldict = library.__fill__(
	graph,
	'tensorflow',
	dict(),
	subset,
	0
)

for something in subset:
	print '[%s]' %something
	print graph['documentation'][something]
	print '...'
print fillstring
