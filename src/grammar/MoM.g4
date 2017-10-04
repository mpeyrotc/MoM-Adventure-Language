grammar MoM;

program			:	(class_rule
                |   enumeration
                |   specification) + EOF
                ;
arguments		:	ss_exp (COMMA ss_exp)* 
                ; 
assignation		:	((THIS | VARID) PERIOD)? VARID EQUALS (construct_call | ss_exp)
                ;
block			:	(statute SEMI_COLON)*
                ;
class_rule 		:	CLASS CLASSID IS_A complex_type (OF_TYPE CLASSID)? OPEN_BRACKET field construct_def
                            function_def CLOSE_BRACKET SEMI_COLON
                ;
condition		:	IF OPEN_PAREN ss_exp CLOSE_PAREN OPEN_BRACKET block CLOSE_BRACKET
                            (ELSE OPEN_BRACKET block CLOSE_BRACKET)?
                ;
constant		:	INTEGER
                |   REAL
                |   STRING 
                |   VARID
                |   array_var
                |   TRUE
                |   FALSE
                ;
construct_call 	:	NEW CLASSID OPEN_PAREN (arguments)? CLOSE_PAREN
                ;
construct_def	:	CLASSID OPEN_PAREN (function_args)? CLOSE_PAREN OPEN_BRACKET block CLOSE_BRACKET SEMI_COLON
                ;
enum			:	CAPITALID (COMMA CAPITALID)* SEMI_COLON
                ;
enumeration		:	ENUMERATE CLASSID OPEN_BRACKET enum CLOSE_BRACKET SEMI_COLON
                ;
ss_exp			:	s_exp ((AND | OR) s_exp)*
                ;
s_exp 			:	expression (operand expression)?
                ;
expression		:	(function_call | term) ((PLUS | MINUS | condition) (function_call | term))*
                ;
factor 			:	OPEN_PAREN ss_exp CLOSE_PAREN
                |   (PLUS | MINUS | NOT)? constant
                ;
function_args	:	(super_type | array_arg) VARID (COMMA (super_type | array_arg) VARID)*
                ;
function_call	:	((THIS | CLASSID) PERIOD)? VARID OPEN_PAREN (arguments)? CLOSE_PAREN
                ;
function_def	:	(simple_type VARID OPEN_PAREN (function_args)? CLOSE_PAREN OPEN_BRACKET block
                            (RETURN ss_exp SEMI_COLON)? CLOSE_BRACKET SEMI_COLON)*
                ;
operand 		:	LESS_THAN
                |   LESS_EQUAL 
                |   GREATER_THAN 
                |   GREATER_EQUAL 
                |   EQUAL_EQUAL 
                ;
field           :	(FIELD LESS_THAN (super_type | array_def) GREATER_THAN VARID SEMI_COLON)*
                ;
spec_function   :   (simple_type VARID OPEN_PAREN (function_args)? CLOSE_PAREN SEMI_COLON)+
                ;
specification	:	SPEC CLASSID OPEN_BRACKET (spec_function)? CLOSE_BRACKET SEMI_COLON
                ;
assignation_def :   super_type VARID EQUALS (construct_call | ss_exp)
                ;
statute			:	function_call
                |   assignation
                |   assignation_def
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
                |   COMPONENT
                |   CLASSID
                ;
while_loop		:	WHILE OPEN_PAREN ss_exp CLOSE_PAREN OPEN_BRACKET block CLOSE_BRACKET
                ;
array_def       :   super_type OPEN_SBRACKET INTEGER CLOSE_SBRACKET
                ;
array_var       :   ((THIS | CLASSID) PERIOD)? VARID OPEN_SBRACKET INTEGER CLOSE_SBRACKET
                ;
array_arg       :   super_type OPEN_SBRACKET CLOSE_SBRACKET
                ;

OPEN_PAREN		:	'(' ;
COMMA			:	',' ;
CLOSE_PAREN		:	')' ;
OPEN_BRACKET	:	'{' ;
CLOSE_BRACKET	:	'}' ;
OPEN_SBRACKET	:	'[' ;
CLOSE_SBRACKET	:	']' ;
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
BOOLEAN         :   'Boolean' ;
TYPE 			:	'type' ;
OF_TYPE			:	'of_type' ;
IS_A			:	'is_a' ;
WHILE 			:	'while' ;
TRUE            :   'TRUE';
FALSE           :   'FALSE';
fragment DIGIT	:	[0-9] ;
fragment UPPERC	:	[A-Z] ;
fragment LOWERC	:	[a-z] ;
CAPITALID		:	UPPERC+ ;
CLASSID			:	UPPERC (UPPERC | LOWERC | DIGIT | UNDERSCORE)* ;
VARID			:	LOWERC (UPPERC | LOWERC | DIGIT | UNDERSCORE)* ;
INTEGER			:	DIGIT+ ;
REAL			:	DIGIT+ ([.,] DIGIT+)? ;
WHITESPACE		:	' ' -> skip ;
STRING			:	'"' ( ~('\'' | '\\' | '\n' | '\r') ) + '"' ;
WS : [ \t\n]+ -> skip;