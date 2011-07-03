var $gleam = {
    macros: {},
    nodes: [],
    currentNode: [],
    addMacro: function(name, fn) {
        $gleam.macros[name] = fn;
    },
    makeNode: function(name, attrs, value) {
        var node = {name: name, nodes: []};
        $gleam.currentNode[$gleam.currentNode.length - 1].nodes.push(node);
        $gleam.currentNode.push(node);
        if (typeof(value) == 'function') {
            value();
            node.value = null;
        } else {
            node.value = value;
        }
        node.attrs = attrs;
        $gleam.currentNode.pop(node);
    },
    logNodes: function(node, indent) {
        if (!node) {
            node = $gleam;
        }
        if (!indent) {
            indent = 0;
        }
        log = function(msg) {
            console.log(Array(indent + 1).join(".") + msg);
        }
        log(node.name);
        attrs = [];
        for (var key in node.attrs) {
            attrs.push(key + ': ' + node.attrs[key]);
        }
    
        log("+" + attrs.join(", "));
        log("+" + node.value);
        for (var i in node.nodes) {
            $gleam.logNodes(node.nodes[i], indent + 4);
        }
    }
}

$gleam.currentNode = [$gleam];

$gleam.addMacro("form", function(args, value) {
    var class = args["class"];
    $gleam.makeNode("form", {class: class}, value);
});
$gleam.macros.form({class: "class"}, function() {
    $gleam.makeNode("span", {}, "hello");
});

$gleam.logNodes();
