from unittest import TestCase

import antlr3

import gleam
from gleamLexer import gleamLexer
from gleamParser import gleamParser


class TestPythonTarget(TestCase):
    def deindent(self, text):
        lines = [line for line in text.split('\n') if line.strip() != '']
        start_indent = len(lines[0]) - len(lines[0].lstrip())
        lines = [line[start_indent:] for line in lines]
        return '\n'.join(lines) + '\n'

    def check_python(self, code, expected_python):
        char_stream = antlr3.ANTLRStringStream(code)
        lexer = gleamLexer(char_stream)
        tokens = antlr3.CommonTokenStream(lexer)
        parser = gleamParser(tokens)
        response = parser.prog()

        python = gleam.to_python(response.tree, debug=True)
        python = self.deindent(python)
        # Strip the first line - its just an import
        python = '\n'.join(python.split('\n')[1:])

        expected_python = self.deindent(expected_python)
        if expected_python != python:
            print 'Expected:'
            print expected_python
            print '\nActual:'
            print python
        self.assertEquals(expected_python, python)

    def test_node_no_args_simple_value(self):
        self.check_python("""
            node form "text"
        """, """
            gleam.makeNode("form", {}, "text")
        """)

    def test_basic(self):
        self.check_python("""
            node form(class="clazz", name="Bob") "text"
        """, """
            gleam.makeNode("form", {"class": "clazz", "name": "Bob"}, "text")
        """)

    def test_numeric_value(self):
        self.check_python("""
            node span 5
        """, """
            gleam.makeNode("span", {}, 5)
        """)

    def test_define_and_invoke_macro_with_simple_value(self):
        self.check_python("""
            macro form(class) value {
                node form(class=class) value
            }

            form(class='class') "hello"
        """, """
            def form(args, value):
                class = args["class"]
                gleam.makeNode("form", {"class": class}, value)
            
            gleam.addMacro("form", form)
            gleam.macros.form({"class": "class"}, "hello")
        """)

    def test_valueless_macro(self):
        self.check_python("""
            macro br() {
                node br()
            }
        """, """
            def br(args):
                gleam.makeNode("br", {}, None)
            gleam.addMacro("br", br)
        """)

    def test_define_and_invoke_macro_with_block(self):
        self.check_python("""
            macro form(class) value {
                node form(class=class) value
            }

            form(class='class') {
                node span "hello"
            }
        """, """
            def form(args, value):
                class = args["class"]
                gleam.makeNode("form", {"class": class}, value)
            
            gleam.addMacro("form", form)
            def block_0():
                gleam.makeNode("span", {}, "hello")
            gleam.macros.form({"class": "class"}, block_0)
        """)
