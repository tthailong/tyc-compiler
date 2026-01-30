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
program: ID INTLIT FLOATLIT STRINGLIT EOF;

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

LP: '(' ;
RP: ')' ;
LB: '{' ;
RB: '}' ;
CM: ',' ;
SM: ';' ;

ID: [a-zA-Z_][a-zA-Z0-9_]* ;

//INTLIT: [0]|[-]?[1-9][0-9]* ;
INTLIT: [-]?[0-9]+ ;

FLOATLIT: [-]?[0-9]*'.'[0-9]+([Ee][-]?[0-9]+)?|[-]?[0-9]+'.'|[-]?[0-9]+[Ee][-]?[0-9]+;

fragment ESCAPE: '\\'[bfrnt"\\] ;
STRINGLIT: ["](ESCAPE|~["\\\r\n])*["] {self.text = self.text[1:-1]};

//WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs
WS : [ \f\t\r\n]+ -> skip ; // skip spaces, tabs


ILLEGAL_ESCAPE : '"' (ESCAPE | ~["\\\r\n])* '\\' ~[bfrnt"\\\r\n] {self.text = self.text[1:]};
UNCLOSE_STRING: ["](ESCAPE|~["\\\r\n])* {self.text = self.text[1:]};
ERROR_CHAR: .;

typ: INT | FLOAT | STRING | ID;

funcdecl: rettyp? ID LP paramlist RP LB stmtlist RB ;
rettyp: typ | VOID ; //need to recheck this rule
paramlist: pardecl paramtail | ;
paramtail: CM pardecl paramtail | ;
pardecl: typ ID ;

stmtlist: 'statementlist' ;

structdecl: STRUCT ID LB memlist RB SM ;
memlist: memtyp ID SM memlist | ;
memtyp: typ ; //1 test case for already declare struct

structvardecl: ID structvar SM ;
structvar: ID | ID ASSIGN LB exprlist RB ;
exprlist: expr exprtail | ;
exprtail: CM expr exprtail | ;
expr: 'expr' ;

structmemaccess: ID ACCESS ID ;

vardecl: AUTO ID ASSIGN expr SM
        | AUTO ID SM
        | typ ID ASSIGN expr SM
        | typ ID SM
        ;


