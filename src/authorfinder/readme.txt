java -Xmx500M -cp ./antlr-4.7.1-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 rules/AuthorDocumentLexer.g4
java -Xmx500M -cp ./antlr-4.7.1-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 rules/AuthorDocumentParser.g4

java -Xmx500M -cp ./antlr-4.7.1-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 rules/AuthorCommentLexer.g4
java -Xmx500M -cp ./antlr-4.7.1-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 rules/AuthorCommentParser.g4

java -Xmx500M -cp ./antlr-4.7.1-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 rules/AuthorContentLexer.g4
java -Xmx500M -cp ./antlr-4.7.1-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 rules/AuthorContentParser.g4