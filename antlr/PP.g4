grammar PP;

program: (instruction)+ EOF;

instruction: assignment | conditionalStatement | loop | print;

print: 'print' arithmeticalExpression ';';

input: 'input';

variableName: 'X' NONZERODIGIT (NONZERODIGIT | ZERO)*;

integer: (minus = '-')? NONZERODIGIT (NONZERODIGIT | ZERO)*
	| ZERO;

arithmeticalExpression:
	left = arithmeticalExpression op = (ADD | SUB | DIV | MUL) right = arithmeticalExpression
	| integer
	| variableName;

assignment:
	variableName '=' (input | arithmeticalExpression) ';';

conditionalStatement:
	'IF(' cond = condition ')' con_body = conditionBody (else_stat = elseStatement)? ';';

condition:
	left_expr = arithmeticalExpression op = (EQ | NOT_EQ | GT | LT) right_expr = arithmeticalExpression;

conditionBody: (instruction)+;

elseStatement: 'ELSE' con_body = conditionBody;

loop: 'LOOP(' cond = condition ')' loop_body = loopBody ';';

loopBody: (instruction)+;

NONZERODIGIT: [1-9];

ZERO: '0';

ADD: '+';

SUB: '-';

MUL: '*';

DIV: '/';

EQ: '==';

GT: '>';

LT: '<';

NOT_EQ: '!=';
