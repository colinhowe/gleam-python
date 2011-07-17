import gleamParser
from gleamParser import gleamParser as parser

def _indent(text):
    return "\n".join(["    " + line for line in text.split("\n")])

class ToPythonTraverser(object):
    def __init__(self, debug=False):
        self.debug = debug
        self.block_count = 0

    def _to_python(self, node, context=None):
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
            args.append('"%s": %s' % 
                    (identifier_node.text, self._to_python(value_node)))

        return "{%s}" % ", ".join(args)

    def IDENTIFIER(self, node):
        return '%s' % node.text
    
    def NODE__IDENTIFIER(self, node):
        return '"%s"' % node.text

    def BLOCK(self, node):
        block_name = "block_%s" % self.block_count
        self.block_count += 1
        code = '\n'.join([
            self._to_python(stmt)
            for stmt in node.children
        ])
        return """def %s():
%s
""" % (block_name, _indent(code)), block_name

    def EMPTY_EXPR(self, node):
        return "None"

    def NODE(self, node):
        # TODO Could be merged with CALL
        args = '{}'
        name = self._to_python(node.children[0], context=node)
        value = 'None';
        result = ''
        args = self._to_python(node.children[1])
        if node.children[2].type == gleamParser.BLOCK:
            result, value = self.BLOCK(node.children[2])
        else:
            value = self._to_python(node.children[2])
        
        result += 'gleam.makeNode(%s, %s, %s)' % (name, args, value)
        return result

    def MACRO__BLOCK(self, node):
        return '\n'.join([
            self._to_python(stmt)
            for stmt in node.children
        ])

    def MACRO(self, node):
        macro_name_node = node.children[0]
        macro_name = macro_name_node.text
        function_boiler_plate = """def %s(args%s):
%s
%s
"""
        params_node = node.children[1]
        arg_extracts = '\n'.join([
            '%s = args["%s"]' % (param_node.text, param_node.text)
            for param_node in params_node.children
        ])
        arg_extracts = _indent(arg_extracts)
        value_node = node.children[2]
        if value_node.type == gleamParser.EMPTY_VALUE:
            value_name = ""
        else:
            value_name = ", " + value_node.text
        macro_code = _indent(self._to_python(node.children[3], node))
            
        function_code = function_boiler_plate % (
                macro_name, value_name, arg_extracts, macro_code)
        return '%s\ngleam.addMacro("%s", %s)' % (
            function_code, macro_name, macro_name)

        # TODO Macros shouldn't need adding to a central repo

    def CALL(self, node):
        name_node = node.children[0]
        args = '{}'
        value = 'None';
        result = ''
        args = self._to_python(node.children[1])
        if node.children[2].type == gleamParser.BLOCK:
            result, value = self.BLOCK(node.children[2])
        else:
            value = self._to_python(node.children[2])
        result += 'gleam.macros.%s(%s, %s)' % (
            name_node.text, args, value)
        return result

    def PROG(self, node):
        return '\n'.join([
            self._to_python(child)
            for child in node.children
        ])

def to_python(ast, debug=False):
    traverser = ToPythonTraverser(debug)
    return traverser._to_python(ast)
