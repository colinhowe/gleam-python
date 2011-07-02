# $ANTLR 3.1.3 Mar 17, 2009 19:23:44 gleampython/gleam.g 2011-07-02 11:45:33

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
NODE=19
RBRACE=18
LINE_COMMENT=31
LBRACE=17
NUMBER=22
IdentifierStart=32
WHITESPACE=29
FOR=23
EQUALS=20
MINUS=10
MULT=11
EOF=-1
HexDigit=28
LPAREN=15
RPAREN=16
PROG=5
IN=24
T__35=35
SurrogateIdentifer=34
UnicodeEscape=27
STRINGLITERAL=21
IDENTIFIER=14
BLOCK=7
ARGS=4
PLUS=9
CALL=8
DIGIT=25
DIV=12
COMMENT=30
MACRO=13
EscapeSequence=26
IdentifierPart=33
PARAMS=6

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "ARGS", "PROG", "PARAMS", "BLOCK", "CALL", "PLUS", "MINUS", "MULT", 
    "DIV", "MACRO", "IDENTIFIER", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
    "NODE", "EQUALS", "STRINGLITERAL", "NUMBER", "FOR", "IN", "DIGIT", "EscapeSequence", 
    "UnicodeEscape", "HexDigit", "WHITESPACE", "COMMENT", "LINE_COMMENT", 
    "IdentifierStart", "IdentifierPart", "SurrogateIdentifer", "','"
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
    # gleampython/gleam.g:47:1: prog : ( stmt )* -> ^( PROG ( stmt )* ) ;
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

                # gleampython/gleam.g:47:6: ( ( stmt )* -> ^( PROG ( stmt )* ) )
                # gleampython/gleam.g:47:8: ( stmt )*
                pass 
                # gleampython/gleam.g:47:8: ( stmt )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((MACRO <= LA1_0 <= IDENTIFIER) or LA1_0 == NODE) :
                        alt1 = 1


                    if alt1 == 1:
                        # gleampython/gleam.g:0:0: stmt
                        pass 
                        self._state.following.append(self.FOLLOW_stmt_in_prog142)
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
                    # 47:14: -> ^( PROG ( stmt )* )
                    # gleampython/gleam.g:47:17: ^( PROG ( stmt )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROG, "PROG"), root_1)

                    # gleampython/gleam.g:47:24: ( stmt )*
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
    # gleampython/gleam.g:48:1: macro : MACRO IDENTIFIER lparen= '(' ( param ( ',' param )* )? ')' (value= IDENTIFIER )? block -> ^( MACRO IDENTIFIER ^( PARAMS[$lparen] ( param )* ) ( $value)? block ) ;
    def macro(self, ):

        retval = self.macro_return()
        retval.start = self.input.LT(1)
        macro_StartIndex = self.input.index()
        root_0 = None

        lparen = None
        value = None
        MACRO2 = None
        IDENTIFIER3 = None
        char_literal5 = None
        char_literal7 = None
        param4 = None

        param6 = None

        block8 = None


        lparen_tree = None
        value_tree = None
        MACRO2_tree = None
        IDENTIFIER3_tree = None
        char_literal5_tree = None
        char_literal7_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_35 = RewriteRuleTokenStream(self._adaptor, "token 35")
        stream_MACRO = RewriteRuleTokenStream(self._adaptor, "token MACRO")
        stream_IDENTIFIER = RewriteRuleTokenStream(self._adaptor, "token IDENTIFIER")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_param = RewriteRuleSubtreeStream(self._adaptor, "rule param")
        stream_block = RewriteRuleSubtreeStream(self._adaptor, "rule block")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 2):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # gleampython/gleam.g:48:7: ( MACRO IDENTIFIER lparen= '(' ( param ( ',' param )* )? ')' (value= IDENTIFIER )? block -> ^( MACRO IDENTIFIER ^( PARAMS[$lparen] ( param )* ) ( $value)? block ) )
                # gleampython/gleam.g:48:9: MACRO IDENTIFIER lparen= '(' ( param ( ',' param )* )? ')' (value= IDENTIFIER )? block
                pass 
                MACRO2=self.match(self.input, MACRO, self.FOLLOW_MACRO_in_macro159) 
                if self._state.backtracking == 0:
                    stream_MACRO.add(MACRO2)
                IDENTIFIER3=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_macro161) 
                if self._state.backtracking == 0:
                    stream_IDENTIFIER.add(IDENTIFIER3)
                lparen=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_macro165) 
                if self._state.backtracking == 0:
                    stream_LPAREN.add(lparen)
                # gleampython/gleam.g:48:37: ( param ( ',' param )* )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == IDENTIFIER) :
                    alt3 = 1
                if alt3 == 1:
                    # gleampython/gleam.g:48:38: param ( ',' param )*
                    pass 
                    self._state.following.append(self.FOLLOW_param_in_macro168)
                    param4 = self.param()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_param.add(param4.tree)
                    # gleampython/gleam.g:48:44: ( ',' param )*
                    while True: #loop2
                        alt2 = 2
                        LA2_0 = self.input.LA(1)

                        if (LA2_0 == 35) :
                            alt2 = 1


                        if alt2 == 1:
                            # gleampython/gleam.g:48:45: ',' param
                            pass 
                            char_literal5=self.match(self.input, 35, self.FOLLOW_35_in_macro171) 
                            if self._state.backtracking == 0:
                                stream_35.add(char_literal5)
                            self._state.following.append(self.FOLLOW_param_in_macro173)
                            param6 = self.param()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_param.add(param6.tree)


                        else:
                            break #loop2



                char_literal7=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_macro179) 
                if self._state.backtracking == 0:
                    stream_RPAREN.add(char_literal7)
                # gleampython/gleam.g:48:68: (value= IDENTIFIER )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == IDENTIFIER) :
                    alt4 = 1
                if alt4 == 1:
                    # gleampython/gleam.g:0:0: value= IDENTIFIER
                    pass 
                    value=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_macro183) 
                    if self._state.backtracking == 0:
                        stream_IDENTIFIER.add(value)



                self._state.following.append(self.FOLLOW_block_in_macro186)
                block8 = self.block()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_block.add(block8.tree)

                # AST Rewrite
                # elements: IDENTIFIER, block, MACRO, value, param
                # token labels: value
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0
                    stream_value = RewriteRuleTokenStream(self._adaptor, "token value", value)

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 49:7: -> ^( MACRO IDENTIFIER ^( PARAMS[$lparen] ( param )* ) ( $value)? block )
                    # gleampython/gleam.g:49:10: ^( MACRO IDENTIFIER ^( PARAMS[$lparen] ( param )* ) ( $value)? block )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_MACRO.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_IDENTIFIER.nextNode())
                    # gleampython/gleam.g:49:29: ^( PARAMS[$lparen] ( param )* )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(self._adaptor.create(PARAMS, lparen), root_2)

                    # gleampython/gleam.g:49:47: ( param )*
                    while stream_param.hasNext():
                        self._adaptor.addChild(root_2, stream_param.nextTree())


                    stream_param.reset();

                    self._adaptor.addChild(root_1, root_2)
                    # gleampython/gleam.g:49:55: ( $value)?
                    if stream_value.hasNext():
                        self._adaptor.addChild(root_1, stream_value.nextNode())


                    stream_value.reset();
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

    class param_return(ParserRuleReturnScope):
        def __init__(self):
            super(gleamParser.param_return, self).__init__()

            self.tree = None




    # $ANTLR start "param"
    # gleampython/gleam.g:50:1: param : IDENTIFIER ;
    def param(self, ):

        retval = self.param_return()
        retval.start = self.input.LT(1)
        param_StartIndex = self.input.index()
        root_0 = None

        IDENTIFIER9 = None

        IDENTIFIER9_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 3):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # gleampython/gleam.g:50:7: ( IDENTIFIER )
                # gleampython/gleam.g:50:9: IDENTIFIER
                pass 
                root_0 = self._adaptor.nil()

                IDENTIFIER9=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_param222)
                if self._state.backtracking == 0:

                    IDENTIFIER9_tree = self._adaptor.createWithPayload(IDENTIFIER9)
                    self._adaptor.addChild(root_0, IDENTIFIER9_tree)




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
                self.memoize(self.input, 3, param_StartIndex, success)

            pass
        return retval

    # $ANTLR end "param"

    class parameters_return(ParserRuleReturnScope):
        def __init__(self):
            super(gleamParser.parameters_return, self).__init__()

            self.tree = None




    # $ANTLR start "parameters"
    # gleampython/gleam.g:51:1: parameters : LPAREN IDENTIFIER RPAREN ;
    def parameters(self, ):

        retval = self.parameters_return()
        retval.start = self.input.LT(1)
        parameters_StartIndex = self.input.index()
        root_0 = None

        LPAREN10 = None
        IDENTIFIER11 = None
        RPAREN12 = None

        LPAREN10_tree = None
        IDENTIFIER11_tree = None
        RPAREN12_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 4):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # gleampython/gleam.g:51:12: ( LPAREN IDENTIFIER RPAREN )
                # gleampython/gleam.g:51:14: LPAREN IDENTIFIER RPAREN
                pass 
                root_0 = self._adaptor.nil()

                LPAREN10=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_parameters229)
                if self._state.backtracking == 0:

                    LPAREN10_tree = self._adaptor.createWithPayload(LPAREN10)
                    self._adaptor.addChild(root_0, LPAREN10_tree)

                IDENTIFIER11=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_parameters231)
                if self._state.backtracking == 0:

                    IDENTIFIER11_tree = self._adaptor.createWithPayload(IDENTIFIER11)
                    self._adaptor.addChild(root_0, IDENTIFIER11_tree)

                RPAREN12=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_parameters233)
                if self._state.backtracking == 0:

                    RPAREN12_tree = self._adaptor.createWithPayload(RPAREN12)
                    self._adaptor.addChild(root_0, RPAREN12_tree)




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
                self.memoize(self.input, 4, parameters_StartIndex, success)

            pass
        return retval

    # $ANTLR end "parameters"

    class block_return(ParserRuleReturnScope):
        def __init__(self):
            super(gleamParser.block_return, self).__init__()

            self.tree = None




    # $ANTLR start "block"
    # gleampython/gleam.g:52:1: block : LBRACE ( stmt )* RBRACE -> ^( BLOCK ( stmt )* ) ;
    def block(self, ):

        retval = self.block_return()
        retval.start = self.input.LT(1)
        block_StartIndex = self.input.index()
        root_0 = None

        LBRACE13 = None
        RBRACE15 = None
        stmt14 = None


        LBRACE13_tree = None
        RBRACE15_tree = None
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_stmt = RewriteRuleSubtreeStream(self._adaptor, "rule stmt")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 5):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # gleampython/gleam.g:52:7: ( LBRACE ( stmt )* RBRACE -> ^( BLOCK ( stmt )* ) )
                # gleampython/gleam.g:52:9: LBRACE ( stmt )* RBRACE
                pass 
                LBRACE13=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_block240) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE13)
                # gleampython/gleam.g:52:16: ( stmt )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if ((MACRO <= LA5_0 <= IDENTIFIER) or LA5_0 == NODE) :
                        alt5 = 1


                    if alt5 == 1:
                        # gleampython/gleam.g:0:0: stmt
                        pass 
                        self._state.following.append(self.FOLLOW_stmt_in_block242)
                        stmt14 = self.stmt()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_stmt.add(stmt14.tree)


                    else:
                        break #loop5
                RBRACE15=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_block245) 
                if self._state.backtracking == 0:
                    stream_RBRACE.add(RBRACE15)

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
                    # 52:29: -> ^( BLOCK ( stmt )* )
                    # gleampython/gleam.g:52:32: ^( BLOCK ( stmt )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(BLOCK, "BLOCK"), root_1)

                    # gleampython/gleam.g:52:40: ( stmt )*
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
                self.memoize(self.input, 5, block_StartIndex, success)

            pass
        return retval

    # $ANTLR end "block"

    class stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(gleamParser.stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "stmt"
    # gleampython/gleam.g:53:1: stmt : ( macro | NODE IDENTIFIER ( args )? ( expr )? -> ^( NODE IDENTIFIER ( args )? ( expr )? ) | call );
    def stmt(self, ):

        retval = self.stmt_return()
        retval.start = self.input.LT(1)
        stmt_StartIndex = self.input.index()
        root_0 = None

        NODE17 = None
        IDENTIFIER18 = None
        macro16 = None

        args19 = None

        expr20 = None

        call21 = None


        NODE17_tree = None
        IDENTIFIER18_tree = None
        stream_NODE = RewriteRuleTokenStream(self._adaptor, "token NODE")
        stream_IDENTIFIER = RewriteRuleTokenStream(self._adaptor, "token IDENTIFIER")
        stream_args = RewriteRuleSubtreeStream(self._adaptor, "rule args")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 6):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # gleampython/gleam.g:53:6: ( macro | NODE IDENTIFIER ( args )? ( expr )? -> ^( NODE IDENTIFIER ( args )? ( expr )? ) | call )
                alt8 = 3
                LA8 = self.input.LA(1)
                if LA8 == MACRO:
                    alt8 = 1
                elif LA8 == NODE:
                    alt8 = 2
                elif LA8 == IDENTIFIER:
                    alt8 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 8, 0, self.input)

                    raise nvae

                if alt8 == 1:
                    # gleampython/gleam.g:53:8: macro
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_macro_in_stmt261)
                    macro16 = self.macro()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, macro16.tree)


                elif alt8 == 2:
                    # gleampython/gleam.g:54:8: NODE IDENTIFIER ( args )? ( expr )?
                    pass 
                    NODE17=self.match(self.input, NODE, self.FOLLOW_NODE_in_stmt270) 
                    if self._state.backtracking == 0:
                        stream_NODE.add(NODE17)
                    IDENTIFIER18=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_stmt272) 
                    if self._state.backtracking == 0:
                        stream_IDENTIFIER.add(IDENTIFIER18)
                    # gleampython/gleam.g:54:24: ( args )?
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == LPAREN) :
                        alt6 = 1
                    if alt6 == 1:
                        # gleampython/gleam.g:0:0: args
                        pass 
                        self._state.following.append(self.FOLLOW_args_in_stmt274)
                        args19 = self.args()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_args.add(args19.tree)



                    # gleampython/gleam.g:54:30: ( expr )?
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == LBRACE or (STRINGLITERAL <= LA7_0 <= NUMBER)) :
                        alt7 = 1
                    elif (LA7_0 == IDENTIFIER) :
                        LA7_2 = self.input.LA(2)

                        if (self.synpred8_gleam()) :
                            alt7 = 1
                    if alt7 == 1:
                        # gleampython/gleam.g:0:0: expr
                        pass 
                        self._state.following.append(self.FOLLOW_expr_in_stmt277)
                        expr20 = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_expr.add(expr20.tree)




                    # AST Rewrite
                    # elements: IDENTIFIER, NODE, args, expr
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
                        # 54:36: -> ^( NODE IDENTIFIER ( args )? ( expr )? )
                        # gleampython/gleam.g:54:39: ^( NODE IDENTIFIER ( args )? ( expr )? )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(stream_NODE.nextNode(), root_1)

                        self._adaptor.addChild(root_1, stream_IDENTIFIER.nextNode())
                        # gleampython/gleam.g:54:57: ( args )?
                        if stream_args.hasNext():
                            self._adaptor.addChild(root_1, stream_args.nextTree())


                        stream_args.reset();
                        # gleampython/gleam.g:54:63: ( expr )?
                        if stream_expr.hasNext():
                            self._adaptor.addChild(root_1, stream_expr.nextTree())


                        stream_expr.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt8 == 3:
                    # gleampython/gleam.g:55:8: call
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_call_in_stmt301)
                    call21 = self.call()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, call21.tree)


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
                self.memoize(self.input, 6, stmt_StartIndex, success)

            pass
        return retval

    # $ANTLR end "stmt"

    class call_return(ParserRuleReturnScope):
        def __init__(self):
            super(gleamParser.call_return, self).__init__()

            self.tree = None




    # $ANTLR start "call"
    # gleampython/gleam.g:57:1: call : IDENTIFIER ( args )? ( expr )? -> ^( CALL IDENTIFIER ( args )? ( expr )? ) ;
    def call(self, ):

        retval = self.call_return()
        retval.start = self.input.LT(1)
        call_StartIndex = self.input.index()
        root_0 = None

        IDENTIFIER22 = None
        args23 = None

        expr24 = None


        IDENTIFIER22_tree = None
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

                # gleampython/gleam.g:57:6: ( IDENTIFIER ( args )? ( expr )? -> ^( CALL IDENTIFIER ( args )? ( expr )? ) )
                # gleampython/gleam.g:57:8: IDENTIFIER ( args )? ( expr )?
                pass 
                IDENTIFIER22=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_call314) 
                if self._state.backtracking == 0:
                    stream_IDENTIFIER.add(IDENTIFIER22)
                # gleampython/gleam.g:57:19: ( args )?
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == LPAREN) :
                    alt9 = 1
                if alt9 == 1:
                    # gleampython/gleam.g:0:0: args
                    pass 
                    self._state.following.append(self.FOLLOW_args_in_call316)
                    args23 = self.args()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_args.add(args23.tree)



                # gleampython/gleam.g:57:25: ( expr )?
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == LBRACE or (STRINGLITERAL <= LA10_0 <= NUMBER)) :
                    alt10 = 1
                elif (LA10_0 == IDENTIFIER) :
                    LA10_2 = self.input.LA(2)

                    if (self.synpred11_gleam()) :
                        alt10 = 1
                if alt10 == 1:
                    # gleampython/gleam.g:0:0: expr
                    pass 
                    self._state.following.append(self.FOLLOW_expr_in_call319)
                    expr24 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr24.tree)




                # AST Rewrite
                # elements: args, IDENTIFIER, expr
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
                    # 57:31: -> ^( CALL IDENTIFIER ( args )? ( expr )? )
                    # gleampython/gleam.g:57:34: ^( CALL IDENTIFIER ( args )? ( expr )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(CALL, "CALL"), root_1)

                    self._adaptor.addChild(root_1, stream_IDENTIFIER.nextNode())
                    # gleampython/gleam.g:57:52: ( args )?
                    if stream_args.hasNext():
                        self._adaptor.addChild(root_1, stream_args.nextTree())


                    stream_args.reset();
                    # gleampython/gleam.g:57:58: ( expr )?
                    if stream_expr.hasNext():
                        self._adaptor.addChild(root_1, stream_expr.nextTree())


                    stream_expr.reset();

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
                self.memoize(self.input, 7, call_StartIndex, success)

            pass
        return retval

    # $ANTLR end "call"

    class args_return(ParserRuleReturnScope):
        def __init__(self):
            super(gleamParser.args_return, self).__init__()

            self.tree = None




    # $ANTLR start "args"
    # gleampython/gleam.g:58:1: args : lparen= LPAREN ( arg ( ',' arg )* )? RPAREN -> ^( ARGS[$lparen] ( arg )* ) ;
    def args(self, ):

        retval = self.args_return()
        retval.start = self.input.LT(1)
        args_StartIndex = self.input.index()
        root_0 = None

        lparen = None
        char_literal26 = None
        RPAREN28 = None
        arg25 = None

        arg27 = None


        lparen_tree = None
        char_literal26_tree = None
        RPAREN28_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_35 = RewriteRuleTokenStream(self._adaptor, "token 35")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_arg = RewriteRuleSubtreeStream(self._adaptor, "rule arg")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 8):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # gleampython/gleam.g:58:6: (lparen= LPAREN ( arg ( ',' arg )* )? RPAREN -> ^( ARGS[$lparen] ( arg )* ) )
                # gleampython/gleam.g:58:8: lparen= LPAREN ( arg ( ',' arg )* )? RPAREN
                pass 
                lparen=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_args343) 
                if self._state.backtracking == 0:
                    stream_LPAREN.add(lparen)
                # gleampython/gleam.g:58:22: ( arg ( ',' arg )* )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == IDENTIFIER) :
                    alt12 = 1
                if alt12 == 1:
                    # gleampython/gleam.g:58:23: arg ( ',' arg )*
                    pass 
                    self._state.following.append(self.FOLLOW_arg_in_args346)
                    arg25 = self.arg()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_arg.add(arg25.tree)
                    # gleampython/gleam.g:58:27: ( ',' arg )*
                    while True: #loop11
                        alt11 = 2
                        LA11_0 = self.input.LA(1)

                        if (LA11_0 == 35) :
                            alt11 = 1


                        if alt11 == 1:
                            # gleampython/gleam.g:58:28: ',' arg
                            pass 
                            char_literal26=self.match(self.input, 35, self.FOLLOW_35_in_args349) 
                            if self._state.backtracking == 0:
                                stream_35.add(char_literal26)
                            self._state.following.append(self.FOLLOW_arg_in_args351)
                            arg27 = self.arg()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_arg.add(arg27.tree)


                        else:
                            break #loop11



                RPAREN28=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_args357) 
                if self._state.backtracking == 0:
                    stream_RPAREN.add(RPAREN28)

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
                    # 58:47: -> ^( ARGS[$lparen] ( arg )* )
                    # gleampython/gleam.g:58:50: ^( ARGS[$lparen] ( arg )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.create(ARGS, lparen), root_1)

                    # gleampython/gleam.g:58:66: ( arg )*
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
                self.memoize(self.input, 8, args_StartIndex, success)

            pass
        return retval

    # $ANTLR end "args"

    class arg_return(ParserRuleReturnScope):
        def __init__(self):
            super(gleamParser.arg_return, self).__init__()

            self.tree = None




    # $ANTLR start "arg"
    # gleampython/gleam.g:59:1: arg : IDENTIFIER EQUALS expr -> ^( IDENTIFIER expr ) ;
    def arg(self, ):

        retval = self.arg_return()
        retval.start = self.input.LT(1)
        arg_StartIndex = self.input.index()
        root_0 = None

        IDENTIFIER29 = None
        EQUALS30 = None
        expr31 = None


        IDENTIFIER29_tree = None
        EQUALS30_tree = None
        stream_EQUALS = RewriteRuleTokenStream(self._adaptor, "token EQUALS")
        stream_IDENTIFIER = RewriteRuleTokenStream(self._adaptor, "token IDENTIFIER")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 9):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # gleampython/gleam.g:59:5: ( IDENTIFIER EQUALS expr -> ^( IDENTIFIER expr ) )
                # gleampython/gleam.g:59:7: IDENTIFIER EQUALS expr
                pass 
                IDENTIFIER29=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_arg374) 
                if self._state.backtracking == 0:
                    stream_IDENTIFIER.add(IDENTIFIER29)
                EQUALS30=self.match(self.input, EQUALS, self.FOLLOW_EQUALS_in_arg376) 
                if self._state.backtracking == 0:
                    stream_EQUALS.add(EQUALS30)
                self._state.following.append(self.FOLLOW_expr_in_arg378)
                expr31 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expr.add(expr31.tree)

                # AST Rewrite
                # elements: IDENTIFIER, expr
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
                    # 59:30: -> ^( IDENTIFIER expr )
                    # gleampython/gleam.g:59:33: ^( IDENTIFIER expr )
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
                self.memoize(self.input, 9, arg_StartIndex, success)

            pass
        return retval

    # $ANTLR end "arg"

    class expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(gleamParser.expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "expr"
    # gleampython/gleam.g:60:1: expr : ( STRINGLITERAL | NUMBER | IDENTIFIER | block );
    def expr(self, ):

        retval = self.expr_return()
        retval.start = self.input.LT(1)
        expr_StartIndex = self.input.index()
        root_0 = None

        STRINGLITERAL32 = None
        NUMBER33 = None
        IDENTIFIER34 = None
        block35 = None


        STRINGLITERAL32_tree = None
        NUMBER33_tree = None
        IDENTIFIER34_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 10):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # gleampython/gleam.g:60:6: ( STRINGLITERAL | NUMBER | IDENTIFIER | block )
                alt13 = 4
                LA13 = self.input.LA(1)
                if LA13 == STRINGLITERAL:
                    alt13 = 1
                elif LA13 == NUMBER:
                    alt13 = 2
                elif LA13 == IDENTIFIER:
                    alt13 = 3
                elif LA13 == LBRACE:
                    alt13 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 13, 0, self.input)

                    raise nvae

                if alt13 == 1:
                    # gleampython/gleam.g:60:8: STRINGLITERAL
                    pass 
                    root_0 = self._adaptor.nil()

                    STRINGLITERAL32=self.match(self.input, STRINGLITERAL, self.FOLLOW_STRINGLITERAL_in_expr393)
                    if self._state.backtracking == 0:

                        STRINGLITERAL32_tree = self._adaptor.createWithPayload(STRINGLITERAL32)
                        self._adaptor.addChild(root_0, STRINGLITERAL32_tree)



                elif alt13 == 2:
                    # gleampython/gleam.g:60:24: NUMBER
                    pass 
                    root_0 = self._adaptor.nil()

                    NUMBER33=self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_expr397)
                    if self._state.backtracking == 0:

                        NUMBER33_tree = self._adaptor.createWithPayload(NUMBER33)
                        self._adaptor.addChild(root_0, NUMBER33_tree)



                elif alt13 == 3:
                    # gleampython/gleam.g:60:33: IDENTIFIER
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENTIFIER34=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_expr401)
                    if self._state.backtracking == 0:

                        IDENTIFIER34_tree = self._adaptor.createWithPayload(IDENTIFIER34)
                        self._adaptor.addChild(root_0, IDENTIFIER34_tree)



                elif alt13 == 4:
                    # gleampython/gleam.g:60:46: block
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_block_in_expr405)
                    block35 = self.block()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, block35.tree)


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
                self.memoize(self.input, 10, expr_StartIndex, success)

            pass
        return retval

    # $ANTLR end "expr"

    class for_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(gleamParser.for_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "for_expr"
    # gleampython/gleam.g:61:1: for_expr : FOR IDENTIFIER IN IDENTIFIER block ;
    def for_expr(self, ):

        retval = self.for_expr_return()
        retval.start = self.input.LT(1)
        for_expr_StartIndex = self.input.index()
        root_0 = None

        FOR36 = None
        IDENTIFIER37 = None
        IN38 = None
        IDENTIFIER39 = None
        block40 = None


        FOR36_tree = None
        IDENTIFIER37_tree = None
        IN38_tree = None
        IDENTIFIER39_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 11):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # gleampython/gleam.g:61:10: ( FOR IDENTIFIER IN IDENTIFIER block )
                # gleampython/gleam.g:61:12: FOR IDENTIFIER IN IDENTIFIER block
                pass 
                root_0 = self._adaptor.nil()

                FOR36=self.match(self.input, FOR, self.FOLLOW_FOR_in_for_expr412)
                if self._state.backtracking == 0:

                    FOR36_tree = self._adaptor.createWithPayload(FOR36)
                    self._adaptor.addChild(root_0, FOR36_tree)

                IDENTIFIER37=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_for_expr414)
                if self._state.backtracking == 0:

                    IDENTIFIER37_tree = self._adaptor.createWithPayload(IDENTIFIER37)
                    self._adaptor.addChild(root_0, IDENTIFIER37_tree)

                IN38=self.match(self.input, IN, self.FOLLOW_IN_in_for_expr416)
                if self._state.backtracking == 0:

                    IN38_tree = self._adaptor.createWithPayload(IN38)
                    self._adaptor.addChild(root_0, IN38_tree)

                IDENTIFIER39=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_for_expr418)
                if self._state.backtracking == 0:

                    IDENTIFIER39_tree = self._adaptor.createWithPayload(IDENTIFIER39)
                    self._adaptor.addChild(root_0, IDENTIFIER39_tree)

                self._state.following.append(self.FOLLOW_block_in_for_expr420)
                block40 = self.block()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, block40.tree)



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
                self.memoize(self.input, 11, for_expr_StartIndex, success)

            pass
        return retval

    # $ANTLR end "for_expr"

    # $ANTLR start "synpred8_gleam"
    def synpred8_gleam_fragment(self, ):
        # gleampython/gleam.g:54:30: ( expr )
        # gleampython/gleam.g:54:30: expr
        pass 
        self._state.following.append(self.FOLLOW_expr_in_synpred8_gleam277)
        self.expr()

        self._state.following.pop()


    # $ANTLR end "synpred8_gleam"



    # $ANTLR start "synpred11_gleam"
    def synpred11_gleam_fragment(self, ):
        # gleampython/gleam.g:57:25: ( expr )
        # gleampython/gleam.g:57:25: expr
        pass 
        self._state.following.append(self.FOLLOW_expr_in_synpred11_gleam319)
        self.expr()

        self._state.following.pop()


    # $ANTLR end "synpred11_gleam"




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

    def synpred11_gleam(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred11_gleam_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



 

    FOLLOW_stmt_in_prog142 = frozenset([1, 13, 14, 19])
    FOLLOW_MACRO_in_macro159 = frozenset([14])
    FOLLOW_IDENTIFIER_in_macro161 = frozenset([15])
    FOLLOW_LPAREN_in_macro165 = frozenset([14, 16])
    FOLLOW_param_in_macro168 = frozenset([16, 35])
    FOLLOW_35_in_macro171 = frozenset([14])
    FOLLOW_param_in_macro173 = frozenset([16, 35])
    FOLLOW_RPAREN_in_macro179 = frozenset([14, 17])
    FOLLOW_IDENTIFIER_in_macro183 = frozenset([14, 17])
    FOLLOW_block_in_macro186 = frozenset([1])
    FOLLOW_IDENTIFIER_in_param222 = frozenset([1])
    FOLLOW_LPAREN_in_parameters229 = frozenset([14])
    FOLLOW_IDENTIFIER_in_parameters231 = frozenset([16])
    FOLLOW_RPAREN_in_parameters233 = frozenset([1])
    FOLLOW_LBRACE_in_block240 = frozenset([13, 14, 18, 19])
    FOLLOW_stmt_in_block242 = frozenset([13, 14, 18, 19])
    FOLLOW_RBRACE_in_block245 = frozenset([1])
    FOLLOW_macro_in_stmt261 = frozenset([1])
    FOLLOW_NODE_in_stmt270 = frozenset([14])
    FOLLOW_IDENTIFIER_in_stmt272 = frozenset([1, 14, 15, 17, 21, 22])
    FOLLOW_args_in_stmt274 = frozenset([1, 14, 17, 21, 22])
    FOLLOW_expr_in_stmt277 = frozenset([1])
    FOLLOW_call_in_stmt301 = frozenset([1])
    FOLLOW_IDENTIFIER_in_call314 = frozenset([1, 14, 15, 17, 21, 22])
    FOLLOW_args_in_call316 = frozenset([1, 14, 17, 21, 22])
    FOLLOW_expr_in_call319 = frozenset([1])
    FOLLOW_LPAREN_in_args343 = frozenset([14, 16])
    FOLLOW_arg_in_args346 = frozenset([16, 35])
    FOLLOW_35_in_args349 = frozenset([14])
    FOLLOW_arg_in_args351 = frozenset([16, 35])
    FOLLOW_RPAREN_in_args357 = frozenset([1])
    FOLLOW_IDENTIFIER_in_arg374 = frozenset([20])
    FOLLOW_EQUALS_in_arg376 = frozenset([14, 17, 21, 22])
    FOLLOW_expr_in_arg378 = frozenset([1])
    FOLLOW_STRINGLITERAL_in_expr393 = frozenset([1])
    FOLLOW_NUMBER_in_expr397 = frozenset([1])
    FOLLOW_IDENTIFIER_in_expr401 = frozenset([1])
    FOLLOW_block_in_expr405 = frozenset([1])
    FOLLOW_FOR_in_for_expr412 = frozenset([14])
    FOLLOW_IDENTIFIER_in_for_expr414 = frozenset([24])
    FOLLOW_IN_in_for_expr416 = frozenset([14])
    FOLLOW_IDENTIFIER_in_for_expr418 = frozenset([14, 17])
    FOLLOW_block_in_for_expr420 = frozenset([1])
    FOLLOW_expr_in_synpred8_gleam277 = frozenset([1])
    FOLLOW_expr_in_synpred11_gleam319 = frozenset([1])



       
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
