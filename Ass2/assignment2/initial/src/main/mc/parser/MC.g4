/**
 * Student name: Tran Thi Tham
 * Student ID: 1713214
 */
grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::member {
def emit(self):
    tk = self.type
    if tk == UNCLOSE_STRING:
        result = super.emit();
        raise UncloseString(result.text);
    elif tk == ILLEGAL_ESCAPE:
        result = super.emit();
        raise IllegalEscape(result.text);
    elif tk == ERROR_CHAR:
        result = super.emit();
        raise ErrorToken(result.text);
    else:
        return super.emit();
}
options{
	language=Python3;
}

program  :declares EOF ;
INTLIT
    : [0-9]+
    ;
declares: declare+ ;
declare
    : varDeclare| funcDeclare
    ;
varDeclare
    : primitivetype manyVariable SEMI
    ;
manyVariable
    : variable (CM variable)*
    ;
variable
    : id_single
    | id_array
    ;
id_single: ID;
id_array: ID LQB INTLIT RQB;

funcDeclare
    : mctype ID LB paraList? RB blockstmt
    ;

paraList
    :  paraDecl (CM paraDecl)*
    ;
paraDecl
    :  primitivetype ID (LQB RQB)?
    ;
blockstmt
    : LP var_stmt* RP
    ;
var_stmt
    : varDeclare| stmt
    ;
stmt
    : ifstmt|forstmt|do_whilestmt|breakstmt|continuestmt|returnstmt|blockstmt|exp SEMI
    ;
ifstmt
    : IF LB exp RB stmt (ELSE stmt)?
    ;
do_whilestmt
    : DO stmt+ WHILE exp SEMI
    ;
forstmt
    : FOR LB exp SEMI exp SEMI exp RB stmt
    ;
breakstmt
    : BREAK SEMI
    ;
continuestmt
    : CONTINUE SEMI
    ;
returnstmt
    : RETURN exp? SEMI
    ;
mctype: primitivetype | arraypointertype | VOIDTYPE ;

exp
    : exp1 ASSIGN exp
    | exp1
    ;
exp1
    : exp1 OR exp2
    | exp2
    ;
exp2
    : exp2 AND exp3
    | exp3
    ;
exp3
    : exp4 EQUAL exp4
    | exp4 NOTEQUAL exp4
    | exp4
    ;
exp4
    : exp5 LESS exp5
    | exp5 LESSEQUAL exp5
    | exp5 GREATEREQUAL exp5
    | exp5 GREATER exp5
    | exp5
    ;
exp5
    : exp5 ADD exp6
    | exp5 SUB exp6
    | exp6
    ;
exp6
    : exp6 DIV exp7
    | exp6 MUL exp7
    | exp6 MODUL exp7
    | exp7
    ;
exp7
    : NOT exp7
    | SUB exp7
    |exp8
    ;
exp8
    : exp9 LQB exp RQB
    | exp9
    ;
exp9
    : LB exp RB
    | operand
    ;
operand
    : Realit|Booleanlit|INTLIT|ID|funcall|Stringlit
    ;

funcall
    : ID LB (parameter (CM parameter)*)? RB
    ;
parameterList
    : parameter (CM parameter)*
    ;
parameter: Realit|Booleanlit|INTLIT|ID|exp|Stringlit ;
fragment Letter
    : [a-zA-Z]
    ;

Realit
    :    (Digit+) '.' (Digit)* Exponent?| (Digit)* '.'(Digit+) Exponent?|Digit+ Exponent?
    ;

fragment Exponent
    :('e' | 'E') '-'? Digit+
    ;
Booleanlit
    : ('true'|'false')
    ;
Stringlit
    : '"'('\\'[bfrnt"\\] | ~[\b\f\r\n\t\\"])* '"'
    {self.text = self.text[1:-1]}
    ;

fragment Digit
    : [0-9]
    ;
IF
    : 'if'
    ;
ELSE
    : 'else'
    ;

CONTINUE
    : 'continue'
    ;
FOR
    : 'for'
    ;
WHILE
    :'while'
    ;
DO
    : 'do'
    ;
BREAK
    :'break'
    ;
RETURN
    :'return'
    ;
TRUE
    : 'true'
    ;
FALSE
    : 'false'
    ;
BLOCK_COMMENT
    : '/*' .*? '*/' -> skip
    ;
LINE_COMMENT
    : '//' (~[\n\r])* -> skip
    ;

//SEPARATORS
LB
    : '('
    ;
RB
    : ')'
    ;
LP
    : '{'
    ;
RP
    : '}'
    ;
LQB
    : '['
    ;
RQB
    : ']'
    ;
CM
    : ','
    ;
SEMI
    : ';'
    ;

//OPERATOR
ADD
    : '+'
    ;
SUB
    : '-'
    ;

DIV
    : '/'
    ;
MUL
    :'*'
    ;
NOT
    : '!'
    ;
NOTEQUAL
    : '!='
    ;
OR
    : '||'
    ;
LESS
    : '<'
    ;
LESSEQUAL
    : '<='
    ;
ASSIGN
    : '='
    ;
MODUL
    : '%'
    ;
AND
    : '&&'
    ;
EQUAL
    : '=='
    ;
GREATER
    : '>'
    ;
GREATEREQUAL
    :'>='
    ;
fragment UNDERSCORE
    :'_'
    ;

WS
    : [ \t\r\n\f]+ -> skip
    ; // skip spaces, tabs, newlines

//4. TYPES AND VALUES
//4.1 VOID TYPE AND VALUES
INTTYPE
    : 'int'
    ;

VOIDTYPE
    : 'void'
    ;
BOOLEANTYPE
    : 'boolean'
    ;
FLOATTYPE
    : 'float'
    ;
STRINGTYPE
    : 'string'
    ;
primitivetype
    : INTTYPE|BOOLEANTYPE|STRINGTYPE|FLOATTYPE
    ;
arraypointertype
    : primitivetype ID? LQB RQB
    ;
ID
    : (Letter|UNDERSCORE)(Letter|UNDERSCORE|Digit)*
    ;
ILLEGAL_ESCAPE
    : '"' ('\\'[bfrnt"\\] | ~[\b\f\r\n\t\\"])* ('\\'~[bntrf"\\] | [\b\t\f"\\])
    {raise IllegalEscape(self.text[1:])}
    ;
UNCLOSE_STRING
    : '"' ('\\'[bfnrt"\\] | ~[\b\f\n\r\t"\\])*
    {raise UncloseString(self.text[1:])}
    ;
ERROR_CHAR
    : .
    {raise ErrorToken(self.text)}
    ;