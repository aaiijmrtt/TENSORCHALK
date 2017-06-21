import sys, os
import tensorflow
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'code')))
import graph, graphs

subset = set(['add', 'dot', 'w', 'y'])
cgraph = graphs.one

fillstring, filldict = graph.__fill__(
	cgraph,
	'add',
	dict(),
	subset,
	0
)

print fillstring
