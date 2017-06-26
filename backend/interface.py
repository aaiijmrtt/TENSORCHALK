import sys, SimpleHTTPServer, SocketServer
import tensorflow
import library

graph = library.__create__(
	dict(),
	'tensorflow.',
	tensorflow
)

fillstring, filldict = library.__fill__(
	graph,
	'tensorflow.',
	dict(),
	3
)

docstring = library.__docs__(
	graph,
	3
)

replacements = {
	'<<api>>': fillstring,
	'<<docs>>': docstring
}

with open('backend/interface.html', 'w') as interface:
	for line in open('backend/_interface.html'):
		if line.strip() in replacements: line = replacements[line.strip()]
		interface.write(line)

port = int(sys.argv[1]) if len(sys.argv) > 1 else 6666
httpd = SocketServer.TCPServer(('localhost', port), SimpleHTTPServer.SimpleHTTPRequestHandler)
print 'serving TensorChalk at http://localhost:%i/backend/interface.html' %port
try:
	httpd.serve_forever()
except:
	pass
print 'shutting down TensorChalk'
httpd.shutdown()
