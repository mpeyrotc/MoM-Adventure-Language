grammar MoM;

program			:	(class_rule)+ EOF
                ;
arguments		:	ss_exp (COMMA ss_exp)* 
                ; 
assignation		:	VARID EQUALS (construct_call | ss_exp)
                ;
block			:	(statute SEMI_COLON)*
                ;
class_rule 		:	CLASS CLASSID IS_A complex_type (OF_TYPE CLASSID)? OPEN_BRACKET field construct_def function_def CLOSE_BRACKET
                ;
condition		:	IF OPEN_PAREN ss_exp CLOSE_PAREN OPEN_BRACKET block CLOSE_BRACKET (ELSE OPEN_BRACKET block CLOSE_BRACKET)?
                ;
constant		:	INTEGER
                |   REAL
                |   STRING 
                |   VARID
                ;
construct_call 	:	NEW CLASSID OPEN_PAREN (arguments)? CLOSE_PAREN
                ;
construct_def	:	(CLASSID OPEN_PAREN (function_args)? CLOSE_PAREN OPEN_BRACKET block CLOSE_BRACKET SEMI_COLON)+
                ;
enum			:	CAPITALID (COMMA CAPITALID)* SEMI_COLON
                ;
enumeration		:	ENUMERATE CLASSID OPEN_BRACKET enum CLOSE_BRACKET
                ;
ss_exp			:	s_exp ((AND | OR) s_exp)*
                ;
s_exp 			:	expression (operand expression)?
                ;
expression		:	(function_call | term) ((PLUS | MINUS | condition) (function_call | term))*
                ;
factor 			:	OPEN_BRACKET ss_exp CLOSE_BRACKET
                |   (PLUS | MINUS | NOT)? constant
                ;
function_args	:	super_type VARID (COMMA super_type VARID)*
                ;
function_call	:	(THIS | CLASSID) PERIOD VARID OPEN_PAREN (arguments)? CLOSE_PAREN SEMI_COLON
                ;
function_def	:	(simple_type VARID OPEN_PAREN (function_args)? CLOSE_PAREN OPEN_BRACKET block (RETURN ss_exp SEMI_COLON)? CLOSE_BRACKET SEMI_COLON)*
                ;
operand 		:	LESS_THAN
                |   LESS_EQUAL 
                |   GREATER_THAN 
                |   GREATER_EQUAL 
                |   EQUAL_EQUAL 
                ;
field           :	(FIELD LESS_THAN super_type GREATER_THAN VARID SEMI_COLON)* 
                ;
spec_function   :   (simple_type VARID OPEN_PAREN (function_args)? CLOSE_PAREN SEMI_COLON)+
                ;
specification	:	SPEC CLASSID OPEN_BRACKET (spec_function)? CLOSE_BRACKET 
                ;
statute			:	assignation 
                |   while_loop 
                |   condition 
                ;
term			:	factor ((STAR | SLASH) factor)* 
                ;
super_type 		:	simple_type 
                |   complex_type 
                ;
simple_type		:	INT  
                |   TEXT 
                |   FLOAT
                |   NOTHING 
                |   BOOLEAN
                ;
complex_type	:	SET
                |   MAP 
                |   SIZE 
                |   ARRAY 
                |   COMPONENT
                |   CLASSID
                ;
while_loop		:	WHILE OPEN_PAREN ss_exp CLOSE_PAREN OPEN_BRACKET block CLOSE_BRACKET 
                ;

OPEN_PAREN		:	'(' ;
COMMA			:	',' ;
CLOSE_PAREN		:	')' ;
OPEN_BRACKET	:	'{' ;
CLOSE_BRACKET	:	'}' ;
SEMI_COLON 		:	';' ;
STAR			:	'*' ;
SLASH			:	'/' ;
PLUS			:	'+' ;
MINUS			:	'-' ;
EQUALS			:	'=' ;
UNDERSCORE		:	'_' ;
PERIOD			:	'.' ;
NOT 			:	'!' ;
NOT_EQUALS 		:	'!=' ;
LESS_THAN		:	'<' ;
LESS_EQUAL		:	'<=' ;
GREATER_THAN	:	'>' ;
GREATER_EQUAL	:	'>=' ;
EQUAL_EQUAL		:	'==' ;
AND				:	'&&' ;
OR 				:	'||' ;
THIS			:	'this' ;
IF				:	'if' ; 
ELSE			:	'else' ;
ARRAY 			:	'Array' ;
COMPONENT		:	'Component' ;
INT 			:	'Int' ;
TEXT			:	'Text' ;
FLOAT			:	'Real' ;
SET 			:	'Set' ;
MAP				:	'Map' ;
SIZE			:	'Size' ;
NOTHING 		:	'Nothing' ;
CLASS 			:	'class' ;
NEW				:	'new' ;
ENUMERATE		:	'enumerate' ;
FIELD           :	'field' ;
SPEC			:	'specification' ;
RETURN          :   'return' ;
BOOLEAN         :   'boolean' ;
TYPE 			:	'type' ;
OF_TYPE			:	'of_type' ;
IS_A			:	'is_a' ;
fragment DIGIT	:	[0-9] ;
fragment UPPERC	:	[A-Z] ;
fragment LOWERC	:	[a-z] ;
CAPITALID		:	UPPERC+ ;
CLASSID			:	UPPERC (UPPERC | LOWERC | DIGIT | UNDERSCORE)* ;
VARID			:	LOWERC (UPPERC | LOWERC | DIGIT | UNDERSCORE)* ;
INTEGER			:	DIGIT+ ;
REAL			:	DIGIT+ ([.,] DIGIT+)? ;
WHITESPACE		:	' ' -> skip ;
STRING			:	'\"' ( ~('\'' | '\\' | '\n' | '\r') ) + '\"' ;
WHILE 			:	'while' ;
WS : [ \t\n]+ -> skip;