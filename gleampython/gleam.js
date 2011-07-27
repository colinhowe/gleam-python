var $gleam = {
    macros: {},
    nodes: [],
    views: {},
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
    },
    insertView: function(viewName, insertId) {
        /* Runs the given view and inserts the nodes into the element with ID insertId */
        this.views[viewName]();
        var container = document.getElementById(insertId);
        for (var i = 0; i < this.nodes.length; i++) {
            var node = this.nodes[i];
            this._insertNode(node, container);
        }
        this.nodes = [];
    },
    _insertNode: function(node, container) {
        /* Inserts the given node as HTML into the given container */
        var nodeElement = document.createElement(node.name);
        for (var key in node.attrs) {
            nodeElement.setAttribute(key, node.attrs[key]);
        }
        if (node.value) {
            var textNode = document.createTextNode(node.value);
            nodeElement.appendChild(textNode);
        }
        for (var i = 0; i < node.nodes.length; i++) {
            this._insertNode(node.nodes[i], nodeElement);
        }
        container.appendChild(nodeElement);
    }
}

$gleam.currentNode = [$gleam];
