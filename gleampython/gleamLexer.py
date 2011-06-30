# $ANTLR 3.1.3 Mar 17, 2009 19:23:44 gleampython/gleam.g 2011-06-30 19:56:31

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
NODE=18
RBRACE=17
LINE_COMMENT=30
LBRACE=16
NUMBER=21
IdentifierStart=31
WHITESPACE=28
FOR=22
EQUALS=19
MINUS=9
MULT=10
EOF=-1
HexDigit=27
LPAREN=14
RPAREN=15
PROG=5
T__34=34
IN=23
IDENTIFIER=13
STRINGLITERAL=20
UnicodeEscape=26
SurrogateIdentifer=33
BLOCK=7
ARGS=4
PLUS=8
DIGIT=24
DIV=11
COMMENT=29
MACRO=12
EscapeSequence=25
IdentifierPart=32
PARAMS=6


class gleamLexer(Lexer):

    grammarFileName = "gleampython/gleam.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 17, 2009 19:23:44")
    antlr_version_str = "3.1.3 Mar 17, 2009 19:23:44"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(gleamLexer, self).__init__(input, state)


        self.dfa9 = self.DFA9(
            self, 9,
            eot = self.DFA9_eot,
            eof = self.DFA9_eof,
            min = self.DFA9_min,
            max = self.DFA9_max,
            accept = self.DFA9_accept,
            special = self.DFA9_special,
            transition = self.DFA9_transition
            )

        self.dfa13 = self.DFA13(
            self, 13,
            eot = self.DFA13_eot,
            eof = self.DFA13_eof,
            min = self.DFA13_min,
            max = self.DFA13_max,
            accept = self.DFA13_accept,
            special = self.DFA13_special,
            transition = self.DFA13_transition
            )






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



    # $ANTLR start "T__34"
    def mT__34(self, ):

        try:
            _type = T__34
            _channel = DEFAULT_CHANNEL

            # gleampython/gleam.g:11:7: ( ',' )
            # gleampython/gleam.g:11:9: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__34"



    # $ANTLR start "MACRO"
    def mMACRO(self, ):

        try:
            _type = MACRO
            _channel = DEFAULT_CHANNEL

            # gleampython/gleam.g:65:7: ( 'macro' )
            # gleampython/gleam.g:65:9: 'macro'
            pass 
            self.match("macro")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MACRO"



    # $ANTLR start "FOR"
    def mFOR(self, ):

        try:
            _type = FOR
            _channel = DEFAULT_CHANNEL

            # gleampython/gleam.g:66:5: ( 'for' )
            # gleampython/gleam.g:66:7: 'for'
            pass 
            self.match("for")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FOR"



    # $ANTLR start "IN"
    def mIN(self, ):

        try:
            _type = IN
            _channel = DEFAULT_CHANNEL

            # gleampython/gleam.g:67:4: ( 'in' )
            # gleampython/gleam.g:67:6: 'in'
            pass 
            self.match("in")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IN"



    # $ANTLR start "NODE"
    def mNODE(self, ):

        try:
            _type = NODE
            _channel = DEFAULT_CHANNEL

            # gleampython/gleam.g:68:6: ( 'node' )
            # gleampython/gleam.g:68:8: 'node'
            pass 
            self.match("node")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NODE"



    # $ANTLR start "LBRACE"
    def mLBRACE(self, ):

        try:
            _type = LBRACE
            _channel = DEFAULT_CHANNEL

            # gleampython/gleam.g:69:8: ( '{' )
            # gleampython/gleam.g:69:10: '{'
            pass 
            self.match(123)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LBRACE"



    # $ANTLR start "RBRACE"
    def mRBRACE(self, ):

        try:
            _type = RBRACE
            _channel = DEFAULT_CHANNEL

            # gleampython/gleam.g:70:8: ( '}' )
            # gleampython/gleam.g:70:10: '}'
            pass 
            self.match(125)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RBRACE"



    # $ANTLR start "LPAREN"
    def mLPAREN(self, ):

        try:
            _type = LPAREN
            _channel = DEFAULT_CHANNEL

            # gleampython/gleam.g:71:8: ( '(' )
            # gleampython/gleam.g:71:10: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LPAREN"



    # $ANTLR start "RPAREN"
    def mRPAREN(self, ):

        try:
            _type = RPAREN
            _channel = DEFAULT_CHANNEL

            # gleampython/gleam.g:72:8: ( ')' )
            # gleampython/gleam.g:72:10: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RPAREN"



    # $ANTLR start "EQUALS"
    def mEQUALS(self, ):

        try:
            _type = EQUALS
            _channel = DEFAULT_CHANNEL

            # gleampython/gleam.g:73:8: ( '=' )
            # gleampython/gleam.g:73:10: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EQUALS"



    # $ANTLR start "NUMBER"
    def mNUMBER(self, ):

        try:
            _type = NUMBER
            _channel = DEFAULT_CHANNEL

            # gleampython/gleam.g:76:8: ( ( DIGIT )+ )
            # gleampython/gleam.g:76:10: ( DIGIT )+
            pass 
            # gleampython/gleam.g:76:10: ( DIGIT )+
            cnt1 = 0
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((48 <= LA1_0 <= 57)) :
                    alt1 = 1


                if alt1 == 1:
                    # gleampython/gleam.g:76:11: DIGIT
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



    # $ANTLR start "STRINGLITERAL"
    def mSTRINGLITERAL(self, ):

        try:
            _type = STRINGLITERAL
            _channel = DEFAULT_CHANNEL

            # gleampython/gleam.g:79:5: ( '\"' ( EscapeSequence | ~ ( '\\\\' | '\"' ) )* '\"' )
            # gleampython/gleam.g:79:8: '\"' ( EscapeSequence | ~ ( '\\\\' | '\"' ) )* '\"'
            pass 
            self.match(34)
            # gleampython/gleam.g:79:12: ( EscapeSequence | ~ ( '\\\\' | '\"' ) )*
            while True: #loop2
                alt2 = 3
                LA2_0 = self.input.LA(1)

                if (LA2_0 == 92) :
                    alt2 = 1
                elif ((0 <= LA2_0 <= 33) or (35 <= LA2_0 <= 91) or (93 <= LA2_0 <= 65535)) :
                    alt2 = 2


                if alt2 == 1:
                    # gleampython/gleam.g:79:14: EscapeSequence
                    pass 
                    self.mEscapeSequence()


                elif alt2 == 2:
                    # gleampython/gleam.g:79:31: ~ ( '\\\\' | '\"' )
                    pass 
                    if (0 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop2
            self.match(34)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STRINGLITERAL"



    # $ANTLR start "EscapeSequence"
    def mEscapeSequence(self, ):

        try:
            # gleampython/gleam.g:84:5: ( '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' ) | UnicodeEscape )
            alt3 = 2
            LA3_0 = self.input.LA(1)

            if (LA3_0 == 92) :
                LA3_1 = self.input.LA(2)

                if (LA3_1 == 34 or LA3_1 == 39 or LA3_1 == 92 or LA3_1 == 98 or LA3_1 == 102 or LA3_1 == 110 or LA3_1 == 114 or LA3_1 == 116) :
                    alt3 = 1
                elif (LA3_1 == 117) :
                    alt3 = 2
                else:
                    nvae = NoViableAltException("", 3, 1, self.input)

                    raise nvae

            else:
                nvae = NoViableAltException("", 3, 0, self.input)

                raise nvae

            if alt3 == 1:
                # gleampython/gleam.g:84:9: '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' )
                pass 
                self.match(92)
                if self.input.LA(1) == 34 or self.input.LA(1) == 39 or self.input.LA(1) == 92 or self.input.LA(1) == 98 or self.input.LA(1) == 102 or self.input.LA(1) == 110 or self.input.LA(1) == 114 or self.input.LA(1) == 116:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse



            elif alt3 == 2:
                # gleampython/gleam.g:85:9: UnicodeEscape
                pass 
                self.mUnicodeEscape()



        finally:

            pass

    # $ANTLR end "EscapeSequence"



    # $ANTLR start "HexDigit"
    def mHexDigit(self, ):

        try:
            # gleampython/gleam.g:90:10: ( ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' ) )
            # gleampython/gleam.g:90:12: ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' )
            pass 
            if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 70) or (97 <= self.input.LA(1) <= 102):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "HexDigit"



    # $ANTLR start "UnicodeEscape"
    def mUnicodeEscape(self, ):

        try:
            # gleampython/gleam.g:94:5: ( '\\\\' 'u' HexDigit HexDigit HexDigit HexDigit )
            # gleampython/gleam.g:94:9: '\\\\' 'u' HexDigit HexDigit HexDigit HexDigit
            pass 
            self.match(92)
            self.match(117)
            self.mHexDigit()
            self.mHexDigit()
            self.mHexDigit()
            self.mHexDigit()




        finally:

            pass

    # $ANTLR end "UnicodeEscape"



    # $ANTLR start "WHITESPACE"
    def mWHITESPACE(self, ):

        try:
            _type = WHITESPACE
            _channel = DEFAULT_CHANNEL

            # gleampython/gleam.g:97:12: ( ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+ )
            # gleampython/gleam.g:97:14: ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+
            pass 
            # gleampython/gleam.g:97:14: ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+
            cnt4 = 0
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if ((9 <= LA4_0 <= 10) or (12 <= LA4_0 <= 13) or LA4_0 == 32) :
                    alt4 = 1


                if alt4 == 1:
                    # gleampython/gleam.g:
                    pass 
                    if (9 <= self.input.LA(1) <= 10) or (12 <= self.input.LA(1) <= 13) or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt4 >= 1:
                        break #loop4

                    eee = EarlyExitException(4, self.input)
                    raise eee

                cnt4 += 1
            #action start
            _channel = HIDDEN; 
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WHITESPACE"



    # $ANTLR start "COMMENT"
    def mCOMMENT(self, ):

        try:
            _type = COMMENT
            _channel = DEFAULT_CHANNEL

            # gleampython/gleam.g:101:5: ( '/*' ( options {greedy=false; } : . )* '*/' )
            # gleampython/gleam.g:101:9: '/*' ( options {greedy=false; } : . )* '*/'
            pass 
            self.match("/*")
            # gleampython/gleam.g:102:9: ( options {greedy=false; } : . )*
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == 42) :
                    LA5_1 = self.input.LA(2)

                    if (LA5_1 == 47) :
                        alt5 = 2
                    elif ((0 <= LA5_1 <= 46) or (48 <= LA5_1 <= 65535)) :
                        alt5 = 1


                elif ((0 <= LA5_0 <= 41) or (43 <= LA5_0 <= 65535)) :
                    alt5 = 1


                if alt5 == 1:
                    # gleampython/gleam.g:102:36: .
                    pass 
                    self.matchAny()


                else:
                    break #loop5
            self.match("*/")
            #action start
                         
            _channel=HIDDEN
                        
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMENT"



    # $ANTLR start "LINE_COMMENT"
    def mLINE_COMMENT(self, ):

        try:
            _type = LINE_COMMENT
            _channel = DEFAULT_CHANNEL

            # gleampython/gleam.g:110:5: ( '//' (~ ( '\\n' | '\\r' ) )* ( '\\r\\n' | '\\r' | '\\n' ) | '//' (~ ( '\\n' | '\\r' ) )* )
            alt9 = 2
            alt9 = self.dfa9.predict(self.input)
            if alt9 == 1:
                # gleampython/gleam.g:110:9: '//' (~ ( '\\n' | '\\r' ) )* ( '\\r\\n' | '\\r' | '\\n' )
                pass 
                self.match("//")
                # gleampython/gleam.g:110:14: (~ ( '\\n' | '\\r' ) )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if ((0 <= LA6_0 <= 9) or (11 <= LA6_0 <= 12) or (14 <= LA6_0 <= 65535)) :
                        alt6 = 1


                    if alt6 == 1:
                        # gleampython/gleam.g:110:14: ~ ( '\\n' | '\\r' )
                        pass 
                        if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    else:
                        break #loop6
                # gleampython/gleam.g:110:29: ( '\\r\\n' | '\\r' | '\\n' )
                alt7 = 3
                LA7_0 = self.input.LA(1)

                if (LA7_0 == 13) :
                    LA7_1 = self.input.LA(2)

                    if (LA7_1 == 10) :
                        alt7 = 1
                    else:
                        alt7 = 2
                elif (LA7_0 == 10) :
                    alt7 = 3
                else:
                    nvae = NoViableAltException("", 7, 0, self.input)

                    raise nvae

                if alt7 == 1:
                    # gleampython/gleam.g:110:30: '\\r\\n'
                    pass 
                    self.match("\r\n")


                elif alt7 == 2:
                    # gleampython/gleam.g:110:39: '\\r'
                    pass 
                    self.match(13)


                elif alt7 == 3:
                    # gleampython/gleam.g:110:46: '\\n'
                    pass 
                    self.match(10)



                #action start
                             
                skip()
                            
                #action end


            elif alt9 == 2:
                # gleampython/gleam.g:114:9: '//' (~ ( '\\n' | '\\r' ) )*
                pass 
                self.match("//")
                # gleampython/gleam.g:114:14: (~ ( '\\n' | '\\r' ) )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if ((0 <= LA8_0 <= 9) or (11 <= LA8_0 <= 12) or (14 <= LA8_0 <= 65535)) :
                        alt8 = 1


                    if alt8 == 1:
                        # gleampython/gleam.g:114:14: ~ ( '\\n' | '\\r' )
                        pass 
                        if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    else:
                        break #loop8
                #action start
                             
                skip()
                            
                #action end


            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LINE_COMMENT"



    # $ANTLR start "DIGIT"
    def mDIGIT(self, ):

        try:
            # gleampython/gleam.g:121:16: ( '0' .. '9' )
            # gleampython/gleam.g:121:18: '0' .. '9'
            pass 
            self.matchRange(48, 57)




        finally:

            pass

    # $ANTLR end "DIGIT"



    # $ANTLR start "IDENTIFIER"
    def mIDENTIFIER(self, ):

        try:
            _type = IDENTIFIER
            _channel = DEFAULT_CHANNEL

            # gleampython/gleam.g:124:5: ( IdentifierStart ( IdentifierPart )* )
            # gleampython/gleam.g:124:9: IdentifierStart ( IdentifierPart )*
            pass 
            self.mIdentifierStart()
            # gleampython/gleam.g:124:25: ( IdentifierPart )*
            while True: #loop10
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if ((0 <= LA10_0 <= 8) or (14 <= LA10_0 <= 27) or LA10_0 == 36 or (48 <= LA10_0 <= 57) or (65 <= LA10_0 <= 90) or LA10_0 == 95 or (97 <= LA10_0 <= 122) or (127 <= LA10_0 <= 159) or (162 <= LA10_0 <= 165) or LA10_0 == 170 or LA10_0 == 173 or LA10_0 == 181 or LA10_0 == 186 or (192 <= LA10_0 <= 214) or (216 <= LA10_0 <= 246) or (248 <= LA10_0 <= 566) or (592 <= LA10_0 <= 705) or (710 <= LA10_0 <= 721) or (736 <= LA10_0 <= 740) or LA10_0 == 750 or (768 <= LA10_0 <= 855) or (861 <= LA10_0 <= 879) or LA10_0 == 890 or LA10_0 == 902 or (904 <= LA10_0 <= 906) or LA10_0 == 908 or (910 <= LA10_0 <= 929) or (931 <= LA10_0 <= 974) or (976 <= LA10_0 <= 1013) or (1015 <= LA10_0 <= 1019) or (1024 <= LA10_0 <= 1153) or (1155 <= LA10_0 <= 1158) or (1162 <= LA10_0 <= 1230) or (1232 <= LA10_0 <= 1269) or (1272 <= LA10_0 <= 1273) or (1280 <= LA10_0 <= 1295) or (1329 <= LA10_0 <= 1366) or LA10_0 == 1369 or (1377 <= LA10_0 <= 1415) or (1425 <= LA10_0 <= 1441) or (1443 <= LA10_0 <= 1465) or (1467 <= LA10_0 <= 1469) or LA10_0 == 1471 or (1473 <= LA10_0 <= 1474) or LA10_0 == 1476 or (1488 <= LA10_0 <= 1514) or (1520 <= LA10_0 <= 1522) or (1536 <= LA10_0 <= 1539) or (1552 <= LA10_0 <= 1557) or (1569 <= LA10_0 <= 1594) or (1600 <= LA10_0 <= 1624) or (1632 <= LA10_0 <= 1641) or (1646 <= LA10_0 <= 1747) or (1749 <= LA10_0 <= 1757) or (1759 <= LA10_0 <= 1768) or (1770 <= LA10_0 <= 1788) or LA10_0 == 1791 or (1807 <= LA10_0 <= 1866) or (1869 <= LA10_0 <= 1871) or (1920 <= LA10_0 <= 1969) or (2305 <= LA10_0 <= 2361) or (2364 <= LA10_0 <= 2381) or (2384 <= LA10_0 <= 2388) or (2392 <= LA10_0 <= 2403) or (2406 <= LA10_0 <= 2415) or (2433 <= LA10_0 <= 2435) or (2437 <= LA10_0 <= 2444) or (2447 <= LA10_0 <= 2448) or (2451 <= LA10_0 <= 2472) or (2474 <= LA10_0 <= 2480) or LA10_0 == 2482 or (2486 <= LA10_0 <= 2489) or (2492 <= LA10_0 <= 2500) or (2503 <= LA10_0 <= 2504) or (2507 <= LA10_0 <= 2509) or LA10_0 == 2519 or (2524 <= LA10_0 <= 2525) or (2527 <= LA10_0 <= 2531) or (2534 <= LA10_0 <= 2547) or (2561 <= LA10_0 <= 2563) or (2565 <= LA10_0 <= 2570) or (2575 <= LA10_0 <= 2576) or (2579 <= LA10_0 <= 2600) or (2602 <= LA10_0 <= 2608) or (2610 <= LA10_0 <= 2611) or (2613 <= LA10_0 <= 2614) or (2616 <= LA10_0 <= 2617) or LA10_0 == 2620 or (2622 <= LA10_0 <= 2626) or (2631 <= LA10_0 <= 2632) or (2635 <= LA10_0 <= 2637) or (2649 <= LA10_0 <= 2652) or LA10_0 == 2654 or (2662 <= LA10_0 <= 2676) or (2689 <= LA10_0 <= 2691) or (2693 <= LA10_0 <= 2701) or (2703 <= LA10_0 <= 2705) or (2707 <= LA10_0 <= 2728) or (2730 <= LA10_0 <= 2736) or (2738 <= LA10_0 <= 2739) or (2741 <= LA10_0 <= 2745) or (2748 <= LA10_0 <= 2757) or (2759 <= LA10_0 <= 2761) or (2763 <= LA10_0 <= 2765) or LA10_0 == 2768 or (2784 <= LA10_0 <= 2787) or (2790 <= LA10_0 <= 2799) or LA10_0 == 2801 or (2817 <= LA10_0 <= 2819) or (2821 <= LA10_0 <= 2828) or (2831 <= LA10_0 <= 2832) or (2835 <= LA10_0 <= 2856) or (2858 <= LA10_0 <= 2864) or (2866 <= LA10_0 <= 2867) or (2869 <= LA10_0 <= 2873) or (2876 <= LA10_0 <= 2883) or (2887 <= LA10_0 <= 2888) or (2891 <= LA10_0 <= 2893) or (2902 <= LA10_0 <= 2903) or (2908 <= LA10_0 <= 2909) or (2911 <= LA10_0 <= 2913) or (2918 <= LA10_0 <= 2927) or LA10_0 == 2929 or (2946 <= LA10_0 <= 2947) or (2949 <= LA10_0 <= 2954) or (2958 <= LA10_0 <= 2960) or (2962 <= LA10_0 <= 2965) or (2969 <= LA10_0 <= 2970) or LA10_0 == 2972 or (2974 <= LA10_0 <= 2975) or (2979 <= LA10_0 <= 2980) or (2984 <= LA10_0 <= 2986) or (2990 <= LA10_0 <= 2997) or (2999 <= LA10_0 <= 3001) or (3006 <= LA10_0 <= 3010) or (3014 <= LA10_0 <= 3016) or (3018 <= LA10_0 <= 3021) or LA10_0 == 3031 or (3047 <= LA10_0 <= 3055) or LA10_0 == 3065 or (3073 <= LA10_0 <= 3075) or (3077 <= LA10_0 <= 3084) or (3086 <= LA10_0 <= 3088) or (3090 <= LA10_0 <= 3112) or (3114 <= LA10_0 <= 3123) or (3125 <= LA10_0 <= 3129) or (3134 <= LA10_0 <= 3140) or (3142 <= LA10_0 <= 3144) or (3146 <= LA10_0 <= 3149) or (3157 <= LA10_0 <= 3158) or (3168 <= LA10_0 <= 3169) or (3174 <= LA10_0 <= 3183) or (3202 <= LA10_0 <= 3203) or (3205 <= LA10_0 <= 3212) or (3214 <= LA10_0 <= 3216) or (3218 <= LA10_0 <= 3240) or (3242 <= LA10_0 <= 3251) or (3253 <= LA10_0 <= 3257) or (3260 <= LA10_0 <= 3268) or (3270 <= LA10_0 <= 3272) or (3274 <= LA10_0 <= 3277) or (3285 <= LA10_0 <= 3286) or LA10_0 == 3294 or (3296 <= LA10_0 <= 3297) or (3302 <= LA10_0 <= 3311) or (3330 <= LA10_0 <= 3331) or (3333 <= LA10_0 <= 3340) or (3342 <= LA10_0 <= 3344) or (3346 <= LA10_0 <= 3368) or (3370 <= LA10_0 <= 3385) or (3390 <= LA10_0 <= 3395) or (3398 <= LA10_0 <= 3400) or (3402 <= LA10_0 <= 3405) or LA10_0 == 3415 or (3424 <= LA10_0 <= 3425) or (3430 <= LA10_0 <= 3439) or (3458 <= LA10_0 <= 3459) or (3461 <= LA10_0 <= 3478) or (3482 <= LA10_0 <= 3505) or (3507 <= LA10_0 <= 3515) or LA10_0 == 3517 or (3520 <= LA10_0 <= 3526) or LA10_0 == 3530 or (3535 <= LA10_0 <= 3540) or LA10_0 == 3542 or (3544 <= LA10_0 <= 3551) or (3570 <= LA10_0 <= 3571) or (3585 <= LA10_0 <= 3642) or (3647 <= LA10_0 <= 3662) or (3664 <= LA10_0 <= 3673) or (3713 <= LA10_0 <= 3714) or LA10_0 == 3716 or (3719 <= LA10_0 <= 3720) or LA10_0 == 3722 or LA10_0 == 3725 or (3732 <= LA10_0 <= 3735) or (3737 <= LA10_0 <= 3743) or (3745 <= LA10_0 <= 3747) or LA10_0 == 3749 or LA10_0 == 3751 or (3754 <= LA10_0 <= 3755) or (3757 <= LA10_0 <= 3769) or (3771 <= LA10_0 <= 3773) or (3776 <= LA10_0 <= 3780) or LA10_0 == 3782 or (3784 <= LA10_0 <= 3789) or (3792 <= LA10_0 <= 3801) or (3804 <= LA10_0 <= 3805) or LA10_0 == 3840 or (3864 <= LA10_0 <= 3865) or (3872 <= LA10_0 <= 3881) or LA10_0 == 3893 or LA10_0 == 3895 or LA10_0 == 3897 or (3902 <= LA10_0 <= 3911) or (3913 <= LA10_0 <= 3946) or (3953 <= LA10_0 <= 3972) or (3974 <= LA10_0 <= 3979) or (3984 <= LA10_0 <= 3991) or (3993 <= LA10_0 <= 4028) or LA10_0 == 4038 or (4096 <= LA10_0 <= 4129) or (4131 <= LA10_0 <= 4135) or (4137 <= LA10_0 <= 4138) or (4140 <= LA10_0 <= 4146) or (4150 <= LA10_0 <= 4153) or (4160 <= LA10_0 <= 4169) or (4176 <= LA10_0 <= 4185) or (4256 <= LA10_0 <= 4293) or (4304 <= LA10_0 <= 4344) or (4352 <= LA10_0 <= 4441) or (4447 <= LA10_0 <= 4514) or (4520 <= LA10_0 <= 4601) or (4608 <= LA10_0 <= 4614) or (4616 <= LA10_0 <= 4678) or LA10_0 == 4680 or (4682 <= LA10_0 <= 4685) or (4688 <= LA10_0 <= 4694) or LA10_0 == 4696 or (4698 <= LA10_0 <= 4701) or (4704 <= LA10_0 <= 4742) or LA10_0 == 4744 or (4746 <= LA10_0 <= 4749) or (4752 <= LA10_0 <= 4782) or LA10_0 == 4784 or (4786 <= LA10_0 <= 4789) or (4792 <= LA10_0 <= 4798) or LA10_0 == 4800 or (4802 <= LA10_0 <= 4805) or (4808 <= LA10_0 <= 4814) or (4816 <= LA10_0 <= 4822) or (4824 <= LA10_0 <= 4846) or (4848 <= LA10_0 <= 4878) or LA10_0 == 4880 or (4882 <= LA10_0 <= 4885) or (4888 <= LA10_0 <= 4894) or (4896 <= LA10_0 <= 4934) or (4936 <= LA10_0 <= 4954) or (4969 <= LA10_0 <= 4977) or (5024 <= LA10_0 <= 5108) or (5121 <= LA10_0 <= 5740) or (5743 <= LA10_0 <= 5750) or (5761 <= LA10_0 <= 5786) or (5792 <= LA10_0 <= 5866) or (5870 <= LA10_0 <= 5872) or (5888 <= LA10_0 <= 5900) or (5902 <= LA10_0 <= 5908) or (5920 <= LA10_0 <= 5940) or (5952 <= LA10_0 <= 5971) or (5984 <= LA10_0 <= 5996) or (5998 <= LA10_0 <= 6000) or (6002 <= LA10_0 <= 6003) or (6016 <= LA10_0 <= 6099) or LA10_0 == 6103 or (6107 <= LA10_0 <= 6109) or (6112 <= LA10_0 <= 6121) or (6155 <= LA10_0 <= 6157) or (6160 <= LA10_0 <= 6169) or (6176 <= LA10_0 <= 6263) or (6272 <= LA10_0 <= 6313) or (6400 <= LA10_0 <= 6428) or (6432 <= LA10_0 <= 6443) or (6448 <= LA10_0 <= 6459) or (6470 <= LA10_0 <= 6509) or (6512 <= LA10_0 <= 6516) or (7424 <= LA10_0 <= 7531) or (7680 <= LA10_0 <= 7835) or (7840 <= LA10_0 <= 7929) or (7936 <= LA10_0 <= 7957) or (7960 <= LA10_0 <= 7965) or (7968 <= LA10_0 <= 8005) or (8008 <= LA10_0 <= 8013) or (8016 <= LA10_0 <= 8023) or LA10_0 == 8025 or LA10_0 == 8027 or LA10_0 == 8029 or (8031 <= LA10_0 <= 8061) or (8064 <= LA10_0 <= 8116) or (8118 <= LA10_0 <= 8124) or LA10_0 == 8126 or (8130 <= LA10_0 <= 8132) or (8134 <= LA10_0 <= 8140) or (8144 <= LA10_0 <= 8147) or (8150 <= LA10_0 <= 8155) or (8160 <= LA10_0 <= 8172) or (8178 <= LA10_0 <= 8180) or (8182 <= LA10_0 <= 8188) or (8204 <= LA10_0 <= 8207) or (8234 <= LA10_0 <= 8238) or (8255 <= LA10_0 <= 8256) or LA10_0 == 8276 or (8288 <= LA10_0 <= 8291) or (8298 <= LA10_0 <= 8303) or LA10_0 == 8305 or LA10_0 == 8319 or (8352 <= LA10_0 <= 8369) or (8400 <= LA10_0 <= 8412) or LA10_0 == 8417 or (8421 <= LA10_0 <= 8426) or LA10_0 == 8450 or LA10_0 == 8455 or (8458 <= LA10_0 <= 8467) or LA10_0 == 8469 or (8473 <= LA10_0 <= 8477) or LA10_0 == 8484 or LA10_0 == 8486 or LA10_0 == 8488 or (8490 <= LA10_0 <= 8493) or (8495 <= LA10_0 <= 8497) or (8499 <= LA10_0 <= 8505) or (8509 <= LA10_0 <= 8511) or (8517 <= LA10_0 <= 8521) or (8544 <= LA10_0 <= 8579) or (12293 <= LA10_0 <= 12295) or (12321 <= LA10_0 <= 12335) or (12337 <= LA10_0 <= 12341) or (12344 <= LA10_0 <= 12348) or (12353 <= LA10_0 <= 12438) or (12441 <= LA10_0 <= 12442) or (12445 <= LA10_0 <= 12447) or (12449 <= LA10_0 <= 12543) or (12549 <= LA10_0 <= 12588) or (12593 <= LA10_0 <= 12686) or (12704 <= LA10_0 <= 12727) or (12784 <= LA10_0 <= 12799) or (13312 <= LA10_0 <= 19893) or (19968 <= LA10_0 <= 40869) or (40960 <= LA10_0 <= 42124) or (44032 <= LA10_0 <= 55203) or (55296 <= LA10_0 <= 56319) or (63744 <= LA10_0 <= 64045) or (64048 <= LA10_0 <= 64106) or (64256 <= LA10_0 <= 64262) or (64275 <= LA10_0 <= 64279) or (64285 <= LA10_0 <= 64296) or (64298 <= LA10_0 <= 64310) or (64312 <= LA10_0 <= 64316) or LA10_0 == 64318 or (64320 <= LA10_0 <= 64321) or (64323 <= LA10_0 <= 64324) or (64326 <= LA10_0 <= 64433) or (64467 <= LA10_0 <= 64829) or (64848 <= LA10_0 <= 64911) or (64914 <= LA10_0 <= 64967) or (65008 <= LA10_0 <= 65020) or (65024 <= LA10_0 <= 65039) or (65056 <= LA10_0 <= 65059) or (65075 <= LA10_0 <= 65076) or (65101 <= LA10_0 <= 65103) or LA10_0 == 65129 or (65136 <= LA10_0 <= 65140) or (65142 <= LA10_0 <= 65276) or LA10_0 == 65279 or LA10_0 == 65284 or (65296 <= LA10_0 <= 65305) or (65313 <= LA10_0 <= 65338) or LA10_0 == 65343 or (65345 <= LA10_0 <= 65370) or (65381 <= LA10_0 <= 65470) or (65474 <= LA10_0 <= 65479) or (65482 <= LA10_0 <= 65487) or (65490 <= LA10_0 <= 65495) or (65498 <= LA10_0 <= 65500) or (65504 <= LA10_0 <= 65505) or (65509 <= LA10_0 <= 65510) or (65529 <= LA10_0 <= 65531)) :
                    alt10 = 1


                if alt10 == 1:
                    # gleampython/gleam.g:124:25: IdentifierPart
                    pass 
                    self.mIdentifierPart()


                else:
                    break #loop10



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IDENTIFIER"



    # $ANTLR start "SurrogateIdentifer"
    def mSurrogateIdentifer(self, ):

        try:
            # gleampython/gleam.g:129:5: ( ( '\\ud800' .. '\\udbff' ) ( '\\udc00' .. '\\udfff' ) )
            # gleampython/gleam.g:129:9: ( '\\ud800' .. '\\udbff' ) ( '\\udc00' .. '\\udfff' )
            pass 
            # gleampython/gleam.g:129:9: ( '\\ud800' .. '\\udbff' )
            # gleampython/gleam.g:129:10: '\\ud800' .. '\\udbff'
            pass 
            self.matchRange(55296, 56319)



            # gleampython/gleam.g:129:30: ( '\\udc00' .. '\\udfff' )
            # gleampython/gleam.g:129:31: '\\udc00' .. '\\udfff'
            pass 
            self.matchRange(56320, 57343)







        finally:

            pass

    # $ANTLR end "SurrogateIdentifer"



    # $ANTLR start "IdentifierStart"
    def mIdentifierStart(self, ):

        try:
            # gleampython/gleam.g:134:5: ( '\\u0024' | '\\u0041' .. '\\u005a' | '\\u005f' | '\\u0061' .. '\\u007a' | '\\u00a2' .. '\\u00a5' | '\\u00aa' | '\\u00b5' | '\\u00ba' | '\\u00c0' .. '\\u00d6' | '\\u00d8' .. '\\u00f6' | '\\u00f8' .. '\\u0236' | '\\u0250' .. '\\u02c1' | '\\u02c6' .. '\\u02d1' | '\\u02e0' .. '\\u02e4' | '\\u02ee' | '\\u037a' | '\\u0386' | '\\u0388' .. '\\u038a' | '\\u038c' | '\\u038e' .. '\\u03a1' | '\\u03a3' .. '\\u03ce' | '\\u03d0' .. '\\u03f5' | '\\u03f7' .. '\\u03fb' | '\\u0400' .. '\\u0481' | '\\u048a' .. '\\u04ce' | '\\u04d0' .. '\\u04f5' | '\\u04f8' .. '\\u04f9' | '\\u0500' .. '\\u050f' | '\\u0531' .. '\\u0556' | '\\u0559' | '\\u0561' .. '\\u0587' | '\\u05d0' .. '\\u05ea' | '\\u05f0' .. '\\u05f2' | '\\u0621' .. '\\u063a' | '\\u0640' .. '\\u064a' | '\\u066e' .. '\\u066f' | '\\u0671' .. '\\u06d3' | '\\u06d5' | '\\u06e5' .. '\\u06e6' | '\\u06ee' .. '\\u06ef' | '\\u06fa' .. '\\u06fc' | '\\u06ff' | '\\u0710' | '\\u0712' .. '\\u072f' | '\\u074d' .. '\\u074f' | '\\u0780' .. '\\u07a5' | '\\u07b1' | '\\u0904' .. '\\u0939' | '\\u093d' | '\\u0950' | '\\u0958' .. '\\u0961' | '\\u0985' .. '\\u098c' | '\\u098f' .. '\\u0990' | '\\u0993' .. '\\u09a8' | '\\u09aa' .. '\\u09b0' | '\\u09b2' | '\\u09b6' .. '\\u09b9' | '\\u09bd' | '\\u09dc' .. '\\u09dd' | '\\u09df' .. '\\u09e1' | '\\u09f0' .. '\\u09f3' | '\\u0a05' .. '\\u0a0a' | '\\u0a0f' .. '\\u0a10' | '\\u0a13' .. '\\u0a28' | '\\u0a2a' .. '\\u0a30' | '\\u0a32' .. '\\u0a33' | '\\u0a35' .. '\\u0a36' | '\\u0a38' .. '\\u0a39' | '\\u0a59' .. '\\u0a5c' | '\\u0a5e' | '\\u0a72' .. '\\u0a74' | '\\u0a85' .. '\\u0a8d' | '\\u0a8f' .. '\\u0a91' | '\\u0a93' .. '\\u0aa8' | '\\u0aaa' .. '\\u0ab0' | '\\u0ab2' .. '\\u0ab3' | '\\u0ab5' .. '\\u0ab9' | '\\u0abd' | '\\u0ad0' | '\\u0ae0' .. '\\u0ae1' | '\\u0af1' | '\\u0b05' .. '\\u0b0c' | '\\u0b0f' .. '\\u0b10' | '\\u0b13' .. '\\u0b28' | '\\u0b2a' .. '\\u0b30' | '\\u0b32' .. '\\u0b33' | '\\u0b35' .. '\\u0b39' | '\\u0b3d' | '\\u0b5c' .. '\\u0b5d' | '\\u0b5f' .. '\\u0b61' | '\\u0b71' | '\\u0b83' | '\\u0b85' .. '\\u0b8a' | '\\u0b8e' .. '\\u0b90' | '\\u0b92' .. '\\u0b95' | '\\u0b99' .. '\\u0b9a' | '\\u0b9c' | '\\u0b9e' .. '\\u0b9f' | '\\u0ba3' .. '\\u0ba4' | '\\u0ba8' .. '\\u0baa' | '\\u0bae' .. '\\u0bb5' | '\\u0bb7' .. '\\u0bb9' | '\\u0bf9' | '\\u0c05' .. '\\u0c0c' | '\\u0c0e' .. '\\u0c10' | '\\u0c12' .. '\\u0c28' | '\\u0c2a' .. '\\u0c33' | '\\u0c35' .. '\\u0c39' | '\\u0c60' .. '\\u0c61' | '\\u0c85' .. '\\u0c8c' | '\\u0c8e' .. '\\u0c90' | '\\u0c92' .. '\\u0ca8' | '\\u0caa' .. '\\u0cb3' | '\\u0cb5' .. '\\u0cb9' | '\\u0cbd' | '\\u0cde' | '\\u0ce0' .. '\\u0ce1' | '\\u0d05' .. '\\u0d0c' | '\\u0d0e' .. '\\u0d10' | '\\u0d12' .. '\\u0d28' | '\\u0d2a' .. '\\u0d39' | '\\u0d60' .. '\\u0d61' | '\\u0d85' .. '\\u0d96' | '\\u0d9a' .. '\\u0db1' | '\\u0db3' .. '\\u0dbb' | '\\u0dbd' | '\\u0dc0' .. '\\u0dc6' | '\\u0e01' .. '\\u0e30' | '\\u0e32' .. '\\u0e33' | '\\u0e3f' .. '\\u0e46' | '\\u0e81' .. '\\u0e82' | '\\u0e84' | '\\u0e87' .. '\\u0e88' | '\\u0e8a' | '\\u0e8d' | '\\u0e94' .. '\\u0e97' | '\\u0e99' .. '\\u0e9f' | '\\u0ea1' .. '\\u0ea3' | '\\u0ea5' | '\\u0ea7' | '\\u0eaa' .. '\\u0eab' | '\\u0ead' .. '\\u0eb0' | '\\u0eb2' .. '\\u0eb3' | '\\u0ebd' | '\\u0ec0' .. '\\u0ec4' | '\\u0ec6' | '\\u0edc' .. '\\u0edd' | '\\u0f00' | '\\u0f40' .. '\\u0f47' | '\\u0f49' .. '\\u0f6a' | '\\u0f88' .. '\\u0f8b' | '\\u1000' .. '\\u1021' | '\\u1023' .. '\\u1027' | '\\u1029' .. '\\u102a' | '\\u1050' .. '\\u1055' | '\\u10a0' .. '\\u10c5' | '\\u10d0' .. '\\u10f8' | '\\u1100' .. '\\u1159' | '\\u115f' .. '\\u11a2' | '\\u11a8' .. '\\u11f9' | '\\u1200' .. '\\u1206' | '\\u1208' .. '\\u1246' | '\\u1248' | '\\u124a' .. '\\u124d' | '\\u1250' .. '\\u1256' | '\\u1258' | '\\u125a' .. '\\u125d' | '\\u1260' .. '\\u1286' | '\\u1288' | '\\u128a' .. '\\u128d' | '\\u1290' .. '\\u12ae' | '\\u12b0' | '\\u12b2' .. '\\u12b5' | '\\u12b8' .. '\\u12be' | '\\u12c0' | '\\u12c2' .. '\\u12c5' | '\\u12c8' .. '\\u12ce' | '\\u12d0' .. '\\u12d6' | '\\u12d8' .. '\\u12ee' | '\\u12f0' .. '\\u130e' | '\\u1310' | '\\u1312' .. '\\u1315' | '\\u1318' .. '\\u131e' | '\\u1320' .. '\\u1346' | '\\u1348' .. '\\u135a' | '\\u13a0' .. '\\u13f4' | '\\u1401' .. '\\u166c' | '\\u166f' .. '\\u1676' | '\\u1681' .. '\\u169a' | '\\u16a0' .. '\\u16ea' | '\\u16ee' .. '\\u16f0' | '\\u1700' .. '\\u170c' | '\\u170e' .. '\\u1711' | '\\u1720' .. '\\u1731' | '\\u1740' .. '\\u1751' | '\\u1760' .. '\\u176c' | '\\u176e' .. '\\u1770' | '\\u1780' .. '\\u17b3' | '\\u17d7' | '\\u17db' .. '\\u17dc' | '\\u1820' .. '\\u1877' | '\\u1880' .. '\\u18a8' | '\\u1900' .. '\\u191c' | '\\u1950' .. '\\u196d' | '\\u1970' .. '\\u1974' | '\\u1d00' .. '\\u1d6b' | '\\u1e00' .. '\\u1e9b' | '\\u1ea0' .. '\\u1ef9' | '\\u1f00' .. '\\u1f15' | '\\u1f18' .. '\\u1f1d' | '\\u1f20' .. '\\u1f45' | '\\u1f48' .. '\\u1f4d' | '\\u1f50' .. '\\u1f57' | '\\u1f59' | '\\u1f5b' | '\\u1f5d' | '\\u1f5f' .. '\\u1f7d' | '\\u1f80' .. '\\u1fb4' | '\\u1fb6' .. '\\u1fbc' | '\\u1fbe' | '\\u1fc2' .. '\\u1fc4' | '\\u1fc6' .. '\\u1fcc' | '\\u1fd0' .. '\\u1fd3' | '\\u1fd6' .. '\\u1fdb' | '\\u1fe0' .. '\\u1fec' | '\\u1ff2' .. '\\u1ff4' | '\\u1ff6' .. '\\u1ffc' | '\\u203f' .. '\\u2040' | '\\u2054' | '\\u2071' | '\\u207f' | '\\u20a0' .. '\\u20b1' | '\\u2102' | '\\u2107' | '\\u210a' .. '\\u2113' | '\\u2115' | '\\u2119' .. '\\u211d' | '\\u2124' | '\\u2126' | '\\u2128' | '\\u212a' .. '\\u212d' | '\\u212f' .. '\\u2131' | '\\u2133' .. '\\u2139' | '\\u213d' .. '\\u213f' | '\\u2145' .. '\\u2149' | '\\u2160' .. '\\u2183' | '\\u3005' .. '\\u3007' | '\\u3021' .. '\\u3029' | '\\u3031' .. '\\u3035' | '\\u3038' .. '\\u303c' | '\\u3041' .. '\\u3096' | '\\u309d' .. '\\u309f' | '\\u30a1' .. '\\u30ff' | '\\u3105' .. '\\u312c' | '\\u3131' .. '\\u318e' | '\\u31a0' .. '\\u31b7' | '\\u31f0' .. '\\u31ff' | '\\u3400' .. '\\u4db5' | '\\u4e00' .. '\\u9fa5' | '\\ua000' .. '\\ua48c' | '\\uac00' .. '\\ud7a3' | '\\uf900' .. '\\ufa2d' | '\\ufa30' .. '\\ufa6a' | '\\ufb00' .. '\\ufb06' | '\\ufb13' .. '\\ufb17' | '\\ufb1d' | '\\ufb1f' .. '\\ufb28' | '\\ufb2a' .. '\\ufb36' | '\\ufb38' .. '\\ufb3c' | '\\ufb3e' | '\\ufb40' .. '\\ufb41' | '\\ufb43' .. '\\ufb44' | '\\ufb46' .. '\\ufbb1' | '\\ufbd3' .. '\\ufd3d' | '\\ufd50' .. '\\ufd8f' | '\\ufd92' .. '\\ufdc7' | '\\ufdf0' .. '\\ufdfc' | '\\ufe33' .. '\\ufe34' | '\\ufe4d' .. '\\ufe4f' | '\\ufe69' | '\\ufe70' .. '\\ufe74' | '\\ufe76' .. '\\ufefc' | '\\uff04' | '\\uff21' .. '\\uff3a' | '\\uff3f' | '\\uff41' .. '\\uff5a' | '\\uff65' .. '\\uffbe' | '\\uffc2' .. '\\uffc7' | '\\uffca' .. '\\uffcf' | '\\uffd2' .. '\\uffd7' | '\\uffda' .. '\\uffdc' | '\\uffe0' .. '\\uffe1' | '\\uffe5' .. '\\uffe6' | ( '\\ud800' .. '\\udbff' ) ( '\\udc00' .. '\\udfff' ) )
            alt11 = 294
            LA11_0 = self.input.LA(1)

            if (LA11_0 == 36) :
                alt11 = 1
            elif ((65 <= LA11_0 <= 90)) :
                alt11 = 2
            elif (LA11_0 == 95) :
                alt11 = 3
            elif ((97 <= LA11_0 <= 122)) :
                alt11 = 4
            elif ((162 <= LA11_0 <= 165)) :
                alt11 = 5
            elif (LA11_0 == 170) :
                alt11 = 6
            elif (LA11_0 == 181) :
                alt11 = 7
            elif (LA11_0 == 186) :
                alt11 = 8
            elif ((192 <= LA11_0 <= 214)) :
                alt11 = 9
            elif ((216 <= LA11_0 <= 246)) :
                alt11 = 10
            elif ((248 <= LA11_0 <= 566)) :
                alt11 = 11
            elif ((592 <= LA11_0 <= 705)) :
                alt11 = 12
            elif ((710 <= LA11_0 <= 721)) :
                alt11 = 13
            elif ((736 <= LA11_0 <= 740)) :
                alt11 = 14
            elif (LA11_0 == 750) :
                alt11 = 15
            elif (LA11_0 == 890) :
                alt11 = 16
            elif (LA11_0 == 902) :
                alt11 = 17
            elif ((904 <= LA11_0 <= 906)) :
                alt11 = 18
            elif (LA11_0 == 908) :
                alt11 = 19
            elif ((910 <= LA11_0 <= 929)) :
                alt11 = 20
            elif ((931 <= LA11_0 <= 974)) :
                alt11 = 21
            elif ((976 <= LA11_0 <= 1013)) :
                alt11 = 22
            elif ((1015 <= LA11_0 <= 1019)) :
                alt11 = 23
            elif ((1024 <= LA11_0 <= 1153)) :
                alt11 = 24
            elif ((1162 <= LA11_0 <= 1230)) :
                alt11 = 25
            elif ((1232 <= LA11_0 <= 1269)) :
                alt11 = 26
            elif ((1272 <= LA11_0 <= 1273)) :
                alt11 = 27
            elif ((1280 <= LA11_0 <= 1295)) :
                alt11 = 28
            elif ((1329 <= LA11_0 <= 1366)) :
                alt11 = 29
            elif (LA11_0 == 1369) :
                alt11 = 30
            elif ((1377 <= LA11_0 <= 1415)) :
                alt11 = 31
            elif ((1488 <= LA11_0 <= 1514)) :
                alt11 = 32
            elif ((1520 <= LA11_0 <= 1522)) :
                alt11 = 33
            elif ((1569 <= LA11_0 <= 1594)) :
                alt11 = 34
            elif ((1600 <= LA11_0 <= 1610)) :
                alt11 = 35
            elif ((1646 <= LA11_0 <= 1647)) :
                alt11 = 36
            elif ((1649 <= LA11_0 <= 1747)) :
                alt11 = 37
            elif (LA11_0 == 1749) :
                alt11 = 38
            elif ((1765 <= LA11_0 <= 1766)) :
                alt11 = 39
            elif ((1774 <= LA11_0 <= 1775)) :
                alt11 = 40
            elif ((1786 <= LA11_0 <= 1788)) :
                alt11 = 41
            elif (LA11_0 == 1791) :
                alt11 = 42
            elif (LA11_0 == 1808) :
                alt11 = 43
            elif ((1810 <= LA11_0 <= 1839)) :
                alt11 = 44
            elif ((1869 <= LA11_0 <= 1871)) :
                alt11 = 45
            elif ((1920 <= LA11_0 <= 1957)) :
                alt11 = 46
            elif (LA11_0 == 1969) :
                alt11 = 47
            elif ((2308 <= LA11_0 <= 2361)) :
                alt11 = 48
            elif (LA11_0 == 2365) :
                alt11 = 49
            elif (LA11_0 == 2384) :
                alt11 = 50
            elif ((2392 <= LA11_0 <= 2401)) :
                alt11 = 51
            elif ((2437 <= LA11_0 <= 2444)) :
                alt11 = 52
            elif ((2447 <= LA11_0 <= 2448)) :
                alt11 = 53
            elif ((2451 <= LA11_0 <= 2472)) :
                alt11 = 54
            elif ((2474 <= LA11_0 <= 2480)) :
                alt11 = 55
            elif (LA11_0 == 2482) :
                alt11 = 56
            elif ((2486 <= LA11_0 <= 2489)) :
                alt11 = 57
            elif (LA11_0 == 2493) :
                alt11 = 58
            elif ((2524 <= LA11_0 <= 2525)) :
                alt11 = 59
            elif ((2527 <= LA11_0 <= 2529)) :
                alt11 = 60
            elif ((2544 <= LA11_0 <= 2547)) :
                alt11 = 61
            elif ((2565 <= LA11_0 <= 2570)) :
                alt11 = 62
            elif ((2575 <= LA11_0 <= 2576)) :
                alt11 = 63
            elif ((2579 <= LA11_0 <= 2600)) :
                alt11 = 64
            elif ((2602 <= LA11_0 <= 2608)) :
                alt11 = 65
            elif ((2610 <= LA11_0 <= 2611)) :
                alt11 = 66
            elif ((2613 <= LA11_0 <= 2614)) :
                alt11 = 67
            elif ((2616 <= LA11_0 <= 2617)) :
                alt11 = 68
            elif ((2649 <= LA11_0 <= 2652)) :
                alt11 = 69
            elif (LA11_0 == 2654) :
                alt11 = 70
            elif ((2674 <= LA11_0 <= 2676)) :
                alt11 = 71
            elif ((2693 <= LA11_0 <= 2701)) :
                alt11 = 72
            elif ((2703 <= LA11_0 <= 2705)) :
                alt11 = 73
            elif ((2707 <= LA11_0 <= 2728)) :
                alt11 = 74
            elif ((2730 <= LA11_0 <= 2736)) :
                alt11 = 75
            elif ((2738 <= LA11_0 <= 2739)) :
                alt11 = 76
            elif ((2741 <= LA11_0 <= 2745)) :
                alt11 = 77
            elif (LA11_0 == 2749) :
                alt11 = 78
            elif (LA11_0 == 2768) :
                alt11 = 79
            elif ((2784 <= LA11_0 <= 2785)) :
                alt11 = 80
            elif (LA11_0 == 2801) :
                alt11 = 81
            elif ((2821 <= LA11_0 <= 2828)) :
                alt11 = 82
            elif ((2831 <= LA11_0 <= 2832)) :
                alt11 = 83
            elif ((2835 <= LA11_0 <= 2856)) :
                alt11 = 84
            elif ((2858 <= LA11_0 <= 2864)) :
                alt11 = 85
            elif ((2866 <= LA11_0 <= 2867)) :
                alt11 = 86
            elif ((2869 <= LA11_0 <= 2873)) :
                alt11 = 87
            elif (LA11_0 == 2877) :
                alt11 = 88
            elif ((2908 <= LA11_0 <= 2909)) :
                alt11 = 89
            elif ((2911 <= LA11_0 <= 2913)) :
                alt11 = 90
            elif (LA11_0 == 2929) :
                alt11 = 91
            elif (LA11_0 == 2947) :
                alt11 = 92
            elif ((2949 <= LA11_0 <= 2954)) :
                alt11 = 93
            elif ((2958 <= LA11_0 <= 2960)) :
                alt11 = 94
            elif ((2962 <= LA11_0 <= 2965)) :
                alt11 = 95
            elif ((2969 <= LA11_0 <= 2970)) :
                alt11 = 96
            elif (LA11_0 == 2972) :
                alt11 = 97
            elif ((2974 <= LA11_0 <= 2975)) :
                alt11 = 98
            elif ((2979 <= LA11_0 <= 2980)) :
                alt11 = 99
            elif ((2984 <= LA11_0 <= 2986)) :
                alt11 = 100
            elif ((2990 <= LA11_0 <= 2997)) :
                alt11 = 101
            elif ((2999 <= LA11_0 <= 3001)) :
                alt11 = 102
            elif (LA11_0 == 3065) :
                alt11 = 103
            elif ((3077 <= LA11_0 <= 3084)) :
                alt11 = 104
            elif ((3086 <= LA11_0 <= 3088)) :
                alt11 = 105
            elif ((3090 <= LA11_0 <= 3112)) :
                alt11 = 106
            elif ((3114 <= LA11_0 <= 3123)) :
                alt11 = 107
            elif ((3125 <= LA11_0 <= 3129)) :
                alt11 = 108
            elif ((3168 <= LA11_0 <= 3169)) :
                alt11 = 109
            elif ((3205 <= LA11_0 <= 3212)) :
                alt11 = 110
            elif ((3214 <= LA11_0 <= 3216)) :
                alt11 = 111
            elif ((3218 <= LA11_0 <= 3240)) :
                alt11 = 112
            elif ((3242 <= LA11_0 <= 3251)) :
                alt11 = 113
            elif ((3253 <= LA11_0 <= 3257)) :
                alt11 = 114
            elif (LA11_0 == 3261) :
                alt11 = 115
            elif (LA11_0 == 3294) :
                alt11 = 116
            elif ((3296 <= LA11_0 <= 3297)) :
                alt11 = 117
            elif ((3333 <= LA11_0 <= 3340)) :
                alt11 = 118
            elif ((3342 <= LA11_0 <= 3344)) :
                alt11 = 119
            elif ((3346 <= LA11_0 <= 3368)) :
                alt11 = 120
            elif ((3370 <= LA11_0 <= 3385)) :
                alt11 = 121
            elif ((3424 <= LA11_0 <= 3425)) :
                alt11 = 122
            elif ((3461 <= LA11_0 <= 3478)) :
                alt11 = 123
            elif ((3482 <= LA11_0 <= 3505)) :
                alt11 = 124
            elif ((3507 <= LA11_0 <= 3515)) :
                alt11 = 125
            elif (LA11_0 == 3517) :
                alt11 = 126
            elif ((3520 <= LA11_0 <= 3526)) :
                alt11 = 127
            elif ((3585 <= LA11_0 <= 3632)) :
                alt11 = 128
            elif ((3634 <= LA11_0 <= 3635)) :
                alt11 = 129
            elif ((3647 <= LA11_0 <= 3654)) :
                alt11 = 130
            elif ((3713 <= LA11_0 <= 3714)) :
                alt11 = 131
            elif (LA11_0 == 3716) :
                alt11 = 132
            elif ((3719 <= LA11_0 <= 3720)) :
                alt11 = 133
            elif (LA11_0 == 3722) :
                alt11 = 134
            elif (LA11_0 == 3725) :
                alt11 = 135
            elif ((3732 <= LA11_0 <= 3735)) :
                alt11 = 136
            elif ((3737 <= LA11_0 <= 3743)) :
                alt11 = 137
            elif ((3745 <= LA11_0 <= 3747)) :
                alt11 = 138
            elif (LA11_0 == 3749) :
                alt11 = 139
            elif (LA11_0 == 3751) :
                alt11 = 140
            elif ((3754 <= LA11_0 <= 3755)) :
                alt11 = 141
            elif ((3757 <= LA11_0 <= 3760)) :
                alt11 = 142
            elif ((3762 <= LA11_0 <= 3763)) :
                alt11 = 143
            elif (LA11_0 == 3773) :
                alt11 = 144
            elif ((3776 <= LA11_0 <= 3780)) :
                alt11 = 145
            elif (LA11_0 == 3782) :
                alt11 = 146
            elif ((3804 <= LA11_0 <= 3805)) :
                alt11 = 147
            elif (LA11_0 == 3840) :
                alt11 = 148
            elif ((3904 <= LA11_0 <= 3911)) :
                alt11 = 149
            elif ((3913 <= LA11_0 <= 3946)) :
                alt11 = 150
            elif ((3976 <= LA11_0 <= 3979)) :
                alt11 = 151
            elif ((4096 <= LA11_0 <= 4129)) :
                alt11 = 152
            elif ((4131 <= LA11_0 <= 4135)) :
                alt11 = 153
            elif ((4137 <= LA11_0 <= 4138)) :
                alt11 = 154
            elif ((4176 <= LA11_0 <= 4181)) :
                alt11 = 155
            elif ((4256 <= LA11_0 <= 4293)) :
                alt11 = 156
            elif ((4304 <= LA11_0 <= 4344)) :
                alt11 = 157
            elif ((4352 <= LA11_0 <= 4441)) :
                alt11 = 158
            elif ((4447 <= LA11_0 <= 4514)) :
                alt11 = 159
            elif ((4520 <= LA11_0 <= 4601)) :
                alt11 = 160
            elif ((4608 <= LA11_0 <= 4614)) :
                alt11 = 161
            elif ((4616 <= LA11_0 <= 4678)) :
                alt11 = 162
            elif (LA11_0 == 4680) :
                alt11 = 163
            elif ((4682 <= LA11_0 <= 4685)) :
                alt11 = 164
            elif ((4688 <= LA11_0 <= 4694)) :
                alt11 = 165
            elif (LA11_0 == 4696) :
                alt11 = 166
            elif ((4698 <= LA11_0 <= 4701)) :
                alt11 = 167
            elif ((4704 <= LA11_0 <= 4742)) :
                alt11 = 168
            elif (LA11_0 == 4744) :
                alt11 = 169
            elif ((4746 <= LA11_0 <= 4749)) :
                alt11 = 170
            elif ((4752 <= LA11_0 <= 4782)) :
                alt11 = 171
            elif (LA11_0 == 4784) :
                alt11 = 172
            elif ((4786 <= LA11_0 <= 4789)) :
                alt11 = 173
            elif ((4792 <= LA11_0 <= 4798)) :
                alt11 = 174
            elif (LA11_0 == 4800) :
                alt11 = 175
            elif ((4802 <= LA11_0 <= 4805)) :
                alt11 = 176
            elif ((4808 <= LA11_0 <= 4814)) :
                alt11 = 177
            elif ((4816 <= LA11_0 <= 4822)) :
                alt11 = 178
            elif ((4824 <= LA11_0 <= 4846)) :
                alt11 = 179
            elif ((4848 <= LA11_0 <= 4878)) :
                alt11 = 180
            elif (LA11_0 == 4880) :
                alt11 = 181
            elif ((4882 <= LA11_0 <= 4885)) :
                alt11 = 182
            elif ((4888 <= LA11_0 <= 4894)) :
                alt11 = 183
            elif ((4896 <= LA11_0 <= 4934)) :
                alt11 = 184
            elif ((4936 <= LA11_0 <= 4954)) :
                alt11 = 185
            elif ((5024 <= LA11_0 <= 5108)) :
                alt11 = 186
            elif ((5121 <= LA11_0 <= 5740)) :
                alt11 = 187
            elif ((5743 <= LA11_0 <= 5750)) :
                alt11 = 188
            elif ((5761 <= LA11_0 <= 5786)) :
                alt11 = 189
            elif ((5792 <= LA11_0 <= 5866)) :
                alt11 = 190
            elif ((5870 <= LA11_0 <= 5872)) :
                alt11 = 191
            elif ((5888 <= LA11_0 <= 5900)) :
                alt11 = 192
            elif ((5902 <= LA11_0 <= 5905)) :
                alt11 = 193
            elif ((5920 <= LA11_0 <= 5937)) :
                alt11 = 194
            elif ((5952 <= LA11_0 <= 5969)) :
                alt11 = 195
            elif ((5984 <= LA11_0 <= 5996)) :
                alt11 = 196
            elif ((5998 <= LA11_0 <= 6000)) :
                alt11 = 197
            elif ((6016 <= LA11_0 <= 6067)) :
                alt11 = 198
            elif (LA11_0 == 6103) :
                alt11 = 199
            elif ((6107 <= LA11_0 <= 6108)) :
                alt11 = 200
            elif ((6176 <= LA11_0 <= 6263)) :
                alt11 = 201
            elif ((6272 <= LA11_0 <= 6312)) :
                alt11 = 202
            elif ((6400 <= LA11_0 <= 6428)) :
                alt11 = 203
            elif ((6480 <= LA11_0 <= 6509)) :
                alt11 = 204
            elif ((6512 <= LA11_0 <= 6516)) :
                alt11 = 205
            elif ((7424 <= LA11_0 <= 7531)) :
                alt11 = 206
            elif ((7680 <= LA11_0 <= 7835)) :
                alt11 = 207
            elif ((7840 <= LA11_0 <= 7929)) :
                alt11 = 208
            elif ((7936 <= LA11_0 <= 7957)) :
                alt11 = 209
            elif ((7960 <= LA11_0 <= 7965)) :
                alt11 = 210
            elif ((7968 <= LA11_0 <= 8005)) :
                alt11 = 211
            elif ((8008 <= LA11_0 <= 8013)) :
                alt11 = 212
            elif ((8016 <= LA11_0 <= 8023)) :
                alt11 = 213
            elif (LA11_0 == 8025) :
                alt11 = 214
            elif (LA11_0 == 8027) :
                alt11 = 215
            elif (LA11_0 == 8029) :
                alt11 = 216
            elif ((8031 <= LA11_0 <= 8061)) :
                alt11 = 217
            elif ((8064 <= LA11_0 <= 8116)) :
                alt11 = 218
            elif ((8118 <= LA11_0 <= 8124)) :
                alt11 = 219
            elif (LA11_0 == 8126) :
                alt11 = 220
            elif ((8130 <= LA11_0 <= 8132)) :
                alt11 = 221
            elif ((8134 <= LA11_0 <= 8140)) :
                alt11 = 222
            elif ((8144 <= LA11_0 <= 8147)) :
                alt11 = 223
            elif ((8150 <= LA11_0 <= 8155)) :
                alt11 = 224
            elif ((8160 <= LA11_0 <= 8172)) :
                alt11 = 225
            elif ((8178 <= LA11_0 <= 8180)) :
                alt11 = 226
            elif ((8182 <= LA11_0 <= 8188)) :
                alt11 = 227
            elif ((8255 <= LA11_0 <= 8256)) :
                alt11 = 228
            elif (LA11_0 == 8276) :
                alt11 = 229
            elif (LA11_0 == 8305) :
                alt11 = 230
            elif (LA11_0 == 8319) :
                alt11 = 231
            elif ((8352 <= LA11_0 <= 8369)) :
                alt11 = 232
            elif (LA11_0 == 8450) :
                alt11 = 233
            elif (LA11_0 == 8455) :
                alt11 = 234
            elif ((8458 <= LA11_0 <= 8467)) :
                alt11 = 235
            elif (LA11_0 == 8469) :
                alt11 = 236
            elif ((8473 <= LA11_0 <= 8477)) :
                alt11 = 237
            elif (LA11_0 == 8484) :
                alt11 = 238
            elif (LA11_0 == 8486) :
                alt11 = 239
            elif (LA11_0 == 8488) :
                alt11 = 240
            elif ((8490 <= LA11_0 <= 8493)) :
                alt11 = 241
            elif ((8495 <= LA11_0 <= 8497)) :
                alt11 = 242
            elif ((8499 <= LA11_0 <= 8505)) :
                alt11 = 243
            elif ((8509 <= LA11_0 <= 8511)) :
                alt11 = 244
            elif ((8517 <= LA11_0 <= 8521)) :
                alt11 = 245
            elif ((8544 <= LA11_0 <= 8579)) :
                alt11 = 246
            elif ((12293 <= LA11_0 <= 12295)) :
                alt11 = 247
            elif ((12321 <= LA11_0 <= 12329)) :
                alt11 = 248
            elif ((12337 <= LA11_0 <= 12341)) :
                alt11 = 249
            elif ((12344 <= LA11_0 <= 12348)) :
                alt11 = 250
            elif ((12353 <= LA11_0 <= 12438)) :
                alt11 = 251
            elif ((12445 <= LA11_0 <= 12447)) :
                alt11 = 252
            elif ((12449 <= LA11_0 <= 12543)) :
                alt11 = 253
            elif ((12549 <= LA11_0 <= 12588)) :
                alt11 = 254
            elif ((12593 <= LA11_0 <= 12686)) :
                alt11 = 255
            elif ((12704 <= LA11_0 <= 12727)) :
                alt11 = 256
            elif ((12784 <= LA11_0 <= 12799)) :
                alt11 = 257
            elif ((13312 <= LA11_0 <= 19893)) :
                alt11 = 258
            elif ((19968 <= LA11_0 <= 40869)) :
                alt11 = 259
            elif ((40960 <= LA11_0 <= 42124)) :
                alt11 = 260
            elif ((44032 <= LA11_0 <= 55203)) :
                alt11 = 261
            elif ((63744 <= LA11_0 <= 64045)) :
                alt11 = 262
            elif ((64048 <= LA11_0 <= 64106)) :
                alt11 = 263
            elif ((64256 <= LA11_0 <= 64262)) :
                alt11 = 264
            elif ((64275 <= LA11_0 <= 64279)) :
                alt11 = 265
            elif (LA11_0 == 64285) :
                alt11 = 266
            elif ((64287 <= LA11_0 <= 64296)) :
                alt11 = 267
            elif ((64298 <= LA11_0 <= 64310)) :
                alt11 = 268
            elif ((64312 <= LA11_0 <= 64316)) :
                alt11 = 269
            elif (LA11_0 == 64318) :
                alt11 = 270
            elif ((64320 <= LA11_0 <= 64321)) :
                alt11 = 271
            elif ((64323 <= LA11_0 <= 64324)) :
                alt11 = 272
            elif ((64326 <= LA11_0 <= 64433)) :
                alt11 = 273
            elif ((64467 <= LA11_0 <= 64829)) :
                alt11 = 274
            elif ((64848 <= LA11_0 <= 64911)) :
                alt11 = 275
            elif ((64914 <= LA11_0 <= 64967)) :
                alt11 = 276
            elif ((65008 <= LA11_0 <= 65020)) :
                alt11 = 277
            elif ((65075 <= LA11_0 <= 65076)) :
                alt11 = 278
            elif ((65101 <= LA11_0 <= 65103)) :
                alt11 = 279
            elif (LA11_0 == 65129) :
                alt11 = 280
            elif ((65136 <= LA11_0 <= 65140)) :
                alt11 = 281
            elif ((65142 <= LA11_0 <= 65276)) :
                alt11 = 282
            elif (LA11_0 == 65284) :
                alt11 = 283
            elif ((65313 <= LA11_0 <= 65338)) :
                alt11 = 284
            elif (LA11_0 == 65343) :
                alt11 = 285
            elif ((65345 <= LA11_0 <= 65370)) :
                alt11 = 286
            elif ((65381 <= LA11_0 <= 65470)) :
                alt11 = 287
            elif ((65474 <= LA11_0 <= 65479)) :
                alt11 = 288
            elif ((65482 <= LA11_0 <= 65487)) :
                alt11 = 289
            elif ((65490 <= LA11_0 <= 65495)) :
                alt11 = 290
            elif ((65498 <= LA11_0 <= 65500)) :
                alt11 = 291
            elif ((65504 <= LA11_0 <= 65505)) :
                alt11 = 292
            elif ((65509 <= LA11_0 <= 65510)) :
                alt11 = 293
            elif ((55296 <= LA11_0 <= 56319)) :
                alt11 = 294
            else:
                nvae = NoViableAltException("", 11, 0, self.input)

                raise nvae

            if alt11 == 1:
                # gleampython/gleam.g:134:9: '\\u0024'
                pass 
                self.match(36)


            elif alt11 == 2:
                # gleampython/gleam.g:135:9: '\\u0041' .. '\\u005a'
                pass 
                self.matchRange(65, 90)


            elif alt11 == 3:
                # gleampython/gleam.g:136:9: '\\u005f'
                pass 
                self.match(95)


            elif alt11 == 4:
                # gleampython/gleam.g:137:9: '\\u0061' .. '\\u007a'
                pass 
                self.matchRange(97, 122)


            elif alt11 == 5:
                # gleampython/gleam.g:138:9: '\\u00a2' .. '\\u00a5'
                pass 
                self.matchRange(162, 165)


            elif alt11 == 6:
                # gleampython/gleam.g:139:9: '\\u00aa'
                pass 
                self.match(170)


            elif alt11 == 7:
                # gleampython/gleam.g:140:9: '\\u00b5'
                pass 
                self.match(181)


            elif alt11 == 8:
                # gleampython/gleam.g:141:9: '\\u00ba'
                pass 
                self.match(186)


            elif alt11 == 9:
                # gleampython/gleam.g:142:9: '\\u00c0' .. '\\u00d6'
                pass 
                self.matchRange(192, 214)


            elif alt11 == 10:
                # gleampython/gleam.g:143:9: '\\u00d8' .. '\\u00f6'
                pass 
                self.matchRange(216, 246)


            elif alt11 == 11:
                # gleampython/gleam.g:144:9: '\\u00f8' .. '\\u0236'
                pass 
                self.matchRange(248, 566)


            elif alt11 == 12:
                # gleampython/gleam.g:145:9: '\\u0250' .. '\\u02c1'
                pass 
                self.matchRange(592, 705)


            elif alt11 == 13:
                # gleampython/gleam.g:146:9: '\\u02c6' .. '\\u02d1'
                pass 
                self.matchRange(710, 721)


            elif alt11 == 14:
                # gleampython/gleam.g:147:9: '\\u02e0' .. '\\u02e4'
                pass 
                self.matchRange(736, 740)


            elif alt11 == 15:
                # gleampython/gleam.g:148:9: '\\u02ee'
                pass 
                self.match(750)


            elif alt11 == 16:
                # gleampython/gleam.g:149:9: '\\u037a'
                pass 
                self.match(890)


            elif alt11 == 17:
                # gleampython/gleam.g:150:9: '\\u0386'
                pass 
                self.match(902)


            elif alt11 == 18:
                # gleampython/gleam.g:151:9: '\\u0388' .. '\\u038a'
                pass 
                self.matchRange(904, 906)


            elif alt11 == 19:
                # gleampython/gleam.g:152:9: '\\u038c'
                pass 
                self.match(908)


            elif alt11 == 20:
                # gleampython/gleam.g:153:9: '\\u038e' .. '\\u03a1'
                pass 
                self.matchRange(910, 929)


            elif alt11 == 21:
                # gleampython/gleam.g:154:9: '\\u03a3' .. '\\u03ce'
                pass 
                self.matchRange(931, 974)


            elif alt11 == 22:
                # gleampython/gleam.g:155:9: '\\u03d0' .. '\\u03f5'
                pass 
                self.matchRange(976, 1013)


            elif alt11 == 23:
                # gleampython/gleam.g:156:9: '\\u03f7' .. '\\u03fb'
                pass 
                self.matchRange(1015, 1019)


            elif alt11 == 24:
                # gleampython/gleam.g:157:9: '\\u0400' .. '\\u0481'
                pass 
                self.matchRange(1024, 1153)


            elif alt11 == 25:
                # gleampython/gleam.g:158:9: '\\u048a' .. '\\u04ce'
                pass 
                self.matchRange(1162, 1230)


            elif alt11 == 26:
                # gleampython/gleam.g:159:9: '\\u04d0' .. '\\u04f5'
                pass 
                self.matchRange(1232, 1269)


            elif alt11 == 27:
                # gleampython/gleam.g:160:9: '\\u04f8' .. '\\u04f9'
                pass 
                self.matchRange(1272, 1273)


            elif alt11 == 28:
                # gleampython/gleam.g:161:9: '\\u0500' .. '\\u050f'
                pass 
                self.matchRange(1280, 1295)


            elif alt11 == 29:
                # gleampython/gleam.g:162:9: '\\u0531' .. '\\u0556'
                pass 
                self.matchRange(1329, 1366)


            elif alt11 == 30:
                # gleampython/gleam.g:163:9: '\\u0559'
                pass 
                self.match(1369)


            elif alt11 == 31:
                # gleampython/gleam.g:164:9: '\\u0561' .. '\\u0587'
                pass 
                self.matchRange(1377, 1415)


            elif alt11 == 32:
                # gleampython/gleam.g:165:9: '\\u05d0' .. '\\u05ea'
                pass 
                self.matchRange(1488, 1514)


            elif alt11 == 33:
                # gleampython/gleam.g:166:9: '\\u05f0' .. '\\u05f2'
                pass 
                self.matchRange(1520, 1522)


            elif alt11 == 34:
                # gleampython/gleam.g:167:9: '\\u0621' .. '\\u063a'
                pass 
                self.matchRange(1569, 1594)


            elif alt11 == 35:
                # gleampython/gleam.g:168:9: '\\u0640' .. '\\u064a'
                pass 
                self.matchRange(1600, 1610)


            elif alt11 == 36:
                # gleampython/gleam.g:169:9: '\\u066e' .. '\\u066f'
                pass 
                self.matchRange(1646, 1647)


            elif alt11 == 37:
                # gleampython/gleam.g:170:9: '\\u0671' .. '\\u06d3'
                pass 
                self.matchRange(1649, 1747)


            elif alt11 == 38:
                # gleampython/gleam.g:171:9: '\\u06d5'
                pass 
                self.match(1749)


            elif alt11 == 39:
                # gleampython/gleam.g:172:9: '\\u06e5' .. '\\u06e6'
                pass 
                self.matchRange(1765, 1766)


            elif alt11 == 40:
                # gleampython/gleam.g:173:9: '\\u06ee' .. '\\u06ef'
                pass 
                self.matchRange(1774, 1775)


            elif alt11 == 41:
                # gleampython/gleam.g:174:9: '\\u06fa' .. '\\u06fc'
                pass 
                self.matchRange(1786, 1788)


            elif alt11 == 42:
                # gleampython/gleam.g:175:9: '\\u06ff'
                pass 
                self.match(1791)


            elif alt11 == 43:
                # gleampython/gleam.g:176:9: '\\u0710'
                pass 
                self.match(1808)


            elif alt11 == 44:
                # gleampython/gleam.g:177:9: '\\u0712' .. '\\u072f'
                pass 
                self.matchRange(1810, 1839)


            elif alt11 == 45:
                # gleampython/gleam.g:178:9: '\\u074d' .. '\\u074f'
                pass 
                self.matchRange(1869, 1871)


            elif alt11 == 46:
                # gleampython/gleam.g:179:9: '\\u0780' .. '\\u07a5'
                pass 
                self.matchRange(1920, 1957)


            elif alt11 == 47:
                # gleampython/gleam.g:180:9: '\\u07b1'
                pass 
                self.match(1969)


            elif alt11 == 48:
                # gleampython/gleam.g:181:9: '\\u0904' .. '\\u0939'
                pass 
                self.matchRange(2308, 2361)


            elif alt11 == 49:
                # gleampython/gleam.g:182:9: '\\u093d'
                pass 
                self.match(2365)


            elif alt11 == 50:
                # gleampython/gleam.g:183:9: '\\u0950'
                pass 
                self.match(2384)


            elif alt11 == 51:
                # gleampython/gleam.g:184:9: '\\u0958' .. '\\u0961'
                pass 
                self.matchRange(2392, 2401)


            elif alt11 == 52:
                # gleampython/gleam.g:185:9: '\\u0985' .. '\\u098c'
                pass 
                self.matchRange(2437, 2444)


            elif alt11 == 53:
                # gleampython/gleam.g:186:9: '\\u098f' .. '\\u0990'
                pass 
                self.matchRange(2447, 2448)


            elif alt11 == 54:
                # gleampython/gleam.g:187:9: '\\u0993' .. '\\u09a8'
                pass 
                self.matchRange(2451, 2472)


            elif alt11 == 55:
                # gleampython/gleam.g:188:9: '\\u09aa' .. '\\u09b0'
                pass 
                self.matchRange(2474, 2480)


            elif alt11 == 56:
                # gleampython/gleam.g:189:9: '\\u09b2'
                pass 
                self.match(2482)


            elif alt11 == 57:
                # gleampython/gleam.g:190:9: '\\u09b6' .. '\\u09b9'
                pass 
                self.matchRange(2486, 2489)


            elif alt11 == 58:
                # gleampython/gleam.g:191:9: '\\u09bd'
                pass 
                self.match(2493)


            elif alt11 == 59:
                # gleampython/gleam.g:192:9: '\\u09dc' .. '\\u09dd'
                pass 
                self.matchRange(2524, 2525)


            elif alt11 == 60:
                # gleampython/gleam.g:193:9: '\\u09df' .. '\\u09e1'
                pass 
                self.matchRange(2527, 2529)


            elif alt11 == 61:
                # gleampython/gleam.g:194:9: '\\u09f0' .. '\\u09f3'
                pass 
                self.matchRange(2544, 2547)


            elif alt11 == 62:
                # gleampython/gleam.g:195:9: '\\u0a05' .. '\\u0a0a'
                pass 
                self.matchRange(2565, 2570)


            elif alt11 == 63:
                # gleampython/gleam.g:196:9: '\\u0a0f' .. '\\u0a10'
                pass 
                self.matchRange(2575, 2576)


            elif alt11 == 64:
                # gleampython/gleam.g:197:9: '\\u0a13' .. '\\u0a28'
                pass 
                self.matchRange(2579, 2600)


            elif alt11 == 65:
                # gleampython/gleam.g:198:9: '\\u0a2a' .. '\\u0a30'
                pass 
                self.matchRange(2602, 2608)


            elif alt11 == 66:
                # gleampython/gleam.g:199:9: '\\u0a32' .. '\\u0a33'
                pass 
                self.matchRange(2610, 2611)


            elif alt11 == 67:
                # gleampython/gleam.g:200:9: '\\u0a35' .. '\\u0a36'
                pass 
                self.matchRange(2613, 2614)


            elif alt11 == 68:
                # gleampython/gleam.g:201:9: '\\u0a38' .. '\\u0a39'
                pass 
                self.matchRange(2616, 2617)


            elif alt11 == 69:
                # gleampython/gleam.g:202:9: '\\u0a59' .. '\\u0a5c'
                pass 
                self.matchRange(2649, 2652)


            elif alt11 == 70:
                # gleampython/gleam.g:203:9: '\\u0a5e'
                pass 
                self.match(2654)


            elif alt11 == 71:
                # gleampython/gleam.g:204:9: '\\u0a72' .. '\\u0a74'
                pass 
                self.matchRange(2674, 2676)


            elif alt11 == 72:
                # gleampython/gleam.g:205:9: '\\u0a85' .. '\\u0a8d'
                pass 
                self.matchRange(2693, 2701)


            elif alt11 == 73:
                # gleampython/gleam.g:206:9: '\\u0a8f' .. '\\u0a91'
                pass 
                self.matchRange(2703, 2705)


            elif alt11 == 74:
                # gleampython/gleam.g:207:9: '\\u0a93' .. '\\u0aa8'
                pass 
                self.matchRange(2707, 2728)


            elif alt11 == 75:
                # gleampython/gleam.g:208:9: '\\u0aaa' .. '\\u0ab0'
                pass 
                self.matchRange(2730, 2736)


            elif alt11 == 76:
                # gleampython/gleam.g:209:9: '\\u0ab2' .. '\\u0ab3'
                pass 
                self.matchRange(2738, 2739)


            elif alt11 == 77:
                # gleampython/gleam.g:210:9: '\\u0ab5' .. '\\u0ab9'
                pass 
                self.matchRange(2741, 2745)


            elif alt11 == 78:
                # gleampython/gleam.g:211:9: '\\u0abd'
                pass 
                self.match(2749)


            elif alt11 == 79:
                # gleampython/gleam.g:212:9: '\\u0ad0'
                pass 
                self.match(2768)


            elif alt11 == 80:
                # gleampython/gleam.g:213:9: '\\u0ae0' .. '\\u0ae1'
                pass 
                self.matchRange(2784, 2785)


            elif alt11 == 81:
                # gleampython/gleam.g:214:9: '\\u0af1'
                pass 
                self.match(2801)


            elif alt11 == 82:
                # gleampython/gleam.g:215:9: '\\u0b05' .. '\\u0b0c'
                pass 
                self.matchRange(2821, 2828)


            elif alt11 == 83:
                # gleampython/gleam.g:216:9: '\\u0b0f' .. '\\u0b10'
                pass 
                self.matchRange(2831, 2832)


            elif alt11 == 84:
                # gleampython/gleam.g:217:9: '\\u0b13' .. '\\u0b28'
                pass 
                self.matchRange(2835, 2856)


            elif alt11 == 85:
                # gleampython/gleam.g:218:9: '\\u0b2a' .. '\\u0b30'
                pass 
                self.matchRange(2858, 2864)


            elif alt11 == 86:
                # gleampython/gleam.g:219:9: '\\u0b32' .. '\\u0b33'
                pass 
                self.matchRange(2866, 2867)


            elif alt11 == 87:
                # gleampython/gleam.g:220:9: '\\u0b35' .. '\\u0b39'
                pass 
                self.matchRange(2869, 2873)


            elif alt11 == 88:
                # gleampython/gleam.g:221:9: '\\u0b3d'
                pass 
                self.match(2877)


            elif alt11 == 89:
                # gleampython/gleam.g:222:9: '\\u0b5c' .. '\\u0b5d'
                pass 
                self.matchRange(2908, 2909)


            elif alt11 == 90:
                # gleampython/gleam.g:223:9: '\\u0b5f' .. '\\u0b61'
                pass 
                self.matchRange(2911, 2913)


            elif alt11 == 91:
                # gleampython/gleam.g:224:9: '\\u0b71'
                pass 
                self.match(2929)


            elif alt11 == 92:
                # gleampython/gleam.g:225:9: '\\u0b83'
                pass 
                self.match(2947)


            elif alt11 == 93:
                # gleampython/gleam.g:226:9: '\\u0b85' .. '\\u0b8a'
                pass 
                self.matchRange(2949, 2954)


            elif alt11 == 94:
                # gleampython/gleam.g:227:9: '\\u0b8e' .. '\\u0b90'
                pass 
                self.matchRange(2958, 2960)


            elif alt11 == 95:
                # gleampython/gleam.g:228:9: '\\u0b92' .. '\\u0b95'
                pass 
                self.matchRange(2962, 2965)


            elif alt11 == 96:
                # gleampython/gleam.g:229:9: '\\u0b99' .. '\\u0b9a'
                pass 
                self.matchRange(2969, 2970)


            elif alt11 == 97:
                # gleampython/gleam.g:230:9: '\\u0b9c'
                pass 
                self.match(2972)


            elif alt11 == 98:
                # gleampython/gleam.g:231:9: '\\u0b9e' .. '\\u0b9f'
                pass 
                self.matchRange(2974, 2975)


            elif alt11 == 99:
                # gleampython/gleam.g:232:9: '\\u0ba3' .. '\\u0ba4'
                pass 
                self.matchRange(2979, 2980)


            elif alt11 == 100:
                # gleampython/gleam.g:233:9: '\\u0ba8' .. '\\u0baa'
                pass 
                self.matchRange(2984, 2986)


            elif alt11 == 101:
                # gleampython/gleam.g:234:9: '\\u0bae' .. '\\u0bb5'
                pass 
                self.matchRange(2990, 2997)


            elif alt11 == 102:
                # gleampython/gleam.g:235:9: '\\u0bb7' .. '\\u0bb9'
                pass 
                self.matchRange(2999, 3001)


            elif alt11 == 103:
                # gleampython/gleam.g:236:9: '\\u0bf9'
                pass 
                self.match(3065)


            elif alt11 == 104:
                # gleampython/gleam.g:237:9: '\\u0c05' .. '\\u0c0c'
                pass 
                self.matchRange(3077, 3084)


            elif alt11 == 105:
                # gleampython/gleam.g:238:9: '\\u0c0e' .. '\\u0c10'
                pass 
                self.matchRange(3086, 3088)


            elif alt11 == 106:
                # gleampython/gleam.g:239:9: '\\u0c12' .. '\\u0c28'
                pass 
                self.matchRange(3090, 3112)


            elif alt11 == 107:
                # gleampython/gleam.g:240:9: '\\u0c2a' .. '\\u0c33'
                pass 
                self.matchRange(3114, 3123)


            elif alt11 == 108:
                # gleampython/gleam.g:241:9: '\\u0c35' .. '\\u0c39'
                pass 
                self.matchRange(3125, 3129)


            elif alt11 == 109:
                # gleampython/gleam.g:242:9: '\\u0c60' .. '\\u0c61'
                pass 
                self.matchRange(3168, 3169)


            elif alt11 == 110:
                # gleampython/gleam.g:243:9: '\\u0c85' .. '\\u0c8c'
                pass 
                self.matchRange(3205, 3212)


            elif alt11 == 111:
                # gleampython/gleam.g:244:9: '\\u0c8e' .. '\\u0c90'
                pass 
                self.matchRange(3214, 3216)


            elif alt11 == 112:
                # gleampython/gleam.g:245:9: '\\u0c92' .. '\\u0ca8'
                pass 
                self.matchRange(3218, 3240)


            elif alt11 == 113:
                # gleampython/gleam.g:246:9: '\\u0caa' .. '\\u0cb3'
                pass 
                self.matchRange(3242, 3251)


            elif alt11 == 114:
                # gleampython/gleam.g:247:9: '\\u0cb5' .. '\\u0cb9'
                pass 
                self.matchRange(3253, 3257)


            elif alt11 == 115:
                # gleampython/gleam.g:248:9: '\\u0cbd'
                pass 
                self.match(3261)


            elif alt11 == 116:
                # gleampython/gleam.g:249:9: '\\u0cde'
                pass 
                self.match(3294)


            elif alt11 == 117:
                # gleampython/gleam.g:250:9: '\\u0ce0' .. '\\u0ce1'
                pass 
                self.matchRange(3296, 3297)


            elif alt11 == 118:
                # gleampython/gleam.g:251:9: '\\u0d05' .. '\\u0d0c'
                pass 
                self.matchRange(3333, 3340)


            elif alt11 == 119:
                # gleampython/gleam.g:252:9: '\\u0d0e' .. '\\u0d10'
                pass 
                self.matchRange(3342, 3344)


            elif alt11 == 120:
                # gleampython/gleam.g:253:9: '\\u0d12' .. '\\u0d28'
                pass 
                self.matchRange(3346, 3368)


            elif alt11 == 121:
                # gleampython/gleam.g:254:9: '\\u0d2a' .. '\\u0d39'
                pass 
                self.matchRange(3370, 3385)


            elif alt11 == 122:
                # gleampython/gleam.g:255:9: '\\u0d60' .. '\\u0d61'
                pass 
                self.matchRange(3424, 3425)


            elif alt11 == 123:
                # gleampython/gleam.g:256:9: '\\u0d85' .. '\\u0d96'
                pass 
                self.matchRange(3461, 3478)


            elif alt11 == 124:
                # gleampython/gleam.g:257:9: '\\u0d9a' .. '\\u0db1'
                pass 
                self.matchRange(3482, 3505)


            elif alt11 == 125:
                # gleampython/gleam.g:258:9: '\\u0db3' .. '\\u0dbb'
                pass 
                self.matchRange(3507, 3515)


            elif alt11 == 126:
                # gleampython/gleam.g:259:9: '\\u0dbd'
                pass 
                self.match(3517)


            elif alt11 == 127:
                # gleampython/gleam.g:260:9: '\\u0dc0' .. '\\u0dc6'
                pass 
                self.matchRange(3520, 3526)


            elif alt11 == 128:
                # gleampython/gleam.g:261:9: '\\u0e01' .. '\\u0e30'
                pass 
                self.matchRange(3585, 3632)


            elif alt11 == 129:
                # gleampython/gleam.g:262:9: '\\u0e32' .. '\\u0e33'
                pass 
                self.matchRange(3634, 3635)


            elif alt11 == 130:
                # gleampython/gleam.g:263:9: '\\u0e3f' .. '\\u0e46'
                pass 
                self.matchRange(3647, 3654)


            elif alt11 == 131:
                # gleampython/gleam.g:264:9: '\\u0e81' .. '\\u0e82'
                pass 
                self.matchRange(3713, 3714)


            elif alt11 == 132:
                # gleampython/gleam.g:265:9: '\\u0e84'
                pass 
                self.match(3716)


            elif alt11 == 133:
                # gleampython/gleam.g:266:9: '\\u0e87' .. '\\u0e88'
                pass 
                self.matchRange(3719, 3720)


            elif alt11 == 134:
                # gleampython/gleam.g:267:9: '\\u0e8a'
                pass 
                self.match(3722)


            elif alt11 == 135:
                # gleampython/gleam.g:268:9: '\\u0e8d'
                pass 
                self.match(3725)


            elif alt11 == 136:
                # gleampython/gleam.g:269:9: '\\u0e94' .. '\\u0e97'
                pass 
                self.matchRange(3732, 3735)


            elif alt11 == 137:
                # gleampython/gleam.g:270:9: '\\u0e99' .. '\\u0e9f'
                pass 
                self.matchRange(3737, 3743)


            elif alt11 == 138:
                # gleampython/gleam.g:271:9: '\\u0ea1' .. '\\u0ea3'
                pass 
                self.matchRange(3745, 3747)


            elif alt11 == 139:
                # gleampython/gleam.g:272:9: '\\u0ea5'
                pass 
                self.match(3749)


            elif alt11 == 140:
                # gleampython/gleam.g:273:9: '\\u0ea7'
                pass 
                self.match(3751)


            elif alt11 == 141:
                # gleampython/gleam.g:274:9: '\\u0eaa' .. '\\u0eab'
                pass 
                self.matchRange(3754, 3755)


            elif alt11 == 142:
                # gleampython/gleam.g:275:9: '\\u0ead' .. '\\u0eb0'
                pass 
                self.matchRange(3757, 3760)


            elif alt11 == 143:
                # gleampython/gleam.g:276:9: '\\u0eb2' .. '\\u0eb3'
                pass 
                self.matchRange(3762, 3763)


            elif alt11 == 144:
                # gleampython/gleam.g:277:9: '\\u0ebd'
                pass 
                self.match(3773)


            elif alt11 == 145:
                # gleampython/gleam.g:278:9: '\\u0ec0' .. '\\u0ec4'
                pass 
                self.matchRange(3776, 3780)


            elif alt11 == 146:
                # gleampython/gleam.g:279:9: '\\u0ec6'
                pass 
                self.match(3782)


            elif alt11 == 147:
                # gleampython/gleam.g:280:9: '\\u0edc' .. '\\u0edd'
                pass 
                self.matchRange(3804, 3805)


            elif alt11 == 148:
                # gleampython/gleam.g:281:9: '\\u0f00'
                pass 
                self.match(3840)


            elif alt11 == 149:
                # gleampython/gleam.g:282:9: '\\u0f40' .. '\\u0f47'
                pass 
                self.matchRange(3904, 3911)


            elif alt11 == 150:
                # gleampython/gleam.g:283:9: '\\u0f49' .. '\\u0f6a'
                pass 
                self.matchRange(3913, 3946)


            elif alt11 == 151:
                # gleampython/gleam.g:284:9: '\\u0f88' .. '\\u0f8b'
                pass 
                self.matchRange(3976, 3979)


            elif alt11 == 152:
                # gleampython/gleam.g:285:9: '\\u1000' .. '\\u1021'
                pass 
                self.matchRange(4096, 4129)


            elif alt11 == 153:
                # gleampython/gleam.g:286:9: '\\u1023' .. '\\u1027'
                pass 
                self.matchRange(4131, 4135)


            elif alt11 == 154:
                # gleampython/gleam.g:287:9: '\\u1029' .. '\\u102a'
                pass 
                self.matchRange(4137, 4138)


            elif alt11 == 155:
                # gleampython/gleam.g:288:9: '\\u1050' .. '\\u1055'
                pass 
                self.matchRange(4176, 4181)


            elif alt11 == 156:
                # gleampython/gleam.g:289:9: '\\u10a0' .. '\\u10c5'
                pass 
                self.matchRange(4256, 4293)


            elif alt11 == 157:
                # gleampython/gleam.g:290:9: '\\u10d0' .. '\\u10f8'
                pass 
                self.matchRange(4304, 4344)


            elif alt11 == 158:
                # gleampython/gleam.g:291:9: '\\u1100' .. '\\u1159'
                pass 
                self.matchRange(4352, 4441)


            elif alt11 == 159:
                # gleampython/gleam.g:292:9: '\\u115f' .. '\\u11a2'
                pass 
                self.matchRange(4447, 4514)


            elif alt11 == 160:
                # gleampython/gleam.g:293:9: '\\u11a8' .. '\\u11f9'
                pass 
                self.matchRange(4520, 4601)


            elif alt11 == 161:
                # gleampython/gleam.g:294:9: '\\u1200' .. '\\u1206'
                pass 
                self.matchRange(4608, 4614)


            elif alt11 == 162:
                # gleampython/gleam.g:295:9: '\\u1208' .. '\\u1246'
                pass 
                self.matchRange(4616, 4678)


            elif alt11 == 163:
                # gleampython/gleam.g:296:9: '\\u1248'
                pass 
                self.match(4680)


            elif alt11 == 164:
                # gleampython/gleam.g:297:9: '\\u124a' .. '\\u124d'
                pass 
                self.matchRange(4682, 4685)


            elif alt11 == 165:
                # gleampython/gleam.g:298:9: '\\u1250' .. '\\u1256'
                pass 
                self.matchRange(4688, 4694)


            elif alt11 == 166:
                # gleampython/gleam.g:299:9: '\\u1258'
                pass 
                self.match(4696)


            elif alt11 == 167:
                # gleampython/gleam.g:300:9: '\\u125a' .. '\\u125d'
                pass 
                self.matchRange(4698, 4701)


            elif alt11 == 168:
                # gleampython/gleam.g:301:9: '\\u1260' .. '\\u1286'
                pass 
                self.matchRange(4704, 4742)


            elif alt11 == 169:
                # gleampython/gleam.g:302:9: '\\u1288'
                pass 
                self.match(4744)


            elif alt11 == 170:
                # gleampython/gleam.g:303:9: '\\u128a' .. '\\u128d'
                pass 
                self.matchRange(4746, 4749)


            elif alt11 == 171:
                # gleampython/gleam.g:304:9: '\\u1290' .. '\\u12ae'
                pass 
                self.matchRange(4752, 4782)


            elif alt11 == 172:
                # gleampython/gleam.g:305:9: '\\u12b0'
                pass 
                self.match(4784)


            elif alt11 == 173:
                # gleampython/gleam.g:306:9: '\\u12b2' .. '\\u12b5'
                pass 
                self.matchRange(4786, 4789)


            elif alt11 == 174:
                # gleampython/gleam.g:307:9: '\\u12b8' .. '\\u12be'
                pass 
                self.matchRange(4792, 4798)


            elif alt11 == 175:
                # gleampython/gleam.g:308:9: '\\u12c0'
                pass 
                self.match(4800)


            elif alt11 == 176:
                # gleampython/gleam.g:309:9: '\\u12c2' .. '\\u12c5'
                pass 
                self.matchRange(4802, 4805)


            elif alt11 == 177:
                # gleampython/gleam.g:310:9: '\\u12c8' .. '\\u12ce'
                pass 
                self.matchRange(4808, 4814)


            elif alt11 == 178:
                # gleampython/gleam.g:311:9: '\\u12d0' .. '\\u12d6'
                pass 
                self.matchRange(4816, 4822)


            elif alt11 == 179:
                # gleampython/gleam.g:312:9: '\\u12d8' .. '\\u12ee'
                pass 
                self.matchRange(4824, 4846)


            elif alt11 == 180:
                # gleampython/gleam.g:313:9: '\\u12f0' .. '\\u130e'
                pass 
                self.matchRange(4848, 4878)


            elif alt11 == 181:
                # gleampython/gleam.g:314:9: '\\u1310'
                pass 
                self.match(4880)


            elif alt11 == 182:
                # gleampython/gleam.g:315:9: '\\u1312' .. '\\u1315'
                pass 
                self.matchRange(4882, 4885)


            elif alt11 == 183:
                # gleampython/gleam.g:316:9: '\\u1318' .. '\\u131e'
                pass 
                self.matchRange(4888, 4894)


            elif alt11 == 184:
                # gleampython/gleam.g:317:9: '\\u1320' .. '\\u1346'
                pass 
                self.matchRange(4896, 4934)


            elif alt11 == 185:
                # gleampython/gleam.g:318:9: '\\u1348' .. '\\u135a'
                pass 
                self.matchRange(4936, 4954)


            elif alt11 == 186:
                # gleampython/gleam.g:319:9: '\\u13a0' .. '\\u13f4'
                pass 
                self.matchRange(5024, 5108)


            elif alt11 == 187:
                # gleampython/gleam.g:320:9: '\\u1401' .. '\\u166c'
                pass 
                self.matchRange(5121, 5740)


            elif alt11 == 188:
                # gleampython/gleam.g:321:9: '\\u166f' .. '\\u1676'
                pass 
                self.matchRange(5743, 5750)


            elif alt11 == 189:
                # gleampython/gleam.g:322:9: '\\u1681' .. '\\u169a'
                pass 
                self.matchRange(5761, 5786)


            elif alt11 == 190:
                # gleampython/gleam.g:323:9: '\\u16a0' .. '\\u16ea'
                pass 
                self.matchRange(5792, 5866)


            elif alt11 == 191:
                # gleampython/gleam.g:324:9: '\\u16ee' .. '\\u16f0'
                pass 
                self.matchRange(5870, 5872)


            elif alt11 == 192:
                # gleampython/gleam.g:325:9: '\\u1700' .. '\\u170c'
                pass 
                self.matchRange(5888, 5900)


            elif alt11 == 193:
                # gleampython/gleam.g:326:9: '\\u170e' .. '\\u1711'
                pass 
                self.matchRange(5902, 5905)


            elif alt11 == 194:
                # gleampython/gleam.g:327:9: '\\u1720' .. '\\u1731'
                pass 
                self.matchRange(5920, 5937)


            elif alt11 == 195:
                # gleampython/gleam.g:328:9: '\\u1740' .. '\\u1751'
                pass 
                self.matchRange(5952, 5969)


            elif alt11 == 196:
                # gleampython/gleam.g:329:9: '\\u1760' .. '\\u176c'
                pass 
                self.matchRange(5984, 5996)


            elif alt11 == 197:
                # gleampython/gleam.g:330:9: '\\u176e' .. '\\u1770'
                pass 
                self.matchRange(5998, 6000)


            elif alt11 == 198:
                # gleampython/gleam.g:331:9: '\\u1780' .. '\\u17b3'
                pass 
                self.matchRange(6016, 6067)


            elif alt11 == 199:
                # gleampython/gleam.g:332:9: '\\u17d7'
                pass 
                self.match(6103)


            elif alt11 == 200:
                # gleampython/gleam.g:333:9: '\\u17db' .. '\\u17dc'
                pass 
                self.matchRange(6107, 6108)


            elif alt11 == 201:
                # gleampython/gleam.g:334:9: '\\u1820' .. '\\u1877'
                pass 
                self.matchRange(6176, 6263)


            elif alt11 == 202:
                # gleampython/gleam.g:335:9: '\\u1880' .. '\\u18a8'
                pass 
                self.matchRange(6272, 6312)


            elif alt11 == 203:
                # gleampython/gleam.g:336:9: '\\u1900' .. '\\u191c'
                pass 
                self.matchRange(6400, 6428)


            elif alt11 == 204:
                # gleampython/gleam.g:337:9: '\\u1950' .. '\\u196d'
                pass 
                self.matchRange(6480, 6509)


            elif alt11 == 205:
                # gleampython/gleam.g:338:9: '\\u1970' .. '\\u1974'
                pass 
                self.matchRange(6512, 6516)


            elif alt11 == 206:
                # gleampython/gleam.g:339:9: '\\u1d00' .. '\\u1d6b'
                pass 
                self.matchRange(7424, 7531)


            elif alt11 == 207:
                # gleampython/gleam.g:340:9: '\\u1e00' .. '\\u1e9b'
                pass 
                self.matchRange(7680, 7835)


            elif alt11 == 208:
                # gleampython/gleam.g:341:9: '\\u1ea0' .. '\\u1ef9'
                pass 
                self.matchRange(7840, 7929)


            elif alt11 == 209:
                # gleampython/gleam.g:342:9: '\\u1f00' .. '\\u1f15'
                pass 
                self.matchRange(7936, 7957)


            elif alt11 == 210:
                # gleampython/gleam.g:343:9: '\\u1f18' .. '\\u1f1d'
                pass 
                self.matchRange(7960, 7965)


            elif alt11 == 211:
                # gleampython/gleam.g:344:9: '\\u1f20' .. '\\u1f45'
                pass 
                self.matchRange(7968, 8005)


            elif alt11 == 212:
                # gleampython/gleam.g:345:9: '\\u1f48' .. '\\u1f4d'
                pass 
                self.matchRange(8008, 8013)


            elif alt11 == 213:
                # gleampython/gleam.g:346:9: '\\u1f50' .. '\\u1f57'
                pass 
                self.matchRange(8016, 8023)


            elif alt11 == 214:
                # gleampython/gleam.g:347:9: '\\u1f59'
                pass 
                self.match(8025)


            elif alt11 == 215:
                # gleampython/gleam.g:348:9: '\\u1f5b'
                pass 
                self.match(8027)


            elif alt11 == 216:
                # gleampython/gleam.g:349:9: '\\u1f5d'
                pass 
                self.match(8029)


            elif alt11 == 217:
                # gleampython/gleam.g:350:9: '\\u1f5f' .. '\\u1f7d'
                pass 
                self.matchRange(8031, 8061)


            elif alt11 == 218:
                # gleampython/gleam.g:351:9: '\\u1f80' .. '\\u1fb4'
                pass 
                self.matchRange(8064, 8116)


            elif alt11 == 219:
                # gleampython/gleam.g:352:9: '\\u1fb6' .. '\\u1fbc'
                pass 
                self.matchRange(8118, 8124)


            elif alt11 == 220:
                # gleampython/gleam.g:353:9: '\\u1fbe'
                pass 
                self.match(8126)


            elif alt11 == 221:
                # gleampython/gleam.g:354:9: '\\u1fc2' .. '\\u1fc4'
                pass 
                self.matchRange(8130, 8132)


            elif alt11 == 222:
                # gleampython/gleam.g:355:9: '\\u1fc6' .. '\\u1fcc'
                pass 
                self.matchRange(8134, 8140)


            elif alt11 == 223:
                # gleampython/gleam.g:356:9: '\\u1fd0' .. '\\u1fd3'
                pass 
                self.matchRange(8144, 8147)


            elif alt11 == 224:
                # gleampython/gleam.g:357:9: '\\u1fd6' .. '\\u1fdb'
                pass 
                self.matchRange(8150, 8155)


            elif alt11 == 225:
                # gleampython/gleam.g:358:9: '\\u1fe0' .. '\\u1fec'
                pass 
                self.matchRange(8160, 8172)


            elif alt11 == 226:
                # gleampython/gleam.g:359:9: '\\u1ff2' .. '\\u1ff4'
                pass 
                self.matchRange(8178, 8180)


            elif alt11 == 227:
                # gleampython/gleam.g:360:9: '\\u1ff6' .. '\\u1ffc'
                pass 
                self.matchRange(8182, 8188)


            elif alt11 == 228:
                # gleampython/gleam.g:361:9: '\\u203f' .. '\\u2040'
                pass 
                self.matchRange(8255, 8256)


            elif alt11 == 229:
                # gleampython/gleam.g:362:9: '\\u2054'
                pass 
                self.match(8276)


            elif alt11 == 230:
                # gleampython/gleam.g:363:9: '\\u2071'
                pass 
                self.match(8305)


            elif alt11 == 231:
                # gleampython/gleam.g:364:9: '\\u207f'
                pass 
                self.match(8319)


            elif alt11 == 232:
                # gleampython/gleam.g:365:9: '\\u20a0' .. '\\u20b1'
                pass 
                self.matchRange(8352, 8369)


            elif alt11 == 233:
                # gleampython/gleam.g:366:9: '\\u2102'
                pass 
                self.match(8450)


            elif alt11 == 234:
                # gleampython/gleam.g:367:9: '\\u2107'
                pass 
                self.match(8455)


            elif alt11 == 235:
                # gleampython/gleam.g:368:9: '\\u210a' .. '\\u2113'
                pass 
                self.matchRange(8458, 8467)


            elif alt11 == 236:
                # gleampython/gleam.g:369:9: '\\u2115'
                pass 
                self.match(8469)


            elif alt11 == 237:
                # gleampython/gleam.g:370:9: '\\u2119' .. '\\u211d'
                pass 
                self.matchRange(8473, 8477)


            elif alt11 == 238:
                # gleampython/gleam.g:371:9: '\\u2124'
                pass 
                self.match(8484)


            elif alt11 == 239:
                # gleampython/gleam.g:372:9: '\\u2126'
                pass 
                self.match(8486)


            elif alt11 == 240:
                # gleampython/gleam.g:373:9: '\\u2128'
                pass 
                self.match(8488)


            elif alt11 == 241:
                # gleampython/gleam.g:374:9: '\\u212a' .. '\\u212d'
                pass 
                self.matchRange(8490, 8493)


            elif alt11 == 242:
                # gleampython/gleam.g:375:9: '\\u212f' .. '\\u2131'
                pass 
                self.matchRange(8495, 8497)


            elif alt11 == 243:
                # gleampython/gleam.g:376:9: '\\u2133' .. '\\u2139'
                pass 
                self.matchRange(8499, 8505)


            elif alt11 == 244:
                # gleampython/gleam.g:377:9: '\\u213d' .. '\\u213f'
                pass 
                self.matchRange(8509, 8511)


            elif alt11 == 245:
                # gleampython/gleam.g:378:9: '\\u2145' .. '\\u2149'
                pass 
                self.matchRange(8517, 8521)


            elif alt11 == 246:
                # gleampython/gleam.g:379:9: '\\u2160' .. '\\u2183'
                pass 
                self.matchRange(8544, 8579)


            elif alt11 == 247:
                # gleampython/gleam.g:380:9: '\\u3005' .. '\\u3007'
                pass 
                self.matchRange(12293, 12295)


            elif alt11 == 248:
                # gleampython/gleam.g:381:9: '\\u3021' .. '\\u3029'
                pass 
                self.matchRange(12321, 12329)


            elif alt11 == 249:
                # gleampython/gleam.g:382:9: '\\u3031' .. '\\u3035'
                pass 
                self.matchRange(12337, 12341)


            elif alt11 == 250:
                # gleampython/gleam.g:383:9: '\\u3038' .. '\\u303c'
                pass 
                self.matchRange(12344, 12348)


            elif alt11 == 251:
                # gleampython/gleam.g:384:9: '\\u3041' .. '\\u3096'
                pass 
                self.matchRange(12353, 12438)


            elif alt11 == 252:
                # gleampython/gleam.g:385:9: '\\u309d' .. '\\u309f'
                pass 
                self.matchRange(12445, 12447)


            elif alt11 == 253:
                # gleampython/gleam.g:386:9: '\\u30a1' .. '\\u30ff'
                pass 
                self.matchRange(12449, 12543)


            elif alt11 == 254:
                # gleampython/gleam.g:387:9: '\\u3105' .. '\\u312c'
                pass 
                self.matchRange(12549, 12588)


            elif alt11 == 255:
                # gleampython/gleam.g:388:9: '\\u3131' .. '\\u318e'
                pass 
                self.matchRange(12593, 12686)


            elif alt11 == 256:
                # gleampython/gleam.g:389:9: '\\u31a0' .. '\\u31b7'
                pass 
                self.matchRange(12704, 12727)


            elif alt11 == 257:
                # gleampython/gleam.g:390:9: '\\u31f0' .. '\\u31ff'
                pass 
                self.matchRange(12784, 12799)


            elif alt11 == 258:
                # gleampython/gleam.g:391:9: '\\u3400' .. '\\u4db5'
                pass 
                self.matchRange(13312, 19893)


            elif alt11 == 259:
                # gleampython/gleam.g:392:9: '\\u4e00' .. '\\u9fa5'
                pass 
                self.matchRange(19968, 40869)


            elif alt11 == 260:
                # gleampython/gleam.g:393:9: '\\ua000' .. '\\ua48c'
                pass 
                self.matchRange(40960, 42124)


            elif alt11 == 261:
                # gleampython/gleam.g:394:9: '\\uac00' .. '\\ud7a3'
                pass 
                self.matchRange(44032, 55203)


            elif alt11 == 262:
                # gleampython/gleam.g:395:9: '\\uf900' .. '\\ufa2d'
                pass 
                self.matchRange(63744, 64045)


            elif alt11 == 263:
                # gleampython/gleam.g:396:9: '\\ufa30' .. '\\ufa6a'
                pass 
                self.matchRange(64048, 64106)


            elif alt11 == 264:
                # gleampython/gleam.g:397:9: '\\ufb00' .. '\\ufb06'
                pass 
                self.matchRange(64256, 64262)


            elif alt11 == 265:
                # gleampython/gleam.g:398:9: '\\ufb13' .. '\\ufb17'
                pass 
                self.matchRange(64275, 64279)


            elif alt11 == 266:
                # gleampython/gleam.g:399:9: '\\ufb1d'
                pass 
                self.match(64285)


            elif alt11 == 267:
                # gleampython/gleam.g:400:9: '\\ufb1f' .. '\\ufb28'
                pass 
                self.matchRange(64287, 64296)


            elif alt11 == 268:
                # gleampython/gleam.g:401:9: '\\ufb2a' .. '\\ufb36'
                pass 
                self.matchRange(64298, 64310)


            elif alt11 == 269:
                # gleampython/gleam.g:402:9: '\\ufb38' .. '\\ufb3c'
                pass 
                self.matchRange(64312, 64316)


            elif alt11 == 270:
                # gleampython/gleam.g:403:9: '\\ufb3e'
                pass 
                self.match(64318)


            elif alt11 == 271:
                # gleampython/gleam.g:404:9: '\\ufb40' .. '\\ufb41'
                pass 
                self.matchRange(64320, 64321)


            elif alt11 == 272:
                # gleampython/gleam.g:405:9: '\\ufb43' .. '\\ufb44'
                pass 
                self.matchRange(64323, 64324)


            elif alt11 == 273:
                # gleampython/gleam.g:406:9: '\\ufb46' .. '\\ufbb1'
                pass 
                self.matchRange(64326, 64433)


            elif alt11 == 274:
                # gleampython/gleam.g:407:9: '\\ufbd3' .. '\\ufd3d'
                pass 
                self.matchRange(64467, 64829)


            elif alt11 == 275:
                # gleampython/gleam.g:408:9: '\\ufd50' .. '\\ufd8f'
                pass 
                self.matchRange(64848, 64911)


            elif alt11 == 276:
                # gleampython/gleam.g:409:9: '\\ufd92' .. '\\ufdc7'
                pass 
                self.matchRange(64914, 64967)


            elif alt11 == 277:
                # gleampython/gleam.g:410:9: '\\ufdf0' .. '\\ufdfc'
                pass 
                self.matchRange(65008, 65020)


            elif alt11 == 278:
                # gleampython/gleam.g:411:9: '\\ufe33' .. '\\ufe34'
                pass 
                self.matchRange(65075, 65076)


            elif alt11 == 279:
                # gleampython/gleam.g:412:9: '\\ufe4d' .. '\\ufe4f'
                pass 
                self.matchRange(65101, 65103)


            elif alt11 == 280:
                # gleampython/gleam.g:413:9: '\\ufe69'
                pass 
                self.match(65129)


            elif alt11 == 281:
                # gleampython/gleam.g:414:9: '\\ufe70' .. '\\ufe74'
                pass 
                self.matchRange(65136, 65140)


            elif alt11 == 282:
                # gleampython/gleam.g:415:9: '\\ufe76' .. '\\ufefc'
                pass 
                self.matchRange(65142, 65276)


            elif alt11 == 283:
                # gleampython/gleam.g:416:9: '\\uff04'
                pass 
                self.match(65284)


            elif alt11 == 284:
                # gleampython/gleam.g:417:9: '\\uff21' .. '\\uff3a'
                pass 
                self.matchRange(65313, 65338)


            elif alt11 == 285:
                # gleampython/gleam.g:418:9: '\\uff3f'
                pass 
                self.match(65343)


            elif alt11 == 286:
                # gleampython/gleam.g:419:9: '\\uff41' .. '\\uff5a'
                pass 
                self.matchRange(65345, 65370)


            elif alt11 == 287:
                # gleampython/gleam.g:420:9: '\\uff65' .. '\\uffbe'
                pass 
                self.matchRange(65381, 65470)


            elif alt11 == 288:
                # gleampython/gleam.g:421:9: '\\uffc2' .. '\\uffc7'
                pass 
                self.matchRange(65474, 65479)


            elif alt11 == 289:
                # gleampython/gleam.g:422:9: '\\uffca' .. '\\uffcf'
                pass 
                self.matchRange(65482, 65487)


            elif alt11 == 290:
                # gleampython/gleam.g:423:9: '\\uffd2' .. '\\uffd7'
                pass 
                self.matchRange(65490, 65495)


            elif alt11 == 291:
                # gleampython/gleam.g:424:9: '\\uffda' .. '\\uffdc'
                pass 
                self.matchRange(65498, 65500)


            elif alt11 == 292:
                # gleampython/gleam.g:425:9: '\\uffe0' .. '\\uffe1'
                pass 
                self.matchRange(65504, 65505)


            elif alt11 == 293:
                # gleampython/gleam.g:426:9: '\\uffe5' .. '\\uffe6'
                pass 
                self.matchRange(65509, 65510)


            elif alt11 == 294:
                # gleampython/gleam.g:427:9: ( '\\ud800' .. '\\udbff' ) ( '\\udc00' .. '\\udfff' )
                pass 
                # gleampython/gleam.g:427:9: ( '\\ud800' .. '\\udbff' )
                # gleampython/gleam.g:427:10: '\\ud800' .. '\\udbff'
                pass 
                self.matchRange(55296, 56319)



                # gleampython/gleam.g:427:30: ( '\\udc00' .. '\\udfff' )
                # gleampython/gleam.g:427:31: '\\udc00' .. '\\udfff'
                pass 
                self.matchRange(56320, 57343)






        finally:

            pass

    # $ANTLR end "IdentifierStart"



    # $ANTLR start "IdentifierPart"
    def mIdentifierPart(self, ):

        try:
            # gleampython/gleam.g:432:5: ( '\\u0000' .. '\\u0008' | '\\u000e' .. '\\u001b' | '\\u0024' | '\\u0030' .. '\\u0039' | '\\u0041' .. '\\u005a' | '\\u005f' | '\\u0061' .. '\\u007a' | '\\u007f' .. '\\u009f' | '\\u00a2' .. '\\u00a5' | '\\u00aa' | '\\u00ad' | '\\u00b5' | '\\u00ba' | '\\u00c0' .. '\\u00d6' | '\\u00d8' .. '\\u00f6' | '\\u00f8' .. '\\u0236' | '\\u0250' .. '\\u02c1' | '\\u02c6' .. '\\u02d1' | '\\u02e0' .. '\\u02e4' | '\\u02ee' | '\\u0300' .. '\\u0357' | '\\u035d' .. '\\u036f' | '\\u037a' | '\\u0386' | '\\u0388' .. '\\u038a' | '\\u038c' | '\\u038e' .. '\\u03a1' | '\\u03a3' .. '\\u03ce' | '\\u03d0' .. '\\u03f5' | '\\u03f7' .. '\\u03fb' | '\\u0400' .. '\\u0481' | '\\u0483' .. '\\u0486' | '\\u048a' .. '\\u04ce' | '\\u04d0' .. '\\u04f5' | '\\u04f8' .. '\\u04f9' | '\\u0500' .. '\\u050f' | '\\u0531' .. '\\u0556' | '\\u0559' | '\\u0561' .. '\\u0587' | '\\u0591' .. '\\u05a1' | '\\u05a3' .. '\\u05b9' | '\\u05bb' .. '\\u05bd' | '\\u05bf' | '\\u05c1' .. '\\u05c2' | '\\u05c4' | '\\u05d0' .. '\\u05ea' | '\\u05f0' .. '\\u05f2' | '\\u0600' .. '\\u0603' | '\\u0610' .. '\\u0615' | '\\u0621' .. '\\u063a' | '\\u0640' .. '\\u0658' | '\\u0660' .. '\\u0669' | '\\u066e' .. '\\u06d3' | '\\u06d5' .. '\\u06dd' | '\\u06df' .. '\\u06e8' | '\\u06ea' .. '\\u06fc' | '\\u06ff' | '\\u070f' .. '\\u074a' | '\\u074d' .. '\\u074f' | '\\u0780' .. '\\u07b1' | '\\u0901' .. '\\u0939' | '\\u093c' .. '\\u094d' | '\\u0950' .. '\\u0954' | '\\u0958' .. '\\u0963' | '\\u0966' .. '\\u096f' | '\\u0981' .. '\\u0983' | '\\u0985' .. '\\u098c' | '\\u098f' .. '\\u0990' | '\\u0993' .. '\\u09a8' | '\\u09aa' .. '\\u09b0' | '\\u09b2' | '\\u09b6' .. '\\u09b9' | '\\u09bc' .. '\\u09c4' | '\\u09c7' .. '\\u09c8' | '\\u09cb' .. '\\u09cd' | '\\u09d7' | '\\u09dc' .. '\\u09dd' | '\\u09df' .. '\\u09e3' | '\\u09e6' .. '\\u09f3' | '\\u0a01' .. '\\u0a03' | '\\u0a05' .. '\\u0a0a' | '\\u0a0f' .. '\\u0a10' | '\\u0a13' .. '\\u0a28' | '\\u0a2a' .. '\\u0a30' | '\\u0a32' .. '\\u0a33' | '\\u0a35' .. '\\u0a36' | '\\u0a38' .. '\\u0a39' | '\\u0a3c' | '\\u0a3e' .. '\\u0a42' | '\\u0a47' .. '\\u0a48' | '\\u0a4b' .. '\\u0a4d' | '\\u0a59' .. '\\u0a5c' | '\\u0a5e' | '\\u0a66' .. '\\u0a74' | '\\u0a81' .. '\\u0a83' | '\\u0a85' .. '\\u0a8d' | '\\u0a8f' .. '\\u0a91' | '\\u0a93' .. '\\u0aa8' | '\\u0aaa' .. '\\u0ab0' | '\\u0ab2' .. '\\u0ab3' | '\\u0ab5' .. '\\u0ab9' | '\\u0abc' .. '\\u0ac5' | '\\u0ac7' .. '\\u0ac9' | '\\u0acb' .. '\\u0acd' | '\\u0ad0' | '\\u0ae0' .. '\\u0ae3' | '\\u0ae6' .. '\\u0aef' | '\\u0af1' | '\\u0b01' .. '\\u0b03' | '\\u0b05' .. '\\u0b0c' | '\\u0b0f' .. '\\u0b10' | '\\u0b13' .. '\\u0b28' | '\\u0b2a' .. '\\u0b30' | '\\u0b32' .. '\\u0b33' | '\\u0b35' .. '\\u0b39' | '\\u0b3c' .. '\\u0b43' | '\\u0b47' .. '\\u0b48' | '\\u0b4b' .. '\\u0b4d' | '\\u0b56' .. '\\u0b57' | '\\u0b5c' .. '\\u0b5d' | '\\u0b5f' .. '\\u0b61' | '\\u0b66' .. '\\u0b6f' | '\\u0b71' | '\\u0b82' .. '\\u0b83' | '\\u0b85' .. '\\u0b8a' | '\\u0b8e' .. '\\u0b90' | '\\u0b92' .. '\\u0b95' | '\\u0b99' .. '\\u0b9a' | '\\u0b9c' | '\\u0b9e' .. '\\u0b9f' | '\\u0ba3' .. '\\u0ba4' | '\\u0ba8' .. '\\u0baa' | '\\u0bae' .. '\\u0bb5' | '\\u0bb7' .. '\\u0bb9' | '\\u0bbe' .. '\\u0bc2' | '\\u0bc6' .. '\\u0bc8' | '\\u0bca' .. '\\u0bcd' | '\\u0bd7' | '\\u0be7' .. '\\u0bef' | '\\u0bf9' | '\\u0c01' .. '\\u0c03' | '\\u0c05' .. '\\u0c0c' | '\\u0c0e' .. '\\u0c10' | '\\u0c12' .. '\\u0c28' | '\\u0c2a' .. '\\u0c33' | '\\u0c35' .. '\\u0c39' | '\\u0c3e' .. '\\u0c44' | '\\u0c46' .. '\\u0c48' | '\\u0c4a' .. '\\u0c4d' | '\\u0c55' .. '\\u0c56' | '\\u0c60' .. '\\u0c61' | '\\u0c66' .. '\\u0c6f' | '\\u0c82' .. '\\u0c83' | '\\u0c85' .. '\\u0c8c' | '\\u0c8e' .. '\\u0c90' | '\\u0c92' .. '\\u0ca8' | '\\u0caa' .. '\\u0cb3' | '\\u0cb5' .. '\\u0cb9' | '\\u0cbc' .. '\\u0cc4' | '\\u0cc6' .. '\\u0cc8' | '\\u0cca' .. '\\u0ccd' | '\\u0cd5' .. '\\u0cd6' | '\\u0cde' | '\\u0ce0' .. '\\u0ce1' | '\\u0ce6' .. '\\u0cef' | '\\u0d02' .. '\\u0d03' | '\\u0d05' .. '\\u0d0c' | '\\u0d0e' .. '\\u0d10' | '\\u0d12' .. '\\u0d28' | '\\u0d2a' .. '\\u0d39' | '\\u0d3e' .. '\\u0d43' | '\\u0d46' .. '\\u0d48' | '\\u0d4a' .. '\\u0d4d' | '\\u0d57' | '\\u0d60' .. '\\u0d61' | '\\u0d66' .. '\\u0d6f' | '\\u0d82' .. '\\u0d83' | '\\u0d85' .. '\\u0d96' | '\\u0d9a' .. '\\u0db1' | '\\u0db3' .. '\\u0dbb' | '\\u0dbd' | '\\u0dc0' .. '\\u0dc6' | '\\u0dca' | '\\u0dcf' .. '\\u0dd4' | '\\u0dd6' | '\\u0dd8' .. '\\u0ddf' | '\\u0df2' .. '\\u0df3' | '\\u0e01' .. '\\u0e3a' | '\\u0e3f' .. '\\u0e4e' | '\\u0e50' .. '\\u0e59' | '\\u0e81' .. '\\u0e82' | '\\u0e84' | '\\u0e87' .. '\\u0e88' | '\\u0e8a' | '\\u0e8d' | '\\u0e94' .. '\\u0e97' | '\\u0e99' .. '\\u0e9f' | '\\u0ea1' .. '\\u0ea3' | '\\u0ea5' | '\\u0ea7' | '\\u0eaa' .. '\\u0eab' | '\\u0ead' .. '\\u0eb9' | '\\u0ebb' .. '\\u0ebd' | '\\u0ec0' .. '\\u0ec4' | '\\u0ec6' | '\\u0ec8' .. '\\u0ecd' | '\\u0ed0' .. '\\u0ed9' | '\\u0edc' .. '\\u0edd' | '\\u0f00' | '\\u0f18' .. '\\u0f19' | '\\u0f20' .. '\\u0f29' | '\\u0f35' | '\\u0f37' | '\\u0f39' | '\\u0f3e' .. '\\u0f47' | '\\u0f49' .. '\\u0f6a' | '\\u0f71' .. '\\u0f84' | '\\u0f86' .. '\\u0f8b' | '\\u0f90' .. '\\u0f97' | '\\u0f99' .. '\\u0fbc' | '\\u0fc6' | '\\u1000' .. '\\u1021' | '\\u1023' .. '\\u1027' | '\\u1029' .. '\\u102a' | '\\u102c' .. '\\u1032' | '\\u1036' .. '\\u1039' | '\\u1040' .. '\\u1049' | '\\u1050' .. '\\u1059' | '\\u10a0' .. '\\u10c5' | '\\u10d0' .. '\\u10f8' | '\\u1100' .. '\\u1159' | '\\u115f' .. '\\u11a2' | '\\u11a8' .. '\\u11f9' | '\\u1200' .. '\\u1206' | '\\u1208' .. '\\u1246' | '\\u1248' | '\\u124a' .. '\\u124d' | '\\u1250' .. '\\u1256' | '\\u1258' | '\\u125a' .. '\\u125d' | '\\u1260' .. '\\u1286' | '\\u1288' | '\\u128a' .. '\\u128d' | '\\u1290' .. '\\u12ae' | '\\u12b0' | '\\u12b2' .. '\\u12b5' | '\\u12b8' .. '\\u12be' | '\\u12c0' | '\\u12c2' .. '\\u12c5' | '\\u12c8' .. '\\u12ce' | '\\u12d0' .. '\\u12d6' | '\\u12d8' .. '\\u12ee' | '\\u12f0' .. '\\u130e' | '\\u1310' | '\\u1312' .. '\\u1315' | '\\u1318' .. '\\u131e' | '\\u1320' .. '\\u1346' | '\\u1348' .. '\\u135a' | '\\u1369' .. '\\u1371' | '\\u13a0' .. '\\u13f4' | '\\u1401' .. '\\u166c' | '\\u166f' .. '\\u1676' | '\\u1681' .. '\\u169a' | '\\u16a0' .. '\\u16ea' | '\\u16ee' .. '\\u16f0' | '\\u1700' .. '\\u170c' | '\\u170e' .. '\\u1714' | '\\u1720' .. '\\u1734' | '\\u1740' .. '\\u1753' | '\\u1760' .. '\\u176c' | '\\u176e' .. '\\u1770' | '\\u1772' .. '\\u1773' | '\\u1780' .. '\\u17d3' | '\\u17d7' | '\\u17db' .. '\\u17dd' | '\\u17e0' .. '\\u17e9' | '\\u180b' .. '\\u180d' | '\\u1810' .. '\\u1819' | '\\u1820' .. '\\u1877' | '\\u1880' .. '\\u18a9' | '\\u1900' .. '\\u191c' | '\\u1920' .. '\\u192b' | '\\u1930' .. '\\u193b' | '\\u1946' .. '\\u196d' | '\\u1970' .. '\\u1974' | '\\u1d00' .. '\\u1d6b' | '\\u1e00' .. '\\u1e9b' | '\\u1ea0' .. '\\u1ef9' | '\\u1f00' .. '\\u1f15' | '\\u1f18' .. '\\u1f1d' | '\\u1f20' .. '\\u1f45' | '\\u1f48' .. '\\u1f4d' | '\\u1f50' .. '\\u1f57' | '\\u1f59' | '\\u1f5b' | '\\u1f5d' | '\\u1f5f' .. '\\u1f7d' | '\\u1f80' .. '\\u1fb4' | '\\u1fb6' .. '\\u1fbc' | '\\u1fbe' | '\\u1fc2' .. '\\u1fc4' | '\\u1fc6' .. '\\u1fcc' | '\\u1fd0' .. '\\u1fd3' | '\\u1fd6' .. '\\u1fdb' | '\\u1fe0' .. '\\u1fec' | '\\u1ff2' .. '\\u1ff4' | '\\u1ff6' .. '\\u1ffc' | '\\u200c' .. '\\u200f' | '\\u202a' .. '\\u202e' | '\\u203f' .. '\\u2040' | '\\u2054' | '\\u2060' .. '\\u2063' | '\\u206a' .. '\\u206f' | '\\u2071' | '\\u207f' | '\\u20a0' .. '\\u20b1' | '\\u20d0' .. '\\u20dc' | '\\u20e1' | '\\u20e5' .. '\\u20ea' | '\\u2102' | '\\u2107' | '\\u210a' .. '\\u2113' | '\\u2115' | '\\u2119' .. '\\u211d' | '\\u2124' | '\\u2126' | '\\u2128' | '\\u212a' .. '\\u212d' | '\\u212f' .. '\\u2131' | '\\u2133' .. '\\u2139' | '\\u213d' .. '\\u213f' | '\\u2145' .. '\\u2149' | '\\u2160' .. '\\u2183' | '\\u3005' .. '\\u3007' | '\\u3021' .. '\\u302f' | '\\u3031' .. '\\u3035' | '\\u3038' .. '\\u303c' | '\\u3041' .. '\\u3096' | '\\u3099' .. '\\u309a' | '\\u309d' .. '\\u309f' | '\\u30a1' .. '\\u30ff' | '\\u3105' .. '\\u312c' | '\\u3131' .. '\\u318e' | '\\u31a0' .. '\\u31b7' | '\\u31f0' .. '\\u31ff' | '\\u3400' .. '\\u4db5' | '\\u4e00' .. '\\u9fa5' | '\\ua000' .. '\\ua48c' | '\\uac00' .. '\\ud7a3' | '\\uf900' .. '\\ufa2d' | '\\ufa30' .. '\\ufa6a' | '\\ufb00' .. '\\ufb06' | '\\ufb13' .. '\\ufb17' | '\\ufb1d' .. '\\ufb28' | '\\ufb2a' .. '\\ufb36' | '\\ufb38' .. '\\ufb3c' | '\\ufb3e' | '\\ufb40' .. '\\ufb41' | '\\ufb43' .. '\\ufb44' | '\\ufb46' .. '\\ufbb1' | '\\ufbd3' .. '\\ufd3d' | '\\ufd50' .. '\\ufd8f' | '\\ufd92' .. '\\ufdc7' | '\\ufdf0' .. '\\ufdfc' | '\\ufe00' .. '\\ufe0f' | '\\ufe20' .. '\\ufe23' | '\\ufe33' .. '\\ufe34' | '\\ufe4d' .. '\\ufe4f' | '\\ufe69' | '\\ufe70' .. '\\ufe74' | '\\ufe76' .. '\\ufefc' | '\\ufeff' | '\\uff04' | '\\uff10' .. '\\uff19' | '\\uff21' .. '\\uff3a' | '\\uff3f' | '\\uff41' .. '\\uff5a' | '\\uff65' .. '\\uffbe' | '\\uffc2' .. '\\uffc7' | '\\uffca' .. '\\uffcf' | '\\uffd2' .. '\\uffd7' | '\\uffda' .. '\\uffdc' | '\\uffe0' .. '\\uffe1' | '\\uffe5' .. '\\uffe6' | '\\ufff9' .. '\\ufffb' | ( '\\ud800' .. '\\udbff' ) ( '\\udc00' .. '\\udfff' ) )
            alt12 = 386
            LA12_0 = self.input.LA(1)

            if ((0 <= LA12_0 <= 8)) :
                alt12 = 1
            elif ((14 <= LA12_0 <= 27)) :
                alt12 = 2
            elif (LA12_0 == 36) :
                alt12 = 3
            elif ((48 <= LA12_0 <= 57)) :
                alt12 = 4
            elif ((65 <= LA12_0 <= 90)) :
                alt12 = 5
            elif (LA12_0 == 95) :
                alt12 = 6
            elif ((97 <= LA12_0 <= 122)) :
                alt12 = 7
            elif ((127 <= LA12_0 <= 159)) :
                alt12 = 8
            elif ((162 <= LA12_0 <= 165)) :
                alt12 = 9
            elif (LA12_0 == 170) :
                alt12 = 10
            elif (LA12_0 == 173) :
                alt12 = 11
            elif (LA12_0 == 181) :
                alt12 = 12
            elif (LA12_0 == 186) :
                alt12 = 13
            elif ((192 <= LA12_0 <= 214)) :
                alt12 = 14
            elif ((216 <= LA12_0 <= 246)) :
                alt12 = 15
            elif ((248 <= LA12_0 <= 566)) :
                alt12 = 16
            elif ((592 <= LA12_0 <= 705)) :
                alt12 = 17
            elif ((710 <= LA12_0 <= 721)) :
                alt12 = 18
            elif ((736 <= LA12_0 <= 740)) :
                alt12 = 19
            elif (LA12_0 == 750) :
                alt12 = 20
            elif ((768 <= LA12_0 <= 855)) :
                alt12 = 21
            elif ((861 <= LA12_0 <= 879)) :
                alt12 = 22
            elif (LA12_0 == 890) :
                alt12 = 23
            elif (LA12_0 == 902) :
                alt12 = 24
            elif ((904 <= LA12_0 <= 906)) :
                alt12 = 25
            elif (LA12_0 == 908) :
                alt12 = 26
            elif ((910 <= LA12_0 <= 929)) :
                alt12 = 27
            elif ((931 <= LA12_0 <= 974)) :
                alt12 = 28
            elif ((976 <= LA12_0 <= 1013)) :
                alt12 = 29
            elif ((1015 <= LA12_0 <= 1019)) :
                alt12 = 30
            elif ((1024 <= LA12_0 <= 1153)) :
                alt12 = 31
            elif ((1155 <= LA12_0 <= 1158)) :
                alt12 = 32
            elif ((1162 <= LA12_0 <= 1230)) :
                alt12 = 33
            elif ((1232 <= LA12_0 <= 1269)) :
                alt12 = 34
            elif ((1272 <= LA12_0 <= 1273)) :
                alt12 = 35
            elif ((1280 <= LA12_0 <= 1295)) :
                alt12 = 36
            elif ((1329 <= LA12_0 <= 1366)) :
                alt12 = 37
            elif (LA12_0 == 1369) :
                alt12 = 38
            elif ((1377 <= LA12_0 <= 1415)) :
                alt12 = 39
            elif ((1425 <= LA12_0 <= 1441)) :
                alt12 = 40
            elif ((1443 <= LA12_0 <= 1465)) :
                alt12 = 41
            elif ((1467 <= LA12_0 <= 1469)) :
                alt12 = 42
            elif (LA12_0 == 1471) :
                alt12 = 43
            elif ((1473 <= LA12_0 <= 1474)) :
                alt12 = 44
            elif (LA12_0 == 1476) :
                alt12 = 45
            elif ((1488 <= LA12_0 <= 1514)) :
                alt12 = 46
            elif ((1520 <= LA12_0 <= 1522)) :
                alt12 = 47
            elif ((1536 <= LA12_0 <= 1539)) :
                alt12 = 48
            elif ((1552 <= LA12_0 <= 1557)) :
                alt12 = 49
            elif ((1569 <= LA12_0 <= 1594)) :
                alt12 = 50
            elif ((1600 <= LA12_0 <= 1624)) :
                alt12 = 51
            elif ((1632 <= LA12_0 <= 1641)) :
                alt12 = 52
            elif ((1646 <= LA12_0 <= 1747)) :
                alt12 = 53
            elif ((1749 <= LA12_0 <= 1757)) :
                alt12 = 54
            elif ((1759 <= LA12_0 <= 1768)) :
                alt12 = 55
            elif ((1770 <= LA12_0 <= 1788)) :
                alt12 = 56
            elif (LA12_0 == 1791) :
                alt12 = 57
            elif ((1807 <= LA12_0 <= 1866)) :
                alt12 = 58
            elif ((1869 <= LA12_0 <= 1871)) :
                alt12 = 59
            elif ((1920 <= LA12_0 <= 1969)) :
                alt12 = 60
            elif ((2305 <= LA12_0 <= 2361)) :
                alt12 = 61
            elif ((2364 <= LA12_0 <= 2381)) :
                alt12 = 62
            elif ((2384 <= LA12_0 <= 2388)) :
                alt12 = 63
            elif ((2392 <= LA12_0 <= 2403)) :
                alt12 = 64
            elif ((2406 <= LA12_0 <= 2415)) :
                alt12 = 65
            elif ((2433 <= LA12_0 <= 2435)) :
                alt12 = 66
            elif ((2437 <= LA12_0 <= 2444)) :
                alt12 = 67
            elif ((2447 <= LA12_0 <= 2448)) :
                alt12 = 68
            elif ((2451 <= LA12_0 <= 2472)) :
                alt12 = 69
            elif ((2474 <= LA12_0 <= 2480)) :
                alt12 = 70
            elif (LA12_0 == 2482) :
                alt12 = 71
            elif ((2486 <= LA12_0 <= 2489)) :
                alt12 = 72
            elif ((2492 <= LA12_0 <= 2500)) :
                alt12 = 73
            elif ((2503 <= LA12_0 <= 2504)) :
                alt12 = 74
            elif ((2507 <= LA12_0 <= 2509)) :
                alt12 = 75
            elif (LA12_0 == 2519) :
                alt12 = 76
            elif ((2524 <= LA12_0 <= 2525)) :
                alt12 = 77
            elif ((2527 <= LA12_0 <= 2531)) :
                alt12 = 78
            elif ((2534 <= LA12_0 <= 2547)) :
                alt12 = 79
            elif ((2561 <= LA12_0 <= 2563)) :
                alt12 = 80
            elif ((2565 <= LA12_0 <= 2570)) :
                alt12 = 81
            elif ((2575 <= LA12_0 <= 2576)) :
                alt12 = 82
            elif ((2579 <= LA12_0 <= 2600)) :
                alt12 = 83
            elif ((2602 <= LA12_0 <= 2608)) :
                alt12 = 84
            elif ((2610 <= LA12_0 <= 2611)) :
                alt12 = 85
            elif ((2613 <= LA12_0 <= 2614)) :
                alt12 = 86
            elif ((2616 <= LA12_0 <= 2617)) :
                alt12 = 87
            elif (LA12_0 == 2620) :
                alt12 = 88
            elif ((2622 <= LA12_0 <= 2626)) :
                alt12 = 89
            elif ((2631 <= LA12_0 <= 2632)) :
                alt12 = 90
            elif ((2635 <= LA12_0 <= 2637)) :
                alt12 = 91
            elif ((2649 <= LA12_0 <= 2652)) :
                alt12 = 92
            elif (LA12_0 == 2654) :
                alt12 = 93
            elif ((2662 <= LA12_0 <= 2676)) :
                alt12 = 94
            elif ((2689 <= LA12_0 <= 2691)) :
                alt12 = 95
            elif ((2693 <= LA12_0 <= 2701)) :
                alt12 = 96
            elif ((2703 <= LA12_0 <= 2705)) :
                alt12 = 97
            elif ((2707 <= LA12_0 <= 2728)) :
                alt12 = 98
            elif ((2730 <= LA12_0 <= 2736)) :
                alt12 = 99
            elif ((2738 <= LA12_0 <= 2739)) :
                alt12 = 100
            elif ((2741 <= LA12_0 <= 2745)) :
                alt12 = 101
            elif ((2748 <= LA12_0 <= 2757)) :
                alt12 = 102
            elif ((2759 <= LA12_0 <= 2761)) :
                alt12 = 103
            elif ((2763 <= LA12_0 <= 2765)) :
                alt12 = 104
            elif (LA12_0 == 2768) :
                alt12 = 105
            elif ((2784 <= LA12_0 <= 2787)) :
                alt12 = 106
            elif ((2790 <= LA12_0 <= 2799)) :
                alt12 = 107
            elif (LA12_0 == 2801) :
                alt12 = 108
            elif ((2817 <= LA12_0 <= 2819)) :
                alt12 = 109
            elif ((2821 <= LA12_0 <= 2828)) :
                alt12 = 110
            elif ((2831 <= LA12_0 <= 2832)) :
                alt12 = 111
            elif ((2835 <= LA12_0 <= 2856)) :
                alt12 = 112
            elif ((2858 <= LA12_0 <= 2864)) :
                alt12 = 113
            elif ((2866 <= LA12_0 <= 2867)) :
                alt12 = 114
            elif ((2869 <= LA12_0 <= 2873)) :
                alt12 = 115
            elif ((2876 <= LA12_0 <= 2883)) :
                alt12 = 116
            elif ((2887 <= LA12_0 <= 2888)) :
                alt12 = 117
            elif ((2891 <= LA12_0 <= 2893)) :
                alt12 = 118
            elif ((2902 <= LA12_0 <= 2903)) :
                alt12 = 119
            elif ((2908 <= LA12_0 <= 2909)) :
                alt12 = 120
            elif ((2911 <= LA12_0 <= 2913)) :
                alt12 = 121
            elif ((2918 <= LA12_0 <= 2927)) :
                alt12 = 122
            elif (LA12_0 == 2929) :
                alt12 = 123
            elif ((2946 <= LA12_0 <= 2947)) :
                alt12 = 124
            elif ((2949 <= LA12_0 <= 2954)) :
                alt12 = 125
            elif ((2958 <= LA12_0 <= 2960)) :
                alt12 = 126
            elif ((2962 <= LA12_0 <= 2965)) :
                alt12 = 127
            elif ((2969 <= LA12_0 <= 2970)) :
                alt12 = 128
            elif (LA12_0 == 2972) :
                alt12 = 129
            elif ((2974 <= LA12_0 <= 2975)) :
                alt12 = 130
            elif ((2979 <= LA12_0 <= 2980)) :
                alt12 = 131
            elif ((2984 <= LA12_0 <= 2986)) :
                alt12 = 132
            elif ((2990 <= LA12_0 <= 2997)) :
                alt12 = 133
            elif ((2999 <= LA12_0 <= 3001)) :
                alt12 = 134
            elif ((3006 <= LA12_0 <= 3010)) :
                alt12 = 135
            elif ((3014 <= LA12_0 <= 3016)) :
                alt12 = 136
            elif ((3018 <= LA12_0 <= 3021)) :
                alt12 = 137
            elif (LA12_0 == 3031) :
                alt12 = 138
            elif ((3047 <= LA12_0 <= 3055)) :
                alt12 = 139
            elif (LA12_0 == 3065) :
                alt12 = 140
            elif ((3073 <= LA12_0 <= 3075)) :
                alt12 = 141
            elif ((3077 <= LA12_0 <= 3084)) :
                alt12 = 142
            elif ((3086 <= LA12_0 <= 3088)) :
                alt12 = 143
            elif ((3090 <= LA12_0 <= 3112)) :
                alt12 = 144
            elif ((3114 <= LA12_0 <= 3123)) :
                alt12 = 145
            elif ((3125 <= LA12_0 <= 3129)) :
                alt12 = 146
            elif ((3134 <= LA12_0 <= 3140)) :
                alt12 = 147
            elif ((3142 <= LA12_0 <= 3144)) :
                alt12 = 148
            elif ((3146 <= LA12_0 <= 3149)) :
                alt12 = 149
            elif ((3157 <= LA12_0 <= 3158)) :
                alt12 = 150
            elif ((3168 <= LA12_0 <= 3169)) :
                alt12 = 151
            elif ((3174 <= LA12_0 <= 3183)) :
                alt12 = 152
            elif ((3202 <= LA12_0 <= 3203)) :
                alt12 = 153
            elif ((3205 <= LA12_0 <= 3212)) :
                alt12 = 154
            elif ((3214 <= LA12_0 <= 3216)) :
                alt12 = 155
            elif ((3218 <= LA12_0 <= 3240)) :
                alt12 = 156
            elif ((3242 <= LA12_0 <= 3251)) :
                alt12 = 157
            elif ((3253 <= LA12_0 <= 3257)) :
                alt12 = 158
            elif ((3260 <= LA12_0 <= 3268)) :
                alt12 = 159
            elif ((3270 <= LA12_0 <= 3272)) :
                alt12 = 160
            elif ((3274 <= LA12_0 <= 3277)) :
                alt12 = 161
            elif ((3285 <= LA12_0 <= 3286)) :
                alt12 = 162
            elif (LA12_0 == 3294) :
                alt12 = 163
            elif ((3296 <= LA12_0 <= 3297)) :
                alt12 = 164
            elif ((3302 <= LA12_0 <= 3311)) :
                alt12 = 165
            elif ((3330 <= LA12_0 <= 3331)) :
                alt12 = 166
            elif ((3333 <= LA12_0 <= 3340)) :
                alt12 = 167
            elif ((3342 <= LA12_0 <= 3344)) :
                alt12 = 168
            elif ((3346 <= LA12_0 <= 3368)) :
                alt12 = 169
            elif ((3370 <= LA12_0 <= 3385)) :
                alt12 = 170
            elif ((3390 <= LA12_0 <= 3395)) :
                alt12 = 171
            elif ((3398 <= LA12_0 <= 3400)) :
                alt12 = 172
            elif ((3402 <= LA12_0 <= 3405)) :
                alt12 = 173
            elif (LA12_0 == 3415) :
                alt12 = 174
            elif ((3424 <= LA12_0 <= 3425)) :
                alt12 = 175
            elif ((3430 <= LA12_0 <= 3439)) :
                alt12 = 176
            elif ((3458 <= LA12_0 <= 3459)) :
                alt12 = 177
            elif ((3461 <= LA12_0 <= 3478)) :
                alt12 = 178
            elif ((3482 <= LA12_0 <= 3505)) :
                alt12 = 179
            elif ((3507 <= LA12_0 <= 3515)) :
                alt12 = 180
            elif (LA12_0 == 3517) :
                alt12 = 181
            elif ((3520 <= LA12_0 <= 3526)) :
                alt12 = 182
            elif (LA12_0 == 3530) :
                alt12 = 183
            elif ((3535 <= LA12_0 <= 3540)) :
                alt12 = 184
            elif (LA12_0 == 3542) :
                alt12 = 185
            elif ((3544 <= LA12_0 <= 3551)) :
                alt12 = 186
            elif ((3570 <= LA12_0 <= 3571)) :
                alt12 = 187
            elif ((3585 <= LA12_0 <= 3642)) :
                alt12 = 188
            elif ((3647 <= LA12_0 <= 3662)) :
                alt12 = 189
            elif ((3664 <= LA12_0 <= 3673)) :
                alt12 = 190
            elif ((3713 <= LA12_0 <= 3714)) :
                alt12 = 191
            elif (LA12_0 == 3716) :
                alt12 = 192
            elif ((3719 <= LA12_0 <= 3720)) :
                alt12 = 193
            elif (LA12_0 == 3722) :
                alt12 = 194
            elif (LA12_0 == 3725) :
                alt12 = 195
            elif ((3732 <= LA12_0 <= 3735)) :
                alt12 = 196
            elif ((3737 <= LA12_0 <= 3743)) :
                alt12 = 197
            elif ((3745 <= LA12_0 <= 3747)) :
                alt12 = 198
            elif (LA12_0 == 3749) :
                alt12 = 199
            elif (LA12_0 == 3751) :
                alt12 = 200
            elif ((3754 <= LA12_0 <= 3755)) :
                alt12 = 201
            elif ((3757 <= LA12_0 <= 3769)) :
                alt12 = 202
            elif ((3771 <= LA12_0 <= 3773)) :
                alt12 = 203
            elif ((3776 <= LA12_0 <= 3780)) :
                alt12 = 204
            elif (LA12_0 == 3782) :
                alt12 = 205
            elif ((3784 <= LA12_0 <= 3789)) :
                alt12 = 206
            elif ((3792 <= LA12_0 <= 3801)) :
                alt12 = 207
            elif ((3804 <= LA12_0 <= 3805)) :
                alt12 = 208
            elif (LA12_0 == 3840) :
                alt12 = 209
            elif ((3864 <= LA12_0 <= 3865)) :
                alt12 = 210
            elif ((3872 <= LA12_0 <= 3881)) :
                alt12 = 211
            elif (LA12_0 == 3893) :
                alt12 = 212
            elif (LA12_0 == 3895) :
                alt12 = 213
            elif (LA12_0 == 3897) :
                alt12 = 214
            elif ((3902 <= LA12_0 <= 3911)) :
                alt12 = 215
            elif ((3913 <= LA12_0 <= 3946)) :
                alt12 = 216
            elif ((3953 <= LA12_0 <= 3972)) :
                alt12 = 217
            elif ((3974 <= LA12_0 <= 3979)) :
                alt12 = 218
            elif ((3984 <= LA12_0 <= 3991)) :
                alt12 = 219
            elif ((3993 <= LA12_0 <= 4028)) :
                alt12 = 220
            elif (LA12_0 == 4038) :
                alt12 = 221
            elif ((4096 <= LA12_0 <= 4129)) :
                alt12 = 222
            elif ((4131 <= LA12_0 <= 4135)) :
                alt12 = 223
            elif ((4137 <= LA12_0 <= 4138)) :
                alt12 = 224
            elif ((4140 <= LA12_0 <= 4146)) :
                alt12 = 225
            elif ((4150 <= LA12_0 <= 4153)) :
                alt12 = 226
            elif ((4160 <= LA12_0 <= 4169)) :
                alt12 = 227
            elif ((4176 <= LA12_0 <= 4185)) :
                alt12 = 228
            elif ((4256 <= LA12_0 <= 4293)) :
                alt12 = 229
            elif ((4304 <= LA12_0 <= 4344)) :
                alt12 = 230
            elif ((4352 <= LA12_0 <= 4441)) :
                alt12 = 231
            elif ((4447 <= LA12_0 <= 4514)) :
                alt12 = 232
            elif ((4520 <= LA12_0 <= 4601)) :
                alt12 = 233
            elif ((4608 <= LA12_0 <= 4614)) :
                alt12 = 234
            elif ((4616 <= LA12_0 <= 4678)) :
                alt12 = 235
            elif (LA12_0 == 4680) :
                alt12 = 236
            elif ((4682 <= LA12_0 <= 4685)) :
                alt12 = 237
            elif ((4688 <= LA12_0 <= 4694)) :
                alt12 = 238
            elif (LA12_0 == 4696) :
                alt12 = 239
            elif ((4698 <= LA12_0 <= 4701)) :
                alt12 = 240
            elif ((4704 <= LA12_0 <= 4742)) :
                alt12 = 241
            elif (LA12_0 == 4744) :
                alt12 = 242
            elif ((4746 <= LA12_0 <= 4749)) :
                alt12 = 243
            elif ((4752 <= LA12_0 <= 4782)) :
                alt12 = 244
            elif (LA12_0 == 4784) :
                alt12 = 245
            elif ((4786 <= LA12_0 <= 4789)) :
                alt12 = 246
            elif ((4792 <= LA12_0 <= 4798)) :
                alt12 = 247
            elif (LA12_0 == 4800) :
                alt12 = 248
            elif ((4802 <= LA12_0 <= 4805)) :
                alt12 = 249
            elif ((4808 <= LA12_0 <= 4814)) :
                alt12 = 250
            elif ((4816 <= LA12_0 <= 4822)) :
                alt12 = 251
            elif ((4824 <= LA12_0 <= 4846)) :
                alt12 = 252
            elif ((4848 <= LA12_0 <= 4878)) :
                alt12 = 253
            elif (LA12_0 == 4880) :
                alt12 = 254
            elif ((4882 <= LA12_0 <= 4885)) :
                alt12 = 255
            elif ((4888 <= LA12_0 <= 4894)) :
                alt12 = 256
            elif ((4896 <= LA12_0 <= 4934)) :
                alt12 = 257
            elif ((4936 <= LA12_0 <= 4954)) :
                alt12 = 258
            elif ((4969 <= LA12_0 <= 4977)) :
                alt12 = 259
            elif ((5024 <= LA12_0 <= 5108)) :
                alt12 = 260
            elif ((5121 <= LA12_0 <= 5740)) :
                alt12 = 261
            elif ((5743 <= LA12_0 <= 5750)) :
                alt12 = 262
            elif ((5761 <= LA12_0 <= 5786)) :
                alt12 = 263
            elif ((5792 <= LA12_0 <= 5866)) :
                alt12 = 264
            elif ((5870 <= LA12_0 <= 5872)) :
                alt12 = 265
            elif ((5888 <= LA12_0 <= 5900)) :
                alt12 = 266
            elif ((5902 <= LA12_0 <= 5908)) :
                alt12 = 267
            elif ((5920 <= LA12_0 <= 5940)) :
                alt12 = 268
            elif ((5952 <= LA12_0 <= 5971)) :
                alt12 = 269
            elif ((5984 <= LA12_0 <= 5996)) :
                alt12 = 270
            elif ((5998 <= LA12_0 <= 6000)) :
                alt12 = 271
            elif ((6002 <= LA12_0 <= 6003)) :
                alt12 = 272
            elif ((6016 <= LA12_0 <= 6099)) :
                alt12 = 273
            elif (LA12_0 == 6103) :
                alt12 = 274
            elif ((6107 <= LA12_0 <= 6109)) :
                alt12 = 275
            elif ((6112 <= LA12_0 <= 6121)) :
                alt12 = 276
            elif ((6155 <= LA12_0 <= 6157)) :
                alt12 = 277
            elif ((6160 <= LA12_0 <= 6169)) :
                alt12 = 278
            elif ((6176 <= LA12_0 <= 6263)) :
                alt12 = 279
            elif ((6272 <= LA12_0 <= 6313)) :
                alt12 = 280
            elif ((6400 <= LA12_0 <= 6428)) :
                alt12 = 281
            elif ((6432 <= LA12_0 <= 6443)) :
                alt12 = 282
            elif ((6448 <= LA12_0 <= 6459)) :
                alt12 = 283
            elif ((6470 <= LA12_0 <= 6509)) :
                alt12 = 284
            elif ((6512 <= LA12_0 <= 6516)) :
                alt12 = 285
            elif ((7424 <= LA12_0 <= 7531)) :
                alt12 = 286
            elif ((7680 <= LA12_0 <= 7835)) :
                alt12 = 287
            elif ((7840 <= LA12_0 <= 7929)) :
                alt12 = 288
            elif ((7936 <= LA12_0 <= 7957)) :
                alt12 = 289
            elif ((7960 <= LA12_0 <= 7965)) :
                alt12 = 290
            elif ((7968 <= LA12_0 <= 8005)) :
                alt12 = 291
            elif ((8008 <= LA12_0 <= 8013)) :
                alt12 = 292
            elif ((8016 <= LA12_0 <= 8023)) :
                alt12 = 293
            elif (LA12_0 == 8025) :
                alt12 = 294
            elif (LA12_0 == 8027) :
                alt12 = 295
            elif (LA12_0 == 8029) :
                alt12 = 296
            elif ((8031 <= LA12_0 <= 8061)) :
                alt12 = 297
            elif ((8064 <= LA12_0 <= 8116)) :
                alt12 = 298
            elif ((8118 <= LA12_0 <= 8124)) :
                alt12 = 299
            elif (LA12_0 == 8126) :
                alt12 = 300
            elif ((8130 <= LA12_0 <= 8132)) :
                alt12 = 301
            elif ((8134 <= LA12_0 <= 8140)) :
                alt12 = 302
            elif ((8144 <= LA12_0 <= 8147)) :
                alt12 = 303
            elif ((8150 <= LA12_0 <= 8155)) :
                alt12 = 304
            elif ((8160 <= LA12_0 <= 8172)) :
                alt12 = 305
            elif ((8178 <= LA12_0 <= 8180)) :
                alt12 = 306
            elif ((8182 <= LA12_0 <= 8188)) :
                alt12 = 307
            elif ((8204 <= LA12_0 <= 8207)) :
                alt12 = 308
            elif ((8234 <= LA12_0 <= 8238)) :
                alt12 = 309
            elif ((8255 <= LA12_0 <= 8256)) :
                alt12 = 310
            elif (LA12_0 == 8276) :
                alt12 = 311
            elif ((8288 <= LA12_0 <= 8291)) :
                alt12 = 312
            elif ((8298 <= LA12_0 <= 8303)) :
                alt12 = 313
            elif (LA12_0 == 8305) :
                alt12 = 314
            elif (LA12_0 == 8319) :
                alt12 = 315
            elif ((8352 <= LA12_0 <= 8369)) :
                alt12 = 316
            elif ((8400 <= LA12_0 <= 8412)) :
                alt12 = 317
            elif (LA12_0 == 8417) :
                alt12 = 318
            elif ((8421 <= LA12_0 <= 8426)) :
                alt12 = 319
            elif (LA12_0 == 8450) :
                alt12 = 320
            elif (LA12_0 == 8455) :
                alt12 = 321
            elif ((8458 <= LA12_0 <= 8467)) :
                alt12 = 322
            elif (LA12_0 == 8469) :
                alt12 = 323
            elif ((8473 <= LA12_0 <= 8477)) :
                alt12 = 324
            elif (LA12_0 == 8484) :
                alt12 = 325
            elif (LA12_0 == 8486) :
                alt12 = 326
            elif (LA12_0 == 8488) :
                alt12 = 327
            elif ((8490 <= LA12_0 <= 8493)) :
                alt12 = 328
            elif ((8495 <= LA12_0 <= 8497)) :
                alt12 = 329
            elif ((8499 <= LA12_0 <= 8505)) :
                alt12 = 330
            elif ((8509 <= LA12_0 <= 8511)) :
                alt12 = 331
            elif ((8517 <= LA12_0 <= 8521)) :
                alt12 = 332
            elif ((8544 <= LA12_0 <= 8579)) :
                alt12 = 333
            elif ((12293 <= LA12_0 <= 12295)) :
                alt12 = 334
            elif ((12321 <= LA12_0 <= 12335)) :
                alt12 = 335
            elif ((12337 <= LA12_0 <= 12341)) :
                alt12 = 336
            elif ((12344 <= LA12_0 <= 12348)) :
                alt12 = 337
            elif ((12353 <= LA12_0 <= 12438)) :
                alt12 = 338
            elif ((12441 <= LA12_0 <= 12442)) :
                alt12 = 339
            elif ((12445 <= LA12_0 <= 12447)) :
                alt12 = 340
            elif ((12449 <= LA12_0 <= 12543)) :
                alt12 = 341
            elif ((12549 <= LA12_0 <= 12588)) :
                alt12 = 342
            elif ((12593 <= LA12_0 <= 12686)) :
                alt12 = 343
            elif ((12704 <= LA12_0 <= 12727)) :
                alt12 = 344
            elif ((12784 <= LA12_0 <= 12799)) :
                alt12 = 345
            elif ((13312 <= LA12_0 <= 19893)) :
                alt12 = 346
            elif ((19968 <= LA12_0 <= 40869)) :
                alt12 = 347
            elif ((40960 <= LA12_0 <= 42124)) :
                alt12 = 348
            elif ((44032 <= LA12_0 <= 55203)) :
                alt12 = 349
            elif ((63744 <= LA12_0 <= 64045)) :
                alt12 = 350
            elif ((64048 <= LA12_0 <= 64106)) :
                alt12 = 351
            elif ((64256 <= LA12_0 <= 64262)) :
                alt12 = 352
            elif ((64275 <= LA12_0 <= 64279)) :
                alt12 = 353
            elif ((64285 <= LA12_0 <= 64296)) :
                alt12 = 354
            elif ((64298 <= LA12_0 <= 64310)) :
                alt12 = 355
            elif ((64312 <= LA12_0 <= 64316)) :
                alt12 = 356
            elif (LA12_0 == 64318) :
                alt12 = 357
            elif ((64320 <= LA12_0 <= 64321)) :
                alt12 = 358
            elif ((64323 <= LA12_0 <= 64324)) :
                alt12 = 359
            elif ((64326 <= LA12_0 <= 64433)) :
                alt12 = 360
            elif ((64467 <= LA12_0 <= 64829)) :
                alt12 = 361
            elif ((64848 <= LA12_0 <= 64911)) :
                alt12 = 362
            elif ((64914 <= LA12_0 <= 64967)) :
                alt12 = 363
            elif ((65008 <= LA12_0 <= 65020)) :
                alt12 = 364
            elif ((65024 <= LA12_0 <= 65039)) :
                alt12 = 365
            elif ((65056 <= LA12_0 <= 65059)) :
                alt12 = 366
            elif ((65075 <= LA12_0 <= 65076)) :
                alt12 = 367
            elif ((65101 <= LA12_0 <= 65103)) :
                alt12 = 368
            elif (LA12_0 == 65129) :
                alt12 = 369
            elif ((65136 <= LA12_0 <= 65140)) :
                alt12 = 370
            elif ((65142 <= LA12_0 <= 65276)) :
                alt12 = 371
            elif (LA12_0 == 65279) :
                alt12 = 372
            elif (LA12_0 == 65284) :
                alt12 = 373
            elif ((65296 <= LA12_0 <= 65305)) :
                alt12 = 374
            elif ((65313 <= LA12_0 <= 65338)) :
                alt12 = 375
            elif (LA12_0 == 65343) :
                alt12 = 376
            elif ((65345 <= LA12_0 <= 65370)) :
                alt12 = 377
            elif ((65381 <= LA12_0 <= 65470)) :
                alt12 = 378
            elif ((65474 <= LA12_0 <= 65479)) :
                alt12 = 379
            elif ((65482 <= LA12_0 <= 65487)) :
                alt12 = 380
            elif ((65490 <= LA12_0 <= 65495)) :
                alt12 = 381
            elif ((65498 <= LA12_0 <= 65500)) :
                alt12 = 382
            elif ((65504 <= LA12_0 <= 65505)) :
                alt12 = 383
            elif ((65509 <= LA12_0 <= 65510)) :
                alt12 = 384
            elif ((65529 <= LA12_0 <= 65531)) :
                alt12 = 385
            elif ((55296 <= LA12_0 <= 56319)) :
                alt12 = 386
            else:
                nvae = NoViableAltException("", 12, 0, self.input)

                raise nvae

            if alt12 == 1:
                # gleampython/gleam.g:432:9: '\\u0000' .. '\\u0008'
                pass 
                self.matchRange(0, 8)


            elif alt12 == 2:
                # gleampython/gleam.g:433:9: '\\u000e' .. '\\u001b'
                pass 
                self.matchRange(14, 27)


            elif alt12 == 3:
                # gleampython/gleam.g:434:9: '\\u0024'
                pass 
                self.match(36)


            elif alt12 == 4:
                # gleampython/gleam.g:435:9: '\\u0030' .. '\\u0039'
                pass 
                self.matchRange(48, 57)


            elif alt12 == 5:
                # gleampython/gleam.g:436:9: '\\u0041' .. '\\u005a'
                pass 
                self.matchRange(65, 90)


            elif alt12 == 6:
                # gleampython/gleam.g:437:9: '\\u005f'
                pass 
                self.match(95)


            elif alt12 == 7:
                # gleampython/gleam.g:438:9: '\\u0061' .. '\\u007a'
                pass 
                self.matchRange(97, 122)


            elif alt12 == 8:
                # gleampython/gleam.g:439:9: '\\u007f' .. '\\u009f'
                pass 
                self.matchRange(127, 159)


            elif alt12 == 9:
                # gleampython/gleam.g:440:9: '\\u00a2' .. '\\u00a5'
                pass 
                self.matchRange(162, 165)


            elif alt12 == 10:
                # gleampython/gleam.g:441:9: '\\u00aa'
                pass 
                self.match(170)


            elif alt12 == 11:
                # gleampython/gleam.g:442:9: '\\u00ad'
                pass 
                self.match(173)


            elif alt12 == 12:
                # gleampython/gleam.g:443:9: '\\u00b5'
                pass 
                self.match(181)


            elif alt12 == 13:
                # gleampython/gleam.g:444:9: '\\u00ba'
                pass 
                self.match(186)


            elif alt12 == 14:
                # gleampython/gleam.g:445:9: '\\u00c0' .. '\\u00d6'
                pass 
                self.matchRange(192, 214)


            elif alt12 == 15:
                # gleampython/gleam.g:446:9: '\\u00d8' .. '\\u00f6'
                pass 
                self.matchRange(216, 246)


            elif alt12 == 16:
                # gleampython/gleam.g:447:9: '\\u00f8' .. '\\u0236'
                pass 
                self.matchRange(248, 566)


            elif alt12 == 17:
                # gleampython/gleam.g:448:9: '\\u0250' .. '\\u02c1'
                pass 
                self.matchRange(592, 705)


            elif alt12 == 18:
                # gleampython/gleam.g:449:9: '\\u02c6' .. '\\u02d1'
                pass 
                self.matchRange(710, 721)


            elif alt12 == 19:
                # gleampython/gleam.g:450:9: '\\u02e0' .. '\\u02e4'
                pass 
                self.matchRange(736, 740)


            elif alt12 == 20:
                # gleampython/gleam.g:451:9: '\\u02ee'
                pass 
                self.match(750)


            elif alt12 == 21:
                # gleampython/gleam.g:452:9: '\\u0300' .. '\\u0357'
                pass 
                self.matchRange(768, 855)


            elif alt12 == 22:
                # gleampython/gleam.g:453:9: '\\u035d' .. '\\u036f'
                pass 
                self.matchRange(861, 879)


            elif alt12 == 23:
                # gleampython/gleam.g:454:9: '\\u037a'
                pass 
                self.match(890)


            elif alt12 == 24:
                # gleampython/gleam.g:455:9: '\\u0386'
                pass 
                self.match(902)


            elif alt12 == 25:
                # gleampython/gleam.g:456:9: '\\u0388' .. '\\u038a'
                pass 
                self.matchRange(904, 906)


            elif alt12 == 26:
                # gleampython/gleam.g:457:9: '\\u038c'
                pass 
                self.match(908)


            elif alt12 == 27:
                # gleampython/gleam.g:458:9: '\\u038e' .. '\\u03a1'
                pass 
                self.matchRange(910, 929)


            elif alt12 == 28:
                # gleampython/gleam.g:459:9: '\\u03a3' .. '\\u03ce'
                pass 
                self.matchRange(931, 974)


            elif alt12 == 29:
                # gleampython/gleam.g:460:9: '\\u03d0' .. '\\u03f5'
                pass 
                self.matchRange(976, 1013)


            elif alt12 == 30:
                # gleampython/gleam.g:461:9: '\\u03f7' .. '\\u03fb'
                pass 
                self.matchRange(1015, 1019)


            elif alt12 == 31:
                # gleampython/gleam.g:462:9: '\\u0400' .. '\\u0481'
                pass 
                self.matchRange(1024, 1153)


            elif alt12 == 32:
                # gleampython/gleam.g:463:9: '\\u0483' .. '\\u0486'
                pass 
                self.matchRange(1155, 1158)


            elif alt12 == 33:
                # gleampython/gleam.g:464:9: '\\u048a' .. '\\u04ce'
                pass 
                self.matchRange(1162, 1230)


            elif alt12 == 34:
                # gleampython/gleam.g:465:9: '\\u04d0' .. '\\u04f5'
                pass 
                self.matchRange(1232, 1269)


            elif alt12 == 35:
                # gleampython/gleam.g:466:9: '\\u04f8' .. '\\u04f9'
                pass 
                self.matchRange(1272, 1273)


            elif alt12 == 36:
                # gleampython/gleam.g:467:9: '\\u0500' .. '\\u050f'
                pass 
                self.matchRange(1280, 1295)


            elif alt12 == 37:
                # gleampython/gleam.g:468:9: '\\u0531' .. '\\u0556'
                pass 
                self.matchRange(1329, 1366)


            elif alt12 == 38:
                # gleampython/gleam.g:469:9: '\\u0559'
                pass 
                self.match(1369)


            elif alt12 == 39:
                # gleampython/gleam.g:470:9: '\\u0561' .. '\\u0587'
                pass 
                self.matchRange(1377, 1415)


            elif alt12 == 40:
                # gleampython/gleam.g:471:9: '\\u0591' .. '\\u05a1'
                pass 
                self.matchRange(1425, 1441)


            elif alt12 == 41:
                # gleampython/gleam.g:472:9: '\\u05a3' .. '\\u05b9'
                pass 
                self.matchRange(1443, 1465)


            elif alt12 == 42:
                # gleampython/gleam.g:473:9: '\\u05bb' .. '\\u05bd'
                pass 
                self.matchRange(1467, 1469)


            elif alt12 == 43:
                # gleampython/gleam.g:474:9: '\\u05bf'
                pass 
                self.match(1471)


            elif alt12 == 44:
                # gleampython/gleam.g:475:9: '\\u05c1' .. '\\u05c2'
                pass 
                self.matchRange(1473, 1474)


            elif alt12 == 45:
                # gleampython/gleam.g:476:9: '\\u05c4'
                pass 
                self.match(1476)


            elif alt12 == 46:
                # gleampython/gleam.g:477:9: '\\u05d0' .. '\\u05ea'
                pass 
                self.matchRange(1488, 1514)


            elif alt12 == 47:
                # gleampython/gleam.g:478:9: '\\u05f0' .. '\\u05f2'
                pass 
                self.matchRange(1520, 1522)


            elif alt12 == 48:
                # gleampython/gleam.g:479:9: '\\u0600' .. '\\u0603'
                pass 
                self.matchRange(1536, 1539)


            elif alt12 == 49:
                # gleampython/gleam.g:480:9: '\\u0610' .. '\\u0615'
                pass 
                self.matchRange(1552, 1557)


            elif alt12 == 50:
                # gleampython/gleam.g:481:9: '\\u0621' .. '\\u063a'
                pass 
                self.matchRange(1569, 1594)


            elif alt12 == 51:
                # gleampython/gleam.g:482:9: '\\u0640' .. '\\u0658'
                pass 
                self.matchRange(1600, 1624)


            elif alt12 == 52:
                # gleampython/gleam.g:483:9: '\\u0660' .. '\\u0669'
                pass 
                self.matchRange(1632, 1641)


            elif alt12 == 53:
                # gleampython/gleam.g:484:9: '\\u066e' .. '\\u06d3'
                pass 
                self.matchRange(1646, 1747)


            elif alt12 == 54:
                # gleampython/gleam.g:485:9: '\\u06d5' .. '\\u06dd'
                pass 
                self.matchRange(1749, 1757)


            elif alt12 == 55:
                # gleampython/gleam.g:486:9: '\\u06df' .. '\\u06e8'
                pass 
                self.matchRange(1759, 1768)


            elif alt12 == 56:
                # gleampython/gleam.g:487:9: '\\u06ea' .. '\\u06fc'
                pass 
                self.matchRange(1770, 1788)


            elif alt12 == 57:
                # gleampython/gleam.g:488:9: '\\u06ff'
                pass 
                self.match(1791)


            elif alt12 == 58:
                # gleampython/gleam.g:489:9: '\\u070f' .. '\\u074a'
                pass 
                self.matchRange(1807, 1866)


            elif alt12 == 59:
                # gleampython/gleam.g:490:9: '\\u074d' .. '\\u074f'
                pass 
                self.matchRange(1869, 1871)


            elif alt12 == 60:
                # gleampython/gleam.g:491:9: '\\u0780' .. '\\u07b1'
                pass 
                self.matchRange(1920, 1969)


            elif alt12 == 61:
                # gleampython/gleam.g:492:9: '\\u0901' .. '\\u0939'
                pass 
                self.matchRange(2305, 2361)


            elif alt12 == 62:
                # gleampython/gleam.g:493:9: '\\u093c' .. '\\u094d'
                pass 
                self.matchRange(2364, 2381)


            elif alt12 == 63:
                # gleampython/gleam.g:494:9: '\\u0950' .. '\\u0954'
                pass 
                self.matchRange(2384, 2388)


            elif alt12 == 64:
                # gleampython/gleam.g:495:9: '\\u0958' .. '\\u0963'
                pass 
                self.matchRange(2392, 2403)


            elif alt12 == 65:
                # gleampython/gleam.g:496:9: '\\u0966' .. '\\u096f'
                pass 
                self.matchRange(2406, 2415)


            elif alt12 == 66:
                # gleampython/gleam.g:497:9: '\\u0981' .. '\\u0983'
                pass 
                self.matchRange(2433, 2435)


            elif alt12 == 67:
                # gleampython/gleam.g:498:9: '\\u0985' .. '\\u098c'
                pass 
                self.matchRange(2437, 2444)


            elif alt12 == 68:
                # gleampython/gleam.g:499:9: '\\u098f' .. '\\u0990'
                pass 
                self.matchRange(2447, 2448)


            elif alt12 == 69:
                # gleampython/gleam.g:500:9: '\\u0993' .. '\\u09a8'
                pass 
                self.matchRange(2451, 2472)


            elif alt12 == 70:
                # gleampython/gleam.g:501:9: '\\u09aa' .. '\\u09b0'
                pass 
                self.matchRange(2474, 2480)


            elif alt12 == 71:
                # gleampython/gleam.g:502:9: '\\u09b2'
                pass 
                self.match(2482)


            elif alt12 == 72:
                # gleampython/gleam.g:503:9: '\\u09b6' .. '\\u09b9'
                pass 
                self.matchRange(2486, 2489)


            elif alt12 == 73:
                # gleampython/gleam.g:504:9: '\\u09bc' .. '\\u09c4'
                pass 
                self.matchRange(2492, 2500)


            elif alt12 == 74:
                # gleampython/gleam.g:505:9: '\\u09c7' .. '\\u09c8'
                pass 
                self.matchRange(2503, 2504)


            elif alt12 == 75:
                # gleampython/gleam.g:506:9: '\\u09cb' .. '\\u09cd'
                pass 
                self.matchRange(2507, 2509)


            elif alt12 == 76:
                # gleampython/gleam.g:507:9: '\\u09d7'
                pass 
                self.match(2519)


            elif alt12 == 77:
                # gleampython/gleam.g:508:9: '\\u09dc' .. '\\u09dd'
                pass 
                self.matchRange(2524, 2525)


            elif alt12 == 78:
                # gleampython/gleam.g:509:9: '\\u09df' .. '\\u09e3'
                pass 
                self.matchRange(2527, 2531)


            elif alt12 == 79:
                # gleampython/gleam.g:510:9: '\\u09e6' .. '\\u09f3'
                pass 
                self.matchRange(2534, 2547)


            elif alt12 == 80:
                # gleampython/gleam.g:511:9: '\\u0a01' .. '\\u0a03'
                pass 
                self.matchRange(2561, 2563)


            elif alt12 == 81:
                # gleampython/gleam.g:512:9: '\\u0a05' .. '\\u0a0a'
                pass 
                self.matchRange(2565, 2570)


            elif alt12 == 82:
                # gleampython/gleam.g:513:9: '\\u0a0f' .. '\\u0a10'
                pass 
                self.matchRange(2575, 2576)


            elif alt12 == 83:
                # gleampython/gleam.g:514:9: '\\u0a13' .. '\\u0a28'
                pass 
                self.matchRange(2579, 2600)


            elif alt12 == 84:
                # gleampython/gleam.g:515:9: '\\u0a2a' .. '\\u0a30'
                pass 
                self.matchRange(2602, 2608)


            elif alt12 == 85:
                # gleampython/gleam.g:516:9: '\\u0a32' .. '\\u0a33'
                pass 
                self.matchRange(2610, 2611)


            elif alt12 == 86:
                # gleampython/gleam.g:517:9: '\\u0a35' .. '\\u0a36'
                pass 
                self.matchRange(2613, 2614)


            elif alt12 == 87:
                # gleampython/gleam.g:518:9: '\\u0a38' .. '\\u0a39'
                pass 
                self.matchRange(2616, 2617)


            elif alt12 == 88:
                # gleampython/gleam.g:519:9: '\\u0a3c'
                pass 
                self.match(2620)


            elif alt12 == 89:
                # gleampython/gleam.g:520:9: '\\u0a3e' .. '\\u0a42'
                pass 
                self.matchRange(2622, 2626)


            elif alt12 == 90:
                # gleampython/gleam.g:521:9: '\\u0a47' .. '\\u0a48'
                pass 
                self.matchRange(2631, 2632)


            elif alt12 == 91:
                # gleampython/gleam.g:522:9: '\\u0a4b' .. '\\u0a4d'
                pass 
                self.matchRange(2635, 2637)


            elif alt12 == 92:
                # gleampython/gleam.g:523:9: '\\u0a59' .. '\\u0a5c'
                pass 
                self.matchRange(2649, 2652)


            elif alt12 == 93:
                # gleampython/gleam.g:524:9: '\\u0a5e'
                pass 
                self.match(2654)


            elif alt12 == 94:
                # gleampython/gleam.g:525:9: '\\u0a66' .. '\\u0a74'
                pass 
                self.matchRange(2662, 2676)


            elif alt12 == 95:
                # gleampython/gleam.g:526:9: '\\u0a81' .. '\\u0a83'
                pass 
                self.matchRange(2689, 2691)


            elif alt12 == 96:
                # gleampython/gleam.g:527:9: '\\u0a85' .. '\\u0a8d'
                pass 
                self.matchRange(2693, 2701)


            elif alt12 == 97:
                # gleampython/gleam.g:528:9: '\\u0a8f' .. '\\u0a91'
                pass 
                self.matchRange(2703, 2705)


            elif alt12 == 98:
                # gleampython/gleam.g:529:9: '\\u0a93' .. '\\u0aa8'
                pass 
                self.matchRange(2707, 2728)


            elif alt12 == 99:
                # gleampython/gleam.g:530:9: '\\u0aaa' .. '\\u0ab0'
                pass 
                self.matchRange(2730, 2736)


            elif alt12 == 100:
                # gleampython/gleam.g:531:9: '\\u0ab2' .. '\\u0ab3'
                pass 
                self.matchRange(2738, 2739)


            elif alt12 == 101:
                # gleampython/gleam.g:532:9: '\\u0ab5' .. '\\u0ab9'
                pass 
                self.matchRange(2741, 2745)


            elif alt12 == 102:
                # gleampython/gleam.g:533:9: '\\u0abc' .. '\\u0ac5'
                pass 
                self.matchRange(2748, 2757)


            elif alt12 == 103:
                # gleampython/gleam.g:534:9: '\\u0ac7' .. '\\u0ac9'
                pass 
                self.matchRange(2759, 2761)


            elif alt12 == 104:
                # gleampython/gleam.g:535:9: '\\u0acb' .. '\\u0acd'
                pass 
                self.matchRange(2763, 2765)


            elif alt12 == 105:
                # gleampython/gleam.g:536:9: '\\u0ad0'
                pass 
                self.match(2768)


            elif alt12 == 106:
                # gleampython/gleam.g:537:9: '\\u0ae0' .. '\\u0ae3'
                pass 
                self.matchRange(2784, 2787)


            elif alt12 == 107:
                # gleampython/gleam.g:538:9: '\\u0ae6' .. '\\u0aef'
                pass 
                self.matchRange(2790, 2799)


            elif alt12 == 108:
                # gleampython/gleam.g:539:9: '\\u0af1'
                pass 
                self.match(2801)


            elif alt12 == 109:
                # gleampython/gleam.g:540:9: '\\u0b01' .. '\\u0b03'
                pass 
                self.matchRange(2817, 2819)


            elif alt12 == 110:
                # gleampython/gleam.g:541:9: '\\u0b05' .. '\\u0b0c'
                pass 
                self.matchRange(2821, 2828)


            elif alt12 == 111:
                # gleampython/gleam.g:542:9: '\\u0b0f' .. '\\u0b10'
                pass 
                self.matchRange(2831, 2832)


            elif alt12 == 112:
                # gleampython/gleam.g:543:9: '\\u0b13' .. '\\u0b28'
                pass 
                self.matchRange(2835, 2856)


            elif alt12 == 113:
                # gleampython/gleam.g:544:9: '\\u0b2a' .. '\\u0b30'
                pass 
                self.matchRange(2858, 2864)


            elif alt12 == 114:
                # gleampython/gleam.g:545:9: '\\u0b32' .. '\\u0b33'
                pass 
                self.matchRange(2866, 2867)


            elif alt12 == 115:
                # gleampython/gleam.g:546:9: '\\u0b35' .. '\\u0b39'
                pass 
                self.matchRange(2869, 2873)


            elif alt12 == 116:
                # gleampython/gleam.g:547:9: '\\u0b3c' .. '\\u0b43'
                pass 
                self.matchRange(2876, 2883)


            elif alt12 == 117:
                # gleampython/gleam.g:548:9: '\\u0b47' .. '\\u0b48'
                pass 
                self.matchRange(2887, 2888)


            elif alt12 == 118:
                # gleampython/gleam.g:549:9: '\\u0b4b' .. '\\u0b4d'
                pass 
                self.matchRange(2891, 2893)


            elif alt12 == 119:
                # gleampython/gleam.g:550:9: '\\u0b56' .. '\\u0b57'
                pass 
                self.matchRange(2902, 2903)


            elif alt12 == 120:
                # gleampython/gleam.g:551:9: '\\u0b5c' .. '\\u0b5d'
                pass 
                self.matchRange(2908, 2909)


            elif alt12 == 121:
                # gleampython/gleam.g:552:9: '\\u0b5f' .. '\\u0b61'
                pass 
                self.matchRange(2911, 2913)


            elif alt12 == 122:
                # gleampython/gleam.g:553:9: '\\u0b66' .. '\\u0b6f'
                pass 
                self.matchRange(2918, 2927)


            elif alt12 == 123:
                # gleampython/gleam.g:554:9: '\\u0b71'
                pass 
                self.match(2929)


            elif alt12 == 124:
                # gleampython/gleam.g:555:9: '\\u0b82' .. '\\u0b83'
                pass 
                self.matchRange(2946, 2947)


            elif alt12 == 125:
                # gleampython/gleam.g:556:9: '\\u0b85' .. '\\u0b8a'
                pass 
                self.matchRange(2949, 2954)


            elif alt12 == 126:
                # gleampython/gleam.g:557:9: '\\u0b8e' .. '\\u0b90'
                pass 
                self.matchRange(2958, 2960)


            elif alt12 == 127:
                # gleampython/gleam.g:558:9: '\\u0b92' .. '\\u0b95'
                pass 
                self.matchRange(2962, 2965)


            elif alt12 == 128:
                # gleampython/gleam.g:559:9: '\\u0b99' .. '\\u0b9a'
                pass 
                self.matchRange(2969, 2970)


            elif alt12 == 129:
                # gleampython/gleam.g:560:9: '\\u0b9c'
                pass 
                self.match(2972)


            elif alt12 == 130:
                # gleampython/gleam.g:561:9: '\\u0b9e' .. '\\u0b9f'
                pass 
                self.matchRange(2974, 2975)


            elif alt12 == 131:
                # gleampython/gleam.g:562:9: '\\u0ba3' .. '\\u0ba4'
                pass 
                self.matchRange(2979, 2980)


            elif alt12 == 132:
                # gleampython/gleam.g:563:9: '\\u0ba8' .. '\\u0baa'
                pass 
                self.matchRange(2984, 2986)


            elif alt12 == 133:
                # gleampython/gleam.g:564:9: '\\u0bae' .. '\\u0bb5'
                pass 
                self.matchRange(2990, 2997)


            elif alt12 == 134:
                # gleampython/gleam.g:565:9: '\\u0bb7' .. '\\u0bb9'
                pass 
                self.matchRange(2999, 3001)


            elif alt12 == 135:
                # gleampython/gleam.g:566:9: '\\u0bbe' .. '\\u0bc2'
                pass 
                self.matchRange(3006, 3010)


            elif alt12 == 136:
                # gleampython/gleam.g:567:9: '\\u0bc6' .. '\\u0bc8'
                pass 
                self.matchRange(3014, 3016)


            elif alt12 == 137:
                # gleampython/gleam.g:568:9: '\\u0bca' .. '\\u0bcd'
                pass 
                self.matchRange(3018, 3021)


            elif alt12 == 138:
                # gleampython/gleam.g:569:9: '\\u0bd7'
                pass 
                self.match(3031)


            elif alt12 == 139:
                # gleampython/gleam.g:570:9: '\\u0be7' .. '\\u0bef'
                pass 
                self.matchRange(3047, 3055)


            elif alt12 == 140:
                # gleampython/gleam.g:571:9: '\\u0bf9'
                pass 
                self.match(3065)


            elif alt12 == 141:
                # gleampython/gleam.g:572:9: '\\u0c01' .. '\\u0c03'
                pass 
                self.matchRange(3073, 3075)


            elif alt12 == 142:
                # gleampython/gleam.g:573:9: '\\u0c05' .. '\\u0c0c'
                pass 
                self.matchRange(3077, 3084)


            elif alt12 == 143:
                # gleampython/gleam.g:574:9: '\\u0c0e' .. '\\u0c10'
                pass 
                self.matchRange(3086, 3088)


            elif alt12 == 144:
                # gleampython/gleam.g:575:9: '\\u0c12' .. '\\u0c28'
                pass 
                self.matchRange(3090, 3112)


            elif alt12 == 145:
                # gleampython/gleam.g:576:9: '\\u0c2a' .. '\\u0c33'
                pass 
                self.matchRange(3114, 3123)


            elif alt12 == 146:
                # gleampython/gleam.g:577:9: '\\u0c35' .. '\\u0c39'
                pass 
                self.matchRange(3125, 3129)


            elif alt12 == 147:
                # gleampython/gleam.g:578:9: '\\u0c3e' .. '\\u0c44'
                pass 
                self.matchRange(3134, 3140)


            elif alt12 == 148:
                # gleampython/gleam.g:579:9: '\\u0c46' .. '\\u0c48'
                pass 
                self.matchRange(3142, 3144)


            elif alt12 == 149:
                # gleampython/gleam.g:580:9: '\\u0c4a' .. '\\u0c4d'
                pass 
                self.matchRange(3146, 3149)


            elif alt12 == 150:
                # gleampython/gleam.g:581:9: '\\u0c55' .. '\\u0c56'
                pass 
                self.matchRange(3157, 3158)


            elif alt12 == 151:
                # gleampython/gleam.g:582:9: '\\u0c60' .. '\\u0c61'
                pass 
                self.matchRange(3168, 3169)


            elif alt12 == 152:
                # gleampython/gleam.g:583:9: '\\u0c66' .. '\\u0c6f'
                pass 
                self.matchRange(3174, 3183)


            elif alt12 == 153:
                # gleampython/gleam.g:584:9: '\\u0c82' .. '\\u0c83'
                pass 
                self.matchRange(3202, 3203)


            elif alt12 == 154:
                # gleampython/gleam.g:585:9: '\\u0c85' .. '\\u0c8c'
                pass 
                self.matchRange(3205, 3212)


            elif alt12 == 155:
                # gleampython/gleam.g:586:9: '\\u0c8e' .. '\\u0c90'
                pass 
                self.matchRange(3214, 3216)


            elif alt12 == 156:
                # gleampython/gleam.g:587:9: '\\u0c92' .. '\\u0ca8'
                pass 
                self.matchRange(3218, 3240)


            elif alt12 == 157:
                # gleampython/gleam.g:588:9: '\\u0caa' .. '\\u0cb3'
                pass 
                self.matchRange(3242, 3251)


            elif alt12 == 158:
                # gleampython/gleam.g:589:9: '\\u0cb5' .. '\\u0cb9'
                pass 
                self.matchRange(3253, 3257)


            elif alt12 == 159:
                # gleampython/gleam.g:590:9: '\\u0cbc' .. '\\u0cc4'
                pass 
                self.matchRange(3260, 3268)


            elif alt12 == 160:
                # gleampython/gleam.g:591:9: '\\u0cc6' .. '\\u0cc8'
                pass 
                self.matchRange(3270, 3272)


            elif alt12 == 161:
                # gleampython/gleam.g:592:9: '\\u0cca' .. '\\u0ccd'
                pass 
                self.matchRange(3274, 3277)


            elif alt12 == 162:
                # gleampython/gleam.g:593:9: '\\u0cd5' .. '\\u0cd6'
                pass 
                self.matchRange(3285, 3286)


            elif alt12 == 163:
                # gleampython/gleam.g:594:9: '\\u0cde'
                pass 
                self.match(3294)


            elif alt12 == 164:
                # gleampython/gleam.g:595:9: '\\u0ce0' .. '\\u0ce1'
                pass 
                self.matchRange(3296, 3297)


            elif alt12 == 165:
                # gleampython/gleam.g:596:9: '\\u0ce6' .. '\\u0cef'
                pass 
                self.matchRange(3302, 3311)


            elif alt12 == 166:
                # gleampython/gleam.g:597:9: '\\u0d02' .. '\\u0d03'
                pass 
                self.matchRange(3330, 3331)


            elif alt12 == 167:
                # gleampython/gleam.g:598:9: '\\u0d05' .. '\\u0d0c'
                pass 
                self.matchRange(3333, 3340)


            elif alt12 == 168:
                # gleampython/gleam.g:599:9: '\\u0d0e' .. '\\u0d10'
                pass 
                self.matchRange(3342, 3344)


            elif alt12 == 169:
                # gleampython/gleam.g:600:9: '\\u0d12' .. '\\u0d28'
                pass 
                self.matchRange(3346, 3368)


            elif alt12 == 170:
                # gleampython/gleam.g:601:9: '\\u0d2a' .. '\\u0d39'
                pass 
                self.matchRange(3370, 3385)


            elif alt12 == 171:
                # gleampython/gleam.g:602:9: '\\u0d3e' .. '\\u0d43'
                pass 
                self.matchRange(3390, 3395)


            elif alt12 == 172:
                # gleampython/gleam.g:603:9: '\\u0d46' .. '\\u0d48'
                pass 
                self.matchRange(3398, 3400)


            elif alt12 == 173:
                # gleampython/gleam.g:604:9: '\\u0d4a' .. '\\u0d4d'
                pass 
                self.matchRange(3402, 3405)


            elif alt12 == 174:
                # gleampython/gleam.g:605:9: '\\u0d57'
                pass 
                self.match(3415)


            elif alt12 == 175:
                # gleampython/gleam.g:606:9: '\\u0d60' .. '\\u0d61'
                pass 
                self.matchRange(3424, 3425)


            elif alt12 == 176:
                # gleampython/gleam.g:607:9: '\\u0d66' .. '\\u0d6f'
                pass 
                self.matchRange(3430, 3439)


            elif alt12 == 177:
                # gleampython/gleam.g:608:9: '\\u0d82' .. '\\u0d83'
                pass 
                self.matchRange(3458, 3459)


            elif alt12 == 178:
                # gleampython/gleam.g:609:9: '\\u0d85' .. '\\u0d96'
                pass 
                self.matchRange(3461, 3478)


            elif alt12 == 179:
                # gleampython/gleam.g:610:9: '\\u0d9a' .. '\\u0db1'
                pass 
                self.matchRange(3482, 3505)


            elif alt12 == 180:
                # gleampython/gleam.g:611:9: '\\u0db3' .. '\\u0dbb'
                pass 
                self.matchRange(3507, 3515)


            elif alt12 == 181:
                # gleampython/gleam.g:612:9: '\\u0dbd'
                pass 
                self.match(3517)


            elif alt12 == 182:
                # gleampython/gleam.g:613:9: '\\u0dc0' .. '\\u0dc6'
                pass 
                self.matchRange(3520, 3526)


            elif alt12 == 183:
                # gleampython/gleam.g:614:9: '\\u0dca'
                pass 
                self.match(3530)


            elif alt12 == 184:
                # gleampython/gleam.g:615:9: '\\u0dcf' .. '\\u0dd4'
                pass 
                self.matchRange(3535, 3540)


            elif alt12 == 185:
                # gleampython/gleam.g:616:9: '\\u0dd6'
                pass 
                self.match(3542)


            elif alt12 == 186:
                # gleampython/gleam.g:617:9: '\\u0dd8' .. '\\u0ddf'
                pass 
                self.matchRange(3544, 3551)


            elif alt12 == 187:
                # gleampython/gleam.g:618:9: '\\u0df2' .. '\\u0df3'
                pass 
                self.matchRange(3570, 3571)


            elif alt12 == 188:
                # gleampython/gleam.g:619:9: '\\u0e01' .. '\\u0e3a'
                pass 
                self.matchRange(3585, 3642)


            elif alt12 == 189:
                # gleampython/gleam.g:620:9: '\\u0e3f' .. '\\u0e4e'
                pass 
                self.matchRange(3647, 3662)


            elif alt12 == 190:
                # gleampython/gleam.g:621:9: '\\u0e50' .. '\\u0e59'
                pass 
                self.matchRange(3664, 3673)


            elif alt12 == 191:
                # gleampython/gleam.g:622:9: '\\u0e81' .. '\\u0e82'
                pass 
                self.matchRange(3713, 3714)


            elif alt12 == 192:
                # gleampython/gleam.g:623:9: '\\u0e84'
                pass 
                self.match(3716)


            elif alt12 == 193:
                # gleampython/gleam.g:624:9: '\\u0e87' .. '\\u0e88'
                pass 
                self.matchRange(3719, 3720)


            elif alt12 == 194:
                # gleampython/gleam.g:625:9: '\\u0e8a'
                pass 
                self.match(3722)


            elif alt12 == 195:
                # gleampython/gleam.g:626:9: '\\u0e8d'
                pass 
                self.match(3725)


            elif alt12 == 196:
                # gleampython/gleam.g:627:9: '\\u0e94' .. '\\u0e97'
                pass 
                self.matchRange(3732, 3735)


            elif alt12 == 197:
                # gleampython/gleam.g:628:9: '\\u0e99' .. '\\u0e9f'
                pass 
                self.matchRange(3737, 3743)


            elif alt12 == 198:
                # gleampython/gleam.g:629:9: '\\u0ea1' .. '\\u0ea3'
                pass 
                self.matchRange(3745, 3747)


            elif alt12 == 199:
                # gleampython/gleam.g:630:9: '\\u0ea5'
                pass 
                self.match(3749)


            elif alt12 == 200:
                # gleampython/gleam.g:631:9: '\\u0ea7'
                pass 
                self.match(3751)


            elif alt12 == 201:
                # gleampython/gleam.g:632:9: '\\u0eaa' .. '\\u0eab'
                pass 
                self.matchRange(3754, 3755)


            elif alt12 == 202:
                # gleampython/gleam.g:633:9: '\\u0ead' .. '\\u0eb9'
                pass 
                self.matchRange(3757, 3769)


            elif alt12 == 203:
                # gleampython/gleam.g:634:9: '\\u0ebb' .. '\\u0ebd'
                pass 
                self.matchRange(3771, 3773)


            elif alt12 == 204:
                # gleampython/gleam.g:635:9: '\\u0ec0' .. '\\u0ec4'
                pass 
                self.matchRange(3776, 3780)


            elif alt12 == 205:
                # gleampython/gleam.g:636:9: '\\u0ec6'
                pass 
                self.match(3782)


            elif alt12 == 206:
                # gleampython/gleam.g:637:9: '\\u0ec8' .. '\\u0ecd'
                pass 
                self.matchRange(3784, 3789)


            elif alt12 == 207:
                # gleampython/gleam.g:638:9: '\\u0ed0' .. '\\u0ed9'
                pass 
                self.matchRange(3792, 3801)


            elif alt12 == 208:
                # gleampython/gleam.g:639:9: '\\u0edc' .. '\\u0edd'
                pass 
                self.matchRange(3804, 3805)


            elif alt12 == 209:
                # gleampython/gleam.g:640:9: '\\u0f00'
                pass 
                self.match(3840)


            elif alt12 == 210:
                # gleampython/gleam.g:641:9: '\\u0f18' .. '\\u0f19'
                pass 
                self.matchRange(3864, 3865)


            elif alt12 == 211:
                # gleampython/gleam.g:642:9: '\\u0f20' .. '\\u0f29'
                pass 
                self.matchRange(3872, 3881)


            elif alt12 == 212:
                # gleampython/gleam.g:643:9: '\\u0f35'
                pass 
                self.match(3893)


            elif alt12 == 213:
                # gleampython/gleam.g:644:9: '\\u0f37'
                pass 
                self.match(3895)


            elif alt12 == 214:
                # gleampython/gleam.g:645:9: '\\u0f39'
                pass 
                self.match(3897)


            elif alt12 == 215:
                # gleampython/gleam.g:646:9: '\\u0f3e' .. '\\u0f47'
                pass 
                self.matchRange(3902, 3911)


            elif alt12 == 216:
                # gleampython/gleam.g:647:9: '\\u0f49' .. '\\u0f6a'
                pass 
                self.matchRange(3913, 3946)


            elif alt12 == 217:
                # gleampython/gleam.g:648:9: '\\u0f71' .. '\\u0f84'
                pass 
                self.matchRange(3953, 3972)


            elif alt12 == 218:
                # gleampython/gleam.g:649:9: '\\u0f86' .. '\\u0f8b'
                pass 
                self.matchRange(3974, 3979)


            elif alt12 == 219:
                # gleampython/gleam.g:650:9: '\\u0f90' .. '\\u0f97'
                pass 
                self.matchRange(3984, 3991)


            elif alt12 == 220:
                # gleampython/gleam.g:651:9: '\\u0f99' .. '\\u0fbc'
                pass 
                self.matchRange(3993, 4028)


            elif alt12 == 221:
                # gleampython/gleam.g:652:9: '\\u0fc6'
                pass 
                self.match(4038)


            elif alt12 == 222:
                # gleampython/gleam.g:653:9: '\\u1000' .. '\\u1021'
                pass 
                self.matchRange(4096, 4129)


            elif alt12 == 223:
                # gleampython/gleam.g:654:9: '\\u1023' .. '\\u1027'
                pass 
                self.matchRange(4131, 4135)


            elif alt12 == 224:
                # gleampython/gleam.g:655:9: '\\u1029' .. '\\u102a'
                pass 
                self.matchRange(4137, 4138)


            elif alt12 == 225:
                # gleampython/gleam.g:656:9: '\\u102c' .. '\\u1032'
                pass 
                self.matchRange(4140, 4146)


            elif alt12 == 226:
                # gleampython/gleam.g:657:9: '\\u1036' .. '\\u1039'
                pass 
                self.matchRange(4150, 4153)


            elif alt12 == 227:
                # gleampython/gleam.g:658:9: '\\u1040' .. '\\u1049'
                pass 
                self.matchRange(4160, 4169)


            elif alt12 == 228:
                # gleampython/gleam.g:659:9: '\\u1050' .. '\\u1059'
                pass 
                self.matchRange(4176, 4185)


            elif alt12 == 229:
                # gleampython/gleam.g:660:9: '\\u10a0' .. '\\u10c5'
                pass 
                self.matchRange(4256, 4293)


            elif alt12 == 230:
                # gleampython/gleam.g:661:9: '\\u10d0' .. '\\u10f8'
                pass 
                self.matchRange(4304, 4344)


            elif alt12 == 231:
                # gleampython/gleam.g:662:9: '\\u1100' .. '\\u1159'
                pass 
                self.matchRange(4352, 4441)


            elif alt12 == 232:
                # gleampython/gleam.g:663:9: '\\u115f' .. '\\u11a2'
                pass 
                self.matchRange(4447, 4514)


            elif alt12 == 233:
                # gleampython/gleam.g:664:9: '\\u11a8' .. '\\u11f9'
                pass 
                self.matchRange(4520, 4601)


            elif alt12 == 234:
                # gleampython/gleam.g:665:9: '\\u1200' .. '\\u1206'
                pass 
                self.matchRange(4608, 4614)


            elif alt12 == 235:
                # gleampython/gleam.g:666:9: '\\u1208' .. '\\u1246'
                pass 
                self.matchRange(4616, 4678)


            elif alt12 == 236:
                # gleampython/gleam.g:667:9: '\\u1248'
                pass 
                self.match(4680)


            elif alt12 == 237:
                # gleampython/gleam.g:668:9: '\\u124a' .. '\\u124d'
                pass 
                self.matchRange(4682, 4685)


            elif alt12 == 238:
                # gleampython/gleam.g:669:9: '\\u1250' .. '\\u1256'
                pass 
                self.matchRange(4688, 4694)


            elif alt12 == 239:
                # gleampython/gleam.g:670:9: '\\u1258'
                pass 
                self.match(4696)


            elif alt12 == 240:
                # gleampython/gleam.g:671:9: '\\u125a' .. '\\u125d'
                pass 
                self.matchRange(4698, 4701)


            elif alt12 == 241:
                # gleampython/gleam.g:672:9: '\\u1260' .. '\\u1286'
                pass 
                self.matchRange(4704, 4742)


            elif alt12 == 242:
                # gleampython/gleam.g:673:9: '\\u1288'
                pass 
                self.match(4744)


            elif alt12 == 243:
                # gleampython/gleam.g:674:9: '\\u128a' .. '\\u128d'
                pass 
                self.matchRange(4746, 4749)


            elif alt12 == 244:
                # gleampython/gleam.g:675:9: '\\u1290' .. '\\u12ae'
                pass 
                self.matchRange(4752, 4782)


            elif alt12 == 245:
                # gleampython/gleam.g:676:9: '\\u12b0'
                pass 
                self.match(4784)


            elif alt12 == 246:
                # gleampython/gleam.g:677:9: '\\u12b2' .. '\\u12b5'
                pass 
                self.matchRange(4786, 4789)


            elif alt12 == 247:
                # gleampython/gleam.g:678:9: '\\u12b8' .. '\\u12be'
                pass 
                self.matchRange(4792, 4798)


            elif alt12 == 248:
                # gleampython/gleam.g:679:9: '\\u12c0'
                pass 
                self.match(4800)


            elif alt12 == 249:
                # gleampython/gleam.g:680:9: '\\u12c2' .. '\\u12c5'
                pass 
                self.matchRange(4802, 4805)


            elif alt12 == 250:
                # gleampython/gleam.g:681:9: '\\u12c8' .. '\\u12ce'
                pass 
                self.matchRange(4808, 4814)


            elif alt12 == 251:
                # gleampython/gleam.g:682:9: '\\u12d0' .. '\\u12d6'
                pass 
                self.matchRange(4816, 4822)


            elif alt12 == 252:
                # gleampython/gleam.g:683:9: '\\u12d8' .. '\\u12ee'
                pass 
                self.matchRange(4824, 4846)


            elif alt12 == 253:
                # gleampython/gleam.g:684:9: '\\u12f0' .. '\\u130e'
                pass 
                self.matchRange(4848, 4878)


            elif alt12 == 254:
                # gleampython/gleam.g:685:9: '\\u1310'
                pass 
                self.match(4880)


            elif alt12 == 255:
                # gleampython/gleam.g:686:9: '\\u1312' .. '\\u1315'
                pass 
                self.matchRange(4882, 4885)


            elif alt12 == 256:
                # gleampython/gleam.g:687:9: '\\u1318' .. '\\u131e'
                pass 
                self.matchRange(4888, 4894)


            elif alt12 == 257:
                # gleampython/gleam.g:688:9: '\\u1320' .. '\\u1346'
                pass 
                self.matchRange(4896, 4934)


            elif alt12 == 258:
                # gleampython/gleam.g:689:9: '\\u1348' .. '\\u135a'
                pass 
                self.matchRange(4936, 4954)


            elif alt12 == 259:
                # gleampython/gleam.g:690:9: '\\u1369' .. '\\u1371'
                pass 
                self.matchRange(4969, 4977)


            elif alt12 == 260:
                # gleampython/gleam.g:691:9: '\\u13a0' .. '\\u13f4'
                pass 
                self.matchRange(5024, 5108)


            elif alt12 == 261:
                # gleampython/gleam.g:692:9: '\\u1401' .. '\\u166c'
                pass 
                self.matchRange(5121, 5740)


            elif alt12 == 262:
                # gleampython/gleam.g:693:9: '\\u166f' .. '\\u1676'
                pass 
                self.matchRange(5743, 5750)


            elif alt12 == 263:
                # gleampython/gleam.g:694:9: '\\u1681' .. '\\u169a'
                pass 
                self.matchRange(5761, 5786)


            elif alt12 == 264:
                # gleampython/gleam.g:695:9: '\\u16a0' .. '\\u16ea'
                pass 
                self.matchRange(5792, 5866)


            elif alt12 == 265:
                # gleampython/gleam.g:696:9: '\\u16ee' .. '\\u16f0'
                pass 
                self.matchRange(5870, 5872)


            elif alt12 == 266:
                # gleampython/gleam.g:697:9: '\\u1700' .. '\\u170c'
                pass 
                self.matchRange(5888, 5900)


            elif alt12 == 267:
                # gleampython/gleam.g:698:9: '\\u170e' .. '\\u1714'
                pass 
                self.matchRange(5902, 5908)


            elif alt12 == 268:
                # gleampython/gleam.g:699:9: '\\u1720' .. '\\u1734'
                pass 
                self.matchRange(5920, 5940)


            elif alt12 == 269:
                # gleampython/gleam.g:700:9: '\\u1740' .. '\\u1753'
                pass 
                self.matchRange(5952, 5971)


            elif alt12 == 270:
                # gleampython/gleam.g:701:9: '\\u1760' .. '\\u176c'
                pass 
                self.matchRange(5984, 5996)


            elif alt12 == 271:
                # gleampython/gleam.g:702:9: '\\u176e' .. '\\u1770'
                pass 
                self.matchRange(5998, 6000)


            elif alt12 == 272:
                # gleampython/gleam.g:703:9: '\\u1772' .. '\\u1773'
                pass 
                self.matchRange(6002, 6003)


            elif alt12 == 273:
                # gleampython/gleam.g:704:9: '\\u1780' .. '\\u17d3'
                pass 
                self.matchRange(6016, 6099)


            elif alt12 == 274:
                # gleampython/gleam.g:705:9: '\\u17d7'
                pass 
                self.match(6103)


            elif alt12 == 275:
                # gleampython/gleam.g:706:9: '\\u17db' .. '\\u17dd'
                pass 
                self.matchRange(6107, 6109)


            elif alt12 == 276:
                # gleampython/gleam.g:707:9: '\\u17e0' .. '\\u17e9'
                pass 
                self.matchRange(6112, 6121)


            elif alt12 == 277:
                # gleampython/gleam.g:708:9: '\\u180b' .. '\\u180d'
                pass 
                self.matchRange(6155, 6157)


            elif alt12 == 278:
                # gleampython/gleam.g:709:9: '\\u1810' .. '\\u1819'
                pass 
                self.matchRange(6160, 6169)


            elif alt12 == 279:
                # gleampython/gleam.g:710:9: '\\u1820' .. '\\u1877'
                pass 
                self.matchRange(6176, 6263)


            elif alt12 == 280:
                # gleampython/gleam.g:711:9: '\\u1880' .. '\\u18a9'
                pass 
                self.matchRange(6272, 6313)


            elif alt12 == 281:
                # gleampython/gleam.g:712:9: '\\u1900' .. '\\u191c'
                pass 
                self.matchRange(6400, 6428)


            elif alt12 == 282:
                # gleampython/gleam.g:713:9: '\\u1920' .. '\\u192b'
                pass 
                self.matchRange(6432, 6443)


            elif alt12 == 283:
                # gleampython/gleam.g:714:9: '\\u1930' .. '\\u193b'
                pass 
                self.matchRange(6448, 6459)


            elif alt12 == 284:
                # gleampython/gleam.g:715:9: '\\u1946' .. '\\u196d'
                pass 
                self.matchRange(6470, 6509)


            elif alt12 == 285:
                # gleampython/gleam.g:716:9: '\\u1970' .. '\\u1974'
                pass 
                self.matchRange(6512, 6516)


            elif alt12 == 286:
                # gleampython/gleam.g:717:9: '\\u1d00' .. '\\u1d6b'
                pass 
                self.matchRange(7424, 7531)


            elif alt12 == 287:
                # gleampython/gleam.g:718:9: '\\u1e00' .. '\\u1e9b'
                pass 
                self.matchRange(7680, 7835)


            elif alt12 == 288:
                # gleampython/gleam.g:719:9: '\\u1ea0' .. '\\u1ef9'
                pass 
                self.matchRange(7840, 7929)


            elif alt12 == 289:
                # gleampython/gleam.g:720:9: '\\u1f00' .. '\\u1f15'
                pass 
                self.matchRange(7936, 7957)


            elif alt12 == 290:
                # gleampython/gleam.g:721:9: '\\u1f18' .. '\\u1f1d'
                pass 
                self.matchRange(7960, 7965)


            elif alt12 == 291:
                # gleampython/gleam.g:722:9: '\\u1f20' .. '\\u1f45'
                pass 
                self.matchRange(7968, 8005)


            elif alt12 == 292:
                # gleampython/gleam.g:723:9: '\\u1f48' .. '\\u1f4d'
                pass 
                self.matchRange(8008, 8013)


            elif alt12 == 293:
                # gleampython/gleam.g:724:9: '\\u1f50' .. '\\u1f57'
                pass 
                self.matchRange(8016, 8023)


            elif alt12 == 294:
                # gleampython/gleam.g:725:9: '\\u1f59'
                pass 
                self.match(8025)


            elif alt12 == 295:
                # gleampython/gleam.g:726:9: '\\u1f5b'
                pass 
                self.match(8027)


            elif alt12 == 296:
                # gleampython/gleam.g:727:9: '\\u1f5d'
                pass 
                self.match(8029)


            elif alt12 == 297:
                # gleampython/gleam.g:728:9: '\\u1f5f' .. '\\u1f7d'
                pass 
                self.matchRange(8031, 8061)


            elif alt12 == 298:
                # gleampython/gleam.g:729:9: '\\u1f80' .. '\\u1fb4'
                pass 
                self.matchRange(8064, 8116)


            elif alt12 == 299:
                # gleampython/gleam.g:730:9: '\\u1fb6' .. '\\u1fbc'
                pass 
                self.matchRange(8118, 8124)


            elif alt12 == 300:
                # gleampython/gleam.g:731:9: '\\u1fbe'
                pass 
                self.match(8126)


            elif alt12 == 301:
                # gleampython/gleam.g:732:9: '\\u1fc2' .. '\\u1fc4'
                pass 
                self.matchRange(8130, 8132)


            elif alt12 == 302:
                # gleampython/gleam.g:733:9: '\\u1fc6' .. '\\u1fcc'
                pass 
                self.matchRange(8134, 8140)


            elif alt12 == 303:
                # gleampython/gleam.g:734:9: '\\u1fd0' .. '\\u1fd3'
                pass 
                self.matchRange(8144, 8147)


            elif alt12 == 304:
                # gleampython/gleam.g:735:9: '\\u1fd6' .. '\\u1fdb'
                pass 
                self.matchRange(8150, 8155)


            elif alt12 == 305:
                # gleampython/gleam.g:736:9: '\\u1fe0' .. '\\u1fec'
                pass 
                self.matchRange(8160, 8172)


            elif alt12 == 306:
                # gleampython/gleam.g:737:9: '\\u1ff2' .. '\\u1ff4'
                pass 
                self.matchRange(8178, 8180)


            elif alt12 == 307:
                # gleampython/gleam.g:738:9: '\\u1ff6' .. '\\u1ffc'
                pass 
                self.matchRange(8182, 8188)


            elif alt12 == 308:
                # gleampython/gleam.g:739:9: '\\u200c' .. '\\u200f'
                pass 
                self.matchRange(8204, 8207)


            elif alt12 == 309:
                # gleampython/gleam.g:740:9: '\\u202a' .. '\\u202e'
                pass 
                self.matchRange(8234, 8238)


            elif alt12 == 310:
                # gleampython/gleam.g:741:9: '\\u203f' .. '\\u2040'
                pass 
                self.matchRange(8255, 8256)


            elif alt12 == 311:
                # gleampython/gleam.g:742:9: '\\u2054'
                pass 
                self.match(8276)


            elif alt12 == 312:
                # gleampython/gleam.g:743:9: '\\u2060' .. '\\u2063'
                pass 
                self.matchRange(8288, 8291)


            elif alt12 == 313:
                # gleampython/gleam.g:744:9: '\\u206a' .. '\\u206f'
                pass 
                self.matchRange(8298, 8303)


            elif alt12 == 314:
                # gleampython/gleam.g:745:9: '\\u2071'
                pass 
                self.match(8305)


            elif alt12 == 315:
                # gleampython/gleam.g:746:9: '\\u207f'
                pass 
                self.match(8319)


            elif alt12 == 316:
                # gleampython/gleam.g:747:9: '\\u20a0' .. '\\u20b1'
                pass 
                self.matchRange(8352, 8369)


            elif alt12 == 317:
                # gleampython/gleam.g:748:9: '\\u20d0' .. '\\u20dc'
                pass 
                self.matchRange(8400, 8412)


            elif alt12 == 318:
                # gleampython/gleam.g:749:9: '\\u20e1'
                pass 
                self.match(8417)


            elif alt12 == 319:
                # gleampython/gleam.g:750:9: '\\u20e5' .. '\\u20ea'
                pass 
                self.matchRange(8421, 8426)


            elif alt12 == 320:
                # gleampython/gleam.g:751:9: '\\u2102'
                pass 
                self.match(8450)


            elif alt12 == 321:
                # gleampython/gleam.g:752:9: '\\u2107'
                pass 
                self.match(8455)


            elif alt12 == 322:
                # gleampython/gleam.g:753:9: '\\u210a' .. '\\u2113'
                pass 
                self.matchRange(8458, 8467)


            elif alt12 == 323:
                # gleampython/gleam.g:754:9: '\\u2115'
                pass 
                self.match(8469)


            elif alt12 == 324:
                # gleampython/gleam.g:755:9: '\\u2119' .. '\\u211d'
                pass 
                self.matchRange(8473, 8477)


            elif alt12 == 325:
                # gleampython/gleam.g:756:9: '\\u2124'
                pass 
                self.match(8484)


            elif alt12 == 326:
                # gleampython/gleam.g:757:9: '\\u2126'
                pass 
                self.match(8486)


            elif alt12 == 327:
                # gleampython/gleam.g:758:9: '\\u2128'
                pass 
                self.match(8488)


            elif alt12 == 328:
                # gleampython/gleam.g:759:9: '\\u212a' .. '\\u212d'
                pass 
                self.matchRange(8490, 8493)


            elif alt12 == 329:
                # gleampython/gleam.g:760:9: '\\u212f' .. '\\u2131'
                pass 
                self.matchRange(8495, 8497)


            elif alt12 == 330:
                # gleampython/gleam.g:761:9: '\\u2133' .. '\\u2139'
                pass 
                self.matchRange(8499, 8505)


            elif alt12 == 331:
                # gleampython/gleam.g:762:9: '\\u213d' .. '\\u213f'
                pass 
                self.matchRange(8509, 8511)


            elif alt12 == 332:
                # gleampython/gleam.g:763:9: '\\u2145' .. '\\u2149'
                pass 
                self.matchRange(8517, 8521)


            elif alt12 == 333:
                # gleampython/gleam.g:764:9: '\\u2160' .. '\\u2183'
                pass 
                self.matchRange(8544, 8579)


            elif alt12 == 334:
                # gleampython/gleam.g:765:9: '\\u3005' .. '\\u3007'
                pass 
                self.matchRange(12293, 12295)


            elif alt12 == 335:
                # gleampython/gleam.g:766:9: '\\u3021' .. '\\u302f'
                pass 
                self.matchRange(12321, 12335)


            elif alt12 == 336:
                # gleampython/gleam.g:767:9: '\\u3031' .. '\\u3035'
                pass 
                self.matchRange(12337, 12341)


            elif alt12 == 337:
                # gleampython/gleam.g:768:9: '\\u3038' .. '\\u303c'
                pass 
                self.matchRange(12344, 12348)


            elif alt12 == 338:
                # gleampython/gleam.g:769:9: '\\u3041' .. '\\u3096'
                pass 
                self.matchRange(12353, 12438)


            elif alt12 == 339:
                # gleampython/gleam.g:770:9: '\\u3099' .. '\\u309a'
                pass 
                self.matchRange(12441, 12442)


            elif alt12 == 340:
                # gleampython/gleam.g:771:9: '\\u309d' .. '\\u309f'
                pass 
                self.matchRange(12445, 12447)


            elif alt12 == 341:
                # gleampython/gleam.g:772:9: '\\u30a1' .. '\\u30ff'
                pass 
                self.matchRange(12449, 12543)


            elif alt12 == 342:
                # gleampython/gleam.g:773:9: '\\u3105' .. '\\u312c'
                pass 
                self.matchRange(12549, 12588)


            elif alt12 == 343:
                # gleampython/gleam.g:774:9: '\\u3131' .. '\\u318e'
                pass 
                self.matchRange(12593, 12686)


            elif alt12 == 344:
                # gleampython/gleam.g:775:9: '\\u31a0' .. '\\u31b7'
                pass 
                self.matchRange(12704, 12727)


            elif alt12 == 345:
                # gleampython/gleam.g:776:9: '\\u31f0' .. '\\u31ff'
                pass 
                self.matchRange(12784, 12799)


            elif alt12 == 346:
                # gleampython/gleam.g:777:9: '\\u3400' .. '\\u4db5'
                pass 
                self.matchRange(13312, 19893)


            elif alt12 == 347:
                # gleampython/gleam.g:778:9: '\\u4e00' .. '\\u9fa5'
                pass 
                self.matchRange(19968, 40869)


            elif alt12 == 348:
                # gleampython/gleam.g:779:9: '\\ua000' .. '\\ua48c'
                pass 
                self.matchRange(40960, 42124)


            elif alt12 == 349:
                # gleampython/gleam.g:780:9: '\\uac00' .. '\\ud7a3'
                pass 
                self.matchRange(44032, 55203)


            elif alt12 == 350:
                # gleampython/gleam.g:781:9: '\\uf900' .. '\\ufa2d'
                pass 
                self.matchRange(63744, 64045)


            elif alt12 == 351:
                # gleampython/gleam.g:782:9: '\\ufa30' .. '\\ufa6a'
                pass 
                self.matchRange(64048, 64106)


            elif alt12 == 352:
                # gleampython/gleam.g:783:9: '\\ufb00' .. '\\ufb06'
                pass 
                self.matchRange(64256, 64262)


            elif alt12 == 353:
                # gleampython/gleam.g:784:9: '\\ufb13' .. '\\ufb17'
                pass 
                self.matchRange(64275, 64279)


            elif alt12 == 354:
                # gleampython/gleam.g:785:9: '\\ufb1d' .. '\\ufb28'
                pass 
                self.matchRange(64285, 64296)


            elif alt12 == 355:
                # gleampython/gleam.g:786:9: '\\ufb2a' .. '\\ufb36'
                pass 
                self.matchRange(64298, 64310)


            elif alt12 == 356:
                # gleampython/gleam.g:787:9: '\\ufb38' .. '\\ufb3c'
                pass 
                self.matchRange(64312, 64316)


            elif alt12 == 357:
                # gleampython/gleam.g:788:9: '\\ufb3e'
                pass 
                self.match(64318)


            elif alt12 == 358:
                # gleampython/gleam.g:789:9: '\\ufb40' .. '\\ufb41'
                pass 
                self.matchRange(64320, 64321)


            elif alt12 == 359:
                # gleampython/gleam.g:790:9: '\\ufb43' .. '\\ufb44'
                pass 
                self.matchRange(64323, 64324)


            elif alt12 == 360:
                # gleampython/gleam.g:791:9: '\\ufb46' .. '\\ufbb1'
                pass 
                self.matchRange(64326, 64433)


            elif alt12 == 361:
                # gleampython/gleam.g:792:9: '\\ufbd3' .. '\\ufd3d'
                pass 
                self.matchRange(64467, 64829)


            elif alt12 == 362:
                # gleampython/gleam.g:793:9: '\\ufd50' .. '\\ufd8f'
                pass 
                self.matchRange(64848, 64911)


            elif alt12 == 363:
                # gleampython/gleam.g:794:9: '\\ufd92' .. '\\ufdc7'
                pass 
                self.matchRange(64914, 64967)


            elif alt12 == 364:
                # gleampython/gleam.g:795:9: '\\ufdf0' .. '\\ufdfc'
                pass 
                self.matchRange(65008, 65020)


            elif alt12 == 365:
                # gleampython/gleam.g:796:9: '\\ufe00' .. '\\ufe0f'
                pass 
                self.matchRange(65024, 65039)


            elif alt12 == 366:
                # gleampython/gleam.g:797:9: '\\ufe20' .. '\\ufe23'
                pass 
                self.matchRange(65056, 65059)


            elif alt12 == 367:
                # gleampython/gleam.g:798:9: '\\ufe33' .. '\\ufe34'
                pass 
                self.matchRange(65075, 65076)


            elif alt12 == 368:
                # gleampython/gleam.g:799:9: '\\ufe4d' .. '\\ufe4f'
                pass 
                self.matchRange(65101, 65103)


            elif alt12 == 369:
                # gleampython/gleam.g:800:9: '\\ufe69'
                pass 
                self.match(65129)


            elif alt12 == 370:
                # gleampython/gleam.g:801:9: '\\ufe70' .. '\\ufe74'
                pass 
                self.matchRange(65136, 65140)


            elif alt12 == 371:
                # gleampython/gleam.g:802:9: '\\ufe76' .. '\\ufefc'
                pass 
                self.matchRange(65142, 65276)


            elif alt12 == 372:
                # gleampython/gleam.g:803:9: '\\ufeff'
                pass 
                self.match(65279)


            elif alt12 == 373:
                # gleampython/gleam.g:804:9: '\\uff04'
                pass 
                self.match(65284)


            elif alt12 == 374:
                # gleampython/gleam.g:805:9: '\\uff10' .. '\\uff19'
                pass 
                self.matchRange(65296, 65305)


            elif alt12 == 375:
                # gleampython/gleam.g:806:9: '\\uff21' .. '\\uff3a'
                pass 
                self.matchRange(65313, 65338)


            elif alt12 == 376:
                # gleampython/gleam.g:807:9: '\\uff3f'
                pass 
                self.match(65343)


            elif alt12 == 377:
                # gleampython/gleam.g:808:9: '\\uff41' .. '\\uff5a'
                pass 
                self.matchRange(65345, 65370)


            elif alt12 == 378:
                # gleampython/gleam.g:809:9: '\\uff65' .. '\\uffbe'
                pass 
                self.matchRange(65381, 65470)


            elif alt12 == 379:
                # gleampython/gleam.g:810:9: '\\uffc2' .. '\\uffc7'
                pass 
                self.matchRange(65474, 65479)


            elif alt12 == 380:
                # gleampython/gleam.g:811:9: '\\uffca' .. '\\uffcf'
                pass 
                self.matchRange(65482, 65487)


            elif alt12 == 381:
                # gleampython/gleam.g:812:9: '\\uffd2' .. '\\uffd7'
                pass 
                self.matchRange(65490, 65495)


            elif alt12 == 382:
                # gleampython/gleam.g:813:9: '\\uffda' .. '\\uffdc'
                pass 
                self.matchRange(65498, 65500)


            elif alt12 == 383:
                # gleampython/gleam.g:814:9: '\\uffe0' .. '\\uffe1'
                pass 
                self.matchRange(65504, 65505)


            elif alt12 == 384:
                # gleampython/gleam.g:815:9: '\\uffe5' .. '\\uffe6'
                pass 
                self.matchRange(65509, 65510)


            elif alt12 == 385:
                # gleampython/gleam.g:816:9: '\\ufff9' .. '\\ufffb'
                pass 
                self.matchRange(65529, 65531)


            elif alt12 == 386:
                # gleampython/gleam.g:817:9: ( '\\ud800' .. '\\udbff' ) ( '\\udc00' .. '\\udfff' )
                pass 
                # gleampython/gleam.g:817:9: ( '\\ud800' .. '\\udbff' )
                # gleampython/gleam.g:817:10: '\\ud800' .. '\\udbff'
                pass 
                self.matchRange(55296, 56319)



                # gleampython/gleam.g:817:30: ( '\\udc00' .. '\\udfff' )
                # gleampython/gleam.g:817:31: '\\udc00' .. '\\udfff'
                pass 
                self.matchRange(56320, 57343)






        finally:

            pass

    # $ANTLR end "IdentifierPart"



    def mTokens(self):
        # gleampython/gleam.g:1:8: ( PLUS | MINUS | MULT | DIV | T__34 | MACRO | FOR | IN | NODE | LBRACE | RBRACE | LPAREN | RPAREN | EQUALS | NUMBER | STRINGLITERAL | WHITESPACE | COMMENT | LINE_COMMENT | IDENTIFIER )
        alt13 = 20
        alt13 = self.dfa13.predict(self.input)
        if alt13 == 1:
            # gleampython/gleam.g:1:10: PLUS
            pass 
            self.mPLUS()


        elif alt13 == 2:
            # gleampython/gleam.g:1:15: MINUS
            pass 
            self.mMINUS()


        elif alt13 == 3:
            # gleampython/gleam.g:1:21: MULT
            pass 
            self.mMULT()


        elif alt13 == 4:
            # gleampython/gleam.g:1:26: DIV
            pass 
            self.mDIV()


        elif alt13 == 5:
            # gleampython/gleam.g:1:30: T__34
            pass 
            self.mT__34()


        elif alt13 == 6:
            # gleampython/gleam.g:1:36: MACRO
            pass 
            self.mMACRO()


        elif alt13 == 7:
            # gleampython/gleam.g:1:42: FOR
            pass 
            self.mFOR()


        elif alt13 == 8:
            # gleampython/gleam.g:1:46: IN
            pass 
            self.mIN()


        elif alt13 == 9:
            # gleampython/gleam.g:1:49: NODE
            pass 
            self.mNODE()


        elif alt13 == 10:
            # gleampython/gleam.g:1:54: LBRACE
            pass 
            self.mLBRACE()


        elif alt13 == 11:
            # gleampython/gleam.g:1:61: RBRACE
            pass 
            self.mRBRACE()


        elif alt13 == 12:
            # gleampython/gleam.g:1:68: LPAREN
            pass 
            self.mLPAREN()


        elif alt13 == 13:
            # gleampython/gleam.g:1:75: RPAREN
            pass 
            self.mRPAREN()


        elif alt13 == 14:
            # gleampython/gleam.g:1:82: EQUALS
            pass 
            self.mEQUALS()


        elif alt13 == 15:
            # gleampython/gleam.g:1:89: NUMBER
            pass 
            self.mNUMBER()


        elif alt13 == 16:
            # gleampython/gleam.g:1:96: STRINGLITERAL
            pass 
            self.mSTRINGLITERAL()


        elif alt13 == 17:
            # gleampython/gleam.g:1:110: WHITESPACE
            pass 
            self.mWHITESPACE()


        elif alt13 == 18:
            # gleampython/gleam.g:1:121: COMMENT
            pass 
            self.mCOMMENT()


        elif alt13 == 19:
            # gleampython/gleam.g:1:129: LINE_COMMENT
            pass 
            self.mLINE_COMMENT()


        elif alt13 == 20:
            # gleampython/gleam.g:1:142: IDENTIFIER
            pass 
            self.mIDENTIFIER()







    # lookup tables for DFA #9

    DFA9_eot = DFA.unpack(
        u"\2\uffff\2\4\2\uffff"
        )

    DFA9_eof = DFA.unpack(
        u"\6\uffff"
        )

    DFA9_min = DFA.unpack(
        u"\2\57\2\0\2\uffff"
        )

    DFA9_max = DFA.unpack(
        u"\2\57\2\uffff\2\uffff"
        )

    DFA9_accept = DFA.unpack(
        u"\4\uffff\1\2\1\1"
        )

    DFA9_special = DFA.unpack(
        u"\2\uffff\1\0\1\1\2\uffff"
        )

            
    DFA9_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\2"),
        DFA.unpack(u"\12\3\1\5\2\3\1\5\ufff2\3"),
        DFA.unpack(u"\12\3\1\5\2\3\1\5\ufff2\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #9

    class DFA9(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA9_2 = input.LA(1)

                s = -1
                if ((0 <= LA9_2 <= 9) or (11 <= LA9_2 <= 12) or (14 <= LA9_2 <= 65535)):
                    s = 3

                elif (LA9_2 == 10 or LA9_2 == 13):
                    s = 5

                else:
                    s = 4

                if s >= 0:
                    return s
            elif s == 1: 
                LA9_3 = input.LA(1)

                s = -1
                if (LA9_3 == 10 or LA9_3 == 13):
                    s = 5

                elif ((0 <= LA9_3 <= 9) or (11 <= LA9_3 <= 12) or (14 <= LA9_3 <= 65535)):
                    s = 3

                else:
                    s = 4

                if s >= 0:
                    return s

            nvae = NoViableAltException(self_.getDescription(), 9, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #13

    DFA13_eot = DFA.unpack(
        u"\4\uffff\1\25\1\uffff\4\22\14\uffff\2\22\1\34\2\22\1\37\1\uffff"
        u"\2\22\1\uffff\1\42\1\43\2\uffff"
        )

    DFA13_eof = DFA.unpack(
        u"\44\uffff"
        )

    DFA13_min = DFA.unpack(
        u"\1\11\3\uffff\1\52\1\uffff\1\141\1\157\1\156\1\157\14\uffff\1\143"
        u"\1\162\1\0\1\144\1\162\1\0\1\uffff\1\145\1\157\1\uffff\2\0\2\uffff"
        )

    DFA13_max = DFA.unpack(
        u"\1\uffe6\3\uffff\1\57\1\uffff\1\141\1\157\1\156\1\157\14\uffff"
        u"\1\143\1\162\1\ufffb\1\144\1\162\1\ufffb\1\uffff\1\145\1\157\1"
        u"\uffff\2\ufffb\2\uffff"
        )

    DFA13_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\1\uffff\1\5\4\uffff\1\12\1\13\1\14\1\15\1"
        u"\16\1\17\1\20\1\21\1\24\1\22\1\23\1\4\6\uffff\1\10\2\uffff\1\7"
        u"\2\uffff\1\11\1\6"
        )

    DFA13_special = DFA.unpack(
        u"\44\uffff"
        )

            
    DFA13_transition = [
        DFA.unpack(u"\2\21\1\uffff\2\21\22\uffff\1\21\1\uffff\1\20\1\uffff"
        u"\1\22\3\uffff\1\14\1\15\1\3\1\1\1\5\1\2\1\uffff\1\4\12\17\3\uffff"
        u"\1\16\3\uffff\32\22\4\uffff\1\22\1\uffff\5\22\1\7\2\22\1\10\3\22"
        u"\1\6\1\11\14\22\1\12\1\uffff\1\13\44\uffff\4\22\4\uffff\1\22\12"
        u"\uffff\1\22\4\uffff\1\22\5\uffff\27\22\1\uffff\37\22\1\uffff\u013f"
        u"\22\31\uffff\162\22\4\uffff\14\22\16\uffff\5\22\11\uffff\1\22\u008b"
        u"\uffff\1\22\13\uffff\1\22\1\uffff\3\22\1\uffff\1\22\1\uffff\24"
        u"\22\1\uffff\54\22\1\uffff\46\22\1\uffff\5\22\4\uffff\u0082\22\10"
        u"\uffff\105\22\1\uffff\46\22\2\uffff\2\22\6\uffff\20\22\41\uffff"
        u"\46\22\2\uffff\1\22\7\uffff\47\22\110\uffff\33\22\5\uffff\3\22"
        u"\56\uffff\32\22\5\uffff\13\22\43\uffff\2\22\1\uffff\143\22\1\uffff"
        u"\1\22\17\uffff\2\22\7\uffff\2\22\12\uffff\3\22\2\uffff\1\22\20"
        u"\uffff\1\22\1\uffff\36\22\35\uffff\3\22\60\uffff\46\22\13\uffff"
        u"\1\22\u0152\uffff\66\22\3\uffff\1\22\22\uffff\1\22\7\uffff\12\22"
        u"\43\uffff\10\22\2\uffff\2\22\2\uffff\26\22\1\uffff\7\22\1\uffff"
        u"\1\22\3\uffff\4\22\3\uffff\1\22\36\uffff\2\22\1\uffff\3\22\16\uffff"
        u"\4\22\21\uffff\6\22\4\uffff\2\22\2\uffff\26\22\1\uffff\7\22\1\uffff"
        u"\2\22\1\uffff\2\22\1\uffff\2\22\37\uffff\4\22\1\uffff\1\22\23\uffff"
        u"\3\22\20\uffff\11\22\1\uffff\3\22\1\uffff\26\22\1\uffff\7\22\1"
        u"\uffff\2\22\1\uffff\5\22\3\uffff\1\22\22\uffff\1\22\17\uffff\2"
        u"\22\17\uffff\1\22\23\uffff\10\22\2\uffff\2\22\2\uffff\26\22\1\uffff"
        u"\7\22\1\uffff\2\22\1\uffff\5\22\3\uffff\1\22\36\uffff\2\22\1\uffff"
        u"\3\22\17\uffff\1\22\21\uffff\1\22\1\uffff\6\22\3\uffff\3\22\1\uffff"
        u"\4\22\3\uffff\2\22\1\uffff\1\22\1\uffff\2\22\3\uffff\2\22\3\uffff"
        u"\3\22\3\uffff\10\22\1\uffff\3\22\77\uffff\1\22\13\uffff\10\22\1"
        u"\uffff\3\22\1\uffff\27\22\1\uffff\12\22\1\uffff\5\22\46\uffff\2"
        u"\22\43\uffff\10\22\1\uffff\3\22\1\uffff\27\22\1\uffff\12\22\1\uffff"
        u"\5\22\3\uffff\1\22\40\uffff\1\22\1\uffff\2\22\43\uffff\10\22\1"
        u"\uffff\3\22\1\uffff\27\22\1\uffff\20\22\46\uffff\2\22\43\uffff"
        u"\22\22\3\uffff\30\22\1\uffff\11\22\1\uffff\1\22\2\uffff\7\22\72"
        u"\uffff\60\22\1\uffff\2\22\13\uffff\10\22\72\uffff\2\22\1\uffff"
        u"\1\22\2\uffff\2\22\1\uffff\1\22\2\uffff\1\22\6\uffff\4\22\1\uffff"
        u"\7\22\1\uffff\3\22\1\uffff\1\22\1\uffff\1\22\2\uffff\2\22\1\uffff"
        u"\4\22\1\uffff\2\22\11\uffff\1\22\2\uffff\5\22\1\uffff\1\22\25\uffff"
        u"\2\22\42\uffff\1\22\77\uffff\10\22\1\uffff\42\22\35\uffff\4\22"
        u"\164\uffff\42\22\1\uffff\5\22\1\uffff\2\22\45\uffff\6\22\112\uffff"
        u"\46\22\12\uffff\51\22\7\uffff\132\22\5\uffff\104\22\5\uffff\122"
        u"\22\6\uffff\7\22\1\uffff\77\22\1\uffff\1\22\1\uffff\4\22\2\uffff"
        u"\7\22\1\uffff\1\22\1\uffff\4\22\2\uffff\47\22\1\uffff\1\22\1\uffff"
        u"\4\22\2\uffff\37\22\1\uffff\1\22\1\uffff\4\22\2\uffff\7\22\1\uffff"
        u"\1\22\1\uffff\4\22\2\uffff\7\22\1\uffff\7\22\1\uffff\27\22\1\uffff"
        u"\37\22\1\uffff\1\22\1\uffff\4\22\2\uffff\7\22\1\uffff\47\22\1\uffff"
        u"\23\22\105\uffff\125\22\14\uffff\u026c\22\2\uffff\10\22\12\uffff"
        u"\32\22\5\uffff\113\22\3\uffff\3\22\17\uffff\15\22\1\uffff\4\22"
        u"\16\uffff\22\22\16\uffff\22\22\16\uffff\15\22\1\uffff\3\22\17\uffff"
        u"\64\22\43\uffff\1\22\3\uffff\2\22\103\uffff\130\22\10\uffff\51"
        u"\22\127\uffff\35\22\63\uffff\36\22\2\uffff\5\22\u038b\uffff\154"
        u"\22\u0094\uffff\u009c\22\4\uffff\132\22\6\uffff\26\22\2\uffff\6"
        u"\22\2\uffff\46\22\2\uffff\6\22\2\uffff\10\22\1\uffff\1\22\1\uffff"
        u"\1\22\1\uffff\1\22\1\uffff\37\22\2\uffff\65\22\1\uffff\7\22\1\uffff"
        u"\1\22\3\uffff\3\22\1\uffff\7\22\3\uffff\4\22\2\uffff\6\22\4\uffff"
        u"\15\22\5\uffff\3\22\1\uffff\7\22\102\uffff\2\22\23\uffff\1\22\34"
        u"\uffff\1\22\15\uffff\1\22\40\uffff\22\22\120\uffff\1\22\4\uffff"
        u"\1\22\2\uffff\12\22\1\uffff\1\22\3\uffff\5\22\6\uffff\1\22\1\uffff"
        u"\1\22\1\uffff\1\22\1\uffff\4\22\1\uffff\3\22\1\uffff\7\22\3\uffff"
        u"\3\22\5\uffff\5\22\26\uffff\44\22\u0e81\uffff\3\22\31\uffff\11"
        u"\22\7\uffff\5\22\2\uffff\5\22\4\uffff\126\22\6\uffff\3\22\1\uffff"
        u"\137\22\5\uffff\50\22\4\uffff\136\22\21\uffff\30\22\70\uffff\20"
        u"\22\u0200\uffff\u19b6\22\112\uffff\u51a6\22\132\uffff\u048d\22"
        u"\u0773\uffff\u2ba4\22\134\uffff\u0400\22\u1d00\uffff\u012e\22\2"
        u"\uffff\73\22\u0095\uffff\7\22\14\uffff\5\22\5\uffff\1\22\1\uffff"
        u"\12\22\1\uffff\15\22\1\uffff\5\22\1\uffff\1\22\1\uffff\2\22\1\uffff"
        u"\2\22\1\uffff\154\22\41\uffff\u016b\22\22\uffff\100\22\2\uffff"
        u"\66\22\50\uffff\15\22\66\uffff\2\22\30\uffff\3\22\31\uffff\1\22"
        u"\6\uffff\5\22\1\uffff\u0087\22\7\uffff\1\22\34\uffff\32\22\4\uffff"
        u"\1\22\1\uffff\32\22\12\uffff\132\22\3\uffff\6\22\2\uffff\6\22\2"
        u"\uffff\6\22\2\uffff\3\22\3\uffff\2\22\3\uffff\2\22"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\23\4\uffff\1\24"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\26"),
        DFA.unpack(u"\1\27"),
        DFA.unpack(u"\1\30"),
        DFA.unpack(u"\1\31"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\32"),
        DFA.unpack(u"\1\33"),
        DFA.unpack(u"\11\22\5\uffff\16\22\10\uffff\1\22\13\uffff\12\22\7"
        u"\uffff\32\22\4\uffff\1\22\1\uffff\32\22\4\uffff\41\22\2\uffff\4"
        u"\22\4\uffff\1\22\2\uffff\1\22\7\uffff\1\22\4\uffff\1\22\5\uffff"
        u"\27\22\1\uffff\37\22\1\uffff\u013f\22\31\uffff\162\22\4\uffff\14"
        u"\22\16\uffff\5\22\11\uffff\1\22\21\uffff\130\22\5\uffff\23\22\12"
        u"\uffff\1\22\13\uffff\1\22\1\uffff\3\22\1\uffff\1\22\1\uffff\24"
        u"\22\1\uffff\54\22\1\uffff\46\22\1\uffff\5\22\4\uffff\u0082\22\1"
        u"\uffff\4\22\3\uffff\105\22\1\uffff\46\22\2\uffff\2\22\6\uffff\20"
        u"\22\41\uffff\46\22\2\uffff\1\22\7\uffff\47\22\11\uffff\21\22\1"
        u"\uffff\27\22\1\uffff\3\22\1\uffff\1\22\1\uffff\2\22\1\uffff\1\22"
        u"\13\uffff\33\22\5\uffff\3\22\15\uffff\4\22\14\uffff\6\22\13\uffff"
        u"\32\22\5\uffff\31\22\7\uffff\12\22\4\uffff\146\22\1\uffff\11\22"
        u"\1\uffff\12\22\1\uffff\23\22\2\uffff\1\22\17\uffff\74\22\2\uffff"
        u"\3\22\60\uffff\62\22\u014f\uffff\71\22\2\uffff\22\22\2\uffff\5"
        u"\22\3\uffff\14\22\2\uffff\12\22\21\uffff\3\22\1\uffff\10\22\2\uffff"
        u"\2\22\2\uffff\26\22\1\uffff\7\22\1\uffff\1\22\3\uffff\4\22\2\uffff"
        u"\11\22\2\uffff\2\22\2\uffff\3\22\11\uffff\1\22\4\uffff\2\22\1\uffff"
        u"\5\22\2\uffff\16\22\15\uffff\3\22\1\uffff\6\22\4\uffff\2\22\2\uffff"
        u"\26\22\1\uffff\7\22\1\uffff\2\22\1\uffff\2\22\1\uffff\2\22\2\uffff"
        u"\1\22\1\uffff\5\22\4\uffff\2\22\2\uffff\3\22\13\uffff\4\22\1\uffff"
        u"\1\22\7\uffff\17\22\14\uffff\3\22\1\uffff\11\22\1\uffff\3\22\1"
        u"\uffff\26\22\1\uffff\7\22\1\uffff\2\22\1\uffff\5\22\2\uffff\12"
        u"\22\1\uffff\3\22\1\uffff\3\22\2\uffff\1\22\17\uffff\4\22\2\uffff"
        u"\12\22\1\uffff\1\22\17\uffff\3\22\1\uffff\10\22\2\uffff\2\22\2"
        u"\uffff\26\22\1\uffff\7\22\1\uffff\2\22\1\uffff\5\22\2\uffff\10"
        u"\22\3\uffff\2\22\2\uffff\3\22\10\uffff\2\22\4\uffff\2\22\1\uffff"
        u"\3\22\4\uffff\12\22\1\uffff\1\22\20\uffff\2\22\1\uffff\6\22\3\uffff"
        u"\3\22\1\uffff\4\22\3\uffff\2\22\1\uffff\1\22\1\uffff\2\22\3\uffff"
        u"\2\22\3\uffff\3\22\3\uffff\10\22\1\uffff\3\22\4\uffff\5\22\3\uffff"
        u"\3\22\1\uffff\4\22\11\uffff\1\22\17\uffff\11\22\11\uffff\1\22\7"
        u"\uffff\3\22\1\uffff\10\22\1\uffff\3\22\1\uffff\27\22\1\uffff\12"
        u"\22\1\uffff\5\22\4\uffff\7\22\1\uffff\3\22\1\uffff\4\22\7\uffff"
        u"\2\22\11\uffff\2\22\4\uffff\12\22\22\uffff\2\22\1\uffff\10\22\1"
        u"\uffff\3\22\1\uffff\27\22\1\uffff\12\22\1\uffff\5\22\2\uffff\11"
        u"\22\1\uffff\3\22\1\uffff\4\22\7\uffff\2\22\7\uffff\1\22\1\uffff"
        u"\2\22\4\uffff\12\22\22\uffff\2\22\1\uffff\10\22\1\uffff\3\22\1"
        u"\uffff\27\22\1\uffff\20\22\4\uffff\6\22\2\uffff\3\22\1\uffff\4"
        u"\22\11\uffff\1\22\10\uffff\2\22\4\uffff\12\22\22\uffff\2\22\1\uffff"
        u"\22\22\3\uffff\30\22\1\uffff\11\22\1\uffff\1\22\2\uffff\7\22\3"
        u"\uffff\1\22\4\uffff\6\22\1\uffff\1\22\1\uffff\10\22\22\uffff\2"
        u"\22\15\uffff\72\22\4\uffff\20\22\1\uffff\12\22\47\uffff\2\22\1"
        u"\uffff\1\22\2\uffff\2\22\1\uffff\1\22\2\uffff\1\22\6\uffff\4\22"
        u"\1\uffff\7\22\1\uffff\3\22\1\uffff\1\22\1\uffff\1\22\2\uffff\2"
        u"\22\1\uffff\15\22\1\uffff\3\22\2\uffff\5\22\1\uffff\1\22\1\uffff"
        u"\6\22\2\uffff\12\22\2\uffff\2\22\42\uffff\1\22\27\uffff\2\22\6"
        u"\uffff\12\22\13\uffff\1\22\1\uffff\1\22\1\uffff\1\22\4\uffff\12"
        u"\22\1\uffff\42\22\6\uffff\24\22\1\uffff\6\22\4\uffff\10\22\1\uffff"
        u"\44\22\11\uffff\1\22\71\uffff\42\22\1\uffff\5\22\1\uffff\2\22\1"
        u"\uffff\7\22\3\uffff\4\22\6\uffff\12\22\6\uffff\12\22\106\uffff"
        u"\46\22\12\uffff\51\22\7\uffff\132\22\5\uffff\104\22\5\uffff\122"
        u"\22\6\uffff\7\22\1\uffff\77\22\1\uffff\1\22\1\uffff\4\22\2\uffff"
        u"\7\22\1\uffff\1\22\1\uffff\4\22\2\uffff\47\22\1\uffff\1\22\1\uffff"
        u"\4\22\2\uffff\37\22\1\uffff\1\22\1\uffff\4\22\2\uffff\7\22\1\uffff"
        u"\1\22\1\uffff\4\22\2\uffff\7\22\1\uffff\7\22\1\uffff\27\22\1\uffff"
        u"\37\22\1\uffff\1\22\1\uffff\4\22\2\uffff\7\22\1\uffff\47\22\1\uffff"
        u"\23\22\16\uffff\11\22\56\uffff\125\22\14\uffff\u026c\22\2\uffff"
        u"\10\22\12\uffff\32\22\5\uffff\113\22\3\uffff\3\22\17\uffff\15\22"
        u"\1\uffff\7\22\13\uffff\25\22\13\uffff\24\22\14\uffff\15\22\1\uffff"
        u"\3\22\1\uffff\2\22\14\uffff\124\22\3\uffff\1\22\3\uffff\3\22\2"
        u"\uffff\12\22\41\uffff\3\22\2\uffff\12\22\6\uffff\130\22\10\uffff"
        u"\52\22\126\uffff\35\22\3\uffff\14\22\4\uffff\14\22\12\uffff\50"
        u"\22\2\uffff\5\22\u038b\uffff\154\22\u0094\uffff\u009c\22\4\uffff"
        u"\132\22\6\uffff\26\22\2\uffff\6\22\2\uffff\46\22\2\uffff\6\22\2"
        u"\uffff\10\22\1\uffff\1\22\1\uffff\1\22\1\uffff\1\22\1\uffff\37"
        u"\22\2\uffff\65\22\1\uffff\7\22\1\uffff\1\22\3\uffff\3\22\1\uffff"
        u"\7\22\3\uffff\4\22\2\uffff\6\22\4\uffff\15\22\5\uffff\3\22\1\uffff"
        u"\7\22\17\uffff\4\22\32\uffff\5\22\20\uffff\2\22\23\uffff\1\22\13"
        u"\uffff\4\22\6\uffff\6\22\1\uffff\1\22\15\uffff\1\22\40\uffff\22"
        u"\22\36\uffff\15\22\4\uffff\1\22\3\uffff\6\22\27\uffff\1\22\4\uffff"
        u"\1\22\2\uffff\12\22\1\uffff\1\22\3\uffff\5\22\6\uffff\1\22\1\uffff"
        u"\1\22\1\uffff\1\22\1\uffff\4\22\1\uffff\3\22\1\uffff\7\22\3\uffff"
        u"\3\22\5\uffff\5\22\26\uffff\44\22\u0e81\uffff\3\22\31\uffff\17"
        u"\22\1\uffff\5\22\2\uffff\5\22\4\uffff\126\22\2\uffff\2\22\2\uffff"
        u"\3\22\1\uffff\137\22\5\uffff\50\22\4\uffff\136\22\21\uffff\30\22"
        u"\70\uffff\20\22\u0200\uffff\u19b6\22\112\uffff\u51a6\22\132\uffff"
        u"\u048d\22\u0773\uffff\u2ba4\22\134\uffff\u0400\22\u1d00\uffff\u012e"
        u"\22\2\uffff\73\22\u0095\uffff\7\22\14\uffff\5\22\5\uffff\14\22"
        u"\1\uffff\15\22\1\uffff\5\22\1\uffff\1\22\1\uffff\2\22\1\uffff\2"
        u"\22\1\uffff\154\22\41\uffff\u016b\22\22\uffff\100\22\2\uffff\66"
        u"\22\50\uffff\15\22\3\uffff\20\22\20\uffff\4\22\17\uffff\2\22\30"
        u"\uffff\3\22\31\uffff\1\22\6\uffff\5\22\1\uffff\u0087\22\2\uffff"
        u"\1\22\4\uffff\1\22\13\uffff\12\22\7\uffff\32\22\4\uffff\1\22\1"
        u"\uffff\32\22\12\uffff\132\22\3\uffff\6\22\2\uffff\6\22\2\uffff"
        u"\6\22\2\uffff\3\22\3\uffff\2\22\3\uffff\2\22\22\uffff\3\22"),
        DFA.unpack(u"\1\35"),
        DFA.unpack(u"\1\36"),
        DFA.unpack(u"\11\22\5\uffff\16\22\10\uffff\1\22\13\uffff\12\22\7"
        u"\uffff\32\22\4\uffff\1\22\1\uffff\32\22\4\uffff\41\22\2\uffff\4"
        u"\22\4\uffff\1\22\2\uffff\1\22\7\uffff\1\22\4\uffff\1\22\5\uffff"
        u"\27\22\1\uffff\37\22\1\uffff\u013f\22\31\uffff\162\22\4\uffff\14"
        u"\22\16\uffff\5\22\11\uffff\1\22\21\uffff\130\22\5\uffff\23\22\12"
        u"\uffff\1\22\13\uffff\1\22\1\uffff\3\22\1\uffff\1\22\1\uffff\24"
        u"\22\1\uffff\54\22\1\uffff\46\22\1\uffff\5\22\4\uffff\u0082\22\1"
        u"\uffff\4\22\3\uffff\105\22\1\uffff\46\22\2\uffff\2\22\6\uffff\20"
        u"\22\41\uffff\46\22\2\uffff\1\22\7\uffff\47\22\11\uffff\21\22\1"
        u"\uffff\27\22\1\uffff\3\22\1\uffff\1\22\1\uffff\2\22\1\uffff\1\22"
        u"\13\uffff\33\22\5\uffff\3\22\15\uffff\4\22\14\uffff\6\22\13\uffff"
        u"\32\22\5\uffff\31\22\7\uffff\12\22\4\uffff\146\22\1\uffff\11\22"
        u"\1\uffff\12\22\1\uffff\23\22\2\uffff\1\22\17\uffff\74\22\2\uffff"
        u"\3\22\60\uffff\62\22\u014f\uffff\71\22\2\uffff\22\22\2\uffff\5"
        u"\22\3\uffff\14\22\2\uffff\12\22\21\uffff\3\22\1\uffff\10\22\2\uffff"
        u"\2\22\2\uffff\26\22\1\uffff\7\22\1\uffff\1\22\3\uffff\4\22\2\uffff"
        u"\11\22\2\uffff\2\22\2\uffff\3\22\11\uffff\1\22\4\uffff\2\22\1\uffff"
        u"\5\22\2\uffff\16\22\15\uffff\3\22\1\uffff\6\22\4\uffff\2\22\2\uffff"
        u"\26\22\1\uffff\7\22\1\uffff\2\22\1\uffff\2\22\1\uffff\2\22\2\uffff"
        u"\1\22\1\uffff\5\22\4\uffff\2\22\2\uffff\3\22\13\uffff\4\22\1\uffff"
        u"\1\22\7\uffff\17\22\14\uffff\3\22\1\uffff\11\22\1\uffff\3\22\1"
        u"\uffff\26\22\1\uffff\7\22\1\uffff\2\22\1\uffff\5\22\2\uffff\12"
        u"\22\1\uffff\3\22\1\uffff\3\22\2\uffff\1\22\17\uffff\4\22\2\uffff"
        u"\12\22\1\uffff\1\22\17\uffff\3\22\1\uffff\10\22\2\uffff\2\22\2"
        u"\uffff\26\22\1\uffff\7\22\1\uffff\2\22\1\uffff\5\22\2\uffff\10"
        u"\22\3\uffff\2\22\2\uffff\3\22\10\uffff\2\22\4\uffff\2\22\1\uffff"
        u"\3\22\4\uffff\12\22\1\uffff\1\22\20\uffff\2\22\1\uffff\6\22\3\uffff"
        u"\3\22\1\uffff\4\22\3\uffff\2\22\1\uffff\1\22\1\uffff\2\22\3\uffff"
        u"\2\22\3\uffff\3\22\3\uffff\10\22\1\uffff\3\22\4\uffff\5\22\3\uffff"
        u"\3\22\1\uffff\4\22\11\uffff\1\22\17\uffff\11\22\11\uffff\1\22\7"
        u"\uffff\3\22\1\uffff\10\22\1\uffff\3\22\1\uffff\27\22\1\uffff\12"
        u"\22\1\uffff\5\22\4\uffff\7\22\1\uffff\3\22\1\uffff\4\22\7\uffff"
        u"\2\22\11\uffff\2\22\4\uffff\12\22\22\uffff\2\22\1\uffff\10\22\1"
        u"\uffff\3\22\1\uffff\27\22\1\uffff\12\22\1\uffff\5\22\2\uffff\11"
        u"\22\1\uffff\3\22\1\uffff\4\22\7\uffff\2\22\7\uffff\1\22\1\uffff"
        u"\2\22\4\uffff\12\22\22\uffff\2\22\1\uffff\10\22\1\uffff\3\22\1"
        u"\uffff\27\22\1\uffff\20\22\4\uffff\6\22\2\uffff\3\22\1\uffff\4"
        u"\22\11\uffff\1\22\10\uffff\2\22\4\uffff\12\22\22\uffff\2\22\1\uffff"
        u"\22\22\3\uffff\30\22\1\uffff\11\22\1\uffff\1\22\2\uffff\7\22\3"
        u"\uffff\1\22\4\uffff\6\22\1\uffff\1\22\1\uffff\10\22\22\uffff\2"
        u"\22\15\uffff\72\22\4\uffff\20\22\1\uffff\12\22\47\uffff\2\22\1"
        u"\uffff\1\22\2\uffff\2\22\1\uffff\1\22\2\uffff\1\22\6\uffff\4\22"
        u"\1\uffff\7\22\1\uffff\3\22\1\uffff\1\22\1\uffff\1\22\2\uffff\2"
        u"\22\1\uffff\15\22\1\uffff\3\22\2\uffff\5\22\1\uffff\1\22\1\uffff"
        u"\6\22\2\uffff\12\22\2\uffff\2\22\42\uffff\1\22\27\uffff\2\22\6"
        u"\uffff\12\22\13\uffff\1\22\1\uffff\1\22\1\uffff\1\22\4\uffff\12"
        u"\22\1\uffff\42\22\6\uffff\24\22\1\uffff\6\22\4\uffff\10\22\1\uffff"
        u"\44\22\11\uffff\1\22\71\uffff\42\22\1\uffff\5\22\1\uffff\2\22\1"
        u"\uffff\7\22\3\uffff\4\22\6\uffff\12\22\6\uffff\12\22\106\uffff"
        u"\46\22\12\uffff\51\22\7\uffff\132\22\5\uffff\104\22\5\uffff\122"
        u"\22\6\uffff\7\22\1\uffff\77\22\1\uffff\1\22\1\uffff\4\22\2\uffff"
        u"\7\22\1\uffff\1\22\1\uffff\4\22\2\uffff\47\22\1\uffff\1\22\1\uffff"
        u"\4\22\2\uffff\37\22\1\uffff\1\22\1\uffff\4\22\2\uffff\7\22\1\uffff"
        u"\1\22\1\uffff\4\22\2\uffff\7\22\1\uffff\7\22\1\uffff\27\22\1\uffff"
        u"\37\22\1\uffff\1\22\1\uffff\4\22\2\uffff\7\22\1\uffff\47\22\1\uffff"
        u"\23\22\16\uffff\11\22\56\uffff\125\22\14\uffff\u026c\22\2\uffff"
        u"\10\22\12\uffff\32\22\5\uffff\113\22\3\uffff\3\22\17\uffff\15\22"
        u"\1\uffff\7\22\13\uffff\25\22\13\uffff\24\22\14\uffff\15\22\1\uffff"
        u"\3\22\1\uffff\2\22\14\uffff\124\22\3\uffff\1\22\3\uffff\3\22\2"
        u"\uffff\12\22\41\uffff\3\22\2\uffff\12\22\6\uffff\130\22\10\uffff"
        u"\52\22\126\uffff\35\22\3\uffff\14\22\4\uffff\14\22\12\uffff\50"
        u"\22\2\uffff\5\22\u038b\uffff\154\22\u0094\uffff\u009c\22\4\uffff"
        u"\132\22\6\uffff\26\22\2\uffff\6\22\2\uffff\46\22\2\uffff\6\22\2"
        u"\uffff\10\22\1\uffff\1\22\1\uffff\1\22\1\uffff\1\22\1\uffff\37"
        u"\22\2\uffff\65\22\1\uffff\7\22\1\uffff\1\22\3\uffff\3\22\1\uffff"
        u"\7\22\3\uffff\4\22\2\uffff\6\22\4\uffff\15\22\5\uffff\3\22\1\uffff"
        u"\7\22\17\uffff\4\22\32\uffff\5\22\20\uffff\2\22\23\uffff\1\22\13"
        u"\uffff\4\22\6\uffff\6\22\1\uffff\1\22\15\uffff\1\22\40\uffff\22"
        u"\22\36\uffff\15\22\4\uffff\1\22\3\uffff\6\22\27\uffff\1\22\4\uffff"
        u"\1\22\2\uffff\12\22\1\uffff\1\22\3\uffff\5\22\6\uffff\1\22\1\uffff"
        u"\1\22\1\uffff\1\22\1\uffff\4\22\1\uffff\3\22\1\uffff\7\22\3\uffff"
        u"\3\22\5\uffff\5\22\26\uffff\44\22\u0e81\uffff\3\22\31\uffff\17"
        u"\22\1\uffff\5\22\2\uffff\5\22\4\uffff\126\22\2\uffff\2\22\2\uffff"
        u"\3\22\1\uffff\137\22\5\uffff\50\22\4\uffff\136\22\21\uffff\30\22"
        u"\70\uffff\20\22\u0200\uffff\u19b6\22\112\uffff\u51a6\22\132\uffff"
        u"\u048d\22\u0773\uffff\u2ba4\22\134\uffff\u0400\22\u1d00\uffff\u012e"
        u"\22\2\uffff\73\22\u0095\uffff\7\22\14\uffff\5\22\5\uffff\14\22"
        u"\1\uffff\15\22\1\uffff\5\22\1\uffff\1\22\1\uffff\2\22\1\uffff\2"
        u"\22\1\uffff\154\22\41\uffff\u016b\22\22\uffff\100\22\2\uffff\66"
        u"\22\50\uffff\15\22\3\uffff\20\22\20\uffff\4\22\17\uffff\2\22\30"
        u"\uffff\3\22\31\uffff\1\22\6\uffff\5\22\1\uffff\u0087\22\2\uffff"
        u"\1\22\4\uffff\1\22\13\uffff\12\22\7\uffff\32\22\4\uffff\1\22\1"
        u"\uffff\32\22\12\uffff\132\22\3\uffff\6\22\2\uffff\6\22\2\uffff"
        u"\6\22\2\uffff\3\22\3\uffff\2\22\3\uffff\2\22\22\uffff\3\22"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\40"),
        DFA.unpack(u"\1\41"),
        DFA.unpack(u""),
        DFA.unpack(u"\11\22\5\uffff\16\22\10\uffff\1\22\13\uffff\12\22\7"
        u"\uffff\32\22\4\uffff\1\22\1\uffff\32\22\4\uffff\41\22\2\uffff\4"
        u"\22\4\uffff\1\22\2\uffff\1\22\7\uffff\1\22\4\uffff\1\22\5\uffff"
        u"\27\22\1\uffff\37\22\1\uffff\u013f\22\31\uffff\162\22\4\uffff\14"
        u"\22\16\uffff\5\22\11\uffff\1\22\21\uffff\130\22\5\uffff\23\22\12"
        u"\uffff\1\22\13\uffff\1\22\1\uffff\3\22\1\uffff\1\22\1\uffff\24"
        u"\22\1\uffff\54\22\1\uffff\46\22\1\uffff\5\22\4\uffff\u0082\22\1"
        u"\uffff\4\22\3\uffff\105\22\1\uffff\46\22\2\uffff\2\22\6\uffff\20"
        u"\22\41\uffff\46\22\2\uffff\1\22\7\uffff\47\22\11\uffff\21\22\1"
        u"\uffff\27\22\1\uffff\3\22\1\uffff\1\22\1\uffff\2\22\1\uffff\1\22"
        u"\13\uffff\33\22\5\uffff\3\22\15\uffff\4\22\14\uffff\6\22\13\uffff"
        u"\32\22\5\uffff\31\22\7\uffff\12\22\4\uffff\146\22\1\uffff\11\22"
        u"\1\uffff\12\22\1\uffff\23\22\2\uffff\1\22\17\uffff\74\22\2\uffff"
        u"\3\22\60\uffff\62\22\u014f\uffff\71\22\2\uffff\22\22\2\uffff\5"
        u"\22\3\uffff\14\22\2\uffff\12\22\21\uffff\3\22\1\uffff\10\22\2\uffff"
        u"\2\22\2\uffff\26\22\1\uffff\7\22\1\uffff\1\22\3\uffff\4\22\2\uffff"
        u"\11\22\2\uffff\2\22\2\uffff\3\22\11\uffff\1\22\4\uffff\2\22\1\uffff"
        u"\5\22\2\uffff\16\22\15\uffff\3\22\1\uffff\6\22\4\uffff\2\22\2\uffff"
        u"\26\22\1\uffff\7\22\1\uffff\2\22\1\uffff\2\22\1\uffff\2\22\2\uffff"
        u"\1\22\1\uffff\5\22\4\uffff\2\22\2\uffff\3\22\13\uffff\4\22\1\uffff"
        u"\1\22\7\uffff\17\22\14\uffff\3\22\1\uffff\11\22\1\uffff\3\22\1"
        u"\uffff\26\22\1\uffff\7\22\1\uffff\2\22\1\uffff\5\22\2\uffff\12"
        u"\22\1\uffff\3\22\1\uffff\3\22\2\uffff\1\22\17\uffff\4\22\2\uffff"
        u"\12\22\1\uffff\1\22\17\uffff\3\22\1\uffff\10\22\2\uffff\2\22\2"
        u"\uffff\26\22\1\uffff\7\22\1\uffff\2\22\1\uffff\5\22\2\uffff\10"
        u"\22\3\uffff\2\22\2\uffff\3\22\10\uffff\2\22\4\uffff\2\22\1\uffff"
        u"\3\22\4\uffff\12\22\1\uffff\1\22\20\uffff\2\22\1\uffff\6\22\3\uffff"
        u"\3\22\1\uffff\4\22\3\uffff\2\22\1\uffff\1\22\1\uffff\2\22\3\uffff"
        u"\2\22\3\uffff\3\22\3\uffff\10\22\1\uffff\3\22\4\uffff\5\22\3\uffff"
        u"\3\22\1\uffff\4\22\11\uffff\1\22\17\uffff\11\22\11\uffff\1\22\7"
        u"\uffff\3\22\1\uffff\10\22\1\uffff\3\22\1\uffff\27\22\1\uffff\12"
        u"\22\1\uffff\5\22\4\uffff\7\22\1\uffff\3\22\1\uffff\4\22\7\uffff"
        u"\2\22\11\uffff\2\22\4\uffff\12\22\22\uffff\2\22\1\uffff\10\22\1"
        u"\uffff\3\22\1\uffff\27\22\1\uffff\12\22\1\uffff\5\22\2\uffff\11"
        u"\22\1\uffff\3\22\1\uffff\4\22\7\uffff\2\22\7\uffff\1\22\1\uffff"
        u"\2\22\4\uffff\12\22\22\uffff\2\22\1\uffff\10\22\1\uffff\3\22\1"
        u"\uffff\27\22\1\uffff\20\22\4\uffff\6\22\2\uffff\3\22\1\uffff\4"
        u"\22\11\uffff\1\22\10\uffff\2\22\4\uffff\12\22\22\uffff\2\22\1\uffff"
        u"\22\22\3\uffff\30\22\1\uffff\11\22\1\uffff\1\22\2\uffff\7\22\3"
        u"\uffff\1\22\4\uffff\6\22\1\uffff\1\22\1\uffff\10\22\22\uffff\2"
        u"\22\15\uffff\72\22\4\uffff\20\22\1\uffff\12\22\47\uffff\2\22\1"
        u"\uffff\1\22\2\uffff\2\22\1\uffff\1\22\2\uffff\1\22\6\uffff\4\22"
        u"\1\uffff\7\22\1\uffff\3\22\1\uffff\1\22\1\uffff\1\22\2\uffff\2"
        u"\22\1\uffff\15\22\1\uffff\3\22\2\uffff\5\22\1\uffff\1\22\1\uffff"
        u"\6\22\2\uffff\12\22\2\uffff\2\22\42\uffff\1\22\27\uffff\2\22\6"
        u"\uffff\12\22\13\uffff\1\22\1\uffff\1\22\1\uffff\1\22\4\uffff\12"
        u"\22\1\uffff\42\22\6\uffff\24\22\1\uffff\6\22\4\uffff\10\22\1\uffff"
        u"\44\22\11\uffff\1\22\71\uffff\42\22\1\uffff\5\22\1\uffff\2\22\1"
        u"\uffff\7\22\3\uffff\4\22\6\uffff\12\22\6\uffff\12\22\106\uffff"
        u"\46\22\12\uffff\51\22\7\uffff\132\22\5\uffff\104\22\5\uffff\122"
        u"\22\6\uffff\7\22\1\uffff\77\22\1\uffff\1\22\1\uffff\4\22\2\uffff"
        u"\7\22\1\uffff\1\22\1\uffff\4\22\2\uffff\47\22\1\uffff\1\22\1\uffff"
        u"\4\22\2\uffff\37\22\1\uffff\1\22\1\uffff\4\22\2\uffff\7\22\1\uffff"
        u"\1\22\1\uffff\4\22\2\uffff\7\22\1\uffff\7\22\1\uffff\27\22\1\uffff"
        u"\37\22\1\uffff\1\22\1\uffff\4\22\2\uffff\7\22\1\uffff\47\22\1\uffff"
        u"\23\22\16\uffff\11\22\56\uffff\125\22\14\uffff\u026c\22\2\uffff"
        u"\10\22\12\uffff\32\22\5\uffff\113\22\3\uffff\3\22\17\uffff\15\22"
        u"\1\uffff\7\22\13\uffff\25\22\13\uffff\24\22\14\uffff\15\22\1\uffff"
        u"\3\22\1\uffff\2\22\14\uffff\124\22\3\uffff\1\22\3\uffff\3\22\2"
        u"\uffff\12\22\41\uffff\3\22\2\uffff\12\22\6\uffff\130\22\10\uffff"
        u"\52\22\126\uffff\35\22\3\uffff\14\22\4\uffff\14\22\12\uffff\50"
        u"\22\2\uffff\5\22\u038b\uffff\154\22\u0094\uffff\u009c\22\4\uffff"
        u"\132\22\6\uffff\26\22\2\uffff\6\22\2\uffff\46\22\2\uffff\6\22\2"
        u"\uffff\10\22\1\uffff\1\22\1\uffff\1\22\1\uffff\1\22\1\uffff\37"
        u"\22\2\uffff\65\22\1\uffff\7\22\1\uffff\1\22\3\uffff\3\22\1\uffff"
        u"\7\22\3\uffff\4\22\2\uffff\6\22\4\uffff\15\22\5\uffff\3\22\1\uffff"
        u"\7\22\17\uffff\4\22\32\uffff\5\22\20\uffff\2\22\23\uffff\1\22\13"
        u"\uffff\4\22\6\uffff\6\22\1\uffff\1\22\15\uffff\1\22\40\uffff\22"
        u"\22\36\uffff\15\22\4\uffff\1\22\3\uffff\6\22\27\uffff\1\22\4\uffff"
        u"\1\22\2\uffff\12\22\1\uffff\1\22\3\uffff\5\22\6\uffff\1\22\1\uffff"
        u"\1\22\1\uffff\1\22\1\uffff\4\22\1\uffff\3\22\1\uffff\7\22\3\uffff"
        u"\3\22\5\uffff\5\22\26\uffff\44\22\u0e81\uffff\3\22\31\uffff\17"
        u"\22\1\uffff\5\22\2\uffff\5\22\4\uffff\126\22\2\uffff\2\22\2\uffff"
        u"\3\22\1\uffff\137\22\5\uffff\50\22\4\uffff\136\22\21\uffff\30\22"
        u"\70\uffff\20\22\u0200\uffff\u19b6\22\112\uffff\u51a6\22\132\uffff"
        u"\u048d\22\u0773\uffff\u2ba4\22\134\uffff\u0400\22\u1d00\uffff\u012e"
        u"\22\2\uffff\73\22\u0095\uffff\7\22\14\uffff\5\22\5\uffff\14\22"
        u"\1\uffff\15\22\1\uffff\5\22\1\uffff\1\22\1\uffff\2\22\1\uffff\2"
        u"\22\1\uffff\154\22\41\uffff\u016b\22\22\uffff\100\22\2\uffff\66"
        u"\22\50\uffff\15\22\3\uffff\20\22\20\uffff\4\22\17\uffff\2\22\30"
        u"\uffff\3\22\31\uffff\1\22\6\uffff\5\22\1\uffff\u0087\22\2\uffff"
        u"\1\22\4\uffff\1\22\13\uffff\12\22\7\uffff\32\22\4\uffff\1\22\1"
        u"\uffff\32\22\12\uffff\132\22\3\uffff\6\22\2\uffff\6\22\2\uffff"
        u"\6\22\2\uffff\3\22\3\uffff\2\22\3\uffff\2\22\22\uffff\3\22"),
        DFA.unpack(u"\11\22\5\uffff\16\22\10\uffff\1\22\13\uffff\12\22\7"
        u"\uffff\32\22\4\uffff\1\22\1\uffff\32\22\4\uffff\41\22\2\uffff\4"
        u"\22\4\uffff\1\22\2\uffff\1\22\7\uffff\1\22\4\uffff\1\22\5\uffff"
        u"\27\22\1\uffff\37\22\1\uffff\u013f\22\31\uffff\162\22\4\uffff\14"
        u"\22\16\uffff\5\22\11\uffff\1\22\21\uffff\130\22\5\uffff\23\22\12"
        u"\uffff\1\22\13\uffff\1\22\1\uffff\3\22\1\uffff\1\22\1\uffff\24"
        u"\22\1\uffff\54\22\1\uffff\46\22\1\uffff\5\22\4\uffff\u0082\22\1"
        u"\uffff\4\22\3\uffff\105\22\1\uffff\46\22\2\uffff\2\22\6\uffff\20"
        u"\22\41\uffff\46\22\2\uffff\1\22\7\uffff\47\22\11\uffff\21\22\1"
        u"\uffff\27\22\1\uffff\3\22\1\uffff\1\22\1\uffff\2\22\1\uffff\1\22"
        u"\13\uffff\33\22\5\uffff\3\22\15\uffff\4\22\14\uffff\6\22\13\uffff"
        u"\32\22\5\uffff\31\22\7\uffff\12\22\4\uffff\146\22\1\uffff\11\22"
        u"\1\uffff\12\22\1\uffff\23\22\2\uffff\1\22\17\uffff\74\22\2\uffff"
        u"\3\22\60\uffff\62\22\u014f\uffff\71\22\2\uffff\22\22\2\uffff\5"
        u"\22\3\uffff\14\22\2\uffff\12\22\21\uffff\3\22\1\uffff\10\22\2\uffff"
        u"\2\22\2\uffff\26\22\1\uffff\7\22\1\uffff\1\22\3\uffff\4\22\2\uffff"
        u"\11\22\2\uffff\2\22\2\uffff\3\22\11\uffff\1\22\4\uffff\2\22\1\uffff"
        u"\5\22\2\uffff\16\22\15\uffff\3\22\1\uffff\6\22\4\uffff\2\22\2\uffff"
        u"\26\22\1\uffff\7\22\1\uffff\2\22\1\uffff\2\22\1\uffff\2\22\2\uffff"
        u"\1\22\1\uffff\5\22\4\uffff\2\22\2\uffff\3\22\13\uffff\4\22\1\uffff"
        u"\1\22\7\uffff\17\22\14\uffff\3\22\1\uffff\11\22\1\uffff\3\22\1"
        u"\uffff\26\22\1\uffff\7\22\1\uffff\2\22\1\uffff\5\22\2\uffff\12"
        u"\22\1\uffff\3\22\1\uffff\3\22\2\uffff\1\22\17\uffff\4\22\2\uffff"
        u"\12\22\1\uffff\1\22\17\uffff\3\22\1\uffff\10\22\2\uffff\2\22\2"
        u"\uffff\26\22\1\uffff\7\22\1\uffff\2\22\1\uffff\5\22\2\uffff\10"
        u"\22\3\uffff\2\22\2\uffff\3\22\10\uffff\2\22\4\uffff\2\22\1\uffff"
        u"\3\22\4\uffff\12\22\1\uffff\1\22\20\uffff\2\22\1\uffff\6\22\3\uffff"
        u"\3\22\1\uffff\4\22\3\uffff\2\22\1\uffff\1\22\1\uffff\2\22\3\uffff"
        u"\2\22\3\uffff\3\22\3\uffff\10\22\1\uffff\3\22\4\uffff\5\22\3\uffff"
        u"\3\22\1\uffff\4\22\11\uffff\1\22\17\uffff\11\22\11\uffff\1\22\7"
        u"\uffff\3\22\1\uffff\10\22\1\uffff\3\22\1\uffff\27\22\1\uffff\12"
        u"\22\1\uffff\5\22\4\uffff\7\22\1\uffff\3\22\1\uffff\4\22\7\uffff"
        u"\2\22\11\uffff\2\22\4\uffff\12\22\22\uffff\2\22\1\uffff\10\22\1"
        u"\uffff\3\22\1\uffff\27\22\1\uffff\12\22\1\uffff\5\22\2\uffff\11"
        u"\22\1\uffff\3\22\1\uffff\4\22\7\uffff\2\22\7\uffff\1\22\1\uffff"
        u"\2\22\4\uffff\12\22\22\uffff\2\22\1\uffff\10\22\1\uffff\3\22\1"
        u"\uffff\27\22\1\uffff\20\22\4\uffff\6\22\2\uffff\3\22\1\uffff\4"
        u"\22\11\uffff\1\22\10\uffff\2\22\4\uffff\12\22\22\uffff\2\22\1\uffff"
        u"\22\22\3\uffff\30\22\1\uffff\11\22\1\uffff\1\22\2\uffff\7\22\3"
        u"\uffff\1\22\4\uffff\6\22\1\uffff\1\22\1\uffff\10\22\22\uffff\2"
        u"\22\15\uffff\72\22\4\uffff\20\22\1\uffff\12\22\47\uffff\2\22\1"
        u"\uffff\1\22\2\uffff\2\22\1\uffff\1\22\2\uffff\1\22\6\uffff\4\22"
        u"\1\uffff\7\22\1\uffff\3\22\1\uffff\1\22\1\uffff\1\22\2\uffff\2"
        u"\22\1\uffff\15\22\1\uffff\3\22\2\uffff\5\22\1\uffff\1\22\1\uffff"
        u"\6\22\2\uffff\12\22\2\uffff\2\22\42\uffff\1\22\27\uffff\2\22\6"
        u"\uffff\12\22\13\uffff\1\22\1\uffff\1\22\1\uffff\1\22\4\uffff\12"
        u"\22\1\uffff\42\22\6\uffff\24\22\1\uffff\6\22\4\uffff\10\22\1\uffff"
        u"\44\22\11\uffff\1\22\71\uffff\42\22\1\uffff\5\22\1\uffff\2\22\1"
        u"\uffff\7\22\3\uffff\4\22\6\uffff\12\22\6\uffff\12\22\106\uffff"
        u"\46\22\12\uffff\51\22\7\uffff\132\22\5\uffff\104\22\5\uffff\122"
        u"\22\6\uffff\7\22\1\uffff\77\22\1\uffff\1\22\1\uffff\4\22\2\uffff"
        u"\7\22\1\uffff\1\22\1\uffff\4\22\2\uffff\47\22\1\uffff\1\22\1\uffff"
        u"\4\22\2\uffff\37\22\1\uffff\1\22\1\uffff\4\22\2\uffff\7\22\1\uffff"
        u"\1\22\1\uffff\4\22\2\uffff\7\22\1\uffff\7\22\1\uffff\27\22\1\uffff"
        u"\37\22\1\uffff\1\22\1\uffff\4\22\2\uffff\7\22\1\uffff\47\22\1\uffff"
        u"\23\22\16\uffff\11\22\56\uffff\125\22\14\uffff\u026c\22\2\uffff"
        u"\10\22\12\uffff\32\22\5\uffff\113\22\3\uffff\3\22\17\uffff\15\22"
        u"\1\uffff\7\22\13\uffff\25\22\13\uffff\24\22\14\uffff\15\22\1\uffff"
        u"\3\22\1\uffff\2\22\14\uffff\124\22\3\uffff\1\22\3\uffff\3\22\2"
        u"\uffff\12\22\41\uffff\3\22\2\uffff\12\22\6\uffff\130\22\10\uffff"
        u"\52\22\126\uffff\35\22\3\uffff\14\22\4\uffff\14\22\12\uffff\50"
        u"\22\2\uffff\5\22\u038b\uffff\154\22\u0094\uffff\u009c\22\4\uffff"
        u"\132\22\6\uffff\26\22\2\uffff\6\22\2\uffff\46\22\2\uffff\6\22\2"
        u"\uffff\10\22\1\uffff\1\22\1\uffff\1\22\1\uffff\1\22\1\uffff\37"
        u"\22\2\uffff\65\22\1\uffff\7\22\1\uffff\1\22\3\uffff\3\22\1\uffff"
        u"\7\22\3\uffff\4\22\2\uffff\6\22\4\uffff\15\22\5\uffff\3\22\1\uffff"
        u"\7\22\17\uffff\4\22\32\uffff\5\22\20\uffff\2\22\23\uffff\1\22\13"
        u"\uffff\4\22\6\uffff\6\22\1\uffff\1\22\15\uffff\1\22\40\uffff\22"
        u"\22\36\uffff\15\22\4\uffff\1\22\3\uffff\6\22\27\uffff\1\22\4\uffff"
        u"\1\22\2\uffff\12\22\1\uffff\1\22\3\uffff\5\22\6\uffff\1\22\1\uffff"
        u"\1\22\1\uffff\1\22\1\uffff\4\22\1\uffff\3\22\1\uffff\7\22\3\uffff"
        u"\3\22\5\uffff\5\22\26\uffff\44\22\u0e81\uffff\3\22\31\uffff\17"
        u"\22\1\uffff\5\22\2\uffff\5\22\4\uffff\126\22\2\uffff\2\22\2\uffff"
        u"\3\22\1\uffff\137\22\5\uffff\50\22\4\uffff\136\22\21\uffff\30\22"
        u"\70\uffff\20\22\u0200\uffff\u19b6\22\112\uffff\u51a6\22\132\uffff"
        u"\u048d\22\u0773\uffff\u2ba4\22\134\uffff\u0400\22\u1d00\uffff\u012e"
        u"\22\2\uffff\73\22\u0095\uffff\7\22\14\uffff\5\22\5\uffff\14\22"
        u"\1\uffff\15\22\1\uffff\5\22\1\uffff\1\22\1\uffff\2\22\1\uffff\2"
        u"\22\1\uffff\154\22\41\uffff\u016b\22\22\uffff\100\22\2\uffff\66"
        u"\22\50\uffff\15\22\3\uffff\20\22\20\uffff\4\22\17\uffff\2\22\30"
        u"\uffff\3\22\31\uffff\1\22\6\uffff\5\22\1\uffff\u0087\22\2\uffff"
        u"\1\22\4\uffff\1\22\13\uffff\12\22\7\uffff\32\22\4\uffff\1\22\1"
        u"\uffff\32\22\12\uffff\132\22\3\uffff\6\22\2\uffff\6\22\2\uffff"
        u"\6\22\2\uffff\3\22\3\uffff\2\22\3\uffff\2\22\22\uffff\3\22"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #13

    class DFA13(DFA):
        pass


 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(gleamLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
