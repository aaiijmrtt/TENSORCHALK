import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'code')))
import core, graphs

graph = graphs.one

print 'import tensorflow as tf'
print core.__fill__(graph, 'add', dict(), 0)[0]
print 'with tf.Session() as sess:'
print '\tsess.run(tf.global_variables_initializer())'
print '\tprint sess.run(add, {x: [[1, 2]], y: [[3, 4]]})'
