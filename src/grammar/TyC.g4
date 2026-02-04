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
program: manydecls EOF;
manydecls: decl manydecls | ;
decl: funcdecl | structdecl ;

typ: INT | FLOAT | STRING | ID;

funcdecl: rettyp ID LP paramlist RP LB stmtlist RB 
        | ID LP paramlist RP LB stmtlist RB ;
rettyp: typ | VOID ; //need to recheck this rule
paramlist: pardecl paramtail | ;
paramtail: CM pardecl paramtail | ;
pardecl: typ ID ;

stmtlist: stmt stmtlist | ;

structdecl: STRUCT ID LB memlist RB SM ;
memlist: memtyp ID SM memlist | ;
memtyp: typ ; //1 test case for already declare struct (ID)

structvardecl: ID structvar SM ;
structvar: ID | ID ASSIGN LB exprlist RB ;
exprlist: expr exprtail | ;
exprtail: CM expr exprtail | ;
//expr: 'expr' ;

vardecl: AUTO ID ASSIGN expr 
        | AUTO ID 
        | typ ID ASSIGN expr 
        | typ ID 
        ;

funccalldecl: ID LP arglist RP ;
arglist: expr argtail | ;
argtail: CM expr argtail | ;

expr: expr1 ASSIGN expr | expr1 ;
expr1: expr1 OR expr2 | expr2 ;
expr2: expr2 AND expr3 | expr3 ;
expr3: expr3 EQUAL expr4 | expr3 NOTEQUAL expr4 | expr4 ;
expr4: expr4 LESSTHAN expr5
    | expr4 LESSTHAN_EQUAL expr5
    | expr4 GREATERTHAN expr5
    | expr4 GREATERTHAN_EQUAL expr5
    | expr5 ;
expr5: expr5 ADD expr6 | expr5 SUB expr6 | expr6 ;
expr6: expr6 MUL expr7 | expr6 DIV expr7 | expr6 MOD expr7 | expr7 ;
expr7: NOT expr7 | ADD expr7 | SUB expr7 | expr8 ;
expr8: INCREMENT expr8 | DECREMENT expr8 | expr9 ;
expr9: expr9 INCREMENT | expr9 DECREMENT | expr10 ;
expr10: expr10 ACCESS expr11 | expr11 ;
expr11: INTLIT | FLOATLIT | STRINGLIT | ID | funccalldecl | LP expr RP | LB exprlist RB;
//expr11: ID | LP expr RP ;

stmt: vardecl SM
    | structvardecl
    | blockstmt
    | ifstmt
    | whilestmt
    | forstmt
    | switchstmt
    | breakstmt
    | continuestmt
    | returnstmt
    | exprstmt
    ;

blockstmt: LB stmtlist RB ;

ifstmt: IF LP expr RP stmt | IF LP expr RP stmt ELSE stmt ;

whilestmt: WHILE LP expr RP stmt ;

forstmt: FOR LP init SM cond SM updt RP stmt ;
init: vardecl | expr | ;
cond: expr | ;
updt: expr | ;

switchstmt: SWITCH LP expr RP LB caselist RB ;
caselist: caseclause caselist | ;
caseclause: CASE caseexpr CL stmtlist | DEFAULT CL stmtlist; //recheck case default
caseexpr: expr ;

breakstmt: BREAK SM ;

continuestmt: CONTINUE SM ;

returnstmt: RETURN expr SM | RETURN SM ;

exprstmt: expr SM ;

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
CL: ':' ;


ID: [a-zA-Z_][a-zA-Z0-9_]* ;

INTLIT: [-]?[0-9]+ ;

FLOATLIT: [-]?[0-9]*'.'[0-9]+([Ee](SUB|ADD)?[0-9]+)?|[-]?[0-9]+'.'|[-]?[0-9]+[Ee](SUB|ADD)?[0-9]+;

fragment ESCAPE: '\\'[bfrnt"\\] ;
STRINGLIT: ["](ESCAPE|~["\\\r\n])*["] {self.text = self.text[1:-1]};

WS : [ \f\t\r\n]+ -> skip ; // skip spaces, tabs
LINE_COMMENT: '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT: '/*' .*? '*/' -> skip ;

ILLEGAL_ESCAPE : '"' (ESCAPE | ~["\\\r\n])* '\\' ~[bfrnt"\\\r\n] {self.text = self.text[1:]};
UNCLOSE_STRING: ["](ESCAPE|~["\\\r\n])* {self.text = self.text[1:]};
ERROR_CHAR: .;

