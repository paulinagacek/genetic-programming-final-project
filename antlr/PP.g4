grammar PP;

program: (instruction)+ EOF;

instruction: (
		conditionalStatement
		| assignment
		| loop
		| printExpression
	);

printExpression: 'print(' arithmeticalExpression ');';

inputExpression: 'input';

readExpression: 'read(' positiveInteger ');';

conditionalStatement:
	'IF(' cond = logicalExpression ')' con_body = conditionBody ';';

condition:
	left_expr = arithmeticalExpression op = (
		'=='
		| '!='
		| '>'
		| '<'
	) right_expr = arithmeticalExpression;

logicalExpression:
	'(' left_expr = logicalExpression ')' op = ('AND' | 'OR') '(' right_expr = logicalExpression ')'
	| cond = condition;

arithmeticalExpression:
	left = arithmeticalExpression op = ('+' | '-' | '/' | '*') right = arithmeticalExpression
	| read_ = readExpression
	| integer_ = integer
	| variable_name_ = variableName;

loop:
	'LOOP(' cond = logicalExpression ')' loop_body = loopBody ';';

assignment:
	variableName '=' (
		input_ = inputExpression
		| art_expr = arithmeticalExpression
	) ';';

variableName: 'X' NONZERODIGIT (NONZERODIGIT | ZERO)*;

integer: (minus = '-')? NONZERODIGIT (NONZERODIGIT | ZERO)*
	| ZERO;

positiveInteger: NONZERODIGIT (NONZERODIGIT | ZERO)*;

conditionBody: (instruction)+;

loopBody: (instruction)+;

NONZERODIGIT: [1-9];

ZERO: '0';

