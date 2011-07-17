from unittest import TestCase

import antlr3

from gleamLexer import gleamLexer
from gleamParser import gleamParser


def print_tree(tree, indent=0):
    res = (' ' * indent) + gleamParser.tokenNames[tree.type] + '\n'
    for child in tree.children:
        res += print_tree(child, indent+1)
    return res

class TestBasicNode(TestCase):
    def check_tree(self, expected, actual):
        lines = [line for line in expected.split('\n') if line.strip() != '']
        start_indent = len(lines[0]) - len(lines[0].lstrip())
        lines = [line[start_indent:] for line in lines]
        trees = [print_tree(child) for child in actual.children]
        actual = "".join(trees)
        expected = '\n'.join(lines) + '\n'
        if actual != expected:
            print 'Expected:'
            print expected.replace(' ', '.')
            print '\nActual:'
            print actual.replace(' ', '.')
        self.assertEquals(expected, actual)

    def check_parse(self, code, tree):
        char_stream = antlr3.ANTLRStringStream(code)
        lexer = gleamLexer(char_stream)
        tokens = antlr3.CommonTokenStream(lexer)
        parser = gleamParser(tokens)
        response = parser.prog()

        self.check_tree(tree, response.tree)

    def test_basic(self):
        self.check_parse("""
            node form(class="clazz", name="Bob") "text"
        """, """
            NODE
             IDENTIFIER
             ARGS
              IDENTIFIER
               STRINGLITERAL
              IDENTIFIER
               STRINGLITERAL
             STRINGLITERAL
        """)

        
    def test_2nodes(self):
        self.check_parse("""
            node form() "1"
            node form() "2"
        """, """
            NODE
             IDENTIFIER
             ARGS
             STRINGLITERAL
            NODE
             IDENTIFIER
             ARGS
             STRINGLITERAL
        """)

    def test_macro_defn(self):
        self.check_parse("""
            macro form(class, name) value {
               node form(class=class, name=name) value
            }
        """, """
            MACRO
             IDENTIFIER
             PARAMS
              IDENTIFIER
              IDENTIFIER
             IDENTIFIER
             BLOCK
              NODE
               IDENTIFIER
               ARGS
                IDENTIFIER
                 IDENTIFIER
                IDENTIFIER
                 IDENTIFIER
               IDENTIFIER
        """)

    def test_call_macro_with_block(self):
        self.check_parse("""
            form(class='class') {
            }
        """, """
            CALL
             IDENTIFIER
             ARGS
              IDENTIFIER
               STRINGLITERAL
             BLOCK
        """)
    
    def test_empty_node(self):
        self.check_parse("""
            node br
            node br
        """, """
            NODE
             IDENTIFIER
             ARGS
             EMPTY_EXPR
            NODE
             IDENTIFIER
             ARGS
             EMPTY_EXPR
        """)

    def test_two_valueless_calls(self):
        self.check_parse("""
            br()
            br()
        """, """
            CALL
             IDENTIFIER
             ARGS
             EMPTY_EXPR
            CALL
             IDENTIFIER
             ARGS
             EMPTY_EXPR
        """)

    def test_macro_defn_and_invoke(self):
        self.check_parse("""
            macro form(class) value {
                node form value
            }

            form(class='class') {
                node br
            }
        """, """
            MACRO
             IDENTIFIER
             PARAMS
              IDENTIFIER
             IDENTIFIER
             BLOCK
              NODE
               IDENTIFIER
               ARGS
               IDENTIFIER
            CALL
             IDENTIFIER
             ARGS
              IDENTIFIER
               STRINGLITERAL
             BLOCK
              NODE
               IDENTIFIER
               ARGS
               EMPTY_EXPR
        """)
