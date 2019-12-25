
lexer grammar AuthorDocumentLexer;

// Comments

COMMENT_OPEN:       '/*';
COMMENT_CLOSE:      '*/';
COMMENT_LINE1:      '//';
COMMENT_LINE2:      '--';

// Line feed and identifiers

LINE_FEED:          '\n';
CHARACTERS:         . -> channel(77);