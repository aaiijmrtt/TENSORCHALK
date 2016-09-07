import inspect, types
import tensorflow as tf

def __find__(name):
	if hasattr(tf, name):
		return 'tf.%s' %name
	for module in filter(
		lambda thing:
			isinstance(
				getattr(
					tf,
					thing
				),
				types.ModuleType
			),
		dir(tf)
	):
		if hasattr(
			getattr(
				tf,
				module
			),
			name
		): return 'tf.%s.%s' %(module, name)
	return None

def __fill__(graph, name, check, indent = 0):
	fill = ''
	if name in check and check[name]: return fill, check
	for pre in filter(
		lambda pre:
			pre not in check or
			not check[pre],
			graph[name]['tcpre']
		):
			_fill_, check = __fill__(graph, pre, check)
			fill += _fill_
	for get in graph[name]['tcget']:
		graph[name][get] = __find__(graph[name][get])
	fill += '%s%s = %s(%s)\n' %(
		'\t' * indent,
		name,
		graph[name]['tctype'],
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
						graph[name]['tctype'].split('.')[1: ],
						tf
					))
				)[0]
			)
		])
	)
	check[name] = True
	return fill, check
