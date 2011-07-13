import gleamParser
from gleamParser import gleamParser as parser
from python_target import to_python

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
        return '"%s"' % node.text[1:-1]

    def ARGS(self, node):
        args = []
        for identifier_node in node.children:
            value_node = identifier_node.children[0]
            args.append('%s: %s' % 
                    (identifier_node.text, self._to_js(value_node)))

        return "{%s}" % ", ".join(args)

    def IDENTIFIER(self, node):
        return '%s' % node.text
    
    def NODE__IDENTIFIER(self, node):
        return '"%s"' % node.text

    def BLOCK(self, node):
        code = '\n'.join([
            self._to_js(stmt)
            for stmt in node.children
        ])
        return """function() {
    %s
}""" % code

    def NODE(self, node):
        args = '{}'
        name = self._to_js(node.children.pop(0), context=node)
        value = 'null';
        if node.children and node.children[0].type == gleamParser.ARGS:
            args = self._to_js(node.children.pop(0))
        if node.children:
            value = self._to_js(node.children.pop(0))

        return '$gleam.makeNode(%s, %s, %s);' % (name, args, value)

    def MACRO__BLOCK(self, node):
        return '\n'.join([
            self._to_js(stmt)
            for stmt in node.children
        ])

    def MACRO(self, node):
        macro_name_node = node.children.pop(0)
        function_boiler_plate = """function(args, %s) {
    %s
    %s
}"""
        params_node = node.children.pop(0)
        arg_extracts = '\n'.join([
            'var %s = args["%s"];' % (param_node.text, param_node.text)
            for param_node in params_node.children
        ])
        value_node = node.children.pop(0)
        value_name = value_node.text
        macro_code = self._to_js(node.children.pop(0), node)
            
        function_code = function_boiler_plate % (value_name, arg_extracts, macro_code)
        return '$gleam.addMacro("%s", %s);' % (
            macro_name_node.text, function_code)

    def CALL(self, node):
        name_node = node.children.pop(0)
        args = '{}'
        value = 'null';
        if node.children and node.children[0].type == gleamParser.ARGS:
            args = self._to_js(node.children.pop(0))
        if node.children:
            value = self._to_js(node.children.pop(0))
        return '$gleam.macros.%s(%s, %s);' % (
            name_node.text, args, value)

    def PROG(self, node):
        return '\n'.join([
            self._to_js(child)
            for child in node.children
        ])

def to_js(ast, debug=False):
    traverser = ToJsTraverser(debug)
    return traverser._to_js(ast)
