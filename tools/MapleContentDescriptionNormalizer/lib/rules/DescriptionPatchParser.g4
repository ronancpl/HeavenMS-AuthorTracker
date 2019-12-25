
parser grammar DescriptionPatchParser;

options { tokenVocab=DescriptionPatchLexer; }

dotSpec:
  SIGN |
  MARK
;

anyKeywordSpec:
  KEYWORD_SUCCESS |
  KEYWORD_LEVEL |
  KEYWORD_JOB |
  KEYWORD_CONDITION |
  KEYWORD_CLASS |
  KEYWORD_WHEN |
  KEYWORD_GIVES |
  KEYWORD_IMPROVES |
  KEYWORD_INCREASES |
  KEYWORD_RECOVER |
  KEYWORD_RESTORES |
  KEYWORD_FULLY |
  KEYWORD_CAN |
  KEYWORD_SPEED |
  KEYWORD_MESO |
  KEYWORD_ACCURACY |
  KEYWORD_AVOIDABILITY |
  KEYWORD_EVASION |
  KEYWORD_PROTECTION |
  KEYWORD_DOUBLE |
  KEYWORD_ITEM |
  KEYWORD_JUMP |
  KEYWORD_ATTACK |
  KEYWORD_DEFENSE |
  KEYWORD_WEAPON |
  KEYWORD_MAGIC |
  KEYWORD_DEF |
  KEYWORD_IF |
  KEYWORD_THE |
  NUMBER |
  CODE_C
  ;

textSpec:
  anyKeywordSpec | ANY_CHARACTER | TARGET_R | TARGET_N | TARGET_C
  ;

expectedCarriageReturnSpec:
  (TARGET_BACKSLASH? TARGET_R)
  ;

expectedLineForwardSpec:
  (TARGET_BACKSLASH? TARGET_N)
  ;

expectedLineBreakSpec:
  expectedCarriageReturnSpec? expectedLineForwardSpec
  ;

whitespaceBeforeKeywordSpec:
  WS+
  ;

whitespaceOrLineBreakSpec:
  expectedLineBreakSpec |
  WS+
  ;

codeSpec:
  CODE_C |
  CODE? TARGET_C |
  CODE
  ;

lineBreakMaybeCodeSpec:
  expectedLineBreakSpec codeSpec?
  ;

potentialConflictSpec:
  textSpec dotSpec* whitespaceOrLineBreakSpec* lineBreakMaybeCodeSpec whitespaceBeforeKeywordSpec? anyKeywordSpec
  ;

signMaybeWhitespaceSpec:
  SIGN (SIGN | WS)*
  ;

signConflictSpec:
  textSpec signMaybeWhitespaceSpec whitespaceOrLineBreakSpec* anyKeywordSpec
  ;

whitespaceSpec:
  WS+
  ;

spacedDotSpec:
  whitespaceSpec dotSpec
  ;

moreConflictSpec:
  WS whitespaceSpec |
  dotSpec? (TARGET_MINUS | TARGET_PLUS) whitespaceSpec NUMBER spacedDotSpec? |
  dotSpec (TARGET_MINUS | TARGET_PLUS) whitespaceSpec? NUMBER spacedDotSpec? |
  dotSpec (whitespaceSpec | dotSpec)* dotSpec
  ;

ignoreSpec:
  .
  ;

mainSpec:
  potentialConflictSpec |
  signConflictSpec |
  moreConflictSpec |
  ignoreSpec
  ;

compilationUnit:
  mainSpec* EOF
  ;
