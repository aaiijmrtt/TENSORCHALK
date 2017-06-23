import sys, os
import tensorflow
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'code')))
import library

graph = library.__create__(
	dict(),
	'tensorflow.',
	tensorflow
)

fillstring, filldict = library.__fill__(
	graph,
	'tensorflow.',
	dict()
)

docstring = library.__docs__(
	graph
)

print '\n'.join(fillstring.split('\n')[: 20])
print
print '\n'.join(docstring.split('\n')[: 20])
