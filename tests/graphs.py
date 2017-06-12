one = {
	'r': {
		'__type__': 'tf.truncated_normal',
		'__pre__': [],
		'dtype': 'tf.float32',
		'shape': [2, 2],
		'name': '\'r\''
	},
	'w': {
		'__type__': 'tf.Variable',
		'__pre__': ['r'],
		'dtype': 'tf.float32',
		'initial_value': 'r',
		'name': '\'w\''
	},
	'x': {
		'__type__': 'tf.placeholder',
		'__pre__': [],
		'dtype': 'tf.float32',
		'shape': [1, 2],
		'name': '\'x\''
	},
	'dot': {
		'__type__': 'tf.matmul',
		'__pre__': ['w', 'x'],
		'a': 'x',
		'b': 'w',
		'name': '\'dot\''
	},
	'y': {
		'__type__': 'tf.placeholder',
		'__pre__': [],
		'dtype': 'tf.float32',
		'shape': [1, 2],
		'name': '\'y\''
	},
	'add': {
		'__type__': 'tf.add',
		'__pre__': ['dot', 'y'],
		'x': 'dot',
		'y': 'y',
		'name': '\'add\''
	}
}
