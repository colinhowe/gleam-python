from unittest import TestCase

import antlr3

import gleam
from gleamLexer import gleamLexer
from gleamParser import gleamParser


class TestJsTarget(TestCase):
    def deindent(self, text):
        lines = [line for line in text.split('\n') if line.strip() != '']
        start_indent = len(lines[0]) - len(lines[0].lstrip())
        lines = [line[start_indent:] for line in lines]
        return '\n'.join(lines) + '\n'

    def check_js(self, code, expected_js):
        char_stream = antlr3.ANTLRStringStream(code)
        lexer = gleamLexer(char_stream)
        tokens = antlr3.CommonTokenStream(lexer)
        parser = gleamParser(tokens)
        response = parser.prog()

        js = gleam.to_js(response.tree, debug=True)
        js = self.deindent(js)
        expected_js = self.deindent(expected_js)
        if expected_js != js:
            print 'Expected:'
            print expected_js
            print '\nActual:'
            print js
        self.assertEquals(expected_js, js)

    def test_node_no_args_simple_value(self):
        self.check_js("""
            node form "text"
        """, """
            $gleam.makeNode("form", {}, "text");
        """)

    def test_basic(self):
        self.check_js("""
            node form(class="clazz", name="Bob") "text"
        """, """
            $gleam.makeNode("form", {class: "clazz", name: "Bob"}, "text");
        """)

    def test_numeric(self):
        self.check_js("""
            node span 5
        """, """
            $gleam.makeNode("span", {}, 5);
        """)

    def test_valueless(self):
        self.check_js("""
            node span
        """, """
            $gleam.makeNode("span", {}, null);
        """)

    def test_define_and_invoke_macro_with_simple_value(self):
        self.check_js("""
            macro form(class) value {
                node form(class=class) value
            }

            form(class='class') "hello"
        """, """
            $gleam.addMacro("form", function(args, value) {
                var class = args["class"];
                $gleam.makeNode("form", {class: class}, value);
            });
            $gleam.macros.form({class: "class"}, "hello");
        """)

    def test_define_and_invoke_macro_with_block(self):
        self.check_js("""
            macro form(class) value {
                node form(class=class) value
            }

            form(class='class') {
                node span "hello"
            }
        """, """
            $gleam.addMacro("form", function(args, value) {
                var class = args["class"];
                $gleam.makeNode("form", {class: class}, value);
            });
            $gleam.macros.form({class: "class"}, function() {
                $gleam.makeNode("span", {}, "hello");
            });
        """)
