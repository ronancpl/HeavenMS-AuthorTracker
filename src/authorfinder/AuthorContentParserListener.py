# Generated from rules/AuthorContentParser.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AuthorContentParser import AuthorContentParser
else:
    from AuthorContentParser import AuthorContentParser

# This class defines a complete listener for a parse tree produced by AuthorContentParser.
class AuthorContentParserListener(ParseTreeListener):

    # Enter a parse tree produced by AuthorContentParser#main.
    def enterMain(self, ctx:AuthorContentParser.MainContext):
        pass

    # Exit a parse tree produced by AuthorContentParser#main.
    def exitMain(self, ctx:AuthorContentParser.MainContext):
        pass


    # Enter a parse tree produced by AuthorContentParser#mainSpec.
    def enterMainSpec(self, ctx:AuthorContentParser.MainSpecContext):
        pass

    # Exit a parse tree produced by AuthorContentParser#mainSpec.
    def exitMainSpec(self, ctx:AuthorContentParser.MainSpecContext):
        pass


    # Enter a parse tree produced by AuthorContentParser#codeSpec.
    def enterCodeSpec(self, ctx:AuthorContentParser.CodeSpecContext):
        pass

    # Exit a parse tree produced by AuthorContentParser#codeSpec.
    def exitCodeSpec(self, ctx:AuthorContentParser.CodeSpecContext):
        pass


    # Enter a parse tree produced by AuthorContentParser#commentSpec.
    def enterCommentSpec(self, ctx:AuthorContentParser.CommentSpecContext):
        pass

    # Exit a parse tree produced by AuthorContentParser#commentSpec.
    def exitCommentSpec(self, ctx:AuthorContentParser.CommentSpecContext):
        pass


    # Enter a parse tree produced by AuthorContentParser#commentBlock.
    def enterCommentBlock(self, ctx:AuthorContentParser.CommentBlockContext):
        pass

    # Exit a parse tree produced by AuthorContentParser#commentBlock.
    def exitCommentBlock(self, ctx:AuthorContentParser.CommentBlockContext):
        pass


    # Enter a parse tree produced by AuthorContentParser#commentBlockSpec.
    def enterCommentBlockSpec(self, ctx:AuthorContentParser.CommentBlockSpecContext):
        pass

    # Exit a parse tree produced by AuthorContentParser#commentBlockSpec.
    def exitCommentBlockSpec(self, ctx:AuthorContentParser.CommentBlockSpecContext):
        pass


    # Enter a parse tree produced by AuthorContentParser#out.
    def enterOut(self, ctx:AuthorContentParser.OutContext):
        pass

    # Exit a parse tree produced by AuthorContentParser#out.
    def exitOut(self, ctx:AuthorContentParser.OutContext):
        pass


    # Enter a parse tree produced by AuthorContentParser#commentByBlockSpec.
    def enterCommentByBlockSpec(self, ctx:AuthorContentParser.CommentByBlockSpecContext):
        pass

    # Exit a parse tree produced by AuthorContentParser#commentByBlockSpec.
    def exitCommentByBlockSpec(self, ctx:AuthorContentParser.CommentByBlockSpecContext):
        pass


    # Enter a parse tree produced by AuthorContentParser#commentByHeader.
    def enterCommentByHeader(self, ctx:AuthorContentParser.CommentByHeaderContext):
        pass

    # Exit a parse tree produced by AuthorContentParser#commentByHeader.
    def exitCommentByHeader(self, ctx:AuthorContentParser.CommentByHeaderContext):
        pass


    # Enter a parse tree produced by AuthorContentParser#commentByHeaderSkip.
    def enterCommentByHeaderSkip(self, ctx:AuthorContentParser.CommentByHeaderSkipContext):
        pass

    # Exit a parse tree produced by AuthorContentParser#commentByHeaderSkip.
    def exitCommentByHeaderSkip(self, ctx:AuthorContentParser.CommentByHeaderSkipContext):
        pass


    # Enter a parse tree produced by AuthorContentParser#commentByBody.
    def enterCommentByBody(self, ctx:AuthorContentParser.CommentByBodyContext):
        pass

    # Exit a parse tree produced by AuthorContentParser#commentByBody.
    def exitCommentByBody(self, ctx:AuthorContentParser.CommentByBodyContext):
        pass


    # Enter a parse tree produced by AuthorContentParser#commentByLine.
    def enterCommentByLine(self, ctx:AuthorContentParser.CommentByLineContext):
        pass

    # Exit a parse tree produced by AuthorContentParser#commentByLine.
    def exitCommentByLine(self, ctx:AuthorContentParser.CommentByLineContext):
        pass


    # Enter a parse tree produced by AuthorContentParser#commentLine.
    def enterCommentLine(self, ctx:AuthorContentParser.CommentLineContext):
        pass

    # Exit a parse tree produced by AuthorContentParser#commentLine.
    def exitCommentLine(self, ctx:AuthorContentParser.CommentLineContext):
        pass


    # Enter a parse tree produced by AuthorContentParser#commentInlineSpec.
    def enterCommentInlineSpec(self, ctx:AuthorContentParser.CommentInlineSpecContext):
        pass

    # Exit a parse tree produced by AuthorContentParser#commentInlineSpec.
    def exitCommentInlineSpec(self, ctx:AuthorContentParser.CommentInlineSpecContext):
        pass


    # Enter a parse tree produced by AuthorContentParser#author.
    def enterAuthor(self, ctx:AuthorContentParser.AuthorContext):
        pass

    # Exit a parse tree produced by AuthorContentParser#author.
    def exitAuthor(self, ctx:AuthorContentParser.AuthorContext):
        pass


    # Enter a parse tree produced by AuthorContentParser#contributor.
    def enterContributor(self, ctx:AuthorContentParser.ContributorContext):
        pass

    # Exit a parse tree produced by AuthorContentParser#contributor.
    def exitContributor(self, ctx:AuthorContentParser.ContributorContext):
        pass


    # Enter a parse tree produced by AuthorContentParser#patronNamesWrap.
    def enterPatronNamesWrap(self, ctx:AuthorContentParser.PatronNamesWrapContext):
        pass

    # Exit a parse tree produced by AuthorContentParser#patronNamesWrap.
    def exitPatronNamesWrap(self, ctx:AuthorContentParser.PatronNamesWrapContext):
        pass


    # Enter a parse tree produced by AuthorContentParser#patronNames.
    def enterPatronNames(self, ctx:AuthorContentParser.PatronNamesContext):
        pass

    # Exit a parse tree produced by AuthorContentParser#patronNames.
    def exitPatronNames(self, ctx:AuthorContentParser.PatronNamesContext):
        pass


    # Enter a parse tree produced by AuthorContentParser#patronName.
    def enterPatronName(self, ctx:AuthorContentParser.PatronNameContext):
        pass

    # Exit a parse tree produced by AuthorContentParser#patronName.
    def exitPatronName(self, ctx:AuthorContentParser.PatronNameContext):
        pass


    # Enter a parse tree produced by AuthorContentParser#patronAtomic.
    def enterPatronAtomic(self, ctx:AuthorContentParser.PatronAtomicContext):
        pass

    # Exit a parse tree produced by AuthorContentParser#patronAtomic.
    def exitPatronAtomic(self, ctx:AuthorContentParser.PatronAtomicContext):
        pass


    # Enter a parse tree produced by AuthorContentParser#patronSingleton.
    def enterPatronSingleton(self, ctx:AuthorContentParser.PatronSingletonContext):
        pass

    # Exit a parse tree produced by AuthorContentParser#patronSingleton.
    def exitPatronSingleton(self, ctx:AuthorContentParser.PatronSingletonContext):
        pass


    # Enter a parse tree produced by AuthorContentParser#patronAtomicSkip.
    def enterPatronAtomicSkip(self, ctx:AuthorContentParser.PatronAtomicSkipContext):
        pass

    # Exit a parse tree produced by AuthorContentParser#patronAtomicSkip.
    def exitPatronAtomicSkip(self, ctx:AuthorContentParser.PatronAtomicSkipContext):
        pass


    # Enter a parse tree produced by AuthorContentParser#patronCommentInternal.
    def enterPatronCommentInternal(self, ctx:AuthorContentParser.PatronCommentInternalContext):
        pass

    # Exit a parse tree produced by AuthorContentParser#patronCommentInternal.
    def exitPatronCommentInternal(self, ctx:AuthorContentParser.PatronCommentInternalContext):
        pass


