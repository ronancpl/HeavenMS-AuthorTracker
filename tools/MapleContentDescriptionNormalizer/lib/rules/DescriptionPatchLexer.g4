
lexer grammar DescriptionPatchLexer;

KEYWORD_SUCCESS:	'Success';
KEYWORD_LEVEL:		'Level';
KEYWORD_JOB:		'Job';
KEYWORD_CONDITION:	'Condition';
KEYWORD_CLASS:		'Class';
KEYWORD_WHEN:		'When';
KEYWORD_GIVES:		'Gives';
KEYWORD_IMPROVES:	'Improves';
KEYWORD_INCREASES:	'Increases';
KEYWORD_RECOVER:	'Recover';
KEYWORD_RESTORES:	'Restores';
KEYWORD_FULLY:		'Fully';
KEYWORD_CAN:		'Can';
KEYWORD_SPEED:		'Speed';
KEYWORD_MESO:		'Meso';
KEYWORD_ACCURACY:	'Accuracy';
KEYWORD_AVOIDABILITY:	'Avoidability';
KEYWORD_EVASION:	'Evasion';
KEYWORD_PROTECTION:	'Protection';
KEYWORD_DOUBLE:		'Double';
KEYWORD_ITEM:		'Item';
KEYWORD_JUMP:		'Jump';
KEYWORD_ATTACK:		'Attack';
KEYWORD_DEFENSE:	'Defense';
KEYWORD_WEAPON:		'Weapon';
KEYWORD_MAGIC:		'Magic';
KEYWORD_DEF:		'Def';
KEYWORD_IF:		'If';
KEYWORD_THE:		'The';

NUMBER:			[0-9]+;
CODE_C:			'#c';
CODE:			'#';

// Line feed and identifiers

SIGN:			[.!?];
MARK:			[:;];
WS:			[ \r\t\u000C];


// Target characters

TARGET_BACKSLASH:	'\\';
TARGET_R:		'r';
TARGET_N:		'n';
TARGET_C:		'c';
TARGET_PLUS:		'+';
TARGET_MINUS:		'-';

ANY_CHARACTER:		.;