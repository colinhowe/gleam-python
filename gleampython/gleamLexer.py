# $ANTLR 3.1.3 Mar 17, 2009 19:23:44 gleampython/gleam.g 2011-06-19 18:19:55

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
NUMBER=8
WHITESPACE=10
PLUS=4
DIGIT=9
DIV=7
MULT=6
MINUS=5
EOF=-1


class gleamLexer(Lexer):

    grammarFileName = "gleampython/gleam.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 17, 2009 19:23:44")
    antlr_version_str = "3.1.3 Mar 17, 2009 19:23:44"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(gleamLexer, self).__init__(input, state)







    # $ANTLR start "PLUS"
    def mPLUS(self, ):

        try:
            _type = PLUS
            _channel = DEFAULT_CHANNEL

            # gleampython/gleam.g:7:6: ( '+' )
            # gleampython/gleam.g:7:8: '+'
            pass 
            self.match(43)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PLUS"



    # $ANTLR start "MINUS"
    def mMINUS(self, ):

        try:
            _type = MINUS
            _channel = DEFAULT_CHANNEL

            # gleampython/gleam.g:8:7: ( '-' )
            # gleampython/gleam.g:8:9: '-'
            pass 
            self.match(45)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MINUS"



    # $ANTLR start "MULT"
    def mMULT(self, ):

        try:
            _type = MULT
            _channel = DEFAULT_CHANNEL

            # gleampython/gleam.g:9:6: ( '*' )
            # gleampython/gleam.g:9:8: '*'
            pass 
            self.match(42)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MULT"



    # $ANTLR start "DIV"
    def mDIV(self, ):

        try:
            _type = DIV
            _channel = DEFAULT_CHANNEL

            # gleampython/gleam.g:10:5: ( '/' )
            # gleampython/gleam.g:10:7: '/'
            pass 
            self.match(47)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DIV"



    # $ANTLR start "NUMBER"
    def mNUMBER(self, ):

        try:
            _type = NUMBER
            _channel = DEFAULT_CHANNEL

            # gleampython/gleam.g:49:8: ( ( DIGIT )+ )
            # gleampython/gleam.g:49:10: ( DIGIT )+
            pass 
            # gleampython/gleam.g:49:10: ( DIGIT )+
            cnt1 = 0
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((48 <= LA1_0 <= 57)) :
                    alt1 = 1


                if alt1 == 1:
                    # gleampython/gleam.g:49:11: DIGIT
                    pass 
                    self.mDIGIT()


                else:
                    if cnt1 >= 1:
                        break #loop1

                    eee = EarlyExitException(1, self.input)
                    raise eee

                cnt1 += 1



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NUMBER"



    # $ANTLR start "WHITESPACE"
    def mWHITESPACE(self, ):

        try:
            _type = WHITESPACE
            _channel = DEFAULT_CHANNEL

            # gleampython/gleam.g:51:12: ( ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+ )
            # gleampython/gleam.g:51:14: ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+
            pass 
            # gleampython/gleam.g:51:14: ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+
            cnt2 = 0
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((9 <= LA2_0 <= 10) or (12 <= LA2_0 <= 13) or LA2_0 == 32) :
                    alt2 = 1


                if alt2 == 1:
                    # gleampython/gleam.g:
                    pass 
                    if (9 <= self.input.LA(1) <= 10) or (12 <= self.input.LA(1) <= 13) or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt2 >= 1:
                        break #loop2

                    eee = EarlyExitException(2, self.input)
                    raise eee

                cnt2 += 1
            #action start
            _channel = HIDDEN; 
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WHITESPACE"



    # $ANTLR start "DIGIT"
    def mDIGIT(self, ):

        try:
            # gleampython/gleam.g:53:16: ( '0' .. '9' )
            # gleampython/gleam.g:53:18: '0' .. '9'
            pass 
            self.matchRange(48, 57)




        finally:

            pass

    # $ANTLR end "DIGIT"



    def mTokens(self):
        # gleampython/gleam.g:1:8: ( PLUS | MINUS | MULT | DIV | NUMBER | WHITESPACE )
        alt3 = 6
        LA3 = self.input.LA(1)
        if LA3 == 43:
            alt3 = 1
        elif LA3 == 45:
            alt3 = 2
        elif LA3 == 42:
            alt3 = 3
        elif LA3 == 47:
            alt3 = 4
        elif LA3 == 48 or LA3 == 49 or LA3 == 50 or LA3 == 51 or LA3 == 52 or LA3 == 53 or LA3 == 54 or LA3 == 55 or LA3 == 56 or LA3 == 57:
            alt3 = 5
        elif LA3 == 9 or LA3 == 10 or LA3 == 12 or LA3 == 13 or LA3 == 32:
            alt3 = 6
        else:
            nvae = NoViableAltException("", 3, 0, self.input)

            raise nvae

        if alt3 == 1:
            # gleampython/gleam.g:1:10: PLUS
            pass 
            self.mPLUS()


        elif alt3 == 2:
            # gleampython/gleam.g:1:15: MINUS
            pass 
            self.mMINUS()


        elif alt3 == 3:
            # gleampython/gleam.g:1:21: MULT
            pass 
            self.mMULT()


        elif alt3 == 4:
            # gleampython/gleam.g:1:26: DIV
            pass 
            self.mDIV()


        elif alt3 == 5:
            # gleampython/gleam.g:1:30: NUMBER
            pass 
            self.mNUMBER()


        elif alt3 == 6:
            # gleampython/gleam.g:1:37: WHITESPACE
            pass 
            self.mWHITESPACE()







 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(gleamLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
