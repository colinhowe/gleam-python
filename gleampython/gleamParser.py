# $ANTLR 3.1.3 Mar 17, 2009 19:23:44 gleampython/gleam.g 2011-07-17 14:47:57

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
LINE_COMMENT=34
LBRACE=20
NUMBER=25
IdentifierStart=35
WHITESPACE=32
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
T__38=38
SurrogateIdentifer=37
UnicodeEscape=30
STRINGLITERAL=24
IDENTIFIER=17
BLOCK=7
ARGS=4
EMPTY_VALUE=11
PLUS=12
CALL=8
DIGIT=28
DIV=15
COMMENT=33
MACRO=16
EscapeSequence=29
IdentifierPart=36
PARAMS=6

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "ARGS", "PROG", "PARAMS", "BLOCK", "CALL", "EXPR", "EMPTY_EXPR", "EMPTY_VALUE", 
    "PLUS", "MINUS", "MULT", "DIV", "MACRO", "IDENTIFIER", "LPAREN", "RPAREN", 
    "LBRACE", "RBRACE", "NODE", "EQUALS", "STRINGLITERAL", "NUMBER", "FOR", 
    "IN", "DIGIT", "EscapeSequence", "UnicodeEscape", "HexDigit", "WHITESPACE", 
    "COMMENT", "LINE_COMMENT", "IdentifierStart", "IdentifierPart", "SurrogateIdentifer", 
    "','"
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


    class prog_return(ParserRuleReturnScope):
        def __init__(self):
            super(gleamParser.prog_return, self).__init__()

            self.tree = None




    # $ANTLR start "prog"
    # gleampython/gleam.g:50:1: prog : ( stmt )* -> ^( PROG ( stmt )* ) ;
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

                # gleampython/gleam.g:50:6: ( ( stmt )* -> ^( PROG ( stmt )* ) )
                # gleampython/gleam.g:50:8: ( stmt )*
                pass 
                # gleampython/gleam.g:50:8: ( stmt )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((MACRO <= LA1_0 <= IDENTIFIER) or LA1_0 == NODE) :
                        alt1 = 1


                    if alt1 == 1:
                        # gleampython/gleam.g:0:0: stmt
                        pass 
                        self._state.following.append(self.FOLLOW_stmt_in_prog163)
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
                    # 50:14: -> ^( PROG ( stmt )* )
                    # gleampython/gleam.g:50:17: ^( PROG ( stmt )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROG, "PROG"), root_1)

                    # gleampython/gleam.g:50:24: ( stmt )*
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
    # gleampython/gleam.g:51:1: macro : MACRO IDENTIFIER lparen= '(' ( param ( ',' param )* )? ')' value block -> ^( MACRO IDENTIFIER ^( PARAMS[$lparen] ( param )* ) value block ) ;
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
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_38 = RewriteRuleTokenStream(self._adaptor, "token 38")
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

                # gleampython/gleam.g:51:7: ( MACRO IDENTIFIER lparen= '(' ( param ( ',' param )* )? ')' value block -> ^( MACRO IDENTIFIER ^( PARAMS[$lparen] ( param )* ) value block ) )
                # gleampython/gleam.g:51:9: MACRO IDENTIFIER lparen= '(' ( param ( ',' param )* )? ')' value block
                pass 
                MACRO2=self.match(self.input, MACRO, self.FOLLOW_MACRO_in_macro180) 
                if self._state.backtracking == 0:
                    stream_MACRO.add(MACRO2)
                IDENTIFIER3=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_macro182) 
                if self._state.backtracking == 0:
                    stream_IDENTIFIER.add(IDENTIFIER3)
                lparen=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_macro186) 
                if self._state.backtracking == 0:
                    stream_LPAREN.add(lparen)
                # gleampython/gleam.g:51:37: ( param ( ',' param )* )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == IDENTIFIER) :
                    alt3 = 1
                if alt3 == 1:
                    # gleampython/gleam.g:51:38: param ( ',' param )*
                    pass 
                    self._state.following.append(self.FOLLOW_param_in_macro189)
                    param4 = self.param()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_param.add(param4.tree)
                    # gleampython/gleam.g:51:44: ( ',' param )*
                    while True: #loop2
                        alt2 = 2
                        LA2_0 = self.input.LA(1)

                        if (LA2_0 == 38) :
                            alt2 = 1


                        if alt2 == 1:
                            # gleampython/gleam.g:51:45: ',' param
                            pass 
                            char_literal5=self.match(self.input, 38, self.FOLLOW_38_in_macro192) 
                            if self._state.backtracking == 0:
                                stream_38.add(char_literal5)
                            self._state.following.append(self.FOLLOW_param_in_macro194)
                            param6 = self.param()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_param.add(param6.tree)


                        else:
                            break #loop2



                char_literal7=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_macro200) 
                if self._state.backtracking == 0:
                    stream_RPAREN.add(char_literal7)
                self._state.following.append(self.FOLLOW_value_in_macro202)
                value8 = self.value()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_value.add(value8.tree)
                self._state.following.append(self.FOLLOW_block_in_macro204)
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
                    # 52:7: -> ^( MACRO IDENTIFIER ^( PARAMS[$lparen] ( param )* ) value block )
                    # gleampython/gleam.g:52:10: ^( MACRO IDENTIFIER ^( PARAMS[$lparen] ( param )* ) value block )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_MACRO.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_IDENTIFIER.nextNode())
                    # gleampython/gleam.g:52:29: ^( PARAMS[$lparen] ( param )* )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(self._adaptor.create(PARAMS, lparen), root_2)

                    # gleampython/gleam.g:52:47: ( param )*
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
    # gleampython/gleam.g:53:1: value : ( IDENTIFIER | () -> EMPTY_VALUE );
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

                # gleampython/gleam.g:53:7: ( IDENTIFIER | () -> EMPTY_VALUE )
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
                    # gleampython/gleam.g:54:5: IDENTIFIER
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENTIFIER10=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_value242)
                    if self._state.backtracking == 0:

                        IDENTIFIER10_tree = self._adaptor.createWithPayload(IDENTIFIER10)
                        self._adaptor.addChild(root_0, IDENTIFIER10_tree)



                elif alt4 == 2:
                    # gleampython/gleam.g:55:7: ()
                    pass 
                    # gleampython/gleam.g:55:7: ()
                    # gleampython/gleam.g:55:8: 
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
                        # 55:10: -> EMPTY_VALUE
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
    # gleampython/gleam.g:56:1: param : IDENTIFIER ;
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

                # gleampython/gleam.g:56:7: ( IDENTIFIER )
                # gleampython/gleam.g:56:9: IDENTIFIER
                pass 
                root_0 = self._adaptor.nil()

                IDENTIFIER11=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_param264)
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
    # gleampython/gleam.g:57:1: parameters : LPAREN IDENTIFIER RPAREN ;
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

                # gleampython/gleam.g:57:12: ( LPAREN IDENTIFIER RPAREN )
                # gleampython/gleam.g:57:14: LPAREN IDENTIFIER RPAREN
                pass 
                root_0 = self._adaptor.nil()

                LPAREN12=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_parameters271)
                if self._state.backtracking == 0:

                    LPAREN12_tree = self._adaptor.createWithPayload(LPAREN12)
                    self._adaptor.addChild(root_0, LPAREN12_tree)

                IDENTIFIER13=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_parameters273)
                if self._state.backtracking == 0:

                    IDENTIFIER13_tree = self._adaptor.createWithPayload(IDENTIFIER13)
                    self._adaptor.addChild(root_0, IDENTIFIER13_tree)

                RPAREN14=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_parameters275)
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
    # gleampython/gleam.g:58:1: block : LBRACE ( stmt )* RBRACE -> ^( BLOCK ( stmt )* ) ;
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

                # gleampython/gleam.g:58:7: ( LBRACE ( stmt )* RBRACE -> ^( BLOCK ( stmt )* ) )
                # gleampython/gleam.g:58:9: LBRACE ( stmt )* RBRACE
                pass 
                LBRACE15=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_block282) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE15)
                # gleampython/gleam.g:58:16: ( stmt )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if ((MACRO <= LA5_0 <= IDENTIFIER) or LA5_0 == NODE) :
                        alt5 = 1


                    if alt5 == 1:
                        # gleampython/gleam.g:0:0: stmt
                        pass 
                        self._state.following.append(self.FOLLOW_stmt_in_block284)
                        stmt16 = self.stmt()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_stmt.add(stmt16.tree)


                    else:
                        break #loop5
                RBRACE17=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_block287) 
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
                    # 58:29: -> ^( BLOCK ( stmt )* )
                    # gleampython/gleam.g:58:32: ^( BLOCK ( stmt )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(BLOCK, "BLOCK"), root_1)

                    # gleampython/gleam.g:58:40: ( stmt )*
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
    # gleampython/gleam.g:59:1: stmt : ( macro | NODE IDENTIFIER args expr -> ^( NODE IDENTIFIER args expr ) | call );
    def stmt(self, ):

        retval = self.stmt_return()
        retval.start = self.input.LT(1)
        stmt_StartIndex = self.input.index()
        root_0 = None

        NODE19 = None
        IDENTIFIER20 = None
        macro18 = None

        args21 = None

        expr22 = None

        call23 = None


        NODE19_tree = None
        IDENTIFIER20_tree = None
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

                # gleampython/gleam.g:59:6: ( macro | NODE IDENTIFIER args expr -> ^( NODE IDENTIFIER args expr ) | call )
                alt6 = 3
                LA6 = self.input.LA(1)
                if LA6 == MACRO:
                    alt6 = 1
                elif LA6 == NODE:
                    alt6 = 2
                elif LA6 == IDENTIFIER:
                    alt6 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae

                if alt6 == 1:
                    # gleampython/gleam.g:59:8: macro
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_macro_in_stmt303)
                    macro18 = self.macro()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, macro18.tree)


                elif alt6 == 2:
                    # gleampython/gleam.g:60:8: NODE IDENTIFIER args expr
                    pass 
                    NODE19=self.match(self.input, NODE, self.FOLLOW_NODE_in_stmt312) 
                    if self._state.backtracking == 0:
                        stream_NODE.add(NODE19)
                    IDENTIFIER20=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_stmt314) 
                    if self._state.backtracking == 0:
                        stream_IDENTIFIER.add(IDENTIFIER20)
                    self._state.following.append(self.FOLLOW_args_in_stmt316)
                    args21 = self.args()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_args.add(args21.tree)
                    self._state.following.append(self.FOLLOW_expr_in_stmt318)
                    expr22 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr22.tree)

                    # AST Rewrite
                    # elements: expr, args, IDENTIFIER, NODE
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
                        # 60:34: -> ^( NODE IDENTIFIER args expr )
                        # gleampython/gleam.g:60:37: ^( NODE IDENTIFIER args expr )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(stream_NODE.nextNode(), root_1)

                        self._adaptor.addChild(root_1, stream_IDENTIFIER.nextNode())
                        self._adaptor.addChild(root_1, stream_args.nextTree())
                        self._adaptor.addChild(root_1, stream_expr.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt6 == 3:
                    # gleampython/gleam.g:61:8: call
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_call_in_stmt339)
                    call23 = self.call()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, call23.tree)


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
    # gleampython/gleam.g:63:1: call : IDENTIFIER args expr -> ^( CALL IDENTIFIER args expr ) ;
    def call(self, ):

        retval = self.call_return()
        retval.start = self.input.LT(1)
        call_StartIndex = self.input.index()
        root_0 = None

        IDENTIFIER24 = None
        args25 = None

        expr26 = None


        IDENTIFIER24_tree = None
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

                # gleampython/gleam.g:63:6: ( IDENTIFIER args expr -> ^( CALL IDENTIFIER args expr ) )
                # gleampython/gleam.g:63:8: IDENTIFIER args expr
                pass 
                IDENTIFIER24=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_call352) 
                if self._state.backtracking == 0:
                    stream_IDENTIFIER.add(IDENTIFIER24)
                self._state.following.append(self.FOLLOW_args_in_call354)
                args25 = self.args()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_args.add(args25.tree)
                self._state.following.append(self.FOLLOW_expr_in_call356)
                expr26 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expr.add(expr26.tree)

                # AST Rewrite
                # elements: IDENTIFIER, args, expr
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
                    # 63:29: -> ^( CALL IDENTIFIER args expr )
                    # gleampython/gleam.g:63:32: ^( CALL IDENTIFIER args expr )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(CALL, "CALL"), root_1)

                    self._adaptor.addChild(root_1, stream_IDENTIFIER.nextNode())
                    self._adaptor.addChild(root_1, stream_args.nextTree())
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
                self.memoize(self.input, 8, call_StartIndex, success)

            pass
        return retval

    # $ANTLR end "call"

    class args_return(ParserRuleReturnScope):
        def __init__(self):
            super(gleamParser.args_return, self).__init__()

            self.tree = None




    # $ANTLR start "args"
    # gleampython/gleam.g:64:1: args : ( () -> ^( ARGS ) | lparen= LPAREN ( arg ( ',' arg )* )? RPAREN -> ^( ARGS ( arg )* ) );
    def args(self, ):

        retval = self.args_return()
        retval.start = self.input.LT(1)
        args_StartIndex = self.input.index()
        root_0 = None

        lparen = None
        char_literal28 = None
        RPAREN30 = None
        arg27 = None

        arg29 = None


        lparen_tree = None
        char_literal28_tree = None
        RPAREN30_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_38 = RewriteRuleTokenStream(self._adaptor, "token 38")
        stream_arg = RewriteRuleSubtreeStream(self._adaptor, "rule arg")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 9):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # gleampython/gleam.g:64:6: ( () -> ^( ARGS ) | lparen= LPAREN ( arg ( ',' arg )* )? RPAREN -> ^( ARGS ( arg )* ) )
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == EOF or (MACRO <= LA9_0 <= IDENTIFIER) or (RPAREN <= LA9_0 <= NODE) or (STRINGLITERAL <= LA9_0 <= NUMBER) or LA9_0 == 38) :
                    alt9 = 1
                elif (LA9_0 == LPAREN) :
                    alt9 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 9, 0, self.input)

                    raise nvae

                if alt9 == 1:
                    # gleampython/gleam.g:65:5: ()
                    pass 
                    # gleampython/gleam.g:65:5: ()
                    # gleampython/gleam.g:65:6: 
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
                        # 65:8: -> ^( ARGS )
                        # gleampython/gleam.g:65:11: ^( ARGS )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ARGS, "ARGS"), root_1)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt9 == 2:
                    # gleampython/gleam.g:66:7: lparen= LPAREN ( arg ( ',' arg )* )? RPAREN
                    pass 
                    lparen=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_args397) 
                    if self._state.backtracking == 0:
                        stream_LPAREN.add(lparen)
                    # gleampython/gleam.g:66:21: ( arg ( ',' arg )* )?
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == IDENTIFIER) :
                        alt8 = 1
                    if alt8 == 1:
                        # gleampython/gleam.g:66:22: arg ( ',' arg )*
                        pass 
                        self._state.following.append(self.FOLLOW_arg_in_args400)
                        arg27 = self.arg()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_arg.add(arg27.tree)
                        # gleampython/gleam.g:66:26: ( ',' arg )*
                        while True: #loop7
                            alt7 = 2
                            LA7_0 = self.input.LA(1)

                            if (LA7_0 == 38) :
                                alt7 = 1


                            if alt7 == 1:
                                # gleampython/gleam.g:66:27: ',' arg
                                pass 
                                char_literal28=self.match(self.input, 38, self.FOLLOW_38_in_args403) 
                                if self._state.backtracking == 0:
                                    stream_38.add(char_literal28)
                                self._state.following.append(self.FOLLOW_arg_in_args405)
                                arg29 = self.arg()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    stream_arg.add(arg29.tree)


                            else:
                                break #loop7



                    RPAREN30=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_args411) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN30)

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
                        # 66:46: -> ^( ARGS ( arg )* )
                        # gleampython/gleam.g:66:49: ^( ARGS ( arg )* )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ARGS, "ARGS"), root_1)

                        # gleampython/gleam.g:66:56: ( arg )*
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
    # gleampython/gleam.g:67:1: arg : IDENTIFIER EQUALS expr -> ^( IDENTIFIER expr ) ;
    def arg(self, ):

        retval = self.arg_return()
        retval.start = self.input.LT(1)
        arg_StartIndex = self.input.index()
        root_0 = None

        IDENTIFIER31 = None
        EQUALS32 = None
        expr33 = None


        IDENTIFIER31_tree = None
        EQUALS32_tree = None
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

                # gleampython/gleam.g:67:5: ( IDENTIFIER EQUALS expr -> ^( IDENTIFIER expr ) )
                # gleampython/gleam.g:67:7: IDENTIFIER EQUALS expr
                pass 
                IDENTIFIER31=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_arg427) 
                if self._state.backtracking == 0:
                    stream_IDENTIFIER.add(IDENTIFIER31)
                EQUALS32=self.match(self.input, EQUALS, self.FOLLOW_EQUALS_in_arg429) 
                if self._state.backtracking == 0:
                    stream_EQUALS.add(EQUALS32)
                self._state.following.append(self.FOLLOW_expr_in_arg431)
                expr33 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expr.add(expr33.tree)

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
                    # 67:30: -> ^( IDENTIFIER expr )
                    # gleampython/gleam.g:67:33: ^( IDENTIFIER expr )
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
    # gleampython/gleam.g:68:1: expr : ( STRINGLITERAL | NUMBER | IDENTIFIER | block | () -> EMPTY_EXPR );
    def expr(self, ):

        retval = self.expr_return()
        retval.start = self.input.LT(1)
        expr_StartIndex = self.input.index()
        root_0 = None

        STRINGLITERAL34 = None
        NUMBER35 = None
        IDENTIFIER36 = None
        block37 = None


        STRINGLITERAL34_tree = None
        NUMBER35_tree = None
        IDENTIFIER36_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 11):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # gleampython/gleam.g:68:6: ( STRINGLITERAL | NUMBER | IDENTIFIER | block | () -> EMPTY_EXPR )
                alt10 = 5
                LA10 = self.input.LA(1)
                if LA10 == STRINGLITERAL:
                    alt10 = 1
                elif LA10 == NUMBER:
                    alt10 = 2
                elif LA10 == IDENTIFIER:
                    LA10_3 = self.input.LA(2)

                    if (self.synpred13_gleam()) :
                        alt10 = 3
                    elif (True) :
                        alt10 = 5
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 10, 3, self.input)

                        raise nvae

                elif LA10 == LBRACE:
                    alt10 = 4
                elif LA10 == EOF or LA10 == MACRO or LA10 == RPAREN or LA10 == RBRACE or LA10 == NODE or LA10 == 38:
                    alt10 = 5
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 10, 0, self.input)

                    raise nvae

                if alt10 == 1:
                    # gleampython/gleam.g:69:5: STRINGLITERAL
                    pass 
                    root_0 = self._adaptor.nil()

                    STRINGLITERAL34=self.match(self.input, STRINGLITERAL, self.FOLLOW_STRINGLITERAL_in_expr450)
                    if self._state.backtracking == 0:

                        STRINGLITERAL34_tree = self._adaptor.createWithPayload(STRINGLITERAL34)
                        self._adaptor.addChild(root_0, STRINGLITERAL34_tree)



                elif alt10 == 2:
                    # gleampython/gleam.g:69:21: NUMBER
                    pass 
                    root_0 = self._adaptor.nil()

                    NUMBER35=self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_expr454)
                    if self._state.backtracking == 0:

                        NUMBER35_tree = self._adaptor.createWithPayload(NUMBER35)
                        self._adaptor.addChild(root_0, NUMBER35_tree)



                elif alt10 == 3:
                    # gleampython/gleam.g:69:30: IDENTIFIER
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENTIFIER36=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_expr458)
                    if self._state.backtracking == 0:

                        IDENTIFIER36_tree = self._adaptor.createWithPayload(IDENTIFIER36)
                        self._adaptor.addChild(root_0, IDENTIFIER36_tree)



                elif alt10 == 4:
                    # gleampython/gleam.g:69:43: block
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_block_in_expr462)
                    block37 = self.block()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, block37.tree)


                elif alt10 == 5:
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
                        # 70:10: -> EMPTY_EXPR
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
    # gleampython/gleam.g:71:1: for_expr : FOR IDENTIFIER IN IDENTIFIER block ;
    def for_expr(self, ):

        retval = self.for_expr_return()
        retval.start = self.input.LT(1)
        for_expr_StartIndex = self.input.index()
        root_0 = None

        FOR38 = None
        IDENTIFIER39 = None
        IN40 = None
        IDENTIFIER41 = None
        block42 = None


        FOR38_tree = None
        IDENTIFIER39_tree = None
        IN40_tree = None
        IDENTIFIER41_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 12):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # gleampython/gleam.g:71:10: ( FOR IDENTIFIER IN IDENTIFIER block )
                # gleampython/gleam.g:71:12: FOR IDENTIFIER IN IDENTIFIER block
                pass 
                root_0 = self._adaptor.nil()

                FOR38=self.match(self.input, FOR, self.FOLLOW_FOR_in_for_expr482)
                if self._state.backtracking == 0:

                    FOR38_tree = self._adaptor.createWithPayload(FOR38)
                    self._adaptor.addChild(root_0, FOR38_tree)

                IDENTIFIER39=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_for_expr484)
                if self._state.backtracking == 0:

                    IDENTIFIER39_tree = self._adaptor.createWithPayload(IDENTIFIER39)
                    self._adaptor.addChild(root_0, IDENTIFIER39_tree)

                IN40=self.match(self.input, IN, self.FOLLOW_IN_in_for_expr486)
                if self._state.backtracking == 0:

                    IN40_tree = self._adaptor.createWithPayload(IN40)
                    self._adaptor.addChild(root_0, IN40_tree)

                IDENTIFIER41=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_for_expr488)
                if self._state.backtracking == 0:

                    IDENTIFIER41_tree = self._adaptor.createWithPayload(IDENTIFIER41)
                    self._adaptor.addChild(root_0, IDENTIFIER41_tree)

                self._state.following.append(self.FOLLOW_block_in_for_expr490)
                block42 = self.block()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, block42.tree)



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

    # $ANTLR start "synpred13_gleam"
    def synpred13_gleam_fragment(self, ):
        # gleampython/gleam.g:69:30: ( IDENTIFIER )
        # gleampython/gleam.g:69:30: IDENTIFIER
        pass 
        self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_synpred13_gleam458)


    # $ANTLR end "synpred13_gleam"




    # Delegated rules

    def synpred13_gleam(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred13_gleam_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



 

    FOLLOW_stmt_in_prog163 = frozenset([1, 16, 17, 22])
    FOLLOW_MACRO_in_macro180 = frozenset([17])
    FOLLOW_IDENTIFIER_in_macro182 = frozenset([18])
    FOLLOW_LPAREN_in_macro186 = frozenset([17, 19])
    FOLLOW_param_in_macro189 = frozenset([19, 38])
    FOLLOW_38_in_macro192 = frozenset([17])
    FOLLOW_param_in_macro194 = frozenset([19, 38])
    FOLLOW_RPAREN_in_macro200 = frozenset([17, 20])
    FOLLOW_value_in_macro202 = frozenset([17, 20])
    FOLLOW_block_in_macro204 = frozenset([1])
    FOLLOW_IDENTIFIER_in_value242 = frozenset([1])
    FOLLOW_IDENTIFIER_in_param264 = frozenset([1])
    FOLLOW_LPAREN_in_parameters271 = frozenset([17])
    FOLLOW_IDENTIFIER_in_parameters273 = frozenset([19])
    FOLLOW_RPAREN_in_parameters275 = frozenset([1])
    FOLLOW_LBRACE_in_block282 = frozenset([16, 17, 21, 22])
    FOLLOW_stmt_in_block284 = frozenset([16, 17, 21, 22])
    FOLLOW_RBRACE_in_block287 = frozenset([1])
    FOLLOW_macro_in_stmt303 = frozenset([1])
    FOLLOW_NODE_in_stmt312 = frozenset([17])
    FOLLOW_IDENTIFIER_in_stmt314 = frozenset([17, 18, 20, 24, 25])
    FOLLOW_args_in_stmt316 = frozenset([17, 20, 24, 25])
    FOLLOW_expr_in_stmt318 = frozenset([1])
    FOLLOW_call_in_stmt339 = frozenset([1])
    FOLLOW_IDENTIFIER_in_call352 = frozenset([17, 18, 20, 24, 25])
    FOLLOW_args_in_call354 = frozenset([17, 20, 24, 25])
    FOLLOW_expr_in_call356 = frozenset([1])
    FOLLOW_LPAREN_in_args397 = frozenset([17, 19])
    FOLLOW_arg_in_args400 = frozenset([19, 38])
    FOLLOW_38_in_args403 = frozenset([17])
    FOLLOW_arg_in_args405 = frozenset([19, 38])
    FOLLOW_RPAREN_in_args411 = frozenset([1])
    FOLLOW_IDENTIFIER_in_arg427 = frozenset([23])
    FOLLOW_EQUALS_in_arg429 = frozenset([17, 20, 24, 25])
    FOLLOW_expr_in_arg431 = frozenset([1])
    FOLLOW_STRINGLITERAL_in_expr450 = frozenset([1])
    FOLLOW_NUMBER_in_expr454 = frozenset([1])
    FOLLOW_IDENTIFIER_in_expr458 = frozenset([1])
    FOLLOW_block_in_expr462 = frozenset([1])
    FOLLOW_FOR_in_for_expr482 = frozenset([17])
    FOLLOW_IDENTIFIER_in_for_expr484 = frozenset([27])
    FOLLOW_IN_in_for_expr486 = frozenset([17])
    FOLLOW_IDENTIFIER_in_for_expr488 = frozenset([17, 20])
    FOLLOW_block_in_for_expr490 = frozenset([1])
    FOLLOW_IDENTIFIER_in_synpred13_gleam458 = frozenset([1])



       
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
