import gleamParser
from gleamParser import gleamParser as parser

class ToJsTraverser(object):
    def __init__(self, debug=False):
        self.debug = debug

    def _to_js(self, node, context=None):
        node_name = gleamParser.tokenNames[node.type]
        
        meth = None
        context_name = 'None'
        if context:
            context_name = gleamParser.tokenNames[context.type]
            meth = getattr(self, "%s__%s" % (context_name, node_name), None)
        
        if not meth:
            meth = getattr(self, node_name, None)

        if not meth:
            raise Exception('Unsupported token type %s within context %s' 
                    % (node_name, context_name))

        if self.debug:
            print 'Invoking %s' % meth.func_name

        return meth(node)

    def STRINGLITERAL(self, node):
        return node.text

    def ARGS(self, node):
        args = []
        for identifier_node in node.children:
            value_node = identifier_node.children[0]
            args.append('%s: %s' % 
                    (identifier_node.text, self._to_js(value_node)))

        return "{%s}" % ", ".join(args)
    
    def NODE__IDENTIFIER(self, node):
        return '"%s"' % node.text

    def NODE(self, node):
        args = '{}'
        name = self._to_js(node.children.pop(0), context=node)
        value = 'null';
        if node.children and node.children[0].type == gleamParser.ARGS:
            args = self._to_js(node.children.pop(0))
        if node.children:
            value = self._to_js(node.children.pop(0), context=node)

        return '$gleam.makeNode(%s, %s, %s);' % (name, args, value)

    def PROG(self, node):
        return '\n'.join([
            self._to_js(child)
            for child in node.children
        ])

def to_js(ast, debug=False):
    traverser = ToJsTraverser(debug)
    return traverser._to_js(ast)
