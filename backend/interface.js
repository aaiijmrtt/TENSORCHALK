var documentation = document.getElementById('displaydocumentation');
function apiClick(me) {
	documentation.innerHTML = document.getElementById('documentation.' + me.id).innerHTML;
}

var s = new sigma('graph');
var dragListener = sigma.plugins.dragNodes(s, s.renderers[0]);

var nodeid = 0;
var edgeid = 0;
s.graph.addNode({
	id: nodeid,
	label: nodeid.toString(),
	x: 0,
	y: 1,
	size: 1,
})
nodeid++;
s.graph.addNode({
	id: nodeid,
	label: nodeid.toString(),
	x: 1,
	y: 0,
	size: 1,
})
nodeid++;
s.graph.addEdge({
	id: edgeid,
	source: 0,
	target: 1
});
edgeid++;

s.refresh();
s.bind(
	'rightClickNode',
	function(e) {
		s.graph.addNode({
			id: nodeid,
			label: nodeid.toString(),
			x: 0,
			y: 0,
			size: 1,
		});
		s.graph.addEdge({
			id: edgeid,
			source: e.data.node.id,
			target: nodeid
		})
		s.refresh();
		nodeid++;
		edgeid++;
	}
);
