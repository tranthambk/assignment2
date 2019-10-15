from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class ASTGeneration(MCVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return Program(self.visit(ctx.declares()))

    def visitDeclares(self, ctx:MCParser.DeclaresContext):
        return [j for i in ctx.declare() for j in self.visit(i)]

    # Visit a parse tree produced by MCParser#declare.
    def visitDeclare(self, ctx:MCParser.DeclareContext):
        return self.visit(ctx.varDeclare()) if ctx.varDeclare() else [self.visit(ctx.funcDeclare())]

  # Visit a parse tree produced by MCParser#varDeclare.
    def visitVarDeclare(self, ctx:MCParser.VarDeclareContext):
        result=[]
        varType=self.visit(ctx.primitivetype())
        for i in ctx.manyVariable().variable():
            if(i.id_single()):
                result+=[VarDecl(i.id_single().ID().getText(),varType)]
            if(i.id_array()):
             result+=[VarDecl(i.id_array().ID().getText(), ArrayType(int(i.id_array().INTLIT().getText()),varType))]
        return result
    # Visit a parse tree produced by MCParser#funcDeclare.
    def visitFuncDeclare(self, ctx:MCParser.FuncDeclareContext):
        nameFunc=Id(ctx.ID().getText())
        if ctx.paraList():
            paraFunc=self.visit(ctx.paraList())
        else:
            paraFunc=[]
        returnType=self.visit(ctx.mctype())
        bodyFunc=self.visit(ctx.blockstmt())
        return FuncDecl(nameFunc, paraFunc, returnType, bodyFunc)
    # Visit a parse tree produced by MCParser#paraList.
    def visitParaList(self, ctx:MCParser.ParaListContext):
        return [j for i in ctx.paraDecl() for j in self.visit(i)]

    # Visit a parse tree produced by MCParser#paraDecl.
    def visitParaDecl(self, ctx:MCParser.ParaDeclContext):
        if ctx.getChildCount()==2:
            return [VarDecl(ctx.ID().getText(),self.visit(ctx.primitivetype()))]
        return [VarDecl(ctx.ID().getText(),ArrayPointerType(self.visit(ctx.primitivetype())))]

    # Visit a parse tree produced by MCParser#blockstmt.
    def visitBlockstmt(self, ctx:MCParser.BlockstmtContext):
        return Block([ j for i in ctx.var_stmt() for j in self.visit(i)])
        # if ctx.var_stmt():
        #     return Block([self.visit(ctx.var_stmt())])
        # else:
        #     return Block([])
    # Visit a parse tree produced by MCParser#var_stmt.
    def visitVar_stmt(self, ctx:MCParser.Var_stmtContext):
        if ctx.varDeclare():
            return self.visit(ctx.varDeclare())
        return [self.visit(ctx.stmt())]
    # Visit a parse tree produced by MCParser#stmt.
    def visitStmt(self, ctx:MCParser.StmtContext):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by MCParser#ifstmt.
    def visitIfstmt(self, ctx:MCParser.IfstmtContext):
        expr=self.visit(ctx.exp())
        if ctx.getChildCount()==5:
            return If(expr,self.visit(ctx.stmt(0)))
        return If(expr,self.visit(ctx.stmt(0)), self.visit(ctx.stmt(1)))
    # Visit a parse tree produced by MCParser#do_whilestmt.
    def visitDo_whilestmt(self, ctx:MCParser.Do_whilestmtContext):
        a=[]
        for i in ctx.stmt():
            a+=[self.visit(i)]
        return Dowhile(a,self.visit(ctx.exp()))
    # Visit a parse tree produced by MCParser#forstmt.
    def visitForstmt(self, ctx:MCParser.ForstmtContext):
        return For(self.visit(ctx.exp(0)),self.visit(ctx.exp(1)),self.visit(ctx.exp(2)),self.visit(ctx.stmt()))

    # Visit a parse tree produced by MCParser#breakstmt.
    def visitBreakstmt(self, ctx:MCParser.BreakstmtContext):
        return Break()


    # Visit a parse tree produced by MCParser#continuestmt.
    def visitContinuestmt(self, ctx:MCParser.ContinuestmtContext):
        return Continue()


    # Visit a parse tree produced by MCParser#returnstmt.
    def visitReturnstmt(self, ctx:MCParser.ReturnstmtContext):
        if ctx.exp():
            return Return(self.visit(ctx.exp()))
        return Return()


    # Visit a parse tree produced by MCParser#mctype.
    def visitMctype(self, ctx:MCParser.MctypeContext):
        if ctx.primitivetype():
            return self.visit(ctx.primitivetype())
        elif ctx.arraypointertype():
            return self.visit(ctx.arraypointertype())
        return VoidType()


    # Visit a parse tree produced by MCParser#exp.
    def visitExp(self, ctx:MCParser.ExpContext):
        if ctx.ASSIGN():
            return BinaryOp(ctx.ASSIGN().getText(),self.visit(ctx.exp1()),self.visit(ctx.exp()))
        return self.visit(ctx.exp1())


    # Visit a parse tree produced by MCParser#exp1.
    def visitExp1(self, ctx:MCParser.Exp1Context):
        if ctx.OR():
            return BinaryOp(ctx.OR().getText(),self.visit(ctx.exp1()),self.visit(ctx.exp2()))
        return self.visit(ctx.exp2())


    # Visit a parse tree produced by MCParser#exp2.
    def visitExp2(self, ctx:MCParser.Exp2Context):
        if ctx.AND():
            return BinaryOp(ctx.AND().getText(),self.visit(ctx.exp2()),self.visit(ctx.exp3()))
        return self.visit(ctx.exp3())


    # Visit a parse tree produced by MCParser#exp3.
    def visitExp3(self, ctx:MCParser.Exp3Context):
        if ctx.getChildCount()==3:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp4(0)),self.visit(ctx.exp4(1)))
        return self.visit(ctx.exp4(0))


    # Visit a parse tree produced by MCParser#exp4.
    def visitExp4(self, ctx:MCParser.Exp4Context):
        if ctx.getChildCount()==3:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp5(0)),self.visit(ctx.exp5(1)))
        return self.visit(ctx.exp5(0))


    # Visit a parse tree produced by MCParser#exp5.
    def visitExp5(self, ctx:MCParser.Exp5Context):
        if ctx.getChildCount()==3:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp5()),self.visit(ctx.exp6()))
        return self.visit(ctx.exp6())

    # Visit a parse tree produced by MCParser#exp6.
    def visitExp6(self, ctx:MCParser.Exp6Context):
        if ctx.getChildCount()==3:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp6()),self.visit(ctx.exp7()))
        return self.visit(ctx.exp7())


    # Visit a parse tree produced by MCParser#exp7.
    def visitExp7(self, ctx:MCParser.Exp7Context):
        if(ctx.getChildCount()==2):
            return UnaryOp(ctx.getChild(0).getText(),self.visit(ctx.exp7()))
        return self.visit(ctx.exp8())


    # Visit a parse tree produced by MCParser#exp8.
    def visitExp8(self, ctx:MCParser.Exp8Context):
        if(ctx.getChildCount()==4):
            return ArrayCell(self.visit(ctx.exp9()),self.visit(ctx.exp()))
        return self.visit(ctx.exp9())


    # Visit a parse tree produced by MCParser#exp9.
    def visitExp9(self, ctx:MCParser.Exp9Context):
        if ctx.exp():
            return self.visit(ctx.exp())
        return self.visit(ctx.operand())

    # Visit a parse tree produced by MCParser#operand.
    def visitOperand(self, ctx:MCParser.OperandContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.Booleanlit():
            return BooleanLiteral(True if ctx.Booleanlit().getText()[0]=="t" else False)
        elif ctx.Realit():
            return FloatLiteral(float(ctx.Realit().getText()))
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.Stringlit():
            return StringLiteral(ctx.Stringlit().getText())
        return self.visit(ctx.funcall())


    # Visit a parse tree produced by MCParser#funcall.
    def visitFuncall(self, ctx:MCParser.FuncallContext):
        if ctx.getChildCount()==3:
            return CallExpr(Id(ctx.ID().getText()),[])
        return CallExpr(Id(ctx.ID().getText()), [self.visit(x) for x in ctx.parameter()])

    # Visit a parse tree produced by MCParser#parameterList.

    # Visit a parse tree produced by MCParser#parameter.
    def visitParameter(self, ctx:MCParser.ParameterContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.Booleanlit():
            return BooleanLiteral(True if ctx.Booleanlit().getText()[0]=="t" else False)
        elif ctx.Realit():
            return FloatLiteral(float(ctx.Realit().getText()))
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.Stringlit():
            return StringLiteral(ctx.Stringlit().getText())
        return self.visit(ctx.exp())


    # Visit a parse tree produced by MCParser#primitivetype.
    def visitPrimitivetype(self, ctx:MCParser.PrimitivetypeContext):
        if ctx.INTTYPE():
            return IntType()
        if ctx.BOOLEANTYPE():
            return BoolType()
        if ctx.STRINGTYPE():
            return StringType()
        return FloatType()


    # Visit a parse tree produced by MCParser#arraypointertype.
    def visitArraypointertype(self, ctx:MCParser.ArraypointertypeContext):
        return ArrayPointerType(self.visit(ctx.primitivetype()))