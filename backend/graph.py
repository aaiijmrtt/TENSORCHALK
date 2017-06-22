__internals__ = ['__type__', '__pre__']

def __fill__(graph, name, fill, expand, indent = 0):
	if name in fill: return fill[name], fill
	if name not in expand:
		fill[name] = '%s%s\n' %('\t' * indent, name)
		return fill[name], fill
	string = '%s%s\n' %('\t' * indent, name)
	for key in graph[name]:
		if key in __internals__: continue
		string += '%s%s: %s\n' %(
			'\t' * (indent + 1),
			key,
			graph[name][key]
		)
	for internal in __internals__:
		string += '%s%s: %s\n' %(
			'\t' * (indent + 1),
			internal,
			graph[name][internal]
		)
		if internal != '__pre__': continue
		for key in graph[name][internal]:
			string += '%s' %__fill__(
				graph,
				key,
				fill,
				expand,
				indent + 1
			)[0]
	fill[name] = string
	return fill[name], fill
