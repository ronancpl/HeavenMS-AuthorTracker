
parser grammar AuthorContentParser;

options { tokenVocab=AuthorContentLexer; }

main:
  (commentSpec? codeSpec) mainSpec EOF
  ;

mainSpec:
  (commentSpec codeSpec)+?
  ;

codeSpec:
  (~(COMMENT_OPEN | COMMENT_LINE1 | COMMENT_LINE2))*
  ;

commentSpec:
  commentBlock |
  commentLine
  ;

commentBlock:
  COMMENT_OPEN commentBlockSpec* COMMENT_CLOSE
  ;

commentBlockSpec:
  commentByBlockSpec COMMENT_LINE2 |
  (author | contributor)+ LINE_FEED? |
  out
  ;

out:
  .
  ;

commentByBlockSpec:
  commentByHeader commentByBody
  ;

commentByHeader:
  CM_BY commentByHeaderSkip LINE_FEED
  ;

commentByHeaderSkip:
  (COMMENT_LINE2 | COMMENT_HYPN)*
  ;

commentByBody:
  commentByLine*
  ;

commentByLine:
  patronNamesWrap LINE_FEED |
  commentByHeader |
  patronNamesWrap commentByHeader
  ;

commentLine:
  (COMMENT_LINE1 | COMMENT_LINE2) commentInlineSpec LINE_FEED
  ;

commentInlineSpec:
  (author | contributor | .)+?
  ;

author:
  CT_AUTHOR1 patronNamesWrap |
  CT_AUTHOR2 patronNamesWrap |
  CT_AUTHOR3 patronNamesWrap |
  CT_AUTHOR4 patronNamesWrap |
  CT_AUTHOR5 patronNamesWrap |
  CT_AUTHOR6 patronNamesWrap
  ;

contributor:
  CT_THANKSTO patronNamesWrap |
  CT_THANKS patronNamesWrap |
  CT_CREDIT1 patronNamesWrap |
  CT_CREDIT2 patronNamesWrap |
  CT_CLEANUP patronNamesWrap |
  patronNamesWrap CT_IDEA
  ;

patronNamesWrap:
  patronNames?
  ;

patronNames:
  patronName (AMPERSAND | COMMA) patronNames? |
  patronName |
  (AMPERSAND | COMMA) patronNames? |
  patronAtomicSkip (AMPERSAND | COMMA) patronNames? |
  patronAtomicSkip
  ;

patronName:
  patronAtomic (LPAR patronAtomic RPAR patronSingleton*)?
  ;

patronAtomic:
  patronSingleton DEVTEAM? WS* patronAtomicSkip?
  ;

patronSingleton:
  (IDENTIFIER | WS)+
  ;

patronAtomicSkip:
  (COMMENT_HYPN | FOR) patronCommentInternal
  ;

patronCommentInternal:
  ~(LINE_FEED | EOF | AMPERSAND | COMMA)*?
  ;
