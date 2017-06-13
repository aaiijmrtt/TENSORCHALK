import sys, os
import tensorflow
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'code')))
import library

graph = library.__create__(
	dict(),
	'tensorflow',
	tensorflow
)

fillstring, filldict = library.__fill__(
	graph,
	'tensorflow',
	dict(),
	set(['tensorflow', 'nn', 'addition']),
	0
)

print fillstring
