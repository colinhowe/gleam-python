# $ANTLR 3.1.3 Mar 17, 2009 19:23:44 gleampython/gleam.g 2011-06-19 18:19:55

import sys
from antlr3 import *
from antlr3.compat import set, frozenset
         
import sys
import traceback

from SimpleCalcLexer import SimpleCalcLexer



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
NUMBER=8
WHITESPACE=10
PLUS=4
DIGIT=9
MINUS=5
MULT=6
DIV=7
EOF=-1

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "PLUS", "MINUS", "MULT", "DIV", "NUMBER", "DIGIT", "WHITESPACE"
]




class gleamParser(Parser):
    grammarFileName = "gleampython/gleam.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 17, 2009 19:23:44")
    antlr_version_str = "3.1.3 Mar 17, 2009 19:23:44"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(gleamParser, self).__init__(input, state, *args, **kwargs)






                


        



    # $ANTLR start "expr"
    # gleampython/gleam.g:38:1: expr : term ( ( PLUS | MINUS ) term )* ;
    def expr(self, ):

        try:
            try:
                # gleampython/gleam.g:38:6: ( term ( ( PLUS | MINUS ) term )* )
                # gleampython/gleam.g:38:8: term ( ( PLUS | MINUS ) term )*
                pass 
                self._state.following.append(self.FOLLOW_term_in_expr80)
                self.term()

                self._state.following.pop()
                # gleampython/gleam.g:38:13: ( ( PLUS | MINUS ) term )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((PLUS <= LA1_0 <= MINUS)) :
                        alt1 = 1


                    if alt1 == 1:
                        # gleampython/gleam.g:38:15: ( PLUS | MINUS ) term
                        pass 
                        if (PLUS <= self.input.LA(1) <= MINUS):
                            self.input.consume()
                            self._state.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_term_in_expr95)
                        self.term()

                        self._state.following.pop()


                    else:
                        break #loop1




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "expr"


    # $ANTLR start "term"
    # gleampython/gleam.g:40:1: term : factor ( ( MULT | DIV ) factor )* ;
    def term(self, ):

        try:
            try:
                # gleampython/gleam.g:40:6: ( factor ( ( MULT | DIV ) factor )* )
                # gleampython/gleam.g:40:8: factor ( ( MULT | DIV ) factor )*
                pass 
                self._state.following.append(self.FOLLOW_factor_in_term107)
                self.factor()

                self._state.following.pop()
                # gleampython/gleam.g:40:15: ( ( MULT | DIV ) factor )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if ((MULT <= LA2_0 <= DIV)) :
                        alt2 = 1


                    if alt2 == 1:
                        # gleampython/gleam.g:40:17: ( MULT | DIV ) factor
                        pass 
                        if (MULT <= self.input.LA(1) <= DIV):
                            self.input.consume()
                            self._state.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_factor_in_term121)
                        self.factor()

                        self._state.following.pop()


                    else:
                        break #loop2




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "term"


    # $ANTLR start "factor"
    # gleampython/gleam.g:42:1: factor : NUMBER ;
    def factor(self, ):

        try:
            try:
                # gleampython/gleam.g:42:8: ( NUMBER )
                # gleampython/gleam.g:42:10: NUMBER
                pass 
                self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_factor133)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "factor"


    # Delegated rules


 

    FOLLOW_term_in_expr80 = frozenset([1, 4, 5])
    FOLLOW_set_in_expr84 = frozenset([8])
    FOLLOW_term_in_expr95 = frozenset([1, 4, 5])
    FOLLOW_factor_in_term107 = frozenset([1, 6, 7])
    FOLLOW_set_in_term111 = frozenset([8])
    FOLLOW_factor_in_term121 = frozenset([1, 6, 7])
    FOLLOW_NUMBER_in_factor133 = frozenset([1])



       
def main(argv, otherArg=None):
  char_stream = ANTLRFileStream(sys.argv[1])
  lexer = SimpleCalcLexer(char_stream)
  tokens = CommonTokenStream(lexer)
  parser = SimpleCalcParser(tokens);

  try:
        parser.expr()
  except RecognitionException:
	traceback.print_stack()


if __name__ == '__main__':
    main(sys.argv)
