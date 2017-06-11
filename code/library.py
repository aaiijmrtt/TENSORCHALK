import inspect

def __functions__(module):
	return [func[0] for func in inspect.getmembers(module, inspect.isfunction)]

def __modules__(module):
	return [mod[0] for mod in inspect.getmembers(module, inspect.ismodule)]

def __fill__(graph, name, fill, expand, indent = 0):
	if name in fill: return fill[name], fill
	if name not in expand:
		fill[name] = '%s%s\n' %('\t' * indent, name)
		return fill[name], fill
	string = '%s%s\n' %('\t' * indent, name)
	for key in graph[name]['modules']:
		fillstring, filldict = __fill__(
			graph,
			key,
			fill,
			expand,
			indent + 1
		)
		string += fillstring
	for key in graph[name]['functions']:
		string += '%s%s\n' %('\t' * (indent + 1), key)
	fill[name] = string
	return fill[name], fill

def __create__(graph, key, module):
	if key in graph: return graph
        if 'documentation' not in graph: graph['documentation'] = dict()
	graph[key] = {
		'modules': __modules__(module),
		'functions': __functions__(module)
	}
        graph['documentation'][key] = module.__doc__
	for mod in graph[key]['modules']:
		try:
			graph = __create__(graph, mod, getattr(module, mod))
		except:
			print module, mod
			continue
	for func in graph[key]['functions']:
		graph['documentation'][func] = getattr(module, func).__doc__
	return graph
