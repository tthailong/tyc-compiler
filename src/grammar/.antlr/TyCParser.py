# Generated from d:\Long\Theory\Principles of Programming Languages\BTL\tyc-compiler\src\grammar\TyC.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\64")
        buf.write("V\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\5\3\5\5\5.\n\5\3\6\3\6\3\6\3\6\5\6\64\n\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\5\7;\n\7\3\b\3\b\3\b\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\5\13N\n")
        buf.write("\13\3\f\3\f\5\fR\n\f\3\r\3\r\3\r\2\2\16\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\2\3\5\2\13\13\16\16\20\20\2N\2\32\3\2")
        buf.write("\2\2\4 \3\2\2\2\6\"\3\2\2\2\b-\3\2\2\2\n\63\3\2\2\2\f")
        buf.write(":\3\2\2\2\16<\3\2\2\2\20?\3\2\2\2\22A\3\2\2\2\24M\3\2")
        buf.write("\2\2\26Q\3\2\2\2\30S\3\2\2\2\32\33\7-\2\2\33\34\7.\2\2")
        buf.write("\34\35\7/\2\2\35\36\7\60\2\2\36\37\7\2\2\3\37\3\3\2\2")
        buf.write("\2 !\t\2\2\2!\5\3\2\2\2\"#\5\b\5\2#$\7-\2\2$%\7\'\2\2")
        buf.write("%&\5\n\6\2&\'\7(\2\2\'(\7)\2\2()\5\20\t\2)*\7*\2\2*\7")
        buf.write("\3\2\2\2+.\5\4\3\2,.\7\23\2\2-+\3\2\2\2-,\3\2\2\2.\t\3")
        buf.write("\2\2\2/\60\5\16\b\2\60\61\5\f\7\2\61\64\3\2\2\2\62\64")
        buf.write("\3\2\2\2\63/\3\2\2\2\63\62\3\2\2\2\64\13\3\2\2\2\65\66")
        buf.write("\7+\2\2\66\67\5\16\b\2\678\5\f\7\28;\3\2\2\29;\3\2\2\2")
        buf.write(":\65\3\2\2\2:9\3\2\2\2;\r\3\2\2\2<=\5\4\3\2=>\7-\2\2>")
        buf.write("\17\3\2\2\2?@\7\3\2\2@\21\3\2\2\2AB\7-\2\2BC\7)\2\2CD")
        buf.write("\5\24\13\2DE\7*\2\2EF\7,\2\2F\23\3\2\2\2GH\5\26\f\2HI")
        buf.write("\7-\2\2IJ\7,\2\2JK\5\24\13\2KN\3\2\2\2LN\3\2\2\2MG\3\2")
        buf.write("\2\2ML\3\2\2\2N\25\3\2\2\2OR\5\4\3\2PR\7-\2\2QO\3\2\2")
        buf.write("\2QP\3\2\2\2R\27\3\2\2\2ST\7\4\2\2T\31\3\2\2\2\7-\63:")
        buf.write("MQ")
        return buf.getvalue()


