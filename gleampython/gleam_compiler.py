import antlr3

import gleam
from gleamLexer import gleamLexer
from gleamParser import gleamParser

def compile_gleam(src, target_js, target_python):
    '''Compiles the given src file to the target JS and target Python files.
    '''
    char_stream = antlr3.ANTLRFileStream(src)
    lexer = gleamLexer(char_stream)
    tokens = antlr3.CommonTokenStream(lexer)
    parser = gleamParser(tokens)
    response = parser.prog()

    js = gleam.to_js(response.tree, src, debug=True)
    of = file(target_js, 'w')
    of.write(js)
    of.close()

    python = gleam.to_python(response.tree, debug=True)
    of = file(target_python, 'w')
    of.write(python)
    of.close()
