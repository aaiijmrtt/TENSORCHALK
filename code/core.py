import inspect, types
import tensorflow

def __fill__(graph, name, check, indent = 0):
	fill = str()
	if name in check and check[name]: return fill, check
	for pre in filter(
		lambda pre:
			pre not in check or
			not check[pre],
			graph[name]['__pre__']
		):
			_fill_, check = __fill__(graph, pre, check)
			fill += '%s%s' %(
				'\t' * indent,
				_fill_
			)
	fill += '%s%s = %s(%s)\n' %(
		'\t' * indent,
		name,
		graph[name]['__type__'],
		', '.join([
			'%s = %s' %(
				arg,
				graph[name][arg]
			) for arg in filter(
				lambda arg:
					arg in graph[name],
				inspect.getargspec(
					(lambda argument:
						argument.__init__ if isinstance(
							argument,
							types.TypeType
						)
						else argument
					)(reduce(
						getattr,
						graph[name]['__type__'].split('.')[1: ],
						tensorflow
					))
				)[0]
			)
		])
	)
	check[name] = True
	return fill, check
