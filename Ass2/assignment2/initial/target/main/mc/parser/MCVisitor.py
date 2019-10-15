# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete generic visitor for a parse tree produced by MCParser.

class MCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#declares.
    def visitDeclares(self, ctx:MCParser.DeclaresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#declare.
    def visitDeclare(self, ctx:MCParser.DeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#varDeclare.
    def visitVarDeclare(self, ctx:MCParser.VarDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#manyVariable.
    def visitManyVariable(self, ctx:MCParser.ManyVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#variable.
    def visitVariable(self, ctx:MCParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#id_single.
    def visitId_single(self, ctx:MCParser.Id_singleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#id_array.
    def visitId_array(self, ctx:MCParser.Id_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funcDeclare.
    def visitFuncDeclare(self, ctx:MCParser.FuncDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#paraList.
    def visitParaList(self, ctx:MCParser.ParaListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#paraDecl.
    def visitParaDecl(self, ctx:MCParser.ParaDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#blockstmt.
    def visitBlockstmt(self, ctx:MCParser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#var_stmt.
    def visitVar_stmt(self, ctx:MCParser.Var_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#stmt.
    def visitStmt(self, ctx:MCParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#ifstmt.
    def visitIfstmt(self, ctx:MCParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#do_whilestmt.
    def visitDo_whilestmt(self, ctx:MCParser.Do_whilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#forstmt.
    def visitForstmt(self, ctx:MCParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#breakstmt.
    def visitBreakstmt(self, ctx:MCParser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#continuestmt.
    def visitContinuestmt(self, ctx:MCParser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#returnstmt.
    def visitReturnstmt(self, ctx:MCParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#mctype.
    def visitMctype(self, ctx:MCParser.MctypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp.
    def visitExp(self, ctx:MCParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp1.
    def visitExp1(self, ctx:MCParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp2.
    def visitExp2(self, ctx:MCParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp3.
    def visitExp3(self, ctx:MCParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp4.
    def visitExp4(self, ctx:MCParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp5.
    def visitExp5(self, ctx:MCParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp6.
    def visitExp6(self, ctx:MCParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp7.
    def visitExp7(self, ctx:MCParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp8.
    def visitExp8(self, ctx:MCParser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp9.
    def visitExp9(self, ctx:MCParser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#operand.
    def visitOperand(self, ctx:MCParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funcall.
    def visitFuncall(self, ctx:MCParser.FuncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#parameterList.
    def visitParameterList(self, ctx:MCParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#parameter.
    def visitParameter(self, ctx:MCParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#primitivetype.
    def visitPrimitivetype(self, ctx:MCParser.PrimitivetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#arraypointertype.
    def visitArraypointertype(self, ctx:MCParser.ArraypointertypeContext):
        return self.visitChildren(ctx)



del MCParser