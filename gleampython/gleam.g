grammar gleam;

options {
	language = Python;
}

tokens {
	PLUS 	= '+' ;
	MINUS	= '-' ;
	MULT	= '*' ;
	DIV	= '/' ;
}

@header {
import sys
import traceback

from SimpleCalcLexer import SimpleCalcLexer
}

@main {
def main(argv, otherArg=None):
  char_stream = ANTLRFileStream(sys.argv[1])
  lexer = SimpleCalcLexer(char_stream)
  tokens = CommonTokenStream(lexer)
  parser = SimpleCalcParser(tokens);

  try:
        parser.expr()
  except RecognitionException:
	traceback.print_stack()
}

/*------------------------------------------------------------------
 * PARSER RULES
 *------------------------------------------------------------------*/

expr	: term ( ( PLUS | MINUS )  term )* ;

term	: factor ( ( MULT | DIV ) factor )* ;

factor	: NUMBER ;


/*------------------------------------------------------------------
 * LEXER RULES
 *------------------------------------------------------------------*/

NUMBER	: (DIGIT)+ ;

WHITESPACE : ( '\t' | ' ' | '\r' | '\n'| '\u000C' )+ 	{ $channel = HIDDEN; } ;

fragment DIGIT	: '0'..'9' ;
