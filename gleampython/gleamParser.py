# $ANTLR 3.1.3 Mar 17, 2009 19:23:44 gleampython/gleam.g 2011-06-30 19:56:31

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
RBRACE=17
NODE=18
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
IN=23
T__34=34
SurrogateIdentifer=33
UnicodeEscape=26
STRINGLITERAL=20
IDENTIFIER=13
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

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "ARGS", "PROG", "PARAMS", "BLOCK", "PLUS", "MINUS", "MULT", "DIV", "MACRO", 
    "IDENTIFIER", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "NODE", "EQUALS", 
    "STRINGLITERAL", "NUMBER", "FOR", "IN", "DIGIT", "EscapeSequence", "UnicodeEscape", 
    "HexDigit", "WHITESPACE", "COMMENT", "LINE_COMMENT", "IdentifierStart", 
    "IdentifierPart", "SurrogateIdentifer", "','"
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
    # gleampython/gleam.g:46:1: prog : ( stmt )* -> ^( PROG ( stmt )* ) ;
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

                # gleampython/gleam.g:46:6: ( ( stmt )* -> ^( PROG ( stmt )* ) )
                # gleampython/gleam.g:46:8: ( stmt )*
                pass 
                # gleampython/gleam.g:46:8: ( stmt )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == MACRO or LA1_0 == NODE) :
                        alt1 = 1


                    if alt1 == 1:
                        # gleampython/gleam.g:0:0: stmt
                        pass 
                        self._state.following.append(self.FOLLOW_stmt_in_prog135)
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
                    # 46:14: -> ^( PROG ( stmt )* )
                    # gleampython/gleam.g:46:17: ^( PROG ( stmt )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROG, "PROG"), root_1)

                    # gleampython/gleam.g:46:24: ( stmt )*
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
    # gleampython/gleam.g:47:1: macro : MACRO IDENTIFIER lparen= '(' ( param ( ',' param )* )? ')' (value= IDENTIFIER )? block -> ^( MACRO IDENTIFIER ^( PARAMS[$lparen] ( param )* ) ( $value)? block ) ;
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
        stream_MACRO = RewriteRuleTokenStream(self._adaptor, "token MACRO")
        stream_IDENTIFIER = RewriteRuleTokenStream(self._adaptor, "token IDENTIFIER")
        stream_34 = RewriteRuleTokenStream(self._adaptor, "token 34")
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

                # gleampython/gleam.g:47:7: ( MACRO IDENTIFIER lparen= '(' ( param ( ',' param )* )? ')' (value= IDENTIFIER )? block -> ^( MACRO IDENTIFIER ^( PARAMS[$lparen] ( param )* ) ( $value)? block ) )
                # gleampython/gleam.g:47:9: MACRO IDENTIFIER lparen= '(' ( param ( ',' param )* )? ')' (value= IDENTIFIER )? block
                pass 
                MACRO2=self.match(self.input, MACRO, self.FOLLOW_MACRO_in_macro152) 
                if self._state.backtracking == 0:
                    stream_MACRO.add(MACRO2)
                IDENTIFIER3=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_macro154) 
                if self._state.backtracking == 0:
                    stream_IDENTIFIER.add(IDENTIFIER3)
                lparen=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_macro158) 
                if self._state.backtracking == 0:
                    stream_LPAREN.add(lparen)
                # gleampython/gleam.g:47:37: ( param ( ',' param )* )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == IDENTIFIER) :
                    alt3 = 1
                if alt3 == 1:
                    # gleampython/gleam.g:47:38: param ( ',' param )*
                    pass 
                    self._state.following.append(self.FOLLOW_param_in_macro161)
                    param4 = self.param()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_param.add(param4.tree)
                    # gleampython/gleam.g:47:44: ( ',' param )*
                    while True: #loop2
                        alt2 = 2
                        LA2_0 = self.input.LA(1)

                        if (LA2_0 == 34) :
                            alt2 = 1


                        if alt2 == 1:
                            # gleampython/gleam.g:47:45: ',' param
                            pass 
                            char_literal5=self.match(self.input, 34, self.FOLLOW_34_in_macro164) 
                            if self._state.backtracking == 0:
                                stream_34.add(char_literal5)
                            self._state.following.append(self.FOLLOW_param_in_macro166)
                            param6 = self.param()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_param.add(param6.tree)


                        else:
                            break #loop2



                char_literal7=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_macro172) 
                if self._state.backtracking == 0:
                    stream_RPAREN.add(char_literal7)
                # gleampython/gleam.g:47:68: (value= IDENTIFIER )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == IDENTIFIER) :
                    alt4 = 1
                if alt4 == 1:
                    # gleampython/gleam.g:0:0: value= IDENTIFIER
                    pass 
                    value=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_macro176) 
                    if self._state.backtracking == 0:
                        stream_IDENTIFIER.add(value)



                self._state.following.append(self.FOLLOW_block_in_macro179)
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
                    # 48:7: -> ^( MACRO IDENTIFIER ^( PARAMS[$lparen] ( param )* ) ( $value)? block )
                    # gleampython/gleam.g:48:10: ^( MACRO IDENTIFIER ^( PARAMS[$lparen] ( param )* ) ( $value)? block )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_MACRO.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_IDENTIFIER.nextNode())
                    # gleampython/gleam.g:48:29: ^( PARAMS[$lparen] ( param )* )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(self._adaptor.create(PARAMS, lparen), root_2)

                    # gleampython/gleam.g:48:47: ( param )*
                    while stream_param.hasNext():
                        self._adaptor.addChild(root_2, stream_param.nextTree())


                    stream_param.reset();

                    self._adaptor.addChild(root_1, root_2)
                    # gleampython/gleam.g:48:55: ( $value)?
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
    # gleampython/gleam.g:49:1: param : IDENTIFIER ;
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

                # gleampython/gleam.g:49:7: ( IDENTIFIER )
                # gleampython/gleam.g:49:9: IDENTIFIER
                pass 
                root_0 = self._adaptor.nil()

                IDENTIFIER9=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_param215)
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
    # gleampython/gleam.g:50:1: parameters : LPAREN IDENTIFIER RPAREN ;
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

                # gleampython/gleam.g:50:12: ( LPAREN IDENTIFIER RPAREN )
                # gleampython/gleam.g:50:14: LPAREN IDENTIFIER RPAREN
                pass 
                root_0 = self._adaptor.nil()

                LPAREN10=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_parameters222)
                if self._state.backtracking == 0:

                    LPAREN10_tree = self._adaptor.createWithPayload(LPAREN10)
                    self._adaptor.addChild(root_0, LPAREN10_tree)

                IDENTIFIER11=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_parameters224)
                if self._state.backtracking == 0:

                    IDENTIFIER11_tree = self._adaptor.createWithPayload(IDENTIFIER11)
                    self._adaptor.addChild(root_0, IDENTIFIER11_tree)

                RPAREN12=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_parameters226)
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
    # gleampython/gleam.g:51:1: block : LBRACE ( stmt )* RBRACE -> ^( BLOCK ( stmt )* ) ;
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

                # gleampython/gleam.g:51:7: ( LBRACE ( stmt )* RBRACE -> ^( BLOCK ( stmt )* ) )
                # gleampython/gleam.g:51:9: LBRACE ( stmt )* RBRACE
                pass 
                LBRACE13=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_block233) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE13)
                # gleampython/gleam.g:51:16: ( stmt )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == MACRO or LA5_0 == NODE) :
                        alt5 = 1


                    if alt5 == 1:
                        # gleampython/gleam.g:0:0: stmt
                        pass 
                        self._state.following.append(self.FOLLOW_stmt_in_block235)
                        stmt14 = self.stmt()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_stmt.add(stmt14.tree)


                    else:
                        break #loop5
                RBRACE15=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_block238) 
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
                    # 51:29: -> ^( BLOCK ( stmt )* )
                    # gleampython/gleam.g:51:32: ^( BLOCK ( stmt )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(BLOCK, "BLOCK"), root_1)

                    # gleampython/gleam.g:51:40: ( stmt )*
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
    # gleampython/gleam.g:52:1: stmt : ( macro | NODE IDENTIFIER ( args )? expr -> ^( NODE IDENTIFIER args expr ) );
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

                # gleampython/gleam.g:52:6: ( macro | NODE IDENTIFIER ( args )? expr -> ^( NODE IDENTIFIER args expr ) )
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == MACRO) :
                    alt7 = 1
                elif (LA7_0 == NODE) :
                    alt7 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 7, 0, self.input)

                    raise nvae

                if alt7 == 1:
                    # gleampython/gleam.g:52:8: macro
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_macro_in_stmt254)
                    macro16 = self.macro()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, macro16.tree)


                elif alt7 == 2:
                    # gleampython/gleam.g:53:8: NODE IDENTIFIER ( args )? expr
                    pass 
                    NODE17=self.match(self.input, NODE, self.FOLLOW_NODE_in_stmt263) 
                    if self._state.backtracking == 0:
                        stream_NODE.add(NODE17)
                    IDENTIFIER18=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_stmt265) 
                    if self._state.backtracking == 0:
                        stream_IDENTIFIER.add(IDENTIFIER18)
                    # gleampython/gleam.g:53:24: ( args )?
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == LPAREN) :
                        alt6 = 1
                    if alt6 == 1:
                        # gleampython/gleam.g:0:0: args
                        pass 
                        self._state.following.append(self.FOLLOW_args_in_stmt267)
                        args19 = self.args()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_args.add(args19.tree)



                    self._state.following.append(self.FOLLOW_expr_in_stmt270)
                    expr20 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr20.tree)

                    # AST Rewrite
                    # elements: NODE, expr, IDENTIFIER, args
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
                        # 53:35: -> ^( NODE IDENTIFIER args expr )
                        # gleampython/gleam.g:53:38: ^( NODE IDENTIFIER args expr )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(stream_NODE.nextNode(), root_1)

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
                self.memoize(self.input, 6, stmt_StartIndex, success)

            pass
        return retval

    # $ANTLR end "stmt"

    class args_return(ParserRuleReturnScope):
        def __init__(self):
            super(gleamParser.args_return, self).__init__()

            self.tree = None




    # $ANTLR start "args"
    # gleampython/gleam.g:55:1: args : lparen= LPAREN ( arg ( ',' arg )* )? RPAREN -> ^( ARGS[$lparen] ( arg )* ) ;
    def args(self, ):

        retval = self.args_return()
        retval.start = self.input.LT(1)
        args_StartIndex = self.input.index()
        root_0 = None

        lparen = None
        char_literal22 = None
        RPAREN24 = None
        arg21 = None

        arg23 = None


        lparen_tree = None
        char_literal22_tree = None
        RPAREN24_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_34 = RewriteRuleTokenStream(self._adaptor, "token 34")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_arg = RewriteRuleSubtreeStream(self._adaptor, "rule arg")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 7):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # gleampython/gleam.g:55:6: (lparen= LPAREN ( arg ( ',' arg )* )? RPAREN -> ^( ARGS[$lparen] ( arg )* ) )
                # gleampython/gleam.g:55:8: lparen= LPAREN ( arg ( ',' arg )* )? RPAREN
                pass 
                lparen=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_args297) 
                if self._state.backtracking == 0:
                    stream_LPAREN.add(lparen)
                # gleampython/gleam.g:55:22: ( arg ( ',' arg )* )?
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == IDENTIFIER) :
                    alt9 = 1
                if alt9 == 1:
                    # gleampython/gleam.g:55:23: arg ( ',' arg )*
                    pass 
                    self._state.following.append(self.FOLLOW_arg_in_args300)
                    arg21 = self.arg()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_arg.add(arg21.tree)
                    # gleampython/gleam.g:55:27: ( ',' arg )*
                    while True: #loop8
                        alt8 = 2
                        LA8_0 = self.input.LA(1)

                        if (LA8_0 == 34) :
                            alt8 = 1


                        if alt8 == 1:
                            # gleampython/gleam.g:55:28: ',' arg
                            pass 
                            char_literal22=self.match(self.input, 34, self.FOLLOW_34_in_args303) 
                            if self._state.backtracking == 0:
                                stream_34.add(char_literal22)
                            self._state.following.append(self.FOLLOW_arg_in_args305)
                            arg23 = self.arg()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_arg.add(arg23.tree)


                        else:
                            break #loop8



                RPAREN24=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_args311) 
                if self._state.backtracking == 0:
                    stream_RPAREN.add(RPAREN24)

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
                    # 55:47: -> ^( ARGS[$lparen] ( arg )* )
                    # gleampython/gleam.g:55:50: ^( ARGS[$lparen] ( arg )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.create(ARGS, lparen), root_1)

                    # gleampython/gleam.g:55:66: ( arg )*
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
                self.memoize(self.input, 7, args_StartIndex, success)

            pass
        return retval

    # $ANTLR end "args"

    class arg_return(ParserRuleReturnScope):
        def __init__(self):
            super(gleamParser.arg_return, self).__init__()

            self.tree = None




    # $ANTLR start "arg"
    # gleampython/gleam.g:56:1: arg : IDENTIFIER EQUALS expr -> ^( IDENTIFIER expr ) ;
    def arg(self, ):

        retval = self.arg_return()
        retval.start = self.input.LT(1)
        arg_StartIndex = self.input.index()
        root_0 = None

        IDENTIFIER25 = None
        EQUALS26 = None
        expr27 = None


        IDENTIFIER25_tree = None
        EQUALS26_tree = None
        stream_EQUALS = RewriteRuleTokenStream(self._adaptor, "token EQUALS")
        stream_IDENTIFIER = RewriteRuleTokenStream(self._adaptor, "token IDENTIFIER")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 8):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # gleampython/gleam.g:56:5: ( IDENTIFIER EQUALS expr -> ^( IDENTIFIER expr ) )
                # gleampython/gleam.g:56:7: IDENTIFIER EQUALS expr
                pass 
                IDENTIFIER25=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_arg328) 
                if self._state.backtracking == 0:
                    stream_IDENTIFIER.add(IDENTIFIER25)
                EQUALS26=self.match(self.input, EQUALS, self.FOLLOW_EQUALS_in_arg330) 
                if self._state.backtracking == 0:
                    stream_EQUALS.add(EQUALS26)
                self._state.following.append(self.FOLLOW_expr_in_arg332)
                expr27 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expr.add(expr27.tree)

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
                    # 56:30: -> ^( IDENTIFIER expr )
                    # gleampython/gleam.g:56:33: ^( IDENTIFIER expr )
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
                self.memoize(self.input, 8, arg_StartIndex, success)

            pass
        return retval

    # $ANTLR end "arg"

    class expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(gleamParser.expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "expr"
    # gleampython/gleam.g:57:1: expr : ( STRINGLITERAL | NUMBER | IDENTIFIER );
    def expr(self, ):

        retval = self.expr_return()
        retval.start = self.input.LT(1)
        expr_StartIndex = self.input.index()
        root_0 = None

        set28 = None

        set28_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 9):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # gleampython/gleam.g:57:6: ( STRINGLITERAL | NUMBER | IDENTIFIER )
                # gleampython/gleam.g:
                pass 
                root_0 = self._adaptor.nil()

                set28 = self.input.LT(1)
                if self.input.LA(1) == IDENTIFIER or (STRINGLITERAL <= self.input.LA(1) <= NUMBER):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set28))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





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
                self.memoize(self.input, 9, expr_StartIndex, success)

            pass
        return retval

    # $ANTLR end "expr"

    class for_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(gleamParser.for_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "for_expr"
    # gleampython/gleam.g:58:1: for_expr : FOR IDENTIFIER IN IDENTIFIER block ;
    def for_expr(self, ):

        retval = self.for_expr_return()
        retval.start = self.input.LT(1)
        for_expr_StartIndex = self.input.index()
        root_0 = None

        FOR29 = None
        IDENTIFIER30 = None
        IN31 = None
        IDENTIFIER32 = None
        block33 = None


        FOR29_tree = None
        IDENTIFIER30_tree = None
        IN31_tree = None
        IDENTIFIER32_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 10):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # gleampython/gleam.g:58:10: ( FOR IDENTIFIER IN IDENTIFIER block )
                # gleampython/gleam.g:58:12: FOR IDENTIFIER IN IDENTIFIER block
                pass 
                root_0 = self._adaptor.nil()

                FOR29=self.match(self.input, FOR, self.FOLLOW_FOR_in_for_expr362)
                if self._state.backtracking == 0:

                    FOR29_tree = self._adaptor.createWithPayload(FOR29)
                    self._adaptor.addChild(root_0, FOR29_tree)

                IDENTIFIER30=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_for_expr364)
                if self._state.backtracking == 0:

                    IDENTIFIER30_tree = self._adaptor.createWithPayload(IDENTIFIER30)
                    self._adaptor.addChild(root_0, IDENTIFIER30_tree)

                IN31=self.match(self.input, IN, self.FOLLOW_IN_in_for_expr366)
                if self._state.backtracking == 0:

                    IN31_tree = self._adaptor.createWithPayload(IN31)
                    self._adaptor.addChild(root_0, IN31_tree)

                IDENTIFIER32=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_for_expr368)
                if self._state.backtracking == 0:

                    IDENTIFIER32_tree = self._adaptor.createWithPayload(IDENTIFIER32)
                    self._adaptor.addChild(root_0, IDENTIFIER32_tree)

                self._state.following.append(self.FOLLOW_block_in_for_expr370)
                block33 = self.block()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, block33.tree)



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
                self.memoize(self.input, 10, for_expr_StartIndex, success)

            pass
        return retval

    # $ANTLR end "for_expr"


    # Delegated rules


 

    FOLLOW_stmt_in_prog135 = frozenset([1, 12, 18])
    FOLLOW_MACRO_in_macro152 = frozenset([13])
    FOLLOW_IDENTIFIER_in_macro154 = frozenset([14])
    FOLLOW_LPAREN_in_macro158 = frozenset([13, 15])
    FOLLOW_param_in_macro161 = frozenset([15, 34])
    FOLLOW_34_in_macro164 = frozenset([13])
    FOLLOW_param_in_macro166 = frozenset([15, 34])
    FOLLOW_RPAREN_in_macro172 = frozenset([13, 16])
    FOLLOW_IDENTIFIER_in_macro176 = frozenset([13, 16])
    FOLLOW_block_in_macro179 = frozenset([1])
    FOLLOW_IDENTIFIER_in_param215 = frozenset([1])
    FOLLOW_LPAREN_in_parameters222 = frozenset([13])
    FOLLOW_IDENTIFIER_in_parameters224 = frozenset([15])
    FOLLOW_RPAREN_in_parameters226 = frozenset([1])
    FOLLOW_LBRACE_in_block233 = frozenset([12, 17, 18])
    FOLLOW_stmt_in_block235 = frozenset([12, 17, 18])
    FOLLOW_RBRACE_in_block238 = frozenset([1])
    FOLLOW_macro_in_stmt254 = frozenset([1])
    FOLLOW_NODE_in_stmt263 = frozenset([13])
    FOLLOW_IDENTIFIER_in_stmt265 = frozenset([13, 14, 20, 21])
    FOLLOW_args_in_stmt267 = frozenset([13, 14, 20, 21])
    FOLLOW_expr_in_stmt270 = frozenset([1])
    FOLLOW_LPAREN_in_args297 = frozenset([13, 15])
    FOLLOW_arg_in_args300 = frozenset([15, 34])
    FOLLOW_34_in_args303 = frozenset([13])
    FOLLOW_arg_in_args305 = frozenset([15, 34])
    FOLLOW_RPAREN_in_args311 = frozenset([1])
    FOLLOW_IDENTIFIER_in_arg328 = frozenset([19])
    FOLLOW_EQUALS_in_arg330 = frozenset([13, 14, 20, 21])
    FOLLOW_expr_in_arg332 = frozenset([1])
    FOLLOW_set_in_expr0 = frozenset([1])
    FOLLOW_FOR_in_for_expr362 = frozenset([13])
    FOLLOW_IDENTIFIER_in_for_expr364 = frozenset([23])
    FOLLOW_IN_in_for_expr366 = frozenset([13])
    FOLLOW_IDENTIFIER_in_for_expr368 = frozenset([13, 16])
    FOLLOW_block_in_for_expr370 = frozenset([1])



       
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
