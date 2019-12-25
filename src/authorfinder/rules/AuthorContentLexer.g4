
lexer grammar AuthorContentLexer;

// Text contents

DEVTEAM:            'dev team';
FOR:                ' for ';
AMPERSAND:          '&';
COMMA:              ',';
LPAR:               '(';
RPAR:               ')';

// Authorship content

CT_AUTHOR1:          '@author: ' | '@Author: ' | 'author: ' | 'Author: ';
CT_AUTHOR2:          '@author : ' | '@Author : ' | 'author : ' | 'Author : ';
CT_AUTHOR3:          '@author - ' | '@Author - ' | 'author - ' | 'Author - ';
CT_AUTHOR4:          '@author' | '@Author' | 'author' | 'Author';
CT_AUTHOR5:          'version by ' | 'Version by ';
CT_AUTHOR6:          'up by' | 'ix by' | 'pt by' | 'ed by' | ') by';

// Contributorship content

CT_THANKSTO:        'thanks to ' | 'Thanks to ';
CT_THANKS:          'thanks ' | 'Thanks ';
CT_IDEA:            '\'s idea';
CT_CREDIT1:         'credits to ' | 'Credits to ';
CT_CREDIT2:         'credits to: ' | 'Credits to: ';
CT_CLEANUP:         'cleanup by ' | 'Cleanup by ';

// Special authorship comment section

CM_BY:              'by --' | 'By --';
//CM_BY_END:        '--'; uses COMMENT_LINE2

// Comments

COMMENT_OPEN:       '/*';
COMMENT_CLOSE:      '*/';
COMMENT_LINE1:      '//';
COMMENT_LINE2:      '--';
COMMENT_HYPN:       '-';

// Line feed and identifiers

LINE_FEED:          '\n';
WS:                 ' ';
IGNORE_SPACE:       [\r\t\u000C]+ -> channel(HIDDEN);
IDENTIFIER:         .+?;