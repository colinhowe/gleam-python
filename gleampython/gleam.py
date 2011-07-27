import gleamParser
from gleamParser import gleamParser as parser
from python_target import to_python

def _indent(text):
    return "\n".join(["    " + line for line in text.split("\n")])

class ToJsTraverser(object):
    def __init__(self, view_name, debug=False):
        self.debug = debug
        self.view_name = view_name

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

    def NUMBER(self, node):
        return node.text

    def BLOCK(self, node):
        code = '\n'.join([
            self._to_js(stmt)
            for stmt in node.children
        ])
        return """function() {
%s
}""" % _indent(code)

    def NODE(self, node):
        args = '{}'
        name = self._to_js(node.children[0], context=node)
        value = 'null';
        if len(node.children) > 0 and node.children[1].type == gleamParser.ARGS:
            args = self._to_js(node.children[1])
        if len(node.children) > 1:
            value = self._to_js(node.children[2])

        return '$gleam.makeNode(%s, %s, %s);' % (name, args, value)

    def MACRO__BLOCK(self, node):
        return '\n'.join([
            self._to_js(stmt)
            for stmt in node.children
        ])

    def EMPTY_EXPR(self, node):
        return 'null'

    def MACRO(self, node):
        macro_name_node = node.children[0]
        function_boiler_plate = """function(args, %s) {
%s
%s
}"""
        params_node = node.children[1]
        arg_extracts = '\n'.join([
            'var %s = args["%s"];' % (param_node.text, param_node.text)
            for param_node in params_node.children
        ])
        value_node = node.children[2]
        if value_node.children:
            value_node = value_node.children[0]
        value_name = value_node.text
        macro_code = self._to_js(node.children[3], node)
            
        function_code = function_boiler_plate % (
                value_name, _indent(arg_extracts), _indent(macro_code))
        return '$gleam.addMacro("%s", %s);' % (
            macro_name_node.text, function_code)

    def CALL(self, node):
        name_node = node.children[0]
        args = '{}'
        value = 'null';
        args = self._to_js(node.children[1])
        value = self._to_js(node.children[2])
        if node.children[2].type == gleamParser.EMPTY_EXPR:
            return '$gleam.macros.%s(%s);' % (
                name_node.text, args)
        else:
            return '$gleam.macros.%s(%s, %s);' % (
                name_node.text, args, value)

    def PROG(self, node):
        # Macro blocks need to be at the start of the file.
        # The rest can be in a view sectino if needed
        macro_nodes = [
            child
            for child in node.children
            if child.type == gleamParser.MACRO    
        ]

        view_nodes = [
            child
            for child in node.children
            if child.type != gleamParser.MACRO    
        ]

        code = '\n'.join([
            self._to_js(child)
            for child in macro_nodes
        ])

        if view_nodes:
            view_code = '\n'.join([
                self._to_js(child)
                for child in view_nodes
            ])
            if code:
                code += "\n"
            code += "$gleam.views['%s'] = function() {\n" % self.view_name
            code += _indent(view_code) 
            code += "\n}\n"

        return code

def to_js(ast, view_name, debug=False):
    if view_name.endswith('.gleam'):
        view_name = view_name[:-6]
    traverser = ToJsTraverser(view_name, debug)
    return traverser._to_js(ast)
