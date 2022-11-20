grammar PP;

program: (instruction)+ EOF;

instruction: (conditionalStatement | assignment | loop | print);

conditionalStatement:
	'IF(' cond = logicalExpression ')' con_body = conditionBody  ';';

condition:
	left_expr = arithmeticalExpression op = ('==' | '!=' | '>' | '<') right_expr = arithmeticalExpression;

logicalExpression:
    '(' left_expr = logicalExpression ')' op = ('AND' | 'OR') '(' right_expr = logicalExpression ')'
    | cond = condition;


arithmeticalExpression:
	 left = arithmeticalExpression op = ('+' | '-' | '/' | '*') right = arithmeticalExpression
	| integer
	| variableName;

loop: 'LOOP(' cond = logicalExpression ')' loop_body = loopBody ';';

assignment:
	variableName '=' (input | arithmeticalExpression) ';';

print: 'print(' arithmeticalExpression ');';

input: 'input';

variableName: 'X' NONZERODIGIT (NONZERODIGIT | ZERO)*;

integer: (minus = '-')? NONZERODIGIT (NONZERODIGIT | ZERO)*
	| ZERO;

conditionBody: (instruction)+;

loopBody: (instruction)+;

NONZERODIGIT: [1-9];

ZERO: '0';

