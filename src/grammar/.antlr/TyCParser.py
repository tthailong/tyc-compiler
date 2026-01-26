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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3-")
        buf.write("\b\4\2\t\2\3\2\3\2\3\2\3\2\2\2\3\2\2\2\2\6\2\4\3\2\2\2")
        buf.write("\4\5\7&\2\2\5\6\7\2\2\3\6\3\3\2\2\2\2")
        return buf.getvalue()


class TyCParser ( Parser ):

    grammarFileName = "TyC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'auto'", "'break'", "'case'", "'continue'", 
                     "'default'", "'else'", "'float'", "'for'", "'if'", 
                     "'int'", "'return'", "'string'", "'struct'", "'switch'", 
                     "'void'", "'while'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'||'", 
                     "'&&'", "'!'", "'++'", "'--'", "'='", "'.'" ]

    symbolicNames = [ "<INVALID>", "AUTO", "BREAK", "CASE", "CONTINUE", 
                      "DEFAULT", "ELSE", "FLOAT", "FOR", "IF", "INT", "RETURN", 
                      "STRING", "STRUCT", "SWITCH", "VOID", "WHILE", "ADD", 
                      "SUB", "MUL", "DIV", "MOD", "EQUAL", "NOTEQUAL", "LESSTHAN", 
                      "GREATERTHAN", "LESSTHAN_EQUAL", "GREATERTHAN_EQUAL", 
                      "OR", "AND", "NOT", "INCREMENT", "DECREMENT", "ASSIGN", 
                      "ACCESS", "SEPARATOR", "ID", "INTLIT", "FLOATLIT", 
                      "STRINGLIT", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    AUTO=1
    BREAK=2
    CASE=3
    CONTINUE=4
    DEFAULT=5
    ELSE=6
    FLOAT=7
    FOR=8
    IF=9
    INT=10
    RETURN=11
    STRING=12
    STRUCT=13
    SWITCH=14
    VOID=15
    WHILE=16
    ADD=17
    SUB=18
    MUL=19
    DIV=20
    MOD=21
    EQUAL=22
    NOTEQUAL=23
    LESSTHAN=24
    GREATERTHAN=25
    LESSTHAN_EQUAL=26
    GREATERTHAN_EQUAL=27
    OR=28
    AND=29
    NOT=30
    INCREMENT=31
    DECREMENT=32
    ASSIGN=33
    ACCESS=34
    SEPARATOR=35
    ID=36
    INTLIT=37
    FLOATLIT=38
    STRINGLIT=39
    WS=40
    ERROR_CHAR=41
    ILLEGAL_ESCAPE=42
    UNCLOSE_STRING=43

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

        def EOF(self):
            return self.getToken(TyCParser.EOF, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_program




    def program(self):

        localctx = TyCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(TyCParser.ID)
            self.state = 3
            self.match(TyCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





