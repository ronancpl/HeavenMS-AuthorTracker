
parser grammar AuthorCommentParser;

options { tokenVocab=AuthorCommentLexer; }

anySpec:
  .*?
  ;

commentSpec:
  (LCMP commentSpec RCMP) |
  anySpec
  ;

mainSpec:
  (LCMP commentSpec RCMP)
  ;

scopeSpec:
  .
  ;

main:
  (mainSpec | scopeSpec)* EOF
  ;

