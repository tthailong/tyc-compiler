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
        buf.write("\u0096\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\5\4\60\n\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\5\5<\n\5\3\6\3\6\3")
        buf.write("\6\3\6\5\6B\n\6\3\7\3\7\3\7\3\7\3\7\5\7I\n\7\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\5\13]\n\13\3\f\3\f\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\5\16l\n\16\3\17\3\17\3")
        buf.write("\17\3\17\5\17r\n\17\3\20\3\20\3\20\3\20\3\20\5\20y\n\20")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\5\23\u0094\n\23\3\23\2\2\24\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$\2\3\6\2\13\13\16\16")
        buf.write("\20\20--\2\u008e\2&\3\2\2\2\4,\3\2\2\2\6/\3\2\2\2\b;\3")
        buf.write("\2\2\2\nA\3\2\2\2\fH\3\2\2\2\16J\3\2\2\2\20M\3\2\2\2\22")
        buf.write("O\3\2\2\2\24\\\3\2\2\2\26^\3\2\2\2\30`\3\2\2\2\32k\3\2")
        buf.write("\2\2\34q\3\2\2\2\36x\3\2\2\2 z\3\2\2\2\"|\3\2\2\2$\u0093")
        buf.write("\3\2\2\2&\'\7-\2\2\'(\7.\2\2()\7/\2\2)*\7\60\2\2*+\7\2")
        buf.write("\2\3+\3\3\2\2\2,-\t\2\2\2-\5\3\2\2\2.\60\5\b\5\2/.\3\2")
        buf.write("\2\2/\60\3\2\2\2\60\61\3\2\2\2\61\62\7-\2\2\62\63\7\'")
        buf.write("\2\2\63\64\5\n\6\2\64\65\7(\2\2\65\66\7)\2\2\66\67\5\20")
        buf.write("\t\2\678\7*\2\28\7\3\2\2\29<\5\4\3\2:<\7\23\2\2;9\3\2")
        buf.write("\2\2;:\3\2\2\2<\t\3\2\2\2=>\5\16\b\2>?\5\f\7\2?B\3\2\2")
        buf.write("\2@B\3\2\2\2A=\3\2\2\2A@\3\2\2\2B\13\3\2\2\2CD\7+\2\2")
        buf.write("DE\5\16\b\2EF\5\f\7\2FI\3\2\2\2GI\3\2\2\2HC\3\2\2\2HG")
        buf.write("\3\2\2\2I\r\3\2\2\2JK\5\4\3\2KL\7-\2\2L\17\3\2\2\2MN\7")
        buf.write("\3\2\2N\21\3\2\2\2OP\7\21\2\2PQ\7-\2\2QR\7)\2\2RS\5\24")
        buf.write("\13\2ST\7*\2\2TU\7,\2\2U\23\3\2\2\2VW\5\26\f\2WX\7-\2")
        buf.write("\2XY\7,\2\2YZ\5\24\13\2Z]\3\2\2\2[]\3\2\2\2\\V\3\2\2\2")
        buf.write("\\[\3\2\2\2]\25\3\2\2\2^_\5\4\3\2_\27\3\2\2\2`a\7-\2\2")
        buf.write("ab\5\32\16\2bc\7,\2\2c\31\3\2\2\2dl\7-\2\2ef\7-\2\2fg")
        buf.write("\7%\2\2gh\7)\2\2hi\5\34\17\2ij\7*\2\2jl\3\2\2\2kd\3\2")
        buf.write("\2\2ke\3\2\2\2l\33\3\2\2\2mn\5 \21\2no\5\36\20\2or\3\2")
        buf.write("\2\2pr\3\2\2\2qm\3\2\2\2qp\3\2\2\2r\35\3\2\2\2st\7+\2")
        buf.write("\2tu\5 \21\2uv\5\36\20\2vy\3\2\2\2wy\3\2\2\2xs\3\2\2\2")
        buf.write("xw\3\2\2\2y\37\3\2\2\2z{\7\4\2\2{!\3\2\2\2|}\7-\2\2}~")
        buf.write("\7&\2\2~\177\7-\2\2\177#\3\2\2\2\u0080\u0081\7\5\2\2\u0081")
        buf.write("\u0082\7-\2\2\u0082\u0083\7%\2\2\u0083\u0084\5 \21\2\u0084")
        buf.write("\u0085\7,\2\2\u0085\u0094\3\2\2\2\u0086\u0087\7\5\2\2")
        buf.write("\u0087\u0088\7-\2\2\u0088\u0094\7,\2\2\u0089\u008a\5\4")
        buf.write("\3\2\u008a\u008b\7-\2\2\u008b\u008c\7%\2\2\u008c\u008d")
        buf.write("\5 \21\2\u008d\u008e\7,\2\2\u008e\u0094\3\2\2\2\u008f")
        buf.write("\u0090\5\4\3\2\u0090\u0091\7-\2\2\u0091\u0092\7,\2\2\u0092")
        buf.write("\u0094\3\2\2\2\u0093\u0080\3\2\2\2\u0093\u0086\3\2\2\2")
        buf.write("\u0093\u0089\3\2\2\2\u0093\u008f\3\2\2\2\u0094%\3\2\2")
        buf.write("\2\13/;AH\\kqx\u0093")
        return buf.getvalue()


