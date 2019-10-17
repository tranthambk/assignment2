import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    # def test_simple_program1(self):
    #     """Simple program: int main() {} """
    #     input = """int main() {}"""
    #     expect = "Program([FuncDecl(Id(main),[],IntType,Block([]))])"
    #     self.assertTrue(TestAST.checkASTGen(input,expect,300))
    # def test_more_complex_program2(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn(4);
    #     }"""
    #     expect = "Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(putIntLn),[IntLiteral(4)])]))])"
    #     self.assertTrue(TestAST.checkASTGen(input,expect,301))
    #
    # def test_call_without_parameter3(self):
    #     """More complex program"""
    #     input = """int main () {
    #         getIntLn();
    #     }"""
    #     expect = "Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(getIntLn),[])]))])"
    #     self.assertTrue(TestAST.checkASTGen(input,expect,302))
    def test_varDeclare0(self):
        input = """ int a,b,c;
         """
        expect = "Program([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,IntType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,300))
    def test_varDeclare1(self):
        input = """ int a,b,c[1];
         """
        expect = "Program([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,ArrayType(IntType,1))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    def test_varDeclare2(self):
        input = """ int a,b,c[1];
         """
        expect = "Program([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,ArrayType(IntType,1))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    def test_varDeclare3(self):
        input = """ float a,b,c[1];
         """
        expect = "Program([VarDecl(a,FloatType),VarDecl(b,FloatType),VarDecl(c,ArrayType(FloatType,1))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
    def test_varDeclare4(self):
        input = """ string a,b,c[1];
         """
        expect = "Program([VarDecl(a,StringType),VarDecl(b,StringType),VarDecl(c,ArrayType(StringType,1))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
    def test_varDeclare5(self):
        input = """ string a,b,c[1];
        float a,b,c;
         """
        expect = "Program([VarDecl(a,StringType),VarDecl(b,StringType),VarDecl(c,ArrayType(StringType,1)),VarDecl(a,FloatType),VarDecl(b,FloatType),VarDecl(c,FloatType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,305))
    def test_program1(self):
        input=""" int main(){
        }
        """
        expect= "Program([FuncDecl(Id(main),[],IntType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,306))
    def test_program2(self):
        input=""" int main(int a,float b){
        }
        """
        expect= "Program([FuncDecl(Id(main),[VarDecl(a,IntType),VarDecl(b,FloatType)],IntType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
    def test_program3(self):
        input=""" int main(int a,float b){
            double(2);
        }
        """
        expect= "Program([FuncDecl(Id(main),[VarDecl(a,IntType),VarDecl(b,FloatType)],IntType,Block([CallExpr(Id(double),[IntLiteral(2)])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
    def test_program4(self):
        input=""" int main(int a,float b){
            double();
        }
        """
        expect= "Program([FuncDecl(Id(main),[VarDecl(a,IntType),VarDecl(b,FloatType)],IntType,Block([CallExpr(Id(double),[])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,309))
    def test_program5(self):
        input=""" int main(int a,float b){
            int a,b;
            plus(a,b);
        }
        """
        expect= "Program([FuncDecl(Id(main),[VarDecl(a,IntType),VarDecl(b,FloatType)],IntType,Block([VarDecl(a,IntType),VarDecl(b,IntType),CallExpr(Id(plus),[Id(a),Id(b)])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,310))