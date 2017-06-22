import inspect, re

def __functions__(module):
	return [func[0] for func in inspect.getmembers(module, inspect.isfunction)]

def __modules__(module):
	return [mod[0] for mod in inspect.getmembers(module, inspect.ismodule)]

def __fill__(graph, name, fill, indent = 0):
	if name.split('.')[0] in name.split('.')[1: ]: return str(), fill
	if name in fill: return fill[name], fill
	string = '%s<ul>\n' %('\t' * indent)

	for key in graph[name]['modules']:
		if key.startswith('_'): continue
		string += '%s<li>\n' %('\t' * (indent + 1))
		string += '%s<input id="%s" type="checkbox" onclick="return apiClick(this)" hidden />\n' %(
			'\t' * (indent + 2),
			'%s.%s' %(key, name)
		)
		string += '%s<label for="%s"><span class="fa fa-angle-right"></span>%s</label>\n' %(
			'\t' * (indent + 2),
			'%s.%s' %(key, name),
			key
		)
		fillstring, filldict = __fill__(
			graph,
			'%s.%s' %(key, name),
			fill,
			indent + 2
		)
		string += fillstring
		string += '%s</li>\n' %('\t' * (indent + 1))

	for key in graph[name]['functions']:
		if key.startswith('_'): continue
		string += '%s<li><a id="%s" onclick="return apiClick(this)">%s</a></li>\n' %(
			'\t' * (indent + 1),
			'%s.%s' %(key, name),
			key
		)
	string += '%s</ul>\n' %('\t' * indent)
	fill[name] = string
	return fill[name], fill

def __create__(graph, key, module):
	if key in graph or key.split('.')[0] in key.split('.')[1: ]: return graph
	graph[key] = {
		'base': key.split('.', 1)[1],
		'modules': __modules__(module),
		'functions': __functions__(module),
		'documentation': module.__doc__
	}
	for subkey in ['functions', 'modules']:
		for element in graph[key][subkey]:
			if element.startswith('_'): continue
			try:
				graph = __create__(
					graph,
					'%s.%s' %(element, key),
					getattr(module, element)
				)
			except:
				print module, element
				continue
	return graph

def __docs__(graph, indent = 0):
	embeddedimages = '.*<div style="width:70%; margin:auto; margin-bottom:10px; margin-top:20px;">\n.*<img style="width:100%" src="\.\./\.\./images/.*\.png" alt>\n.*</div>'
	string = str()
	for key in graph:
		if graph[key]['documentation'] is None: graph[key]['documentation'] = str()
		string += '%s<p id="documentation.%s">%s</p>\n' %(
			'\t'  * indent,
			key,
			re.sub(
				embeddedimages,
				str(),
				graph[key]['documentation']
			)
		)
	return string
