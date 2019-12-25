java -Xmx500M -cp ./antlr-4.7.1-complete.jar org.antlr.v4.Tool -Dlanguage=Java rules/DescriptionPatchLexer.g4

java -Xmx500M -cp ./antlr-4.7.1-complete.jar org.antlr.v4.Tool -Dlanguage=Java rules/DescriptionPatchParser.g4

java -Xmx500M -cp ./antlr-4.7.1-complete.jar org.antlr.v4.Tool -Dlanguage=Java rules/DescriptionCodeLexer.g4

java -Xmx500M -cp ./antlr-4.7.1-complete.jar org.antlr.v4.Tool -Dlanguage=Java rules/DescriptionCodeParser.g4