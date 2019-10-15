# Trong file AST.py chinh sua 1 so diem:
#   1. def __str__ trong class VoidType: xoa ()
#   2. def __str__ trong class For: them , vao giua ""
#   3. def ArrayCell: sua thanh class ArrayCell
#

import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """procedure main();begin end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_simple_error_program(self):
        input = """
        procedure a();
        begin
            a();
        end
        """
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[CallStmt(Id(r'a'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,301))

    def test_ambiguous_if(self):
        """Test ambiguous if"""
        input = """
        procedure abc();
        begin
            if a=4 then
                if a=2 then c:=7;
                else w:=3;
        end
        """
        expect = str(Program([FuncDecl(Id(r'abc'),[],[],[If(BinaryOp(r'=',Id(r'a'),IntLiteral(4)),[If(BinaryOp(r'=',Id(r'a'),IntLiteral(2)),[Assign(Id(r'c'),IntLiteral(7))],[Assign(Id(r'w'),IntLiteral(3))])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_var(self):
        """Test var"""
        input = """var a:integer;"""
        expect = str(Program([VarDecl(Id(r'a'),IntType())]))
        self.assertTrue(TestAST.test(input,expect,303))

    def test_multi_var(self):
        input = """var a,b,c:integer;d,e:real;"""
        expect = str(Program([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType()),VarDecl(Id(r'd'),FloatType()),VarDecl(Id(r'e'),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,304))

    def test_double_var(self):
        input = """var a:integer;var b:real;"""
        expect = str(Program([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,305))

    def test_true_bool_lit(self):
        input = """procedure a();begin a:=true;a:=True;a:=tRUE;a:=TrUe; end"""
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[Assign(Id(r'a'),BooleanLiteral(True)),Assign(Id(r'a'),BooleanLiteral(True)),Assign(Id(r'a'),BooleanLiteral(True)),Assign(Id(r'a'),BooleanLiteral(True))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,306))

    def test_false_bool_lit(self):
        input = """procedure a();begin a:=false;a:=False;a:=fALSE;a:=FaLSe; end"""
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[Assign(Id(r'a'),BooleanLiteral(False)),Assign(Id(r'a'),BooleanLiteral(False)),Assign(Id(r'a'),BooleanLiteral(False)),Assign(Id(r'a'),BooleanLiteral(False))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,307))

    def test_float_program(self):
        input = """procedure a();begin a:=5.3;end """
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[Assign(Id(r'a'),FloatLiteral(5.3))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,308))

    def test_assign_operator(self):
        input = """procedure a(); begin a:=b:=c:=d;end"""
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[Assign(Id(r'c'),Id(r'd')),Assign(Id(r'b'),Id(r'c')),Assign(Id(r'a'),Id(r'b'))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,309))

    def test_function(self):
        input = """function try():integer;begin try();end"""
        expect = str(Program([FuncDecl(Id(r'try'),[],[],[CallStmt(Id(r'try'),[])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,310))

    def test_a_little_bit_complex_program(self):
        input = """
            function TCefBrowserRefGetFrameIdentifiers(aFrameCount : InteGeR; aFrameIdentifierArray : string) : boolean;
            var
                i : Integer;
            begin
                Result := False;

                if (aFrameCount > 0) then
                begin
                    SetLength(aFrameIdentifierArray, aFrameCount);
                    i := 0;
                    while (i < aFrameCount) do
                        begin
                           aFrameIdentifierArray[i] := 0;
                           inc(i);
                        end

            PCefBrowserget_frame_identifiers(PCefBrowser(FData), aFrameCount, aFrameIdentifierArray[0]);

            Result := True;
            end
           if CustomExceptionHandler("TCefBrowserRef.GetFrameIdentifiers", e) then break;
            end
        """
        expect = str(Program([FuncDecl(Id(r'TCefBrowserRefGetFrameIdentifiers'),[VarDecl(Id(r'aFrameCount'),IntType()),VarDecl(Id(r'aFrameIdentifierArray'),StringType())],[VarDecl(Id(r'i'),IntType())],[Assign(Id(r'Result'),BooleanLiteral(False)),If(BinaryOp(r'>',Id(r'aFrameCount'),IntLiteral(0)),[CallStmt(Id(r'SetLength'),[Id(r'aFrameIdentifierArray'),Id(r'aFrameCount')]),Assign(Id(r'i'),IntLiteral(0)),While(BinaryOp(r'<',Id(r'i'),Id(r'aFrameCount')),[Assign(ArrayCell(Id(r'aFrameIdentifierArray'),Id(r'i')),IntLiteral(0)),CallStmt(Id(r'inc'),[Id(r'i')])]),CallStmt(Id(r'PCefBrowserget_frame_identifiers'),[CallExpr(Id(r'PCefBrowser'),[Id(r'FData')]),Id(r'aFrameCount'),ArrayCell(Id(r'aFrameIdentifierArray'),IntLiteral(0))]),Assign(Id(r'Result'),BooleanLiteral(True))],[]),If(CallExpr(Id(r'CustomExceptionHandler'),[StringLiteral(r'TCefBrowserRef.GetFrameIdentifiers'),Id(r'e')]),[Break()],[])],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,311))

    def test_complex_func(self):
        input = """
            procedure TCastleBaseTestCaseAssertVectorEquals(Expected, Actual: Integer);
            begin
                if not TVector2ByteEquals(Expected, Actual) then
                Fail(Format("Vectors (TVector2Byte) are not equal: expected: %s, actual: %s"));
            end
        """
        expect = str(Program([FuncDecl(Id(r'TCastleBaseTestCaseAssertVectorEquals'),[VarDecl(Id(r'Expected'),IntType()),VarDecl(Id(r'Actual'),IntType())],[],[If(UnaryOp(r'not',CallExpr(Id(r'TVector2ByteEquals'),[Id(r'Expected'),Id(r'Actual')])),[CallStmt(Id(r'Fail'),[CallExpr(Id(r'Format'),[StringLiteral(r'Vectors (TVector2Byte) are not equal: expected: %s, actual: %s')])])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,312))

    def test_max_func(self):
        input = """
            function max(num1, num2: integer): integer;
            var
                (* local variable declaration *)
                result: integer;
            begin
                if (num1 > num2) then
                result := num1;
            else
                result := num2;
                max := result;
            end
            """
        expect = str(Program([FuncDecl(Id(r'max'),[VarDecl(Id(r'num1'),IntType()),VarDecl(Id(r'num2'),IntType())],[VarDecl(Id(r'result'),IntType())],[If(BinaryOp(r'>',Id(r'num1'),Id(r'num2')),[Assign(Id(r'result'),Id(r'num1'))],[Assign(Id(r'result'),Id(r'num2'))]),Assign(Id(r'max'),Id(r'result'))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,313))

    def test_very_simple_program(self):
        input = """
        procedurE foo (b : real) ;
            begin
             1[1] := 1;
             //(1>=0)[2] := 2+a[1][1]+c+("abc"< 0);
             ahihi(1)[m+1] := 3;
             (1=1)[1]:=1;
             (1+a[1]+(1<0))[10] := 4;
            End
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'b'),FloatType())],[],[Assign(ArrayCell(IntLiteral(1),IntLiteral(1)),IntLiteral(1)),Assign(ArrayCell(CallExpr(Id(r'ahihi'),[IntLiteral(1)]),BinaryOp(r'+',Id(r'm'),IntLiteral(1))),IntLiteral(3)),Assign(ArrayCell(BinaryOp(r'=',IntLiteral(1),IntLiteral(1)),IntLiteral(1)),IntLiteral(1)),Assign(ArrayCell(BinaryOp(r'+',BinaryOp(r'+',IntLiteral(1),ArrayCell(Id(r'a'),IntLiteral(1))),BinaryOp(r'<',IntLiteral(1),IntLiteral(0))),IntLiteral(10)),IntLiteral(4))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,314))

    def test_more_assign_statement(self):
        input = """procedure a(); 
        begin 
            r:=d;
            d:=d;
            d:=r;
            r:=d:=r[2]:=r(r[r]+d)[2]:=d:=r+4;
            if r then r();
        end"""
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[Assign(Id(r'r'),Id(r'd')),Assign(Id(r'd'),Id(r'd')),Assign(Id(r'd'),Id(r'r')),Assign(Id(r'd'),BinaryOp(r'+',Id(r'r'),IntLiteral(4))),Assign(ArrayCell(CallExpr(Id(r'r'),[BinaryOp(r'+',ArrayCell(Id(r'r'),Id(r'r')),Id(r'd'))]),IntLiteral(2)),Id(r'd')),Assign(ArrayCell(Id(r'r'),IntLiteral(2)),ArrayCell(CallExpr(Id(r'r'),[BinaryOp(r'+',ArrayCell(Id(r'r'),Id(r'r')),Id(r'd'))]),IntLiteral(2))),Assign(Id(r'd'),ArrayCell(Id(r'r'),IntLiteral(2))),Assign(Id(r'r'),Id(r'd')),If(Id(r'r'),[CallStmt(Id(r'r'),[])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,315))

    def test_assignment_statement(self):
        input = """
        procedure a(); begin a:=2=2; end
        """
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[Assign(Id(r'a'),BinaryOp(r'=',IntLiteral(2),IntLiteral(2)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,316))

    def test_multi_assignment_statement(self):
        input = """procedure a(); begin a:=2[2]:=e:=wkk(33[32])[1]:=2=2; end"""
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[Assign(ArrayCell(CallExpr(Id(r'wkk'),[ArrayCell(IntLiteral(33),IntLiteral(32))]),IntLiteral(1)),BinaryOp(r'=',IntLiteral(2),IntLiteral(2))),Assign(Id(r'e'),ArrayCell(CallExpr(Id(r'wkk'),[ArrayCell(IntLiteral(33),IntLiteral(32))]),IntLiteral(1))),Assign(ArrayCell(IntLiteral(2),IntLiteral(2)),Id(r'e')),Assign(Id(r'a'),ArrayCell(IntLiteral(2),IntLiteral(2)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,317))

    def test_ambiglious_if_statement(self):
        input = """procedure a(); begin if a=2 then if b() then c(); else a:=4;end"""
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[If(BinaryOp(r'=',Id(r'a'),IntLiteral(2)),[If(CallExpr(Id(r'b'),[]),[CallStmt(Id(r'c'),[])],[Assign(Id(r'a'),IntLiteral(4))])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,318))

    def test_if_statement(self):
        input = """procedure a(); begin if a=2 then b(); end"""
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[If(BinaryOp(r'=',Id(r'a'),IntLiteral(2)),[CallStmt(Id(r'b'),[])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,319))

    def test_if_else_statement(self):
        input = """procedure a(); begin if a=2 then b(); else c(); end"""
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[If(BinaryOp(r'=',Id(r'a'),IntLiteral(2)),[CallStmt(Id(r'b'),[])],[CallStmt(Id(r'c'),[])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,320))

    def test_full_option_if_else_statement(self):
        input = """procedure a();begin if a() then if b() then c(); else d();else e();end"""
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[If(CallExpr(Id(r'a'),[]),[If(CallExpr(Id(r'b'),[]),[CallStmt(Id(r'c'),[])],[CallStmt(Id(r'd'),[])])],[CallStmt(Id(r'e'),[])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,321))

    def test_while_statement(self):
        input = """procedure a(); begin while true do b(); end"""
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[While(BooleanLiteral(True),[CallStmt(Id(r'b'),[])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,322))

    def test_error_while_statement(self):
        input = """procedure a();begin while a() do while false do d(); end"""
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[While(CallExpr(Id(r'a'),[]),[While(BooleanLiteral(False),[CallStmt(Id(r'd'),[])])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,323))

    def test_for_statement(self):
        input = """procedure a(); begin for i:=1 to 2 do b(); end"""
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[For(Id(r'i'),IntLiteral(1),IntLiteral(2),True,[CallStmt(Id(r'b'),[])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,324))

    def test_for_downto_statement(self):
        input = """procedure a(); begin for i:=1 downto 20000 do b(); end"""
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[For(Id(r'i'),IntLiteral(1),IntLiteral(20000),False,[CallStmt(Id(r'b'),[])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,325))

    def test_double_for(self):
        input = """procedure a(); begin for i:=2 to 400 do for j:=i to 400+1 do print(i+j," "); end"""
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[For(Id(r'i'),IntLiteral(2),IntLiteral(400),True,[For(Id(r'j'),Id(r'i'),BinaryOp(r'+',IntLiteral(400),IntLiteral(1)),True,[CallStmt(Id(r'print'),[BinaryOp(r'+',Id(r'i'),Id(r'j')),StringLiteral(r' ')])])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,326))

    def test_quicksort(self):
        input = """    
              procedure sort(l,r: integer);
                var i,j,x,y: integer;
                begin
                  i:=l;
                  j:=r;
                  x:=a[(l+r) div 2];
                  while (i<=j) do
                  begin
                    while a[i]<x do inc(i);
                    while x<a[j] do dec(j);
                    if not(i>j) then
                      begin
                        y:=a[i];
                        a[i]:=a[j];
                        a[j]:=y;
                        inc(i);
                        j:=j-1;
                      end
                  end
                  if l<j then sort(l,j);
                  if i<r then sort(i,r);
                end
            """
        expect = str(Program([FuncDecl(Id(r'sort'),[VarDecl(Id(r'l'),IntType()),VarDecl(Id(r'r'),IntType())],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'j'),IntType()),VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[Assign(Id(r'i'),Id(r'l')),Assign(Id(r'j'),Id(r'r')),Assign(Id(r'x'),ArrayCell(Id(r'a'),BinaryOp(r'div',BinaryOp(r'+',Id(r'l'),Id(r'r')),IntLiteral(2)))),While(BinaryOp(r'<=',Id(r'i'),Id(r'j')),[While(BinaryOp(r'<',ArrayCell(Id(r'a'),Id(r'i')),Id(r'x')),[CallStmt(Id(r'inc'),[Id(r'i')])]),While(BinaryOp(r'<',Id(r'x'),ArrayCell(Id(r'a'),Id(r'j'))),[CallStmt(Id(r'dec'),[Id(r'j')])]),If(UnaryOp(r'not',BinaryOp(r'>',Id(r'i'),Id(r'j'))),[Assign(Id(r'y'),ArrayCell(Id(r'a'),Id(r'i'))),Assign(ArrayCell(Id(r'a'),Id(r'i')),ArrayCell(Id(r'a'),Id(r'j'))),Assign(ArrayCell(Id(r'a'),Id(r'j')),Id(r'y')),CallStmt(Id(r'inc'),[Id(r'i')]),Assign(Id(r'j'),BinaryOp(r'-',Id(r'j'),IntLiteral(1)))],[])]),If(BinaryOp(r'<',Id(r'l'),Id(r'j')),[CallStmt(Id(r'sort'),[Id(r'l'),Id(r'j')])],[]),If(BinaryOp(r'<',Id(r'i'),Id(r'r')),[CallStmt(Id(r'sort'),[Id(r'i'),Id(r'r')])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,327))

    def test_arraycell_assign_arraycell(self):
        input = """
        procedure a();
        begin
            a[2]:=a[4];
        end
        """
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[Assign(ArrayCell(Id(r'a'),IntLiteral(2)),ArrayCell(Id(r'a'),IntLiteral(4)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,328))

    def test_make_square(self):
        input = """
            procedure makesquare( sq : real; limit : integer);
                var
                   num,r,c : integer;
                begin
                   for r:=1 to limit do
                     for c:=1 to limit do
                       sq[rc] := 0;
                   if (limit and 1)<>0 then
                     begin
                        r:=(limit+1) div 2;
                        c:=limit;
                        for num:=1 to limit*limit do
                          begin
                             if sq[rc]<>0 then
                               begin
                                  dec(r);
                                  if r<1 then
                                    inc(r,limit);
                                  dec(c,2);
                                  if c<1 then
                                    inc(c,limit);
                               end
                             sq[rc]:=num;
                             inc(r);
                             if r>limit then
                               dec(r,limit);
                             inc(c);
                             if c>limit then
                               dec(c,limit);
                          end
                     end
                 end
            """
        expect = str(Program([FuncDecl(Id(r'makesquare'),[VarDecl(Id(r'sq'),FloatType()),VarDecl(Id(r'limit'),IntType())],[VarDecl(Id(r'num'),IntType()),VarDecl(Id(r'r'),IntType()),VarDecl(Id(r'c'),IntType())],[For(Id(r'r'),IntLiteral(1),Id(r'limit'),True,[For(Id(r'c'),IntLiteral(1),Id(r'limit'),True,[Assign(ArrayCell(Id(r'sq'),Id(r'rc')),IntLiteral(0))])]),If(BinaryOp(r'<>',BinaryOp(r'and',Id(r'limit'),IntLiteral(1)),IntLiteral(0)),[Assign(Id(r'r'),BinaryOp(r'div',BinaryOp(r'+',Id(r'limit'),IntLiteral(1)),IntLiteral(2))),Assign(Id(r'c'),Id(r'limit')),For(Id(r'num'),IntLiteral(1),BinaryOp(r'*',Id(r'limit'),Id(r'limit')),True,[If(BinaryOp(r'<>',ArrayCell(Id(r'sq'),Id(r'rc')),IntLiteral(0)),[CallStmt(Id(r'dec'),[Id(r'r')]),If(BinaryOp(r'<',Id(r'r'),IntLiteral(1)),[CallStmt(Id(r'inc'),[Id(r'r'),Id(r'limit')])],[]),CallStmt(Id(r'dec'),[Id(r'c'),IntLiteral(2)]),If(BinaryOp(r'<',Id(r'c'),IntLiteral(1)),[CallStmt(Id(r'inc'),[Id(r'c'),Id(r'limit')])],[])],[]),Assign(ArrayCell(Id(r'sq'),Id(r'rc')),Id(r'num')),CallStmt(Id(r'inc'),[Id(r'r')]),If(BinaryOp(r'>',Id(r'r'),Id(r'limit')),[CallStmt(Id(r'dec'),[Id(r'r'),Id(r'limit')])],[]),CallStmt(Id(r'inc'),[Id(r'c')]),If(BinaryOp(r'>',Id(r'c'),Id(r'limit')),[CallStmt(Id(r'dec'),[Id(r'c'),Id(r'limit')])],[])])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,329))

    def test_write_square(self):
        input = """
                procedure writesquare(sq : real;limit : integer);
                var
                   row,col : integer;
                begin
                   for row:=1 to Limit do
                     begin
                        for col:=1 to (limit div 2) do
                          write(sq[row*2*col-1],sq[row*2*col],endl);
                        writeln(sq[row*limit]);
                     end
                end
        """
        expect = str(Program([FuncDecl(Id(r'writesquare'),[VarDecl(Id(r'sq'),FloatType()),VarDecl(Id(r'limit'),IntType())],[VarDecl(Id(r'row'),IntType()),VarDecl(Id(r'col'),IntType())],[For(Id(r'row'),IntLiteral(1),Id(r'Limit'),True,[For(Id(r'col'),IntLiteral(1),BinaryOp(r'div',Id(r'limit'),IntLiteral(2)),True,[CallStmt(Id(r'write'),[ArrayCell(Id(r'sq'),BinaryOp(r'-',BinaryOp(r'*',BinaryOp(r'*',Id(r'row'),IntLiteral(2)),Id(r'col')),IntLiteral(1))),ArrayCell(Id(r'sq'),BinaryOp(r'*',BinaryOp(r'*',Id(r'row'),IntLiteral(2)),Id(r'col'))),Id(r'endl')])]),CallStmt(Id(r'writeln'),[ArrayCell(Id(r'sq'),BinaryOp(r'*',Id(r'row'),Id(r'limit')))])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,330))

    def test_break(self):
        input = """procedure a(); begin for i:=2 to 400 do begin print(i+j," ");break; end end"""
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[For(Id(r'i'),IntLiteral(2),IntLiteral(400),True,[CallStmt(Id(r'print'),[BinaryOp(r'+',Id(r'i'),Id(r'j')),StringLiteral(r' ')]),Break()])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,331))

    def test_continue(self):
        input = """procedure a(); begin for i:=2 to 400 do begin print(i+j," ");continue; end end"""
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[For(Id(r'i'),IntLiteral(2),IntLiteral(400),True,[CallStmt(Id(r'print'),[BinaryOp(r'+',Id(r'i'),Id(r'j')),StringLiteral(r' ')]),Continue()])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,332))

    def test_return(self):
        input = """procedure a(); begin return 2; end"""
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[Return(IntLiteral(2))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,333))

    def test_return_in_function(self):
        input = """function a():integer; begin return; end"""
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[Return(None)],IntType())]))
        self.assertTrue(TestAST.test(input,expect,334))

    def test_nested_compound_statement(self):
        input = """function a():integer; begin begin begin begin end end begin end end end"""
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,335))

    def test_callstmt_and_callexpr(self):
        input = """
        procedure a();
        begin
            a();
            a:=a();
        end
        """
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[CallStmt(Id(r'a'),[]),Assign(Id(r'a'),CallExpr(Id(r'a'),[]))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,336))

    def test_with_statement(self):
        input = """function a():integer; begin with a:integer;b:real; do d:=3; end"""
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),FloatType())],[Assign(Id(r'd'),IntLiteral(3))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,337))

    def test_call_statement(self):
        input = """function a():integer; begin return 1; end"""
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[Return(IntLiteral(1))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,338))

    def test_build_in_function_getInt(self):
        input = """procedure a(); begin getInt();a:=getInt(); end"""
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[CallStmt(Id(r'getInt'),[]),Assign(Id(r'a'),CallExpr(Id(r'getInt'),[]))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,339))

    def test_built_in_procecdure_putInt(self):
        input = """procedure a(); begin putInt();a:=putInt(); end"""
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[CallStmt(Id(r'putInt'),[]),Assign(Id(r'a'),CallExpr(Id(r'putInt'),[]))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,340))

    def test_built_in_procecdure_putIntLn(self):
        input = """procedure a(); begin putIntLn();a:=putIntLn(); end"""
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[CallStmt(Id(r'putIntLn'),[]),Assign(Id(r'a'),CallExpr(Id(r'putIntLn'),[]))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,341))

    def test_built_in_function_getFloat(self):
        input = """procedure a(); begin getFloat();a:=getFloat(); end"""
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[CallStmt(Id(r'getFloat'),[]),Assign(Id(r'a'),CallExpr(Id(r'getFloat'),[]))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,342))

    def test_built_in_procecdure_putFloat(self):
        input = """procedure a(); begin putFloat();a:=putFloat(); end"""
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[CallStmt(Id(r'putFloat'),[]),Assign(Id(r'a'),CallExpr(Id(r'putFloat'),[]))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,343))

    def test_built_in_procecdure_putFloatLn(self):
        input = """procedure a(); begin putFloatLn();a:=putFloatLn(); end"""
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[CallStmt(Id(r'putFloatLn'),[]),Assign(Id(r'a'),CallExpr(Id(r'putFloatLn'),[]))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,344))

    def test_built_in_procecdure_putBool(self):
        input = """procedure a(); begin putBool();a:=putBool(); end"""
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[CallStmt(Id(r'putBool'),[]),Assign(Id(r'a'),CallExpr(Id(r'putBool'),[]))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,345))

    def test_built_in_procecdure_putBoolLn(self):
        input = """procedure a(); begin putBoolLn();a:=putBoolLn(); end"""
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[CallStmt(Id(r'putBoolLn'),[]),Assign(Id(r'a'),CallExpr(Id(r'putBoolLn'),[]))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,346))

    def test_built_in_procecdure_putString(self):
        input = """procedure a(); begin putString();a:=putString(); end"""
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[CallStmt(Id(r'putString'),[]),Assign(Id(r'a'),CallExpr(Id(r'putString'),[]))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,347))

    def test_built_in_procecdure_putStringLn(self):
        input = """procedure a(); begin putStringLn();a:=putStringLn(); end"""
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[CallStmt(Id(r'putStringLn'),[]),Assign(Id(r'a'),CallExpr(Id(r'putStringLn'),[]))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,348))

    def test_built_in_procecdure_putLn(self):
        input = """procedure a(); begin putLn();a:=putLn(); end"""
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[CallStmt(Id(r'putLn'),[]),Assign(Id(r'a'),CallExpr(Id(r'putLn'),[]))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,349))

    def test_add_op(self):
        input = """
                procedure bachkhoa();
                begin
                    x:=abc+4;
                end
                """
        expect = str(Program([FuncDecl(Id(r'bachkhoa'),[],[],[Assign(Id(r'x'),BinaryOp(r'+',Id(r'abc'),IntLiteral(4)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,350))

    def test_mix_program(self):
        input = """
        var a,b,c:integer;d,e:integer;
        procedure a();
        begin
            a();
            w:=w;
            begin
                d:=d;
                opw:=w();
                wqw:=d()[2];
                if a then if c then d();
            end
            w();
        end
        var c,w:real;d:string;q:array[-2 .. 2]of integer;
        """
        expect = str(Program([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType()),VarDecl(Id(r'd'),IntType()),VarDecl(Id(r'e'),IntType()),FuncDecl(Id(r'a'),[],[],[CallStmt(Id(r'a'),[]),Assign(Id(r'w'),Id(r'w')),Assign(Id(r'd'),Id(r'd')),Assign(Id(r'opw'),CallExpr(Id(r'w'),[])),Assign(Id(r'wqw'),ArrayCell(CallExpr(Id(r'd'),[]),IntLiteral(2))),If(Id(r'a'),[If(Id(r'c'),[CallStmt(Id(r'd'),[])],[])],[]),CallStmt(Id(r'w'),[])],VoidType()),VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'w'),FloatType()),VarDecl(Id(r'd'),StringType()),VarDecl(Id(r'q'),ArrayType(-2,2,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,351))

    def test_sub_op(self):
        input = """
                procedure bethoheo();
                begin
                    x:=a-2;
                end
                """
        expect = str(Program([FuncDecl(Id(r'bethoheo'),[],[],[Assign(Id(r'x'),BinaryOp(r'-',Id(r'a'),IntLiteral(2)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,352))

    def test_vardecl(self):
        input = """
        var a:integer;
        var b:real;
        var c:string;
        var d:boolean;
        """
        expect = str(Program([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),StringType()),VarDecl(Id(r'd'),BoolType())]))
        self.assertTrue(TestAST.test(input,expect,353))

    def test_mul_op(self):
        input = """
                procedure kimcute();
                begin
                    x:=a*2;
                end
                """
        expect = str(Program([FuncDecl(Id(r'kimcute'),[],[],[Assign(Id(r'x'),BinaryOp(r'*',Id(r'a'),IntLiteral(2)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,354))

    def test_multivar(self):
        input = """
        var a,b,c:integer;d,e:integer;
        var f,g:boolean;h,j:integer;
        var q,w:string;
        """
        expect = str(Program([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType()),VarDecl(Id(r'd'),IntType()),VarDecl(Id(r'e'),IntType()),VarDecl(Id(r'f'),BoolType()),VarDecl(Id(r'g'),BoolType()),VarDecl(Id(r'h'),IntType()),VarDecl(Id(r'j'),IntType()),VarDecl(Id(r'q'),StringType()),VarDecl(Id(r'w'),StringType())]))
        self.assertTrue(TestAST.test(input,expect,355))

    def test_div_op(self):
        input = """
                procedure tscute();
                begin
                    x:=a/4/6;
                end
                """
        expect = str(Program([FuncDecl(Id(r'tscute'),[],[],[Assign(Id(r'x'),BinaryOp(r'/',BinaryOp(r'/',Id(r'a'),IntLiteral(4)),IntLiteral(6)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,356))

    def test_array_type(self):
        input = """
        var a:array[1 .. 2]of integer;
        var a:array[-1 .. 2]of integer;
        var a:array[1 .. -2]of integer;
        var a:array[-1 .. -2]of integer;
        """
        expect = str(Program([VarDecl(Id(r'a'),ArrayType(1,2,IntType())),VarDecl(Id(r'a'),ArrayType(-1,2,IntType())),VarDecl(Id(r'a'),ArrayType(1,-2,IntType())),VarDecl(Id(r'a'),ArrayType(-1,-2,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,357))

    def test_intdiv_op(self):
        input = """
                procedure linhcute();
                begin
                    x:=a div b ;
                end
                """
        expect = str(Program([FuncDecl(Id(r'linhcute'),[],[],[Assign(Id(r'x'),BinaryOp(r'div',Id(r'a'),Id(r'b')))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,358))

    def test_mixop_complicate(self):
        input = """
        procedure a();
        begin
            a:=a+b-2/d*2 and 2 =243516534 div 211 mod 9 or 2;
        end
        """
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[Assign(Id(r'a'),BinaryOp(r'=',BinaryOp(r'-',BinaryOp(r'+',Id(r'a'),Id(r'b')),BinaryOp(r'and',BinaryOp(r'*',BinaryOp(r'/',IntLiteral(2),Id(r'd')),IntLiteral(2)),IntLiteral(2))),BinaryOp(r'or',BinaryOp(r'mod',BinaryOp(r'div',IntLiteral(243516534),IntLiteral(211)),IntLiteral(9)),IntLiteral(2))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,359))

    def test_not_op(self):
        input = """
                procedure mat();
                begin
                    x:=not b ;
                end"""
        expect = str(Program([FuncDecl(Id(r'mat'),[],[],[Assign(Id(r'x'),UnaryOp(r'not',Id(r'b')))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,360))

    def test_double_not_op(self):
        input = """
        procedure a();
        begin
            x:=not not b;
        end
        """
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[Assign(Id(r'x'),UnaryOp(r'not',UnaryOp(r'not',Id(r'b'))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,361))

    def test_mod_op(self):
        input = """
                procedure daulong();
                begin
                    x:=b mod 2;
                end
                """
        expect = str(Program([FuncDecl(Id(r'daulong'),[],[],[Assign(Id(r'x'),BinaryOp(r'mod',Id(r'b'),IntLiteral(2)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,362))

    def test_triple_not(self):
        input = """
        procedure a();
        begin
            a:=not not not a;
        end
        """
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[Assign(Id(r'a'),UnaryOp(r'not',UnaryOp(r'not',UnaryOp(r'not',Id(r'a')))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,363))

    def test_or_op(self):
        input = """
                procedure radio();
                begin
                    x:= 3 or 2;
                end
                """
        expect = str(Program([FuncDecl(Id(r'radio'),[],[],[Assign(Id(r'x'),BinaryOp(r'or',IntLiteral(3),IntLiteral(2)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,364))

    def test_or_assoc(self):
        input = """
        procedure a();
        begin
            if d or d() or d[d()] then d();
        end
        """
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[If(BinaryOp(r'or',BinaryOp(r'or',Id(r'd'),CallExpr(Id(r'd'),[])),ArrayCell(Id(r'd'),CallExpr(Id(r'd'),[]))),[CallStmt(Id(r'd'),[])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,365))

    def test_and_op(self):
        input = """
                procedure thatbat();
                begin
                    x:= a and b;
                end
                """
        expect = str(Program([FuncDecl(Id(r'thatbat'),[],[],[Assign(Id(r'x'),BinaryOp(r'and',Id(r'a'),Id(r'b')))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,366))

    def test_multi_not(self):
        input = """
        procedure a();
        begin
            x:=a + not not not not not not not a;
        end
        """
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[Assign(Id(r'x'),BinaryOp(r'+',Id(r'a'),UnaryOp(r'not',UnaryOp(r'not',UnaryOp(r'not',UnaryOp(r'not',UnaryOp(r'not',UnaryOp(r'not',UnaryOp(r'not',Id(r'a'))))))))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,367))

    def test_less_op(self):
        input = """
                procedure hgjd();
                begin
                    x:= a < b;
                end
                """
        expect = str(Program([FuncDecl(Id(r'hgjd'),[],[],[Assign(Id(r'x'),BinaryOp(r'<',Id(r'a'),Id(r'b')))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,368))

    def test_another_if(self):
        input = """
        procedure a();
        begin
            if a=2 then
                if a=2 then c:=7;
                else w:=3;
        end

        """
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[If(BinaryOp(r'=',Id(r'a'),IntLiteral(2)),[If(BinaryOp(r'=',Id(r'a'),IntLiteral(2)),[Assign(Id(r'c'),IntLiteral(7))],[Assign(Id(r'w'),IntLiteral(3))])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,369))

    def test_greater_op(self):
        input = """
                procedure abx();
                begin
                    a:=2;
                    b:=4;
                    x:= w > b;
                end
                """
        expect = str(Program([FuncDecl(Id(r'abx'),[],[],[Assign(Id(r'a'),IntLiteral(2)),Assign(Id(r'b'),IntLiteral(4)),Assign(Id(r'x'),BinaryOp(r'>',Id(r'w'),Id(r'b')))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,370))

    def test_float_literal(self):
        input = """
        procedure a();
        begin
            a:=2.3;
            b:=4.5E2;
            c1:=-3.2e-2;
            c2:=-3.2E-5;
            c3:= 3.2e-5;
            c4:= 3.2e-2;
            d:=.2E3;
            e:=2.;
            f:=2.E2;
            g:=-.9;
            pi:=3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989;
        end
        """
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[Assign(Id(r'a'),FloatLiteral(2.3)),Assign(Id(r'b'),FloatLiteral(450.0)),Assign(Id(r'c1'),UnaryOp(r'-',FloatLiteral(0.032))),Assign(Id(r'c2'),UnaryOp(r'-',FloatLiteral(3.2e-05))),Assign(Id(r'c3'),FloatLiteral(3.2e-05)),Assign(Id(r'c4'),FloatLiteral(0.032)),Assign(Id(r'd'),FloatLiteral(200.0)),Assign(Id(r'e'),FloatLiteral(2.0)),Assign(Id(r'f'),FloatLiteral(200.0)),Assign(Id(r'g'),UnaryOp(r'-',FloatLiteral(0.9))),Assign(Id(r'pi'),FloatLiteral(3.141592653589793))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,371))

    def test_notEqual_op(self):
        input = """
                procedure hahaha();
                begin
                    a:=b;
                    b:=b<2;
                    x:= a <> b;
                end
                """
        expect = str(Program([FuncDecl(Id(r'hahaha'),[],[],[Assign(Id(r'a'),Id(r'b')),Assign(Id(r'b'),BinaryOp(r'<',Id(r'b'),IntLiteral(2))),Assign(Id(r'x'),BinaryOp(r'<>',Id(r'a'),Id(r'b')))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,372))

    def test_notEqual_op_error(self):
        input = """
        procedure a();
        begin
            a:=f<>r and then b;
        end
        """
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[Assign(Id(r'a'),BinaryOp(r'andthen',BinaryOp(r'<>',Id(r'f'),Id(r'r')),Id(r'b')))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,373))

    def test_equal_op(self):
        input = """
                procedure main();
                begin
                    a:=9=b;
                    b:=b=2;
                    x:= a = 2 + b;
                end 
                """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'a'),BinaryOp(r'=',IntLiteral(9),Id(r'b'))),Assign(Id(r'b'),BinaryOp(r'=',Id(r'b'),IntLiteral(2))),Assign(Id(r'x'),BinaryOp(r'=',Id(r'a'),BinaryOp(r'+',IntLiteral(2),Id(r'b'))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,374))

    def test_complex_program(self):
        input = """
        VAR First,  Second, Left, Right: BOOLEAN;
        PROCEDURE  printBo2ol(Val: BOOLEAN);
        BEGIN
        IF Val THEN
        print("TRUE ");
        ELSE
        print("FALSE ");
        END { printBool  }
        PROCEDURE Main();
        BEGIN
        { print Header }
        print("Proof  of DeMorgan theorem ");
        print();
        print("First  Second Left Right ");
        print("-----  ------ ----- ----- ");
        { Loop through  all truth value combinations }
        FOR f :=  FALSE TO TRUE DO
        FOR g :=  FALSE TO TRUE DO BEGIN
        { print out  Input values of First, Second }
        printBool(2);
        printBool(e);
        { Separate Input  values from the output }
        print(" ");
        d := (NOT  e) div (NOT 2);
        w := NOT(e mod 2);
        { print out the  new values of Left, Right }
        printBool(2);
        printBool(e);
        print();
        END { Inner FOR  }
        END { TruthTable2  }
        """
        expect = str(Program([VarDecl(Id(r'First'),BoolType()),VarDecl(Id(r'Second'),BoolType()),VarDecl(Id(r'Left'),BoolType()),VarDecl(Id(r'Right'),BoolType()),FuncDecl(Id(r'printBo2ol'),[VarDecl(Id(r'Val'),BoolType())],[],[If(Id(r'Val'),[CallStmt(Id(r'print'),[StringLiteral(r'TRUE ')])],[CallStmt(Id(r'print'),[StringLiteral(r'FALSE ')])])],VoidType()),FuncDecl(Id(r'Main'),[],[],[CallStmt(Id(r'print'),[StringLiteral(r'Proof  of DeMorgan theorem ')]),CallStmt(Id(r'print'),[]),CallStmt(Id(r'print'),[StringLiteral(r'First  Second Left Right ')]),CallStmt(Id(r'print'),[StringLiteral(r'-----  ------ ----- ----- ')]),For(Id(r'f'),BooleanLiteral(False),BooleanLiteral(True),True,[For(Id(r'g'),BooleanLiteral(False),BooleanLiteral(True),True,[CallStmt(Id(r'printBool'),[IntLiteral(2)]),CallStmt(Id(r'printBool'),[Id(r'e')]),CallStmt(Id(r'print'),[StringLiteral(r' ')]),Assign(Id(r'd'),BinaryOp(r'div',UnaryOp(r'NOT',Id(r'e')),UnaryOp(r'NOT',IntLiteral(2)))),Assign(Id(r'w'),UnaryOp(r'NOT',BinaryOp(r'mod',Id(r'e'),IntLiteral(2)))),CallStmt(Id(r'printBool'),[IntLiteral(2)]),CallStmt(Id(r'printBool'),[Id(r'e')]),CallStmt(Id(r'print'),[])])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,375))

    def test_lessOrEqual_op(self):
        input = """
                procedure chas();
                begin
                    a:=4 +  b;
                    b:=b=2;
                    x:= n<=b;
                end 
                """
        expect = str(Program([FuncDecl(Id(r'chas'),[],[],[Assign(Id(r'a'),BinaryOp(r'+',IntLiteral(4),Id(r'b'))),Assign(Id(r'b'),BinaryOp(r'=',Id(r'b'),IntLiteral(2))),Assign(Id(r'x'),BinaryOp(r'<=',Id(r'n'),Id(r'b')))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,376))

    def test_lessOrEqual_op_error(self):
        input = """
        procedure foo(a, b: integer ; c: real) ;
            BEGIN
                with a , b : integer ; c : array [1 .. 2] of real ; do
                d := c [a] + b ;
            END
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),FloatType())],[],[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),ArrayType(1,2,FloatType()))],[Assign(Id(r'd'),BinaryOp(r'+',ArrayCell(Id(r'c'),Id(r'a')),Id(r'b')))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,377))

    def test_greaterOrEqual_op(self):
        input = """
                procedure sua();
                begin
                    a:=man;
                    b:=women;
                    x:= a >= b ;
                end
                """
        expect = str(Program([FuncDecl(Id(r'sua'),[],[],[Assign(Id(r'a'),Id(r'man')),Assign(Id(r'b'),Id(r'women')),Assign(Id(r'x'),BinaryOp(r'>=',Id(r'a'),Id(r'b')))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,378))

    def test_greaterOrEqual_op_error(self):
        input = """
        function foo(n: integer; m:integer): integer;
        begin
            for i:=1 downto n do
                for j := i to n -1 do
                begin
                    s := s + 1;
                    if(i = (m+n)/2) then s:=s-1;
                end
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'n'),IntType()),VarDecl(Id(r'm'),IntType())],[],[For(Id(r'i'),IntLiteral(1),Id(r'n'),False,[For(Id(r'j'),Id(r'i'),BinaryOp(r'-',Id(r'n'),IntLiteral(1)),True,[Assign(Id(r's'),BinaryOp(r'+',Id(r's'),IntLiteral(1))),If(BinaryOp(r'=',Id(r'i'),BinaryOp(r'/',BinaryOp(r'+',Id(r'm'),Id(r'n')),IntLiteral(2))),[Assign(Id(r's'),BinaryOp(r'-',Id(r's'),IntLiteral(1)))],[])])])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,379))

    def test_assign_op(self):
        input = """
                procedure sah();
                begin
                    a:=1;
                    b:=2;
                    x:=a+b ;
                end
                """
        expect = str(Program([FuncDecl(Id(r'sah'),[],[],[Assign(Id(r'a'),IntLiteral(1)),Assign(Id(r'b'),IntLiteral(2)),Assign(Id(r'x'),BinaryOp(r'+',Id(r'a'),Id(r'b')))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,380))

    def test_assign_op_complex(self):
        input = """
        procedure a();
        begin
            a:=d:=e:=w()[2]:=d[1+d()]:=u(u[3]);
        end
        """
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[Assign(ArrayCell(Id(r'd'),BinaryOp(r'+',IntLiteral(1),CallExpr(Id(r'd'),[]))),CallExpr(Id(r'u'),[ArrayCell(Id(r'u'),IntLiteral(3))])),Assign(ArrayCell(CallExpr(Id(r'w'),[]),IntLiteral(2)),ArrayCell(Id(r'd'),BinaryOp(r'+',IntLiteral(1),CallExpr(Id(r'd'),[])))),Assign(Id(r'e'),ArrayCell(CallExpr(Id(r'w'),[]),IntLiteral(2))),Assign(Id(r'd'),Id(r'e')),Assign(Id(r'a'),Id(r'd'))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,381))

    def test_index_op(self):
        input = """
                procedure suag();
                begin
                    a:=1;
                    b:=2;
                    foo(2)[3+x] := a[b[2]] +3;
                end
                """
        expect = str(Program([FuncDecl(Id(r'suag'),[],[],[Assign(Id(r'a'),IntLiteral(1)),Assign(Id(r'b'),IntLiteral(2)),Assign(ArrayCell(CallExpr(Id(r'foo'),[IntLiteral(2)]),BinaryOp(r'+',IntLiteral(3),Id(r'x'))),BinaryOp(r'+',ArrayCell(Id(r'a'),ArrayCell(Id(r'b'),IntLiteral(2))),IntLiteral(3)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,382))

    def test_index_op_compicate(self):
        input = """
                procedure a();
        begin
            a[1[2[t]]]:=abbb(w34[2[5]])[wete[0]];
        end

        """
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[Assign(ArrayCell(Id(r'a'),ArrayCell(IntLiteral(1),ArrayCell(IntLiteral(2),Id(r't')))),ArrayCell(CallExpr(Id(r'abbb'),[ArrayCell(Id(r'w34'),ArrayCell(IntLiteral(2),IntLiteral(5)))]),ArrayCell(Id(r'wete'),IntLiteral(0))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,383))

    def test_index_op_complex(self):
        input = """
                procedure a();
        begin
            jkha(w[22]+d[2]+d)[d23t1[2[t]]]:=thk(f[f+w()[f]])[2[sk+g()]];
        end
        """
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[Assign(ArrayCell(CallExpr(Id(r'jkha'),[BinaryOp(r'+',BinaryOp(r'+',ArrayCell(Id(r'w'),IntLiteral(22)),ArrayCell(Id(r'd'),IntLiteral(2))),Id(r'd'))]),ArrayCell(Id(r'd23t1'),ArrayCell(IntLiteral(2),Id(r't')))),ArrayCell(CallExpr(Id(r'thk'),[ArrayCell(Id(r'f'),BinaryOp(r'+',Id(r'f'),ArrayCell(CallExpr(Id(r'w'),[]),Id(r'f'))))]),ArrayCell(IntLiteral(2),BinaryOp(r'+',Id(r'sk'),CallExpr(Id(r'g'),[])))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,384))

    def test_bracket(self):
        input = """
                procedure uux();
                begin
                    m:=m+(3-4)*2;
                end
                """
        expect = str(Program([FuncDecl(Id(r'uux'),[],[],[Assign(Id(r'm'),BinaryOp(r'+',Id(r'm'),BinaryOp(r'*',BinaryOp(r'-',IntLiteral(3),IntLiteral(4)),IntLiteral(2))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,385))

    def test_bracket_complicate(self):
        input = """
        procedure a();
        begin
            a:=b()+8+2*(e+3)+2/(2 and 2);
        end
        """
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[Assign(Id(r'a'),BinaryOp(r'+',BinaryOp(r'+',BinaryOp(r'+',CallExpr(Id(r'b'),[]),IntLiteral(8)),BinaryOp(r'*',IntLiteral(2),BinaryOp(r'+',Id(r'e'),IntLiteral(3)))),BinaryOp(r'/',IntLiteral(2),BinaryOp(r'and',IntLiteral(2),IntLiteral(2)))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,386))

    def test_bracket_complex(self):
        input = """
                procedure a();
        begin
            if i()-4+5 and 3 and then 2 or else 4<2 mod 6 then a:=true;
        end
        """
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[If(BinaryOp(r'orelse',BinaryOp(r'andthen',BinaryOp(r'+',BinaryOp(r'-',CallExpr(Id(r'i'),[]),IntLiteral(4)),BinaryOp(r'and',IntLiteral(5),IntLiteral(3))),IntLiteral(2)),BinaryOp(r'<',IntLiteral(4),BinaryOp(r'mod',IntLiteral(2),IntLiteral(6)))),[Assign(Id(r'a'),BooleanLiteral(True))],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,387))

    def test_mixOp1(self):
        input = """
                procedure urffss();
                begin
                    w:=(5+6*(8-32)<5) and (23>=432);
                    d:= (2=3) and (7*5 or 0);
                end
                """
        expect = str(Program([FuncDecl(Id(r'urffss'),[],[],[Assign(Id(r'w'),BinaryOp(r'and',BinaryOp(r'<',BinaryOp(r'+',IntLiteral(5),BinaryOp(r'*',IntLiteral(6),BinaryOp(r'-',IntLiteral(8),IntLiteral(32)))),IntLiteral(5)),BinaryOp(r'>=',IntLiteral(23),IntLiteral(432)))),Assign(Id(r'd'),BinaryOp(r'and',BinaryOp(r'=',IntLiteral(2),IntLiteral(3)),BinaryOp(r'or',BinaryOp(r'*',IntLiteral(7),IntLiteral(5)),IntLiteral(0))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,388))

    def test_mixOp2(self):
        input = """
                procedure yrc();
                begin
                    foo(a+94<5)[x>=6]:= 9 div 4 + 3 mod 2;
                end
                """
        expect = str(Program([FuncDecl(Id(r'yrc'),[],[],[Assign(ArrayCell(CallExpr(Id(r'foo'),[BinaryOp(r'<',BinaryOp(r'+',Id(r'a'),IntLiteral(94)),IntLiteral(5))]),BinaryOp(r'>=',Id(r'x'),IntLiteral(6))),BinaryOp(r'+',BinaryOp(r'div',IntLiteral(9),IntLiteral(4)),BinaryOp(r'mod',IntLiteral(3),IntLiteral(2))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,389))

    def test_mixOp3(self):
        input = """
                procedure cub();
                begin
                    p:=(a+b+c)/2;
                    d:=p+3;
                    a:= 1<d;
                end
                """
        expect = str(Program([FuncDecl(Id(r'cub'),[],[],[Assign(Id(r'p'),BinaryOp(r'/',BinaryOp(r'+',BinaryOp(r'+',Id(r'a'),Id(r'b')),Id(r'c')),IntLiteral(2))),Assign(Id(r'd'),BinaryOp(r'+',Id(r'p'),IntLiteral(3))),Assign(Id(r'a'),BinaryOp(r'<',IntLiteral(1),Id(r'd')))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,390))

    def test_mixOp4(self):
        input = """
                procedure tum();
                begin
                    h:= a and b or c + not b;
                end
                """
        expect = str(Program([FuncDecl(Id(r'tum'),[],[],[Assign(Id(r'h'),BinaryOp(r'+',BinaryOp(r'or',BinaryOp(r'and',Id(r'a'),Id(r'b')),Id(r'c')),UnaryOp(r'not',Id(r'b'))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,391))

    def test_mixOp5(self):
        input = """
                procedure nancy();
                begin
                    d:= not a and not b or not c +33*(93<3);
                end
                """
        expect = str(Program([FuncDecl(Id(r'nancy'),[],[],[Assign(Id(r'd'),BinaryOp(r'+',BinaryOp(r'or',BinaryOp(r'and',UnaryOp(r'not',Id(r'a')),UnaryOp(r'not',Id(r'b'))),UnaryOp(r'not',Id(r'c'))),BinaryOp(r'*',IntLiteral(33),BinaryOp(r'<',IntLiteral(93),IntLiteral(3)))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,392))

    def test_some_function(self):
        input = """
        function IsUnwantedComponent( AClassName: string;AComponentSkipList: string): Boolean;
        var
          I: Integer;
        begin
          Result := False;
          if Assigned(AComponentSkipList) then
            for I := 0 to AComponentSkipListCount - 1 do
              if SameText(AClassName, AComponentSkipList[I]) then
              begin
                Result := True;
                Break;
              end
        end
        """
        expect = str(Program([FuncDecl(Id(r'IsUnwantedComponent'),[VarDecl(Id(r'AClassName'),StringType()),VarDecl(Id(r'AComponentSkipList'),StringType())],[VarDecl(Id(r'I'),IntType())],[Assign(Id(r'Result'),BooleanLiteral(False)),If(CallExpr(Id(r'Assigned'),[Id(r'AComponentSkipList')]),[For(Id(r'I'),IntLiteral(0),BinaryOp(r'-',Id(r'AComponentSkipListCount'),IntLiteral(1)),True,[If(CallExpr(Id(r'SameText'),[Id(r'AClassName'),ArrayCell(Id(r'AComponentSkipList'),Id(r'I'))]),[Assign(Id(r'Result'),BooleanLiteral(True)),Break()],[])])],[])],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,393))

    def test_xi_dau(self):
        input = """procedure xidau();begin chan_xi_dau(); end"""
        expect = str(Program([FuncDecl(Id(r'xidau'),[],[],[CallStmt(Id(r'chan_xi_dau'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,394))

    def test_mixOp_assoc(self):
        input = """
                procedure bee();
                begin
                    x:= 3*x-4*a +(2-5)*8 and true;
                end
                """
        expect = str(Program([FuncDecl(Id(r'bee'),[],[],[Assign(Id(r'x'),BinaryOp(r'+',BinaryOp(r'-',BinaryOp(r'*',IntLiteral(3),Id(r'x')),BinaryOp(r'*',IntLiteral(4),Id(r'a'))),BinaryOp(r'and',BinaryOp(r'*',BinaryOp(r'-',IntLiteral(2),IntLiteral(5)),IntLiteral(8)),BooleanLiteral(True))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,395))

    def test_gau_gau_gau(self):
        input = """
        procedure dog();
        var gau:integer;
        begin
            gau:=gaugaugau()+gaugau();
        end
        """
        expect = str(Program([FuncDecl(Id(r'dog'),[],[VarDecl(Id(r'gau'),IntType())],[Assign(Id(r'gau'),BinaryOp(r'+',CallExpr(Id(r'gaugaugau'),[]),CallExpr(Id(r'gaugau'),[])))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,396))

    def test_meo_meo_meo(self):
        input = """
        procedure meo();
        var trymrsugasvatdwad:integer;
        begin
            minhbatchuocloaimeokeunha("meomeomeo");
            if argv[1]="gaugaugau" then print("Keu sai roi, keu meo meo meo di");
            else print("gioi qua gioi qua");
        end
        """
        expect = str(Program([FuncDecl(Id(r'meo'),[],[VarDecl(Id(r'trymrsugasvatdwad'),IntType())],[CallStmt(Id(r'minhbatchuocloaimeokeunha'),[StringLiteral(r'meomeomeo')]),If(BinaryOp(r'=',ArrayCell(Id(r'argv'),IntLiteral(1)),StringLiteral(r'gaugaugau')),[CallStmt(Id(r'print'),[StringLiteral(r'Keu sai roi, keu meo meo meo di')])],[CallStmt(Id(r'print'),[StringLiteral(r'gioi qua gioi qua')])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,397))

    def test_literal(self):
        input = """
                procedure viva();
                begin
                    n:= 12*e10*4+4E-13;
                end
                """
        expect = str(Program([FuncDecl(Id(r'viva'),[],[],[Assign(Id(r'n'),BinaryOp(r'+',BinaryOp(r'*',BinaryOp(r'*',IntLiteral(12),Id(r'e10')),IntLiteral(4)),FloatLiteral(4e-13)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,398))

    def test_literal_error(self):
        input = """
        procedure a(realvar:real);
        var skufe:integer;
        begin
            a:=5+a(1,2,3);
        end
        """
        expect = str(Program([FuncDecl(Id(r'a'),[VarDecl(Id(r'realvar'),FloatType())],[VarDecl(Id(r'skufe'),IntType())],[Assign(Id(r'a'),BinaryOp(r'+',IntLiteral(5),CallExpr(Id(r'a'),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,399))