
parser grammar AuthorDocumentParser;

options { tokenVocab=AuthorDocumentLexer; }

main:
  (mainSpec | codeSpec mainSpec | codeSpec) EOF
  ;

mainSpec:
  ((commentBlock | commentLine) codeSpec)+
  ;

codeSpec:
  .*?
  ;

commentBlock:
  COMMENT_OPEN commentBlockSpec COMMENT_CLOSE
  ;

commentLine:
  (COMMENT_LINE1 | COMMENT_LINE2) commentInlineSpec LINE_FEED
  ;

commentBlockSpec:
  .*?
  ;

commentInlineSpec:
  .*?
  ;