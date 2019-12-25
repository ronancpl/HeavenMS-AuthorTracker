package antlr;

// Generated from rules/DescriptionPatchParser.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link DescriptionPatchParser}.
 */
public interface DescriptionPatchParserListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link DescriptionPatchParser#dotSpec}.
	 * @param ctx the parse tree
	 */
	void enterDotSpec(DescriptionPatchParser.DotSpecContext ctx);
	/**
	 * Exit a parse tree produced by {@link DescriptionPatchParser#dotSpec}.
	 * @param ctx the parse tree
	 */
	void exitDotSpec(DescriptionPatchParser.DotSpecContext ctx);
	/**
	 * Enter a parse tree produced by {@link DescriptionPatchParser#anyKeywordSpec}.
	 * @param ctx the parse tree
	 */
	void enterAnyKeywordSpec(DescriptionPatchParser.AnyKeywordSpecContext ctx);
	/**
	 * Exit a parse tree produced by {@link DescriptionPatchParser#anyKeywordSpec}.
	 * @param ctx the parse tree
	 */
	void exitAnyKeywordSpec(DescriptionPatchParser.AnyKeywordSpecContext ctx);
	/**
	 * Enter a parse tree produced by {@link DescriptionPatchParser#textSpec}.
	 * @param ctx the parse tree
	 */
	void enterTextSpec(DescriptionPatchParser.TextSpecContext ctx);
	/**
	 * Exit a parse tree produced by {@link DescriptionPatchParser#textSpec}.
	 * @param ctx the parse tree
	 */
	void exitTextSpec(DescriptionPatchParser.TextSpecContext ctx);
	/**
	 * Enter a parse tree produced by {@link DescriptionPatchParser#expectedCarriageReturnSpec}.
	 * @param ctx the parse tree
	 */
	void enterExpectedCarriageReturnSpec(DescriptionPatchParser.ExpectedCarriageReturnSpecContext ctx);
	/**
	 * Exit a parse tree produced by {@link DescriptionPatchParser#expectedCarriageReturnSpec}.
	 * @param ctx the parse tree
	 */
	void exitExpectedCarriageReturnSpec(DescriptionPatchParser.ExpectedCarriageReturnSpecContext ctx);
	/**
	 * Enter a parse tree produced by {@link DescriptionPatchParser#expectedLineForwardSpec}.
	 * @param ctx the parse tree
	 */
	void enterExpectedLineForwardSpec(DescriptionPatchParser.ExpectedLineForwardSpecContext ctx);
	/**
	 * Exit a parse tree produced by {@link DescriptionPatchParser#expectedLineForwardSpec}.
	 * @param ctx the parse tree
	 */
	void exitExpectedLineForwardSpec(DescriptionPatchParser.ExpectedLineForwardSpecContext ctx);
	/**
	 * Enter a parse tree produced by {@link DescriptionPatchParser#expectedLineBreakSpec}.
	 * @param ctx the parse tree
	 */
	void enterExpectedLineBreakSpec(DescriptionPatchParser.ExpectedLineBreakSpecContext ctx);
	/**
	 * Exit a parse tree produced by {@link DescriptionPatchParser#expectedLineBreakSpec}.
	 * @param ctx the parse tree
	 */
	void exitExpectedLineBreakSpec(DescriptionPatchParser.ExpectedLineBreakSpecContext ctx);
	/**
	 * Enter a parse tree produced by {@link DescriptionPatchParser#whitespaceBeforeKeywordSpec}.
	 * @param ctx the parse tree
	 */
	void enterWhitespaceBeforeKeywordSpec(DescriptionPatchParser.WhitespaceBeforeKeywordSpecContext ctx);
	/**
	 * Exit a parse tree produced by {@link DescriptionPatchParser#whitespaceBeforeKeywordSpec}.
	 * @param ctx the parse tree
	 */
	void exitWhitespaceBeforeKeywordSpec(DescriptionPatchParser.WhitespaceBeforeKeywordSpecContext ctx);
	/**
	 * Enter a parse tree produced by {@link DescriptionPatchParser#whitespaceOrLineBreakSpec}.
	 * @param ctx the parse tree
	 */
	void enterWhitespaceOrLineBreakSpec(DescriptionPatchParser.WhitespaceOrLineBreakSpecContext ctx);
	/**
	 * Exit a parse tree produced by {@link DescriptionPatchParser#whitespaceOrLineBreakSpec}.
	 * @param ctx the parse tree
	 */
	void exitWhitespaceOrLineBreakSpec(DescriptionPatchParser.WhitespaceOrLineBreakSpecContext ctx);
	/**
	 * Enter a parse tree produced by {@link DescriptionPatchParser#codeSpec}.
	 * @param ctx the parse tree
	 */
	void enterCodeSpec(DescriptionPatchParser.CodeSpecContext ctx);
	/**
	 * Exit a parse tree produced by {@link DescriptionPatchParser#codeSpec}.
	 * @param ctx the parse tree
	 */
	void exitCodeSpec(DescriptionPatchParser.CodeSpecContext ctx);
	/**
	 * Enter a parse tree produced by {@link DescriptionPatchParser#lineBreakMaybeCodeSpec}.
	 * @param ctx the parse tree
	 */
	void enterLineBreakMaybeCodeSpec(DescriptionPatchParser.LineBreakMaybeCodeSpecContext ctx);
	/**
	 * Exit a parse tree produced by {@link DescriptionPatchParser#lineBreakMaybeCodeSpec}.
	 * @param ctx the parse tree
	 */
	void exitLineBreakMaybeCodeSpec(DescriptionPatchParser.LineBreakMaybeCodeSpecContext ctx);
	/**
	 * Enter a parse tree produced by {@link DescriptionPatchParser#potentialConflictSpec}.
	 * @param ctx the parse tree
	 */
	void enterPotentialConflictSpec(DescriptionPatchParser.PotentialConflictSpecContext ctx);
	/**
	 * Exit a parse tree produced by {@link DescriptionPatchParser#potentialConflictSpec}.
	 * @param ctx the parse tree
	 */
	void exitPotentialConflictSpec(DescriptionPatchParser.PotentialConflictSpecContext ctx);
	/**
	 * Enter a parse tree produced by {@link DescriptionPatchParser#signMaybeWhitespaceSpec}.
	 * @param ctx the parse tree
	 */
	void enterSignMaybeWhitespaceSpec(DescriptionPatchParser.SignMaybeWhitespaceSpecContext ctx);
	/**
	 * Exit a parse tree produced by {@link DescriptionPatchParser#signMaybeWhitespaceSpec}.
	 * @param ctx the parse tree
	 */
	void exitSignMaybeWhitespaceSpec(DescriptionPatchParser.SignMaybeWhitespaceSpecContext ctx);
	/**
	 * Enter a parse tree produced by {@link DescriptionPatchParser#signConflictSpec}.
	 * @param ctx the parse tree
	 */
	void enterSignConflictSpec(DescriptionPatchParser.SignConflictSpecContext ctx);
	/**
	 * Exit a parse tree produced by {@link DescriptionPatchParser#signConflictSpec}.
	 * @param ctx the parse tree
	 */
	void exitSignConflictSpec(DescriptionPatchParser.SignConflictSpecContext ctx);
	/**
	 * Enter a parse tree produced by {@link DescriptionPatchParser#whitespaceSpec}.
	 * @param ctx the parse tree
	 */
	void enterWhitespaceSpec(DescriptionPatchParser.WhitespaceSpecContext ctx);
	/**
	 * Exit a parse tree produced by {@link DescriptionPatchParser#whitespaceSpec}.
	 * @param ctx the parse tree
	 */
	void exitWhitespaceSpec(DescriptionPatchParser.WhitespaceSpecContext ctx);
	/**
	 * Enter a parse tree produced by {@link DescriptionPatchParser#spacedDotSpec}.
	 * @param ctx the parse tree
	 */
	void enterSpacedDotSpec(DescriptionPatchParser.SpacedDotSpecContext ctx);
	/**
	 * Exit a parse tree produced by {@link DescriptionPatchParser#spacedDotSpec}.
	 * @param ctx the parse tree
	 */
	void exitSpacedDotSpec(DescriptionPatchParser.SpacedDotSpecContext ctx);
	/**
	 * Enter a parse tree produced by {@link DescriptionPatchParser#moreConflictSpec}.
	 * @param ctx the parse tree
	 */
	void enterMoreConflictSpec(DescriptionPatchParser.MoreConflictSpecContext ctx);
	/**
	 * Exit a parse tree produced by {@link DescriptionPatchParser#moreConflictSpec}.
	 * @param ctx the parse tree
	 */
	void exitMoreConflictSpec(DescriptionPatchParser.MoreConflictSpecContext ctx);
	/**
	 * Enter a parse tree produced by {@link DescriptionPatchParser#ignoreSpec}.
	 * @param ctx the parse tree
	 */
	void enterIgnoreSpec(DescriptionPatchParser.IgnoreSpecContext ctx);
	/**
	 * Exit a parse tree produced by {@link DescriptionPatchParser#ignoreSpec}.
	 * @param ctx the parse tree
	 */
	void exitIgnoreSpec(DescriptionPatchParser.IgnoreSpecContext ctx);
	/**
	 * Enter a parse tree produced by {@link DescriptionPatchParser#mainSpec}.
	 * @param ctx the parse tree
	 */
	void enterMainSpec(DescriptionPatchParser.MainSpecContext ctx);
	/**
	 * Exit a parse tree produced by {@link DescriptionPatchParser#mainSpec}.
	 * @param ctx the parse tree
	 */
	void exitMainSpec(DescriptionPatchParser.MainSpecContext ctx);
	/**
	 * Enter a parse tree produced by {@link DescriptionPatchParser#compilationUnit}.
	 * @param ctx the parse tree
	 */
	void enterCompilationUnit(DescriptionPatchParser.CompilationUnitContext ctx);
	/**
	 * Exit a parse tree produced by {@link DescriptionPatchParser#compilationUnit}.
	 * @param ctx the parse tree
	 */
	void exitCompilationUnit(DescriptionPatchParser.CompilationUnitContext ctx);
}