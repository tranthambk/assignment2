from MCVisitor import MCVisitor
from MPParser import MPParser
from AST import *

class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):
        a=[self.visit(x) for x in ctx.many_declarations().declarations()]
        b=[]
        for i in a:
            if type(i) is not list:
                b.append(i)
            else:
                for j in i:
                    b.append(j)
        return Program(b)

    def visitDeclarations(self, ctx:MPParser.DeclarationsContext):
        return self.visit(ctx.getChild(0))

    def visitFunction_declarations(self,ctx:MPParser.Function_declarationsContext):
        name        = Id(ctx.IDENTIFIERS().getText())
        param       = self.visit(ctx.param_list()) if ctx.param_list() else []
        local       = self.visit(ctx.variable_declarations()) if ctx.variable_declarations() else []
        body        = self.visit(ctx.compound_statement())
        retType     = self.visit(ctx.mptype())
        return FuncDecl(name, param, local, body, retType)

    def visitProcedure_declarations(self, ctx:MPParser.Procedure_declarationsContext):
        name        = Id(ctx.IDENTIFIERS().getText())
        param       = self.visit(ctx.param_list()) if ctx.param_list() else []
        local       = self.visit(ctx.variable_declarations()) if ctx.variable_declarations() else []
        body        = self.visit(ctx.compound_statement())
        return FuncDecl(name, param, local, body, VoidType())

    def visitParam_list(self, ctx:MPParser.Param_listContext):
        a=ctx.var_declarations()
        b=[j for i in a for j in self.visit(i)]
        return b

    def visitVariable_declarations(self, ctx:MPParser.Variable_declarationsContext):
        return [j for i in ctx.list_var_declarations().var_declarations() for j in self.visit(i)]

    def visitList_var_declarations(self, ctx:MPParser.List_var_declarationsContext):
        return [j for i in ctx.var_declarations() for j in self.visit(i)]

    def visitVar_declarations(self, ctx:MPParser.Var_declarationsContext):
        mPtype=self.visit(ctx.mptype())
        a=[VarDecl(Id(i.getText()),mPtype) for i in ctx.IDENTIFIERS()]
        return a

    def visitMptype(self, ctx:MPParser.MptypeContext):
        if ctx.array_type():
            return self.visit(ctx.array_type())
        else:
            return self.visit(ctx.primitive_type())

    def visitPrimitive_type(self, ctx:MPParser.Primitive_typeContext):
        if ctx.INTEGER():
            return IntType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.STRING():
            return StringType()
        else:
            return FloatType()

    def visitArray_type(self, ctx:MPParser.Array_typeContext):
        return ArrayType(self.visit(ctx.lowerupper(0)),self.visit(ctx.lowerupper(1)),self.visit(ctx.primitive_type()))

    def visitLowerupper(self, ctx:MPParser.LowerupperContext):
        if ctx.SUB_OP() is None:
            a=ctx.INTEGERLITERAL().getText()
            b=int(ctx.INTEGERLITERAL().getText())
            return int(ctx.INTEGERLITERAL().getText())
        else:
            a=ctx.INTEGERLITERAL().getText()
            b=int(ctx.INTEGERLITERAL().getText())
            return -int(ctx.INTEGERLITERAL().getText())

    def visitExpression(self, ctx:MPParser.ExpressionContext):
        return self.visit(ctx.exp1())

    def visitExp1(self, ctx:MPParser.Exp1Context):
        if ctx.exp1() is None:
            a=ctx.exp2()
            return self.visit(ctx.exp2())
        else:
            if ctx.AND() is None:
                return BinaryOp("orelse",self.visit(ctx.exp1()),self.visit(ctx.exp2()))
            else:
                return BinaryOp("andthen",self.visit(ctx.exp1()),self.visit(ctx.exp2()))

    def visitExp2(self, ctx:MPParser.Exp2Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp3(0))
        else:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp3(0)),self.visit(ctx.exp3(1)))

    def visitExp3(self, ctx:MPParser.Exp3Context):
        if ctx.exp3() is None:
            return self.visit(ctx.exp4())
        else:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp3()),self.visit(ctx.exp4()))

    def visitExp4(self, ctx:MPParser.Exp4Context):
        if ctx.exp4() is None:
            return self.visit(ctx.exp5())
        else:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp4()),self.visit(ctx.exp5()))

    def visitExp5(self, ctx:MPParser.Exp5Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp6())
        else:
            return UnaryOp(ctx.getChild(0).getText(),self.visit(ctx.exp5()))

    def visitExp6(self, ctx:MPParser.Exp6Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp7())
        else:
            return ArrayCell(self.visit(ctx.exp7()),self.visit(ctx.exp1()))

    def visitExp7(self, ctx:MPParser.Exp7Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp8())
        else:
            return self.visit(ctx.exp1())

    def visitExp8(self, ctx:MPParser.Exp8Context):
        return self.visit(ctx.operands())

    def visitOperands(self, ctx:MPParser.OperandsContext):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.funccall():
            a=ctx.funccall()
            b=Id(a.IDENTIFIERS().getText())
            c=[]
            if a.expression() is None:
                c=[]
            else:
                c=[self.visit(i) for i in a.expression()]
            return CallExpr(b,c);
        else:
            return Id(ctx.IDENTIFIERS().getText())

    def visitIndex_expression(self, ctx:MPParser.Index_expressionContext):
        return ArrayCell(self.visit(ctx.expression(0)),self.visit(ctx.expression(1)))

    def visitLiteral(self, ctx:MPParser.LiteralContext):
        if ctx.INTEGERLITERAL():
            return IntLiteral(int(ctx.INTEGERLITERAL().getText()))
        elif ctx.REALLITERAL():
            return FloatLiteral(float(ctx.REALLITERAL().getText()))
        elif ctx.BOOLEANLITERAL():
            return BooleanLiteral(True if ctx.BOOLEANLITERAL().getText()[0] in ["T","t"] else False)
        else:
            return StringLiteral(ctx.STRINGLITERAL().getText())

    def visitStatement(self, ctx:MPParser.StatementContext):
        if ctx.assignment_statement():
            return self.visit(ctx.assignment_statement())
        elif ctx.if_statement():
            return [self.visit(ctx.if_statement())]
        elif ctx.for_statement():
            return [self.visit(ctx.for_statement())]
        elif ctx.while_statement():
            return [self.visit(ctx.while_statement())]
        elif ctx.break_statement():
            return [self.visit(ctx.break_statement())]
        elif ctx.continue_statement():
            return [self.visit(ctx.continue_statement())]
        elif ctx.return_statement():
            return [self.visit(ctx.return_statement())]
        elif ctx.call_statement():
            return [self.visit(ctx.call_statement())]
        elif ctx.with_statement():
            return [self.visit(ctx.with_statement())]
        else:
            return self.visit(ctx.compound_statement())

    def visitAssignment_statement(self, ctx:MPParser.Assignment_statementContext):
        d=list(reversed(range((ctx.getChildCount()-2)//2)))
        a=self.visit(ctx.expression())
        retList=[]
        for i in d:
            q=ctx.getChild(2*i)
            q=self.visit(q)
            retList.append(Assign(q,a))
            a=q
        return retList

    def visitIid(self, ctx:MPParser.IidContext):
        return Id(ctx.IDENTIFIERS().getText())

    def visitIf_statement(self, ctx:MPParser.If_statementContext):
        if ctx.getChildCount()==4:
            return If(self.visit(ctx.expression()),self.visit(ctx.statement(0)))
        elif ctx.getChildCount()==6:
            return If(self.visit(ctx.expression()),self.visit(ctx.statement(0)),self.visit(ctx.statement(1)))
        else:
            print("Error if child count","askjdh")

    def visitWhile_statement(self, ctx:MPParser.While_statementContext):
        return While(self.visit(ctx.expression()),self.visit(ctx.statement()))

    def visitFor_statement(self, ctx:MPParser.For_statementContext):
        return For(Id(ctx.IDENTIFIERS().getText()),self.visit(ctx.expression(0)),self.visit(ctx.expression(1)),True if ctx.TO() is not None else False,self.visit(ctx.statement()))

    def visitBreak_statement(self, ctx:MPParser.Break_statementContext):
        return Break()

    def visitContinue_statement(self, ctx:MPParser.Continue_statementContext):
        return Continue()

    def visitReturn_statement(self, ctx:MPParser.Return_statementContext):
        if ctx.expression() is None:
            return Return()
        else:
            return Return(self.visit(ctx.expression()))

    def visitCompound_statement(self, ctx:MPParser.Compound_statementContext):
        if ctx.statement():
            return [j for i in ctx.statement() for j in self.visit(i)]
        else:
            return []

    def visitWith_statement(self, ctx:MPParser.With_statementContext):
        a=self.visit(ctx.list_var_declarations())
        b=self.visit(ctx.statement())
        return With(self.visit(ctx.list_var_declarations()),self.visit(ctx.statement()))

    def visitCall_statement(self, ctx:MPParser.Call_statementContext):
        a=ctx.funccall()
        b=Id(a.IDENTIFIERS().getText())
        c=[]
        if a.expression() is None:
            c=[]
        else:
            c=[self.visit(i) for i in a.expression()]
        return CallStmt(b,c);