class TyCParser ( Parser ):

    grammarFileName = "TyC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'statementlist'", "'structvardecl'", 
                     "'auto'", "'break'", "'case'", "'continue'", "'default'", 
                     "'else'", "'float'", "'for'", "'if'", "'int'", "'return'", 
                     "'string'", "'struct'", "'switch'", "'void'", "'while'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", 
                     "'<'", "'>'", "'<='", "'>='", "'||'", "'&&'", "'!'", 
                     "'++'", "'--'", "'='", "'.'", "'('", "')'", "'{'", 
                     "'}'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "AUTO", "BREAK", 
                      "CASE", "CONTINUE", "DEFAULT", "ELSE", "FLOAT", "FOR", 
                      "IF", "INT", "RETURN", "STRING", "STRUCT", "SWITCH", 
                      "VOID", "WHILE", "ADD", "SUB", "MUL", "DIV", "MOD", 
                      "EQUAL", "NOTEQUAL", "LESSTHAN", "GREATERTHAN", "LESSTHAN_EQUAL", 
                      "GREATERTHAN_EQUAL", "OR", "AND", "NOT", "INCREMENT", 
                      "DECREMENT", "ASSIGN", "ACCESS", "LP", "RP", "LB", 
                      "RB", "CM", "SM", "ID", "INTLIT", "FLOATLIT", "STRINGLIT", 
                      "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_typ = 1
    RULE_funcdecl = 2
    RULE_rettyp = 3
    RULE_paramlist = 4
    RULE_paramtail = 5
    RULE_pardecl = 6
    RULE_stmtlist = 7
    RULE_structdecl = 8
    RULE_memlist = 9
    RULE_memtyp = 10
    RULE_structvardecl = 11

    ruleNames =  [ "program", "typ", "funcdecl", "rettyp", "paramlist", 
                   "paramtail", "pardecl", "stmtlist", "structdecl", "memlist", 
                   "memtyp", "structvardecl" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    AUTO=3
    BREAK=4
    CASE=5
    CONTINUE=6
    DEFAULT=7
    ELSE=8
    FLOAT=9
    FOR=10
    IF=11
    INT=12
    RETURN=13
    STRING=14
    STRUCT=15
    SWITCH=16
    VOID=17
    WHILE=18
    ADD=19
    SUB=20
    MUL=21
    DIV=22
    MOD=23
    EQUAL=24
    NOTEQUAL=25
    LESSTHAN=26
    GREATERTHAN=27
    LESSTHAN_EQUAL=28
    GREATERTHAN_EQUAL=29
    OR=30
    AND=31
    NOT=32
    INCREMENT=33
    DECREMENT=34
    ASSIGN=35
    ACCESS=36
    LP=37
    RP=38
    LB=39
    RB=40
    CM=41
    SM=42
    ID=43
    INTLIT=44
    FLOATLIT=45
    STRINGLIT=46
    WS=47
    ILLEGAL_ESCAPE=48
    UNCLOSE_STRING=49
    ERROR_CHAR=50

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def INTLIT(self):
            return self.getToken(TyCParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(TyCParser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(TyCParser.STRINGLIT, 0)

        def EOF(self):
            return self.getToken(TyCParser.EOF, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_program




    def program(self):

        localctx = TyCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(TyCParser.ID)
            self.state = 25
            self.match(TyCParser.INTLIT)
            self.state = 26
            self.match(TyCParser.FLOATLIT)
            self.state = 27
            self.match(TyCParser.STRINGLIT)
            self.state = 28
            self.match(TyCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(TyCParser.INT, 0)

        def FLOAT(self):
            return self.getToken(TyCParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(TyCParser.STRING, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_typ




    def typ(self):

        localctx = TyCParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TyCParser.FLOAT) | (1 << TyCParser.INT) | (1 << TyCParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rettyp(self):
            return self.getTypedRuleContext(TyCParser.RettypContext,0)


        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def LP(self):
            return self.getToken(TyCParser.LP, 0)

        def paramlist(self):
            return self.getTypedRuleContext(TyCParser.ParamlistContext,0)


        def RP(self):
            return self.getToken(TyCParser.RP, 0)

        def LB(self):
            return self.getToken(TyCParser.LB, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(TyCParser.StmtlistContext,0)


        def RB(self):
            return self.getToken(TyCParser.RB, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_funcdecl




    def funcdecl(self):

        localctx = TyCParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.rettyp()
            self.state = 33
            self.match(TyCParser.ID)
            self.state = 34
            self.match(TyCParser.LP)
            self.state = 35
            self.paramlist()
            self.state = 36
            self.match(TyCParser.RP)
            self.state = 37
            self.match(TyCParser.LB)
            self.state = 38
            self.stmtlist()
            self.state = 39
            self.match(TyCParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RettypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(TyCParser.TypContext,0)


        def VOID(self):
            return self.getToken(TyCParser.VOID, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_rettyp




    def rettyp(self):

        localctx = TyCParser.RettypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_rettyp)
        try:
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.FLOAT, TyCParser.INT, TyCParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.typ()
                pass
            elif token in [TyCParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.match(TyCParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pardecl(self):
            return self.getTypedRuleContext(TyCParser.PardeclContext,0)


        def paramtail(self):
            return self.getTypedRuleContext(TyCParser.ParamtailContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_paramlist




    def paramlist(self):

        localctx = TyCParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_paramlist)
        try:
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.FLOAT, TyCParser.INT, TyCParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.pardecl()
                self.state = 46
                self.paramtail()
                pass
            elif token in [TyCParser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamtailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(TyCParser.CM, 0)

        def pardecl(self):
            return self.getTypedRuleContext(TyCParser.PardeclContext,0)


        def paramtail(self):
            return self.getTypedRuleContext(TyCParser.ParamtailContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_paramtail




    def paramtail(self):

        localctx = TyCParser.ParamtailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_paramtail)
        try:
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.match(TyCParser.CM)
                self.state = 52
                self.pardecl()
                self.state = 53
                self.paramtail()
                pass
            elif token in [TyCParser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(TyCParser.TypContext,0)


        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_pardecl




    def pardecl(self):

        localctx = TyCParser.PardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_pardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.typ()
            self.state = 59
            self.match(TyCParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TyCParser.RULE_stmtlist




    def stmtlist(self):

        localctx = TyCParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_stmtlist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(TyCParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def LB(self):
            return self.getToken(TyCParser.LB, 0)

        def memlist(self):
            return self.getTypedRuleContext(TyCParser.MemlistContext,0)


        def RB(self):
            return self.getToken(TyCParser.RB, 0)

        def SM(self):
            return self.getToken(TyCParser.SM, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_structdecl




    def structdecl(self):

        localctx = TyCParser.StructdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_structdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(TyCParser.ID)
            self.state = 64
            self.match(TyCParser.LB)
            self.state = 65
            self.memlist()
            self.state = 66
            self.match(TyCParser.RB)
            self.state = 67
            self.match(TyCParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def memtyp(self):
            return self.getTypedRuleContext(TyCParser.MemtypContext,0)


        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def SM(self):
            return self.getToken(TyCParser.SM, 0)

        def memlist(self):
            return self.getTypedRuleContext(TyCParser.MemlistContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_memlist




    def memlist(self):

        localctx = TyCParser.MemlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_memlist)
        try:
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.FLOAT, TyCParser.INT, TyCParser.STRING, TyCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.memtyp()
                self.state = 70
                self.match(TyCParser.ID)
                self.state = 71
                self.match(TyCParser.SM)
                self.state = 72
                self.memlist()
                pass
            elif token in [TyCParser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemtypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(TyCParser.TypContext,0)


        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_memtyp




    def memtyp(self):

        localctx = TyCParser.MemtypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_memtyp)
        try:
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.FLOAT, TyCParser.INT, TyCParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.typ()
                pass
            elif token in [TyCParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.match(TyCParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructvardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TyCParser.RULE_structvardecl




    def structvardecl(self):

        localctx = TyCParser.StructvardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_structvardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(TyCParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





