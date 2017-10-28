grammar MoM;

program			:	(class_rule
                |   enumeration
                |   specification)+ EOF
                ;
after_argument  :   // nothing
                ;
advance_count   :   // nothing
                ;
arguments		:	ss_exp after_argument advance_count (COMMA ss_exp after_argument advance_count)*
                ;
assignation		:	((THIS | VARID) PERIOD)? (VARID | array_var) EQUALS (construct_call | ss_exp)
                ;
block			:	statute SEMI_COLON
                ;
class_rule 		:	CLASS CLASSID IS_A complex_type (OF_TYPE CLASSID (COMMA CLASSID)*)? OPEN_BRACKET
                            field* construct_def function_def* CLOSE_BRACKET SEMI_COLON
                ;
exit_if_check   :   // nothing.
                ;
condition_end   :   // nothing.
                ;
enter_else      :   // nothing.
                ;
condition		:	IF OPEN_PAREN ss_exp CLOSE_PAREN exit_if_check OPEN_BRACKET block* CLOSE_BRACKET
                            (ELSE enter_else OPEN_BRACKET block* CLOSE_BRACKET)? condition_end
                ;
constant		:	INTEGER
                |   REAL
                |   STRING
                |   VARID
                |   array_var
                |   TRUE
                |   FALSE
                |   function_call
                ;
construct_call 	:	NEW CLASSID OPEN_PAREN (arguments)? CLOSE_PAREN
                ;
exit_con_def    :   // nothing
                ;
construct_def	:	CLASSID OPEN_PAREN (function_args)? CLOSE_PAREN OPEN_BRACKET block* CLOSE_BRACKET
                            exit_con_def SEMI_COLON
                ;
enum			:	CAPITALID (COMMA CAPITALID)* SEMI_COLON
                ;
enumeration		:	ENUMERATE CLASSID OPEN_BRACKET enum CLOSE_BRACKET SEMI_COLON
                ;
exit_sexp       :   // nothing
                ;
and_op          :   // nothing
                ;
or_op           :   // nothing
                ;
ss_exp			:	s_exp exit_sexp ((AND and_op| OR or_op) s_exp exit_sexp)*
                ;
exit_exp        :   // nothing
                ;
s_exp 			:	expression (operand expression exit_exp)?
                ;
exit_term       :   // nothing
                ;
plus_op         :   // nothing
                ;
minus_op        :   // nothing
                ;
expression		:	term exit_term ((PLUS plus_op | MINUS minus_op | condition) term exit_term)*
                ;
open_paren      :   // nothing
                ;
close_paren     :   // nothing
                ;
factor 			:	OPEN_PAREN open_paren ss_exp close_paren CLOSE_PAREN
                |   (PLUS | MINUS | NOT)? constant
                ;
function_args	:	(super_type | array_arg) VARID (COMMA (super_type | array_arg) VARID)*
                ;
function_call	:	((THIS | VARID) PERIOD)? VARID OPEN_PAREN (arguments)? CLOSE_PAREN
                ;
exit_func_def   :   // nothing
                ;
function_def	:	simple_type VARID OPEN_PAREN (function_args)? CLOSE_PAREN OPEN_BRACKET block*
                            (RETURN ss_exp SEMI_COLON)? CLOSE_BRACKET exit_func_def SEMI_COLON
                ;
operand 		:	LESS_THAN
                |   LESS_EQUAL
                |   GREATER_THAN
                |   GREATER_EQUAL
                |   EQUAL_EQUAL
                ;
field           :	FIELD LESS_THAN (super_type | array_def) GREATER_THAN VARID SEMI_COLON
                ;
spec_function   :   simple_type VARID OPEN_PAREN (function_args)? CLOSE_PAREN SEMI_COLON
                ;
specification	:	SPEC CLASSID OPEN_BRACKET spec_function* CLOSE_BRACKET SEMI_COLON
                ;
assignation_def :   super_type VARID EQUALS (construct_call | ss_exp)
                ;
statute			:	function_call
                |   assignation
                |   assignation_def
                |   while_loop
                |   condition
                |   write_func
                |   read_func
                ;
exit_factor     :   // nothing
                ;
star_op         :   // nothing
                ;
div_op          :   // nothing
                ;
term			:	factor exit_factor ((STAR star_op | SLASH div_op) factor exit_factor)*
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
                |   CLASSID
                ;
end_while       :   // nothing.
                ;
after_while     :   // nothing.
                ;
while_loop		:	WHILE after_while OPEN_PAREN ss_exp CLOSE_PAREN exit_if_check OPEN_BRACKET block* CLOSE_BRACKET end_while
                ;
array_def       :   super_type OPEN_SBRACKET INTEGER CLOSE_SBRACKET
                ;
array_var       :   ((THIS | CLASSID) PERIOD)? VARID OPEN_SBRACKET INTEGER CLOSE_SBRACKET
                ;
array_arg       :   super_type OPEN_SBRACKET CLOSE_SBRACKET
                ;
write_func      :   PRINT OPEN_PAREN (s_exp) CLOSE_PAREN
                ;
read_func       :   READ OPEN_PAREN VARID CLOSE_PAREN
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
INT 			:	'Int' ;
TEXT			:	'Text' ;
FLOAT			:	'Real' ;
SET 			:	'Set' ;
MAP				:	'Map' ;
SIZE			:	'Size' ;
NOTHING 		:	'Nothing' ;
PRINT           :   'Write' ;
READ            :   'Read' ;
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
WS : [ \t\n\r]+ -> skip;