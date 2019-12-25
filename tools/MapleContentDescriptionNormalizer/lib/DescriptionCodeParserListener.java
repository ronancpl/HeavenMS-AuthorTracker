// Generated from rules/DescriptionCodeParser.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link DescriptionCodeParser}.
 */
public interface DescriptionCodeParserListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link DescriptionCodeParser#codeTokenSpec}.
	 * @param ctx the parse tree
	 */
	void enterCodeTokenSpec(DescriptionCodeParser.CodeTokenSpecContext ctx);
	/**
	 * Exit a parse tree produced by {@link DescriptionCodeParser#codeTokenSpec}.
	 * @param ctx the parse tree
	 */
	void exitCodeTokenSpec(DescriptionCodeParser.CodeTokenSpecContext ctx);
	/**
	 * Enter a parse tree produced by {@link DescriptionCodeParser#ignoreSpec}.
	 * @param ctx the parse tree
	 */
	void enterIgnoreSpec(DescriptionCodeParser.IgnoreSpecContext ctx);
	/**
	 * Exit a parse tree produced by {@link DescriptionCodeParser#ignoreSpec}.
	 * @param ctx the parse tree
	 */
	void exitIgnoreSpec(DescriptionCodeParser.IgnoreSpecContext ctx);
	/**
	 * Enter a parse tree produced by {@link DescriptionCodeParser#mainSpec}.
	 * @param ctx the parse tree
	 */
	void enterMainSpec(DescriptionCodeParser.MainSpecContext ctx);
	/**
	 * Exit a parse tree produced by {@link DescriptionCodeParser#mainSpec}.
	 * @param ctx the parse tree
	 */
	void exitMainSpec(DescriptionCodeParser.MainSpecContext ctx);
	/**
	 * Enter a parse tree produced by {@link DescriptionCodeParser#compilationUnit}.
	 * @param ctx the parse tree
	 */
	void enterCompilationUnit(DescriptionCodeParser.CompilationUnitContext ctx);
	/**
	 * Exit a parse tree produced by {@link DescriptionCodeParser#compilationUnit}.
	 * @param ctx the parse tree
	 */
	void exitCompilationUnit(DescriptionCodeParser.CompilationUnitContext ctx);
}