# $ANTLR 3.1.3 Mar 17, 2009 19:23:44 gleampython/gleam.g 2011-07-17 17:53:49

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *

         
import sys
import traceback

from gleamLexer import gleamLexer



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
NODE=22
RBRACE=21
LINE_COMMENT=35
LBRACE=20
NUMBER=25
IdentifierStart=36
WHITESPACE=33
FOR=26
EQUALS=23
MINUS=13
MULT=14
EOF=-1
HexDigit=31
LPAREN=18
EMPTY_EXPR=10
RPAREN=19
PROG=5
EXPR=9
IN=27
T__39=39
SurrogateIdentifer=38
UnicodeEscape=30
STRINGLITERAL=24
IDENTIFIER=17
BLOCK=7
ARGS=4
EMPTY_VALUE=11
PLUS=12
CALL=8
NL=32
DIGIT=28
DIV=15
COMMENT=34
MACRO=16
EscapeSequence=29
IdentifierPart=37
PARAMS=6

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "ARGS", "PROG", "PARAMS", "BLOCK", "CALL", "EXPR", "EMPTY_EXPR", "EMPTY_VALUE", 
    "PLUS", "MINUS", "MULT", "DIV", "MACRO", "IDENTIFIER", "LPAREN", "RPAREN", 
    "LBRACE", "RBRACE", "NODE", "EQUALS", "STRINGLITERAL", "NUMBER", "FOR", 
    "IN", "DIGIT", "EscapeSequence", "UnicodeEscape", "HexDigit", "NL", 
    "WHITESPACE", "COMMENT", "LINE_COMMENT", "IdentifierStart", "IdentifierPart", 
    "SurrogateIdentifer", "','"
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

        self._state.ruleMemo = {}





        self._adaptor = None
        self.adaptor = CommonTreeAdaptor()
                


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)

              
    def no_newline_before_next_token(self):
        index = self.input.LB(1).getTokenIndex()
        while (self.input.size() > (index + 1)):
            index += 1
            tkn = self.input.get(index)
            if tkn.getChannel() != DEFAULT_CHANNEL:
                if tkn.getType() == NL:
                    return False
            else:
                break
        return True


    class prog_return(ParserRuleReturnScope):
        def __init__(self):
            super(gleamParser.prog_return, self).__init__()

            self.tree = None




    # $ANTLR start "prog"
    # gleampython/gleam.g:65:1: prog : ( stmt )* -> ^( PROG ( stmt )* ) ;
    def prog(self, ):

        retval = self.prog_return()
        retval.start = self.input.LT(1)
        prog_StartIndex = self.input.index()
        root_0 = None

        stmt1 = None


        stream_stmt = RewriteRuleSubtreeStream(self._adaptor, "rule stmt")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 1):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # gleampython/gleam.g:65:6: ( ( stmt )* -> ^( PROG ( stmt )* ) )
                # gleampython/gleam.g:65:8: ( stmt )*
                pass 
                # gleampython/gleam.g:65:8: ( stmt )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((MACRO <= LA1_0 <= IDENTIFIER) or LA1_0 == NODE) :
                        alt1 = 1


                    if alt1 == 1:
                        # gleampython/gleam.g:0:0: stmt
                        pass 
                        self._state.following.append(self.FOLLOW_stmt_in_prog170)
                        stmt1 = self.stmt()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_stmt.add(stmt1.tree)


                    else:
                        break #loop1

                # AST Rewrite
                # elements: stmt
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 65:14: -> ^( PROG ( stmt )* )
                    # gleampython/gleam.g:65:17: ^( PROG ( stmt )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROG, "PROG"), root_1)

                    # gleampython/gleam.g:65:24: ( stmt )*
                    while stream_stmt.hasNext():
                        self._adaptor.addChild(root_1, stream_stmt.nextTree())


                    stream_stmt.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 1, prog_StartIndex, success)

            pass
        return retval

    # $ANTLR end "prog"

    class macro_return(ParserRuleReturnScope):
        def __init__(self):
            super(gleamParser.macro_return, self).__init__()

            self.tree = None




    # $ANTLR start "macro"
    # gleampython/gleam.g:66:1: macro : MACRO IDENTIFIER lparen= '(' ( param ( ',' param )* )? ')' value block -> ^( MACRO IDENTIFIER ^( PARAMS[$lparen] ( param )* ) value block ) ;
    def macro(self, ):

        retval = self.macro_return()
        retval.start = self.input.LT(1)
        macro_StartIndex = self.input.index()
        root_0 = None

        lparen = None
        MACRO2 = None
        IDENTIFIER3 = None
        char_literal5 = None
        char_literal7 = None
        param4 = None

        param6 = None

        value8 = None

        block9 = None


        lparen_tree = None
        MACRO2_tree = None
        IDENTIFIER3_tree = None
        char_literal5_tree = None
        char_literal7_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_MACRO = RewriteRuleTokenStream(self._adaptor, "token MACRO")
        stream_IDENTIFIER = RewriteRuleTokenStream(self._adaptor, "token IDENTIFIER")
        stream_39 = RewriteRuleTokenStream(self._adaptor, "token 39")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_param = RewriteRuleSubtreeStream(self._adaptor, "rule param")
        stream_value = RewriteRuleSubtreeStream(self._adaptor, "rule value")
        stream_block = RewriteRuleSubtreeStream(self._adaptor, "rule block")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 2):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # gleampython/gleam.g:66:7: ( MACRO IDENTIFIER lparen= '(' ( param ( ',' param )* )? ')' value block -> ^( MACRO IDENTIFIER ^( PARAMS[$lparen] ( param )* ) value block ) )
                # gleampython/gleam.g:66:9: MACRO IDENTIFIER lparen= '(' ( param ( ',' param )* )? ')' value block
                pass 
                MACRO2=self.match(self.input, MACRO, self.FOLLOW_MACRO_in_macro187) 
                if self._state.backtracking == 0:
                    stream_MACRO.add(MACRO2)
                IDENTIFIER3=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_macro189) 
                if self._state.backtracking == 0:
                    stream_IDENTIFIER.add(IDENTIFIER3)
                lparen=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_macro193) 
                if self._state.backtracking == 0:
                    stream_LPAREN.add(lparen)
                # gleampython/gleam.g:66:37: ( param ( ',' param )* )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == IDENTIFIER) :
                    alt3 = 1
                if alt3 == 1:
                    # gleampython/gleam.g:66:38: param ( ',' param )*
                    pass 
                    self._state.following.append(self.FOLLOW_param_in_macro196)
                    param4 = self.param()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_param.add(param4.tree)
                    # gleampython/gleam.g:66:44: ( ',' param )*
                    while True: #loop2
                        alt2 = 2
                        LA2_0 = self.input.LA(1)

                        if (LA2_0 == 39) :
                            alt2 = 1


                        if alt2 == 1:
                            # gleampython/gleam.g:66:45: ',' param
                            pass 
                            char_literal5=self.match(self.input, 39, self.FOLLOW_39_in_macro199) 
                            if self._state.backtracking == 0:
                                stream_39.add(char_literal5)
                            self._state.following.append(self.FOLLOW_param_in_macro201)
                            param6 = self.param()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_param.add(param6.tree)


                        else:
                            break #loop2



                char_literal7=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_macro207) 
                if self._state.backtracking == 0:
                    stream_RPAREN.add(char_literal7)
                self._state.following.append(self.FOLLOW_value_in_macro209)
                value8 = self.value()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_value.add(value8.tree)
                self._state.following.append(self.FOLLOW_block_in_macro211)
                block9 = self.block()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_block.add(block9.tree)

                # AST Rewrite
                # elements: block, MACRO, value, param, IDENTIFIER
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 67:7: -> ^( MACRO IDENTIFIER ^( PARAMS[$lparen] ( param )* ) value block )
                    # gleampython/gleam.g:67:10: ^( MACRO IDENTIFIER ^( PARAMS[$lparen] ( param )* ) value block )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_MACRO.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_IDENTIFIER.nextNode())
                    # gleampython/gleam.g:67:29: ^( PARAMS[$lparen] ( param )* )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(self._adaptor.create(PARAMS, lparen), root_2)

                    # gleampython/gleam.g:67:47: ( param )*
                    while stream_param.hasNext():
                        self._adaptor.addChild(root_2, stream_param.nextTree())


                    stream_param.reset();

                    self._adaptor.addChild(root_1, root_2)
                    self._adaptor.addChild(root_1, stream_value.nextTree())
                    self._adaptor.addChild(root_1, stream_block.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 2, macro_StartIndex, success)

            pass
        return retval

    # $ANTLR end "macro"

    class value_return(ParserRuleReturnScope):
        def __init__(self):
            super(gleamParser.value_return, self).__init__()

            self.tree = None




    # $ANTLR start "value"
    # gleampython/gleam.g:68:1: value : ( IDENTIFIER | () -> EMPTY_VALUE );
    def value(self, ):

        retval = self.value_return()
        retval.start = self.input.LT(1)
        value_StartIndex = self.input.index()
        root_0 = None

        IDENTIFIER10 = None

        IDENTIFIER10_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 3):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # gleampython/gleam.g:68:7: ( IDENTIFIER | () -> EMPTY_VALUE )
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == IDENTIFIER) :
                    alt4 = 1
                elif (LA4_0 == LBRACE) :
                    alt4 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae

                if alt4 == 1:
                    # gleampython/gleam.g:69:5: IDENTIFIER
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENTIFIER10=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_value249)
                    if self._state.backtracking == 0:

                        IDENTIFIER10_tree = self._adaptor.createWithPayload(IDENTIFIER10)
                        self._adaptor.addChild(root_0, IDENTIFIER10_tree)



                elif alt4 == 2:
                    # gleampython/gleam.g:70:7: ()
                    pass 
                    # gleampython/gleam.g:70:7: ()
                    # gleampython/gleam.g:70:8: 
                    pass 



                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 70:10: -> EMPTY_VALUE
                        self._adaptor.addChild(root_0, self._adaptor.createFromType(EMPTY_VALUE, "EMPTY_VALUE"))



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 3, value_StartIndex, success)

            pass
        return retval

    # $ANTLR end "value"

    class param_return(ParserRuleReturnScope):
        def __init__(self):
            super(gleamParser.param_return, self).__init__()

            self.tree = None




    # $ANTLR start "param"
    # gleampython/gleam.g:71:1: param : IDENTIFIER ;
    def param(self, ):

        retval = self.param_return()
        retval.start = self.input.LT(1)
        param_StartIndex = self.input.index()
        root_0 = None

        IDENTIFIER11 = None

        IDENTIFIER11_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 4):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # gleampython/gleam.g:71:7: ( IDENTIFIER )
                # gleampython/gleam.g:71:9: IDENTIFIER
                pass 
                root_0 = self._adaptor.nil()

                IDENTIFIER11=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_param271)
                if self._state.backtracking == 0:

                    IDENTIFIER11_tree = self._adaptor.createWithPayload(IDENTIFIER11)
                    self._adaptor.addChild(root_0, IDENTIFIER11_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 4, param_StartIndex, success)

            pass
        return retval

    # $ANTLR end "param"

    class parameters_return(ParserRuleReturnScope):
        def __init__(self):
            super(gleamParser.parameters_return, self).__init__()

            self.tree = None




    # $ANTLR start "parameters"
    # gleampython/gleam.g:72:1: parameters : LPAREN IDENTIFIER RPAREN ;
    def parameters(self, ):

        retval = self.parameters_return()
        retval.start = self.input.LT(1)
        parameters_StartIndex = self.input.index()
        root_0 = None

        LPAREN12 = None
        IDENTIFIER13 = None
        RPAREN14 = None

        LPAREN12_tree = None
        IDENTIFIER13_tree = None
        RPAREN14_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 5):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # gleampython/gleam.g:72:12: ( LPAREN IDENTIFIER RPAREN )
                # gleampython/gleam.g:72:14: LPAREN IDENTIFIER RPAREN
                pass 
                root_0 = self._adaptor.nil()

                LPAREN12=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_parameters278)
                if self._state.backtracking == 0:

                    LPAREN12_tree = self._adaptor.createWithPayload(LPAREN12)
                    self._adaptor.addChild(root_0, LPAREN12_tree)

                IDENTIFIER13=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_parameters280)
                if self._state.backtracking == 0:

                    IDENTIFIER13_tree = self._adaptor.createWithPayload(IDENTIFIER13)
                    self._adaptor.addChild(root_0, IDENTIFIER13_tree)

                RPAREN14=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_parameters282)
                if self._state.backtracking == 0:

                    RPAREN14_tree = self._adaptor.createWithPayload(RPAREN14)
                    self._adaptor.addChild(root_0, RPAREN14_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 5, parameters_StartIndex, success)

            pass
        return retval

    # $ANTLR end "parameters"

    class block_return(ParserRuleReturnScope):
        def __init__(self):
            super(gleamParser.block_return, self).__init__()

            self.tree = None




    # $ANTLR start "block"
    # gleampython/gleam.g:73:1: block : LBRACE ( stmt )* RBRACE -> ^( BLOCK ( stmt )* ) ;
    def block(self, ):

        retval = self.block_return()
        retval.start = self.input.LT(1)
        block_StartIndex = self.input.index()
        root_0 = None

        LBRACE15 = None
        RBRACE17 = None
        stmt16 = None


        LBRACE15_tree = None
        RBRACE17_tree = None
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_stmt = RewriteRuleSubtreeStream(self._adaptor, "rule stmt")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 6):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # gleampython/gleam.g:73:7: ( LBRACE ( stmt )* RBRACE -> ^( BLOCK ( stmt )* ) )
                # gleampython/gleam.g:73:9: LBRACE ( stmt )* RBRACE
                pass 
                LBRACE15=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_block289) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE15)
                # gleampython/gleam.g:73:16: ( stmt )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if ((MACRO <= LA5_0 <= IDENTIFIER) or LA5_0 == NODE) :
                        alt5 = 1


                    if alt5 == 1:
                        # gleampython/gleam.g:0:0: stmt
                        pass 
                        self._state.following.append(self.FOLLOW_stmt_in_block291)
                        stmt16 = self.stmt()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_stmt.add(stmt16.tree)


                    else:
                        break #loop5
                RBRACE17=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_block294) 
                if self._state.backtracking == 0:
                    stream_RBRACE.add(RBRACE17)

                # AST Rewrite
                # elements: stmt
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 73:29: -> ^( BLOCK ( stmt )* )
                    # gleampython/gleam.g:73:32: ^( BLOCK ( stmt )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(BLOCK, "BLOCK"), root_1)

                    # gleampython/gleam.g:73:40: ( stmt )*
                    while stream_stmt.hasNext():
                        self._adaptor.addChild(root_1, stream_stmt.nextTree())


                    stream_stmt.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 6, block_StartIndex, success)

            pass
        return retval

    # $ANTLR end "block"

    class stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(gleamParser.stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "stmt"
    # gleampython/gleam.g:74:1: stmt : ( macro | NODE IDENTIFIER a= args {...}? => expr -> ^( NODE IDENTIFIER $a expr ) | NODE IDENTIFIER a= args -> ^( NODE IDENTIFIER $a EMPTY_EXPR ) | call );
    def stmt(self, ):

        retval = self.stmt_return()
        retval.start = self.input.LT(1)
        stmt_StartIndex = self.input.index()
        root_0 = None

        NODE19 = None
        IDENTIFIER20 = None
        NODE22 = None
        IDENTIFIER23 = None
        a = None

        macro18 = None

        expr21 = None

        call24 = None


        NODE19_tree = None
        IDENTIFIER20_tree = None
        NODE22_tree = None
        IDENTIFIER23_tree = None
        stream_NODE = RewriteRuleTokenStream(self._adaptor, "token NODE")
        stream_IDENTIFIER = RewriteRuleTokenStream(self._adaptor, "token IDENTIFIER")
        stream_args = RewriteRuleSubtreeStream(self._adaptor, "rule args")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 7):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # gleampython/gleam.g:74:6: ( macro | NODE IDENTIFIER a= args {...}? => expr -> ^( NODE IDENTIFIER $a expr ) | NODE IDENTIFIER a= args -> ^( NODE IDENTIFIER $a EMPTY_EXPR ) | call )
                alt6 = 4
                LA6 = self.input.LA(1)
                if LA6 == MACRO:
                    alt6 = 1
                elif LA6 == NODE:
                    LA6_2 = self.input.LA(2)

                    if (LA6_2 == IDENTIFIER) :
                        LA6_4 = self.input.LA(3)

                        if (self.synpred7_gleam()) :
                            alt6 = 2
                        elif (self.synpred8_gleam()) :
                            alt6 = 3
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 6, 4, self.input)

                            raise nvae

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 6, 2, self.input)

                        raise nvae

                elif LA6 == IDENTIFIER:
                    alt6 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae

                if alt6 == 1:
                    # gleampython/gleam.g:74:8: macro
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_macro_in_stmt310)
                    macro18 = self.macro()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, macro18.tree)


                elif alt6 == 2:
                    # gleampython/gleam.g:75:8: NODE IDENTIFIER a= args {...}? => expr
                    pass 
                    NODE19=self.match(self.input, NODE, self.FOLLOW_NODE_in_stmt319) 
                    if self._state.backtracking == 0:
                        stream_NODE.add(NODE19)
                    IDENTIFIER20=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_stmt321) 
                    if self._state.backtracking == 0:
                        stream_IDENTIFIER.add(IDENTIFIER20)
                    self._state.following.append(self.FOLLOW_args_in_stmt325)
                    a = self.args()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_args.add(a.tree)
                    if not ((self.no_newline_before_next_token() )):
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        raise FailedPredicateException(self.input, "stmt", " self.no_newline_before_next_token() ")

                    self._state.following.append(self.FOLLOW_expr_in_stmt330)
                    expr21 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr21.tree)

                    # AST Rewrite
                    # elements: expr, a, IDENTIFIER, NODE
                    # token labels: 
                    # rule labels: retval, a
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        if a is not None:
                            stream_a = RewriteRuleSubtreeStream(self._adaptor, "rule a", a.tree)
                        else:
                            stream_a = RewriteRuleSubtreeStream(self._adaptor, "token a", None)


                        root_0 = self._adaptor.nil()
                        # 76:8: -> ^( NODE IDENTIFIER $a expr )
                        # gleampython/gleam.g:76:11: ^( NODE IDENTIFIER $a expr )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(stream_NODE.nextNode(), root_1)

                        self._adaptor.addChild(root_1, stream_IDENTIFIER.nextNode())
                        self._adaptor.addChild(root_1, stream_a.nextTree())
                        self._adaptor.addChild(root_1, stream_expr.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt6 == 3:
                    # gleampython/gleam.g:77:8: NODE IDENTIFIER a= args
                    pass 
                    NODE22=self.match(self.input, NODE, self.FOLLOW_NODE_in_stmt360) 
                    if self._state.backtracking == 0:
                        stream_NODE.add(NODE22)
                    IDENTIFIER23=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_stmt362) 
                    if self._state.backtracking == 0:
                        stream_IDENTIFIER.add(IDENTIFIER23)
                    self._state.following.append(self.FOLLOW_args_in_stmt366)
                    a = self.args()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_args.add(a.tree)

                    # AST Rewrite
                    # elements: NODE, IDENTIFIER, a
                    # token labels: 
                    # rule labels: retval, a
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        if a is not None:
                            stream_a = RewriteRuleSubtreeStream(self._adaptor, "rule a", a.tree)
                        else:
                            stream_a = RewriteRuleSubtreeStream(self._adaptor, "token a", None)


                        root_0 = self._adaptor.nil()
                        # 78:8: -> ^( NODE IDENTIFIER $a EMPTY_EXPR )
                        # gleampython/gleam.g:78:11: ^( NODE IDENTIFIER $a EMPTY_EXPR )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(stream_NODE.nextNode(), root_1)

                        self._adaptor.addChild(root_1, stream_IDENTIFIER.nextNode())
                        self._adaptor.addChild(root_1, stream_a.nextTree())
                        self._adaptor.addChild(root_1, self._adaptor.createFromType(EMPTY_EXPR, "EMPTY_EXPR"))

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt6 == 4:
                    # gleampython/gleam.g:79:8: call
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_call_in_stmt396)
                    call24 = self.call()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, call24.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 7, stmt_StartIndex, success)

            pass
        return retval

    # $ANTLR end "stmt"

    class call_return(ParserRuleReturnScope):
        def __init__(self):
            super(gleamParser.call_return, self).__init__()

            self.tree = None




    # $ANTLR start "call"
    # gleampython/gleam.g:81:1: call : ( IDENTIFIER a= args {...}? => expr -> ^( CALL IDENTIFIER $a expr ) | IDENTIFIER a= args -> ^( CALL IDENTIFIER $a EMPTY_EXPR ) );
    def call(self, ):

        retval = self.call_return()
        retval.start = self.input.LT(1)
        call_StartIndex = self.input.index()
        root_0 = None

        IDENTIFIER25 = None
        IDENTIFIER27 = None
        a = None

        expr26 = None


        IDENTIFIER25_tree = None
        IDENTIFIER27_tree = None
        stream_IDENTIFIER = RewriteRuleTokenStream(self._adaptor, "token IDENTIFIER")
        stream_args = RewriteRuleSubtreeStream(self._adaptor, "rule args")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 8):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # gleampython/gleam.g:81:6: ( IDENTIFIER a= args {...}? => expr -> ^( CALL IDENTIFIER $a expr ) | IDENTIFIER a= args -> ^( CALL IDENTIFIER $a EMPTY_EXPR ) )
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == IDENTIFIER) :
                    LA7_1 = self.input.LA(2)

                    if (self.synpred9_gleam()) :
                        alt7 = 1
                    elif (True) :
                        alt7 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 7, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 7, 0, self.input)

                    raise nvae

                if alt7 == 1:
                    # gleampython/gleam.g:81:8: IDENTIFIER a= args {...}? => expr
                    pass 
                    IDENTIFIER25=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_call409) 
                    if self._state.backtracking == 0:
                        stream_IDENTIFIER.add(IDENTIFIER25)
                    self._state.following.append(self.FOLLOW_args_in_call413)
                    a = self.args()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_args.add(a.tree)
                    if not ((self.no_newline_before_next_token() )):
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        raise FailedPredicateException(self.input, "call", " self.no_newline_before_next_token() ")

                    self._state.following.append(self.FOLLOW_expr_in_call418)
                    expr26 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr26.tree)

                    # AST Rewrite
                    # elements: expr, a, IDENTIFIER
                    # token labels: 
                    # rule labels: retval, a
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        if a is not None:
                            stream_a = RewriteRuleSubtreeStream(self._adaptor, "rule a", a.tree)
                        else:
                            stream_a = RewriteRuleSubtreeStream(self._adaptor, "token a", None)


                        root_0 = self._adaptor.nil()
                        # 82:8: -> ^( CALL IDENTIFIER $a expr )
                        # gleampython/gleam.g:82:11: ^( CALL IDENTIFIER $a expr )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(CALL, "CALL"), root_1)

                        self._adaptor.addChild(root_1, stream_IDENTIFIER.nextNode())
                        self._adaptor.addChild(root_1, stream_a.nextTree())
                        self._adaptor.addChild(root_1, stream_expr.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt7 == 2:
                    # gleampython/gleam.g:83:8: IDENTIFIER a= args
                    pass 
                    IDENTIFIER27=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_call448) 
                    if self._state.backtracking == 0:
                        stream_IDENTIFIER.add(IDENTIFIER27)
                    self._state.following.append(self.FOLLOW_args_in_call452)
                    a = self.args()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_args.add(a.tree)

                    # AST Rewrite
                    # elements: a, IDENTIFIER
                    # token labels: 
                    # rule labels: retval, a
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        if a is not None:
                            stream_a = RewriteRuleSubtreeStream(self._adaptor, "rule a", a.tree)
                        else:
                            stream_a = RewriteRuleSubtreeStream(self._adaptor, "token a", None)


                        root_0 = self._adaptor.nil()
                        # 84:8: -> ^( CALL IDENTIFIER $a EMPTY_EXPR )
                        # gleampython/gleam.g:84:11: ^( CALL IDENTIFIER $a EMPTY_EXPR )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(CALL, "CALL"), root_1)

                        self._adaptor.addChild(root_1, stream_IDENTIFIER.nextNode())
                        self._adaptor.addChild(root_1, stream_a.nextTree())
                        self._adaptor.addChild(root_1, self._adaptor.createFromType(EMPTY_EXPR, "EMPTY_EXPR"))

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 8, call_StartIndex, success)

            pass
        return retval

    # $ANTLR end "call"

    class args_return(ParserRuleReturnScope):
        def __init__(self):
            super(gleamParser.args_return, self).__init__()

            self.tree = None




    # $ANTLR start "args"
    # gleampython/gleam.g:85:1: args : ( () -> ^( ARGS ) | lparen= LPAREN ( arg ( ',' arg )* )? RPAREN -> ^( ARGS ( arg )* ) );
    def args(self, ):

        retval = self.args_return()
        retval.start = self.input.LT(1)
        args_StartIndex = self.input.index()
        root_0 = None

        lparen = None
        char_literal29 = None
        RPAREN31 = None
        arg28 = None

        arg30 = None


        lparen_tree = None
        char_literal29_tree = None
        RPAREN31_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_39 = RewriteRuleTokenStream(self._adaptor, "token 39")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_arg = RewriteRuleSubtreeStream(self._adaptor, "rule arg")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 9):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # gleampython/gleam.g:85:6: ( () -> ^( ARGS ) | lparen= LPAREN ( arg ( ',' arg )* )? RPAREN -> ^( ARGS ( arg )* ) )
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == EOF or (MACRO <= LA10_0 <= IDENTIFIER) or (RPAREN <= LA10_0 <= NODE) or (STRINGLITERAL <= LA10_0 <= NUMBER) or LA10_0 == 39) :
                    alt10 = 1
                elif (LA10_0 == LPAREN) :
                    alt10 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 10, 0, self.input)

                    raise nvae

                if alt10 == 1:
                    # gleampython/gleam.g:86:5: ()
                    pass 
                    # gleampython/gleam.g:86:5: ()
                    # gleampython/gleam.g:86:6: 
                    pass 



                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 86:8: -> ^( ARGS )
                        # gleampython/gleam.g:86:11: ^( ARGS )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ARGS, "ARGS"), root_1)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt10 == 2:
                    # gleampython/gleam.g:87:7: lparen= LPAREN ( arg ( ',' arg )* )? RPAREN
                    pass 
                    lparen=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_args502) 
                    if self._state.backtracking == 0:
                        stream_LPAREN.add(lparen)
                    # gleampython/gleam.g:87:21: ( arg ( ',' arg )* )?
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == IDENTIFIER) :
                        alt9 = 1
                    if alt9 == 1:
                        # gleampython/gleam.g:87:22: arg ( ',' arg )*
                        pass 
                        self._state.following.append(self.FOLLOW_arg_in_args505)
                        arg28 = self.arg()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_arg.add(arg28.tree)
                        # gleampython/gleam.g:87:26: ( ',' arg )*
                        while True: #loop8
                            alt8 = 2
                            LA8_0 = self.input.LA(1)

                            if (LA8_0 == 39) :
                                alt8 = 1


                            if alt8 == 1:
                                # gleampython/gleam.g:87:27: ',' arg
                                pass 
                                char_literal29=self.match(self.input, 39, self.FOLLOW_39_in_args508) 
                                if self._state.backtracking == 0:
                                    stream_39.add(char_literal29)
                                self._state.following.append(self.FOLLOW_arg_in_args510)
                                arg30 = self.arg()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    stream_arg.add(arg30.tree)


                            else:
                                break #loop8



                    RPAREN31=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_args516) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN31)

                    # AST Rewrite
                    # elements: arg
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 87:46: -> ^( ARGS ( arg )* )
                        # gleampython/gleam.g:87:49: ^( ARGS ( arg )* )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ARGS, "ARGS"), root_1)

                        # gleampython/gleam.g:87:56: ( arg )*
                        while stream_arg.hasNext():
                            self._adaptor.addChild(root_1, stream_arg.nextTree())


                        stream_arg.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 9, args_StartIndex, success)

            pass
        return retval

    # $ANTLR end "args"

    class arg_return(ParserRuleReturnScope):
        def __init__(self):
            super(gleamParser.arg_return, self).__init__()

            self.tree = None




    # $ANTLR start "arg"
    # gleampython/gleam.g:88:1: arg : IDENTIFIER EQUALS expr -> ^( IDENTIFIER expr ) ;
    def arg(self, ):

        retval = self.arg_return()
        retval.start = self.input.LT(1)
        arg_StartIndex = self.input.index()
        root_0 = None

        IDENTIFIER32 = None
        EQUALS33 = None
        expr34 = None


        IDENTIFIER32_tree = None
        EQUALS33_tree = None
        stream_EQUALS = RewriteRuleTokenStream(self._adaptor, "token EQUALS")
        stream_IDENTIFIER = RewriteRuleTokenStream(self._adaptor, "token IDENTIFIER")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 10):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # gleampython/gleam.g:88:5: ( IDENTIFIER EQUALS expr -> ^( IDENTIFIER expr ) )
                # gleampython/gleam.g:88:7: IDENTIFIER EQUALS expr
                pass 
                IDENTIFIER32=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_arg532) 
                if self._state.backtracking == 0:
                    stream_IDENTIFIER.add(IDENTIFIER32)
                EQUALS33=self.match(self.input, EQUALS, self.FOLLOW_EQUALS_in_arg534) 
                if self._state.backtracking == 0:
                    stream_EQUALS.add(EQUALS33)
                self._state.following.append(self.FOLLOW_expr_in_arg536)
                expr34 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expr.add(expr34.tree)

                # AST Rewrite
                # elements: expr, IDENTIFIER
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 88:30: -> ^( IDENTIFIER expr )
                    # gleampython/gleam.g:88:33: ^( IDENTIFIER expr )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_IDENTIFIER.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_expr.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 10, arg_StartIndex, success)

            pass
        return retval

    # $ANTLR end "arg"

    class expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(gleamParser.expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "expr"
    # gleampython/gleam.g:89:1: expr : ( STRINGLITERAL | NUMBER | IDENTIFIER | block | () -> EMPTY_EXPR );
    def expr(self, ):

        retval = self.expr_return()
        retval.start = self.input.LT(1)
        expr_StartIndex = self.input.index()
        root_0 = None

        STRINGLITERAL35 = None
        NUMBER36 = None
        IDENTIFIER37 = None
        block38 = None


        STRINGLITERAL35_tree = None
        NUMBER36_tree = None
        IDENTIFIER37_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 11):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # gleampython/gleam.g:89:6: ( STRINGLITERAL | NUMBER | IDENTIFIER | block | () -> EMPTY_EXPR )
                alt11 = 5
                LA11 = self.input.LA(1)
                if LA11 == STRINGLITERAL:
                    alt11 = 1
                elif LA11 == NUMBER:
                    alt11 = 2
                elif LA11 == IDENTIFIER:
                    LA11_3 = self.input.LA(2)

                    if (self.synpred15_gleam()) :
                        alt11 = 3
                    elif (True) :
                        alt11 = 5
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 11, 3, self.input)

                        raise nvae

                elif LA11 == LBRACE:
                    alt11 = 4
                elif LA11 == EOF or LA11 == MACRO or LA11 == RPAREN or LA11 == RBRACE or LA11 == NODE or LA11 == 39:
                    alt11 = 5
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 11, 0, self.input)

                    raise nvae

                if alt11 == 1:
                    # gleampython/gleam.g:90:5: STRINGLITERAL
                    pass 
                    root_0 = self._adaptor.nil()

                    STRINGLITERAL35=self.match(self.input, STRINGLITERAL, self.FOLLOW_STRINGLITERAL_in_expr555)
                    if self._state.backtracking == 0:

                        STRINGLITERAL35_tree = self._adaptor.createWithPayload(STRINGLITERAL35)
                        self._adaptor.addChild(root_0, STRINGLITERAL35_tree)



                elif alt11 == 2:
                    # gleampython/gleam.g:90:21: NUMBER
                    pass 
                    root_0 = self._adaptor.nil()

                    NUMBER36=self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_expr559)
                    if self._state.backtracking == 0:

                        NUMBER36_tree = self._adaptor.createWithPayload(NUMBER36)
                        self._adaptor.addChild(root_0, NUMBER36_tree)



                elif alt11 == 3:
                    # gleampython/gleam.g:90:30: IDENTIFIER
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENTIFIER37=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_expr563)
                    if self._state.backtracking == 0:

                        IDENTIFIER37_tree = self._adaptor.createWithPayload(IDENTIFIER37)
                        self._adaptor.addChild(root_0, IDENTIFIER37_tree)



                elif alt11 == 4:
                    # gleampython/gleam.g:90:43: block
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_block_in_expr567)
                    block38 = self.block()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, block38.tree)


                elif alt11 == 5:
                    # gleampython/gleam.g:91:7: ()
                    pass 
                    # gleampython/gleam.g:91:7: ()
                    # gleampython/gleam.g:91:8: 
                    pass 



                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 91:10: -> EMPTY_EXPR
                        self._adaptor.addChild(root_0, self._adaptor.createFromType(EMPTY_EXPR, "EMPTY_EXPR"))



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 11, expr_StartIndex, success)

            pass
        return retval

    # $ANTLR end "expr"

    class for_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(gleamParser.for_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "for_expr"
    # gleampython/gleam.g:92:1: for_expr : FOR IDENTIFIER IN IDENTIFIER block ;
    def for_expr(self, ):

        retval = self.for_expr_return()
        retval.start = self.input.LT(1)
        for_expr_StartIndex = self.input.index()
        root_0 = None

        FOR39 = None
        IDENTIFIER40 = None
        IN41 = None
        IDENTIFIER42 = None
        block43 = None


        FOR39_tree = None
        IDENTIFIER40_tree = None
        IN41_tree = None
        IDENTIFIER42_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 12):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # gleampython/gleam.g:92:10: ( FOR IDENTIFIER IN IDENTIFIER block )
                # gleampython/gleam.g:92:12: FOR IDENTIFIER IN IDENTIFIER block
                pass 
                root_0 = self._adaptor.nil()

                FOR39=self.match(self.input, FOR, self.FOLLOW_FOR_in_for_expr587)
                if self._state.backtracking == 0:

                    FOR39_tree = self._adaptor.createWithPayload(FOR39)
                    self._adaptor.addChild(root_0, FOR39_tree)

                IDENTIFIER40=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_for_expr589)
                if self._state.backtracking == 0:

                    IDENTIFIER40_tree = self._adaptor.createWithPayload(IDENTIFIER40)
                    self._adaptor.addChild(root_0, IDENTIFIER40_tree)

                IN41=self.match(self.input, IN, self.FOLLOW_IN_in_for_expr591)
                if self._state.backtracking == 0:

                    IN41_tree = self._adaptor.createWithPayload(IN41)
                    self._adaptor.addChild(root_0, IN41_tree)

                IDENTIFIER42=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_for_expr593)
                if self._state.backtracking == 0:

                    IDENTIFIER42_tree = self._adaptor.createWithPayload(IDENTIFIER42)
                    self._adaptor.addChild(root_0, IDENTIFIER42_tree)

                self._state.following.append(self.FOLLOW_block_in_for_expr595)
                block43 = self.block()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, block43.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 12, for_expr_StartIndex, success)

            pass
        return retval

    # $ANTLR end "for_expr"

    # $ANTLR start "synpred7_gleam"
    def synpred7_gleam_fragment(self, ):
        # gleampython/gleam.g:75:8: ( NODE IDENTIFIER a= args {...}? => expr )
        # gleampython/gleam.g:75:8: NODE IDENTIFIER a= args {...}? => expr
        pass 
        self.match(self.input, NODE, self.FOLLOW_NODE_in_synpred7_gleam319)
        self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_synpred7_gleam321)
        self._state.following.append(self.FOLLOW_args_in_synpred7_gleam325)
        a = self.args()

        self._state.following.pop()
        if not ((self.no_newline_before_next_token() )):
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            raise FailedPredicateException(self.input, "synpred7_gleam", " self.no_newline_before_next_token() ")

        self._state.following.append(self.FOLLOW_expr_in_synpred7_gleam330)
        self.expr()

        self._state.following.pop()


    # $ANTLR end "synpred7_gleam"



    # $ANTLR start "synpred8_gleam"
    def synpred8_gleam_fragment(self, ):
        # gleampython/gleam.g:77:8: ( NODE IDENTIFIER a= args )
        # gleampython/gleam.g:77:8: NODE IDENTIFIER a= args
        pass 
        self.match(self.input, NODE, self.FOLLOW_NODE_in_synpred8_gleam360)
        self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_synpred8_gleam362)
        self._state.following.append(self.FOLLOW_args_in_synpred8_gleam366)
        a = self.args()

        self._state.following.pop()


    # $ANTLR end "synpred8_gleam"



    # $ANTLR start "synpred9_gleam"
    def synpred9_gleam_fragment(self, ):
        # gleampython/gleam.g:81:8: ( IDENTIFIER a= args {...}? => expr )
        # gleampython/gleam.g:81:8: IDENTIFIER a= args {...}? => expr
        pass 
        self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_synpred9_gleam409)
        self._state.following.append(self.FOLLOW_args_in_synpred9_gleam413)
        a = self.args()

        self._state.following.pop()
        if not ((self.no_newline_before_next_token() )):
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            raise FailedPredicateException(self.input, "synpred9_gleam", " self.no_newline_before_next_token() ")

        self._state.following.append(self.FOLLOW_expr_in_synpred9_gleam418)
        self.expr()

        self._state.following.pop()


    # $ANTLR end "synpred9_gleam"



    # $ANTLR start "synpred15_gleam"
    def synpred15_gleam_fragment(self, ):
        # gleampython/gleam.g:90:30: ( IDENTIFIER )
        # gleampython/gleam.g:90:30: IDENTIFIER
        pass 
        self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_synpred15_gleam563)


    # $ANTLR end "synpred15_gleam"




    # Delegated rules

    def synpred8_gleam(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred8_gleam_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred7_gleam(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred7_gleam_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred15_gleam(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred15_gleam_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred9_gleam(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred9_gleam_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



 

    FOLLOW_stmt_in_prog170 = frozenset([1, 16, 17, 22])
    FOLLOW_MACRO_in_macro187 = frozenset([17])
    FOLLOW_IDENTIFIER_in_macro189 = frozenset([18])
    FOLLOW_LPAREN_in_macro193 = frozenset([17, 19])
    FOLLOW_param_in_macro196 = frozenset([19, 39])
    FOLLOW_39_in_macro199 = frozenset([17])
    FOLLOW_param_in_macro201 = frozenset([19, 39])
    FOLLOW_RPAREN_in_macro207 = frozenset([17, 20])
    FOLLOW_value_in_macro209 = frozenset([17, 20])
    FOLLOW_block_in_macro211 = frozenset([1])
    FOLLOW_IDENTIFIER_in_value249 = frozenset([1])
    FOLLOW_IDENTIFIER_in_param271 = frozenset([1])
    FOLLOW_LPAREN_in_parameters278 = frozenset([17])
    FOLLOW_IDENTIFIER_in_parameters280 = frozenset([19])
    FOLLOW_RPAREN_in_parameters282 = frozenset([1])
    FOLLOW_LBRACE_in_block289 = frozenset([16, 17, 21, 22])
    FOLLOW_stmt_in_block291 = frozenset([16, 17, 21, 22])
    FOLLOW_RBRACE_in_block294 = frozenset([1])
    FOLLOW_macro_in_stmt310 = frozenset([1])
    FOLLOW_NODE_in_stmt319 = frozenset([17])
    FOLLOW_IDENTIFIER_in_stmt321 = frozenset([17, 18, 20, 24, 25])
    FOLLOW_args_in_stmt325 = frozenset([17, 20, 24, 25])
    FOLLOW_expr_in_stmt330 = frozenset([1])
    FOLLOW_NODE_in_stmt360 = frozenset([17])
    FOLLOW_IDENTIFIER_in_stmt362 = frozenset([18])
    FOLLOW_args_in_stmt366 = frozenset([1])
    FOLLOW_call_in_stmt396 = frozenset([1])
    FOLLOW_IDENTIFIER_in_call409 = frozenset([17, 18, 20, 24, 25])
    FOLLOW_args_in_call413 = frozenset([17, 20, 24, 25])
    FOLLOW_expr_in_call418 = frozenset([1])
    FOLLOW_IDENTIFIER_in_call448 = frozenset([18])
    FOLLOW_args_in_call452 = frozenset([1])
    FOLLOW_LPAREN_in_args502 = frozenset([17, 19])
    FOLLOW_arg_in_args505 = frozenset([19, 39])
    FOLLOW_39_in_args508 = frozenset([17])
    FOLLOW_arg_in_args510 = frozenset([19, 39])
    FOLLOW_RPAREN_in_args516 = frozenset([1])
    FOLLOW_IDENTIFIER_in_arg532 = frozenset([23])
    FOLLOW_EQUALS_in_arg534 = frozenset([17, 20, 24, 25])
    FOLLOW_expr_in_arg536 = frozenset([1])
    FOLLOW_STRINGLITERAL_in_expr555 = frozenset([1])
    FOLLOW_NUMBER_in_expr559 = frozenset([1])
    FOLLOW_IDENTIFIER_in_expr563 = frozenset([1])
    FOLLOW_block_in_expr567 = frozenset([1])
    FOLLOW_FOR_in_for_expr587 = frozenset([17])
    FOLLOW_IDENTIFIER_in_for_expr589 = frozenset([27])
    FOLLOW_IN_in_for_expr591 = frozenset([17])
    FOLLOW_IDENTIFIER_in_for_expr593 = frozenset([17, 20])
    FOLLOW_block_in_for_expr595 = frozenset([1])
    FOLLOW_NODE_in_synpred7_gleam319 = frozenset([17])
    FOLLOW_IDENTIFIER_in_synpred7_gleam321 = frozenset([17, 18, 20, 24, 25])
    FOLLOW_args_in_synpred7_gleam325 = frozenset([17, 20, 24, 25])
    FOLLOW_expr_in_synpred7_gleam330 = frozenset([1])
    FOLLOW_NODE_in_synpred8_gleam360 = frozenset([17])
    FOLLOW_IDENTIFIER_in_synpred8_gleam362 = frozenset([18])
    FOLLOW_args_in_synpred8_gleam366 = frozenset([1])
    FOLLOW_IDENTIFIER_in_synpred9_gleam409 = frozenset([17, 18, 20, 24, 25])
    FOLLOW_args_in_synpred9_gleam413 = frozenset([17, 20, 24, 25])
    FOLLOW_expr_in_synpred9_gleam418 = frozenset([1])
    FOLLOW_IDENTIFIER_in_synpred15_gleam563 = frozenset([1])



       
def main(argv, otherArg=None):
  char_stream = ANTLRFileStream(sys.argv[1])
  lexer = gleamLexer(char_stream)
  tokens = CommonTokenStream(lexer)
  parser = gleamParser(tokens)

  try:
        parser.prog()
  except RecognitionException:
	traceback.print_stack()
  return parser, lexer


if __name__ == '__main__':
    main(sys.argv)