class TyCParser ( Parser ):

    grammarFileName = "TyC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'statementlist'", "'expr'", "'auto'", 
                     "'break'", "'case'", "'continue'", "'default'", "'else'", 
                     "'float'", "'for'", "'if'", "'int'", "'return'", "'string'", 
                     "'struct'", "'switch'", "'void'", "'while'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", 
                     "'>'", "'<='", "'>='", "'||'", "'&&'", "'!'", "'++'", 
                     "'--'", "'='", "'.'", "'('", "')'", "'{'", "'}'", "','", 
                     "';'" ]

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
    RULE_structvar = 12
    RULE_exprlist = 13
    RULE_exprtail = 14
    RULE_expr = 15
    RULE_structmemaccess = 16
    RULE_vardecl = 17

    ruleNames =  [ "program", "typ", "funcdecl", "rettyp", "paramlist", 
                   "paramtail", "pardecl", "stmtlist", "structdecl", "memlist", 
                   "memtyp", "structvardecl", "structvar", "exprlist", "exprtail", 
                   "expr", "structmemaccess", "vardecl" ]

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
            self.state = 36
            self.match(TyCParser.ID)
            self.state = 37
            self.match(TyCParser.INTLIT)
            self.state = 38
            self.match(TyCParser.FLOATLIT)
            self.state = 39
            self.match(TyCParser.STRINGLIT)
            self.state = 40
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

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_typ




    def typ(self):

        localctx = TyCParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TyCParser.FLOAT) | (1 << TyCParser.INT) | (1 << TyCParser.STRING) | (1 << TyCParser.ID))) != 0)):
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

        def rettyp(self):
            return self.getTypedRuleContext(TyCParser.RettypContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_funcdecl




    def funcdecl(self):

        localctx = TyCParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 44
                self.rettyp()


            self.state = 47
            self.match(TyCParser.ID)
            self.state = 48
            self.match(TyCParser.LP)
            self.state = 49
            self.paramlist()
            self.state = 50
            self.match(TyCParser.RP)
            self.state = 51
            self.match(TyCParser.LB)
            self.state = 52
            self.stmtlist()
            self.state = 53
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
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.FLOAT, TyCParser.INT, TyCParser.STRING, TyCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.typ()
                pass
            elif token in [TyCParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
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
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.FLOAT, TyCParser.INT, TyCParser.STRING, TyCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.pardecl()
                self.state = 60
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
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.match(TyCParser.CM)
                self.state = 66
                self.pardecl()
                self.state = 67
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
            self.state = 72
            self.typ()
            self.state = 73
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
            self.state = 75
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

        def STRUCT(self):
            return self.getToken(TyCParser.STRUCT, 0)

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
            self.state = 77
            self.match(TyCParser.STRUCT)
            self.state = 78
            self.match(TyCParser.ID)
            self.state = 79
            self.match(TyCParser.LB)
            self.state = 80
            self.memlist()
            self.state = 81
            self.match(TyCParser.RB)
            self.state = 82
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
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.FLOAT, TyCParser.INT, TyCParser.STRING, TyCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.memtyp()
                self.state = 85
                self.match(TyCParser.ID)
                self.state = 86
                self.match(TyCParser.SM)
                self.state = 87
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


        def getRuleIndex(self):
            return TyCParser.RULE_memtyp




    def memtyp(self):

        localctx = TyCParser.MemtypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_memtyp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.typ()
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

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def structvar(self):
            return self.getTypedRuleContext(TyCParser.StructvarContext,0)


        def SM(self):
            return self.getToken(TyCParser.SM, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_structvardecl




    def structvardecl(self):

        localctx = TyCParser.StructvardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_structvardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(TyCParser.ID)
            self.state = 95
            self.structvar()
            self.state = 96
            self.match(TyCParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructvarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(TyCParser.ASSIGN, 0)

        def LB(self):
            return self.getToken(TyCParser.LB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(TyCParser.ExprlistContext,0)


        def RB(self):
            return self.getToken(TyCParser.RB, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_structvar




    def structvar(self):

        localctx = TyCParser.StructvarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_structvar)
        try:
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.match(TyCParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.match(TyCParser.ID)
                self.state = 100
                self.match(TyCParser.ASSIGN)
                self.state = 101
                self.match(TyCParser.LB)
                self.state = 102
                self.exprlist()
                self.state = 103
                self.match(TyCParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def exprtail(self):
            return self.getTypedRuleContext(TyCParser.ExprtailContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_exprlist




    def exprlist(self):

        localctx = TyCParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_exprlist)
        try:
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.expr()
                self.state = 108
                self.exprtail()
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


    class ExprtailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(TyCParser.CM, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def exprtail(self):
            return self.getTypedRuleContext(TyCParser.ExprtailContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_exprtail




    def exprtail(self):

        localctx = TyCParser.ExprtailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_exprtail)
        try:
            self.state = 118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.match(TyCParser.CM)
                self.state = 114
                self.expr()
                self.state = 115
                self.exprtail()
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TyCParser.RULE_expr




    def expr(self):

        localctx = TyCParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(TyCParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructmemaccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.ID)
            else:
                return self.getToken(TyCParser.ID, i)

        def ACCESS(self):
            return self.getToken(TyCParser.ACCESS, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_structmemaccess




    def structmemaccess(self):

        localctx = TyCParser.StructmemaccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_structmemaccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(TyCParser.ID)
            self.state = 123
            self.match(TyCParser.ACCESS)
            self.state = 124
            self.match(TyCParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AUTO(self):
            return self.getToken(TyCParser.AUTO, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(TyCParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def SM(self):
            return self.getToken(TyCParser.SM, 0)

        def typ(self):
            return self.getTypedRuleContext(TyCParser.TypContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_vardecl




    def vardecl(self):

        localctx = TyCParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_vardecl)
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.match(TyCParser.AUTO)
                self.state = 127
                self.match(TyCParser.ID)
                self.state = 128
                self.match(TyCParser.ASSIGN)
                self.state = 129
                self.expr()
                self.state = 130
                self.match(TyCParser.SM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.match(TyCParser.AUTO)
                self.state = 133
                self.match(TyCParser.ID)
                self.state = 134
                self.match(TyCParser.SM)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 135
                self.typ()
                self.state = 136
                self.match(TyCParser.ID)
                self.state = 137
                self.match(TyCParser.ASSIGN)
                self.state = 138
                self.expr()
                self.state = 139
                self.match(TyCParser.SM)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 141
                self.typ()
                self.state = 142
                self.match(TyCParser.ID)
                self.state = 143
                self.match(TyCParser.SM)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





