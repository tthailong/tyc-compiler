grammar TyC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

// TODO: Define grammar rules here
program: ID EOF;

AUTO: 'auto' ;
BREAK: 'break' ;
CASE: 'case' ;
CONTINUE: 'continue' ;
DEFAULT: 'default' ;
ELSE: 'else' ;
FLOAT: 'float' ;
FOR: 'for' ;
IF: 'if' ;
INT: 'int';
RETURN: 'return' ;
STRING: 'string' ;
STRUCT: 'struct' ;
SWITCH: 'switch' ;
VOID: 'void' ;
WHILE: 'while' ;

ADD: '+' ;
SUB: '-' ;
MUL: '*' ;
DIV: '/' ;
MOD: '%' ;
EQUAL: '==' ;
NOTEQUAL: '!=' ;
LESSTHAN: '<' ;
GREATERTHAN: '>' ;
LESSTHAN_EQUAL: '<=' ;
GREATERTHAN_EQUAL: '>=' ;
OR: '||' ;
AND: '&&' ;
NOT: '!' ;
INCREMENT: '++' ;
DECREMENT: '--' ;
ASSIGN: '=' ;
ACCESS: '.' ;

SEPARATOR: '['|']'|'('|')'|'{'|'}'|';'|',' ;


ID: [a-zA-Z_][a-zA-Z0-9_]* ;

//INTLIT: [0]|[-]?[1-9][0-9]* ;
INTLIT: [-]?[0-9]+ ;

FLOATLIT: [-]?[0-9]*'.'[0-9]+([Ee][-]?[0-9]+)?|[-]?[0-9]+ '.';

fragment ESCAPE: '\\'[bfrnt"\\] ;
STRINGLIT: ["](ESCAPE|~["\\\r\n])*["] ;

//WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs
WS : [ \f\t\r\n]+ -> skip ; // skip spaces, tabs

ERROR_CHAR: .;
ILLEGAL_ESCAPE : '"' (ESCAPE | ~["\\\r\n])* '\\' ~[bfrnt"\\\r\n] ;
UNCLOSE_STRING: ["](ESCAPE|~["\\\r\n])*;
