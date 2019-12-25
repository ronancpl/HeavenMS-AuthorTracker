
parser grammar DescriptionCodeParser;

options { tokenVocab=DescriptionCodeLexer; }

codeTokenSpec:
  TOKEN_AMP |
  TOKEN_APOS |
  TOKEN_QUOT
  ;

ignoreSpec:
  .
  ;

mainSpec:
  codeTokenSpec |
  ignoreSpec
  ;

compilationUnit:
  mainSpec* EOF
  ;
