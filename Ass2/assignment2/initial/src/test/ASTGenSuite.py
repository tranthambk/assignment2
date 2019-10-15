# 1713712
import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    
    def test_var_declare_No1(self):
        """Test variable declaration"""
        input = """
            int a,b[5];
        """
        expect = str(
            Program(
            [
                VarDecl('a',IntType()),
                VarDecl('b',ArrayType(5,IntType()))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    def test_var_declare_No2(self):
        """Test variable declaration"""
        input = """
            float b[5];
        """
        expect = str(
            Program(
            [
                VarDecl('b',ArrayType(5,FloatType()))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    
    def test_var_declare_No3(self):
        """Test variable declaration"""
        input = """
            string a,b,c,foo[5];
        """
        expect = str(
            Program(
            [
                VarDecl('a',StringType()),
                VarDecl('b',StringType()),
                VarDecl('c',StringType()),
                VarDecl('foo',ArrayType(5,StringType()))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
    
    def test_func_declare_No4(self):
        """Test function declaration"""
        input = """
            float[] foo(){}
        """
        expect = str(
            Program(
            [
                FuncDecl(Id('foo'),
                [],
                ArrayPointerType(FloatType()),
                Block([]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_func_declare_No5(self):
        """Test function declaration"""
        input = """
            int foo1(){}
        """
        expect = str(
            Program(
            [
                FuncDecl(Id('foo1'),
                [],
                IntType(),
                Block(
                    []
                    ))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_func_declare_No6(self):
        """Test function declaration"""
        input = """
            int foo(int a,float b){}
        """
        expect = str(
            Program(
            [
                FuncDecl(Id('foo'),
                [
                    VarDecl('a',IntType()),
                    VarDecl('b',FloatType())
                ],
                IntType(),
                Block(
                    []
                ))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,306))
    
    def test_func_declare_No7(self):
        """Test function declaration"""
        input = """
            int foo(int a,float b[]){}
        """
        expect = str(
            Program(
            [
                FuncDecl(
                    Id('foo'),
                    [
                        VarDecl('a',IntType()),
                        VarDecl('b',ArrayPointerType(FloatType()))
                    ],
                    IntType(),
                    Block([])
                )
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
    
    def test_func_declare_No8(self):
        """Test function declaration"""
        input = """
            string foo(boolean a[],int b[]){}
        """
        expect = str(
            Program(
            [
                FuncDecl(Id('foo'),
                [
                    VarDecl('a',ArrayPointerType(BoolType())),
                    VarDecl('b',ArrayPointerType(IntType()))
                ],
                StringType(),
                Block([]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
    
    def test_func_declare_No9(self):
        """Test function declaration"""
        input = """
            boolean[] foo(boolean a,int b[]){}
        """
        expect = str(
            Program(
            [
                FuncDecl(Id('foo'),
                [
                    VarDecl('a',BoolType()),
                    VarDecl('b',ArrayPointerType(IntType()))
                ], 
                ArrayPointerType(BoolType()),
                Block([]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_func_declare_No10(self):
        """Test function declaration"""
        input = """
           void foo(float a[],string b){}
        """
        expect = str(
            Program([
                FuncDecl(Id('foo'),
                [
                    VarDecl('a',ArrayPointerType(FloatType())),
                    VarDecl('b',StringType())
                ],
                VoidType(),
                Block([]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_var_declare_and_func_declare_No11(self):
        """Test function declaration"""
        input = """
           int a;
           float b;
           string c;
           boolean foo(){}
           string foo1(){}
           int foo2(int a[], float b){}
        """
        expect = str(
            Program(
            [
                VarDecl('a',IntType()),
                VarDecl('b',FloatType()),
                VarDecl('c',StringType()),
                FuncDecl(Id('foo'),
                    [],
                    BoolType(),
                    Block([])),
                FuncDecl(Id('foo1'),
                    [],
                    StringType(),
                    Block([])),
                FuncDecl(Id('foo2'),
                    [
                        VarDecl('a',ArrayPointerType(IntType())),
                        VarDecl('b',FloatType())
                    ],
                    IntType(),
                    Block([]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_Block_No12(self):
        """Test block declaration"""
        input = """
            int foo(){int a;}
        """
        expect = str(
            Program(
            [
                FuncDecl(Id('foo'),
                [],
                IntType(),
                Block(
                [
                    VarDecl('a',IntType())
                ]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,312))
    
    def test_Block_No13(self):
        """Test block declaration"""
        input = """
            int[] foo(int a[]){
                boolean a[5],b; 
                float c;
            }
        """
        expect = str(
            Program(
            [
                FuncDecl(Id('foo'),
                    [
                        VarDecl('a',ArrayPointerType(IntType()))
                    ],
                    ArrayPointerType(IntType()),
                    Block(
                        [
                            VarDecl('a',ArrayType(5,BoolType())),
                            VarDecl('b',BoolType()),
                            VarDecl('c',FloatType())
                        ]
                    )
                )
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_Block_No14(self):
        """Test block declaration"""
        input = """
            float foo(int a[], float b){
                string a,b,c;
                float cbp[4];
                boolean a;
                }
        """
        expect = str(
            Program(
            [
                FuncDecl(Id('foo'),
                [
                    VarDecl('a',ArrayPointerType(IntType())),
                    VarDecl('b',FloatType())
                ],
                FloatType(),
                Block(
                [
                    VarDecl('a',StringType()),
                    VarDecl('b',StringType()),
                    VarDecl('c',StringType()),
                    VarDecl('cbp',ArrayType(4,FloatType())),
                    VarDecl('a',BoolType())
                ]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,314))
    
    def test_If_stml_No15(self):
        """Test if statement"""
        input = """
            int foo(){
                if (a || b) a && 3; else -b + 3;
            }
        """
        expect = str(
            Program(
            [
                FuncDecl(Id('foo'),
                [],
                IntType(),
                Block(
                [
                    If(
                        BinaryOp('||',Id('a'),Id('b')),
                        BinaryOp('&&',Id('a'),IntLiteral(3)),
                        BinaryOp('+',UnaryOp('-',Id('b')),IntLiteral(3))
                    )
                ]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,315))
    
    def test_If_stml_No16(self):
        """Test if statement"""
        input = """
            int foo(){
                if (a || b) a = 4;
            }
        """
        expect = str(Program(
            [
                FuncDecl(Id('foo'),[],IntType(),Block(
                    [
                        If(
                            BinaryOp('||',Id('a'),Id('b')),
                            BinaryOp('=',Id('a'),IntLiteral(4))
                        )
                    ]))
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_If_stml_No17(self):
        """Test if statement"""
        input = """
            int foo(){
                if (b>a)
                    if (b>c)
                        {
                            max = b;
                        }
                else 
                    max = b;           
            }
        """
        expect = str(
            Program(
            [
                FuncDecl(Id('foo'),
                [],
                IntType(),
                Block(
                [
                    If(
                        BinaryOp('>',Id('b'),Id('a')),
                        If(
                            BinaryOp('>',Id('b'),Id('c')),
                            Block(
                            [
                                BinaryOp('=',Id('max'),Id('b'))
                            ]),
                            BinaryOp('=',Id('max'),Id('b'))
                        )
                    )
                ]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,317))
    
    def test_If_stml_No18(self):
        """Test if statement"""
        input = """
            int foo(){
                if (b>a)
                {
                    x = y + 1;
                    y = 5 + 1;
                }           
                else 
                {
                    x = y * 2;
                    y = 6 * 3;
                }
            }
        """
        expect = str(
            Program(
            [
                FuncDecl(Id('foo'),
                [],
                IntType(),
                Block(
                [
                    If(
                        BinaryOp('>',Id('b'),Id('a')),
                        Block(
                        [
                            BinaryOp('=',Id('x'),BinaryOp('+',Id('y'),IntLiteral(1))),
                            BinaryOp('=',Id('y'),BinaryOp('+',IntLiteral(5),IntLiteral(1)))
                        ]),
                        Block(
                        [
                            BinaryOp('=',Id('x'),BinaryOp('*',Id('y'),IntLiteral(2))),
                            BinaryOp('=',Id('y'),BinaryOp('*',IntLiteral(6),IntLiteral(3)))
                        ])
                    )
                ]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,318))
    
    def test_If_stml_No19(self):
        """Test if statement"""
        input = """
            int foo(){
                if (a == b)
                    max >= 6;
                else 
                {
                    x = 4;
                    {
                        int a;
                        a = 6;
                    }
                }
            }
        """
        expect = str(
            Program(
            [
                FuncDecl(Id('foo'),
                    [],
                    IntType(),
                    Block(
                    [
                        If(
                            BinaryOp('==',Id('a'),Id('b')),
                            BinaryOp('>=',Id('max'),IntLiteral(6)),
                            Block(
                            [
                                BinaryOp('=',Id('x'),IntLiteral(4)),
                                Block(
                                [
                                    VarDecl('a',IntType()),
                                    BinaryOp('=',Id('a'),IntLiteral(6))
                                ])
                            ])
                        )
                    ])
                )
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_For_Stml_No20(self):
        """Test for statement"""
        input = """
            int foo(){
                for(i=1;i<10;i=i+1)
                    a=0;
            }
        """
        expect = str(
            Program(
            [
                FuncDecl(Id('foo'),
                [],
                IntType(),
                Block(
                [
                    For(
                        BinaryOp('=',Id('i'),IntLiteral(1)),
                        BinaryOp('<',Id('i'),IntLiteral(10)),
                        BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
                        BinaryOp('=',Id('a'),IntLiteral(0))
                    )
                ]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,320))
    
    def test_For_Stml_No21(self):
        """Test for statement"""
        input = """
            int foo(){
                for(i=1;i<10;i=i+1)
                {
                    int a;
                    a = a+1;
                }
            }
        """
        expect = str(
            Program(
            [
                FuncDecl(Id('foo'),
                [],
                IntType(),
                Block(
                [
                    For(
                        BinaryOp('=',Id('i'),IntLiteral(1)),
                        BinaryOp('<',Id('i'),IntLiteral(10)),
                        BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
                        Block(
                        [
                            VarDecl('a',IntType()),
                            BinaryOp('=',Id('a'),BinaryOp('+',Id('a'),IntLiteral(1)))
                        ])
                    )
                ]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,321))
    
    def test_For_Stml_No22(self):
        """Test for statement"""
        input = """
            int foo(){
                for(i=1;i<10;i=i+1)
                {
                    if (a = 4)
                        i = i+1;
                }
            }
        """
        expect = str(
            Program(
            [
                FuncDecl(Id('foo'),
                [],
                IntType(),
                Block(
                [
                    For(
                        BinaryOp('=',Id('i'),IntLiteral(1)),
                        BinaryOp('<',Id('i'),IntLiteral(10)),
                        BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
                        Block(
                        [
                            If(
                                BinaryOp('=',Id('a'),IntLiteral(4)),
                                BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1)))
                            )
                        ])
                    )
                ]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_For_Stml_No23(self):
        """Test for statement"""
        input = """
            int foo(){
                if (a>3)
                    for (i = 1; i>-10;i=i-1)
                    {
                        a = 3;
                    }
            }
        """
        expect = str(
            Program(
            [
                FuncDecl(Id('foo'),
                [],
                IntType(),
                Block(
                [
                    If(
                        BinaryOp('>',Id('a'),IntLiteral(3)),
                        For(
                            BinaryOp('=',Id('i'),IntLiteral(1)),
                            BinaryOp('>',Id('i'),UnaryOp('-',IntLiteral(10))),
                            BinaryOp('=',Id('i'),BinaryOp('-',Id('i'),IntLiteral(1))),
                            Block(
                            [
                                BinaryOp('=',Id('a'),IntLiteral(3))
                            ])
                        )
                    )
                ]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,323))
    
    def test_For_Stml_No24(self):
        """Test for statement"""
        input = """
            float foo(){
                    for (i = 1; i>-10;i=i-1)
                    {
                        a = 3;
                        {
                            int b;
                            b = 3;
                        }
                    }
            }
        """
        expect = str(
            Program(
            [
                FuncDecl(Id('foo'),
                [],
                FloatType(),
                Block(
                [
                    For(
                        BinaryOp('=',Id('i'),IntLiteral(1)),
                        BinaryOp('>',Id('i'),UnaryOp('-',IntLiteral(10))),
                        BinaryOp('=',Id('i'),BinaryOp('-',Id('i'),IntLiteral(1))),
                        Block(
                        [
                            BinaryOp('=',Id('a'),IntLiteral(3)),
                            Block(
                            [
                                VarDecl('b',IntType()),
                                BinaryOp('=',Id('b'),IntLiteral(3))
                            ])
                        ])
                    )
                ]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,324))
    
    def test_For_Stml_No25(self):
        """Test for statement"""
        input = """
        int main(string u)
        {
            for (i=1;i<=10;i=i+1)
                for (j=1;j<=10;j=j+1)
                    print(i,"x",j,"= ",i*j);
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl(Id('main'),
                        [
                            VarDecl('u',StringType())
                        ],
                        IntType(),
                        Block(
                            [
                                For(
                                    BinaryOp('=',Id('i'),IntLiteral(1)),
                                    BinaryOp('<=',Id('i'),IntLiteral(10)),
                                    BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
                                    For(
                                        BinaryOp('=',Id('j'),IntLiteral(1)),
                                        BinaryOp('<=',Id('j'),IntLiteral(10)),
                                        BinaryOp('=',Id('j'),BinaryOp('+',Id('j'),IntLiteral(1))),
                                        CallExpr(
                                            Id('print'),
                                            [
                                                Id('i'),StringLiteral('x'),Id('j'),StringLiteral('= '),BinaryOp('*',Id('i'),Id('j'))
                                            ]
                                        )
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,325))
    
    def test_For_Stml_No26(self):
        """Test for statement"""
        input = """
        int foo()
        {
            for(i = 1;(i<3+4)&&(i>=-4);i=i+1)
                print("Khong biet");
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl(Id('foo'),
                        [],
                        IntType(),
                        Block(
                            [
                                For(
                                    BinaryOp('=',Id('i'),IntLiteral(1)),
                                    BinaryOp('&&',BinaryOp('<',Id('i'),BinaryOp('+',IntLiteral(3),IntLiteral(4))),BinaryOp('>=',Id('i'),UnaryOp('-',IntLiteral(4)))),
                                    BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
                                    CallExpr(
                                        Id('print'),
                                        [
                                            StringLiteral('Khong biet')
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_do_while_Stml_No27(self):
        """Test do while statement"""
        input = """
            string tich(){
                int n;
                n = -1;
                do
                    n=n+1;
                while (n > 1);
            }
        """
        expect = str(
            Program(
            [
                FuncDecl(Id('tich'),
                    [],
                    StringType(),
                    Block(
                    [
                        VarDecl('n',IntType()),
                        BinaryOp('=',Id('n'),UnaryOp('-',IntLiteral(1))),
                        Dowhile(
                            [
                                BinaryOp('=',Id('n'),BinaryOp('+',Id('n'),IntLiteral(1)))
                            ],
                            BinaryOp('>',Id('n'),IntLiteral(1))
                        )
                    ])
                )
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_do_while_Stml_No28(self):
        """Test do while statement"""
        input = """
            boolean foo(){
                int n;
                n = 0;
               do 
                {
                    print("tui khong biet gi het");
                    {
                        {
                            print("Tui la ai");
                        }
                    }
                }
                n = n -1;
               while (n>=-10);
            }
        """
        expect = str(
            Program(
                [
                    FuncDecl(Id('foo'),
                    [],
                    BoolType(),
                    Block(
                        [
                            VarDecl('n',IntType()),
                            BinaryOp('=',Id('n'),
                            IntLiteral(0)),
                            Dowhile(
                                [
                                    Block(
                                        [
                                            CallExpr(
                                                Id('print'),
                                                [
                                                    StringLiteral("tui khong biet gi het")
                                                ]),
                                            Block(
                                                [
                                                    Block(
                                                        [
                                                            CallExpr(
                                                                Id('print'),
                                                                [
                                                                    StringLiteral("Tui la ai")
                                                                ]
                                                            )
                                                        ]
                                                    )
                                                ]
                                            )
                                        ]
                                    ),
                                    BinaryOp('=',Id('n'),BinaryOp('-',Id('n'),IntLiteral(1)))
                                ],
                                BinaryOp('>=',Id('n'),UnaryOp('-',IntLiteral(10)))
                            )
                        ]
                    ))
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,328))
    
    def test_do_while_Stml_No29(self):
        """Test do while statement"""
        input = """
            int a[3];
            boolean foo1()
            {
                int n;
                int m;
                float b[19];
                n = 10;
                do 
                    m = 10;
                    do
                        b[m] = m;
                        m = m-1;
                    while (m>1);
                while (n>1);
            }
        """
        expect = str(
            Program(
            [
                VarDecl('a',ArrayType(3,IntType())),
                FuncDecl(Id('foo1'),
                    [],
                    BoolType(),
                    Block(
                        [
                            VarDecl('n',IntType()),
                            VarDecl('m',IntType()),
                            VarDecl('b',ArrayType(19,FloatType())),
                            BinaryOp('=',Id('n'),IntLiteral(10)),
                            Dowhile(
                                [
                                    BinaryOp('=',Id('m'),IntLiteral(10)),
                                    Dowhile(
                                        [
                                            BinaryOp('=',ArrayCell(Id('b'),Id('m')),Id('m')),BinaryOp('=',Id('m'),
                                            BinaryOp('-',Id('m'),IntLiteral(1)))
                                        ],
                                        BinaryOp('>',Id('m'),IntLiteral(1))
                                    )
                                ],
                                BinaryOp('>',Id('n'),IntLiteral(1))
                            )
                        ]
                    )
                )
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,329))
    
    def test_do_while_Stml_No30(self):
        """Test do while statement"""
        input = """
            string[] foo1(boolean a[])
            {
                int sum, i;
                sum = 0;
                i = 1;
                float epsilon;
                do
                    sum = sum+ 1/i;
                    epsilon = 1/i;
                    i = 1+i;
                while (epsilon < 0.e6);
            }
        """
        expect = str(
            Program(
            [
                FuncDecl(Id('foo1'),
                    [
                        VarDecl('a',ArrayPointerType(BoolType()))
                    ],
                    ArrayPointerType(StringType()),
                    Block(
                        [
                            VarDecl('sum',IntType()),
                            VarDecl('i',IntType()),
                            BinaryOp('=',Id('sum'),IntLiteral(0)),
                            BinaryOp('=',Id('i'),IntLiteral(1)),
                            VarDecl('epsilon',FloatType()),
                            Dowhile(
                                [
                                    BinaryOp('=',Id('sum'),BinaryOp('+',Id('sum'),BinaryOp('/',IntLiteral(1),Id('i')))),
                                    BinaryOp('=',Id('epsilon'),BinaryOp('/',IntLiteral(1),Id('i'))),
                                    BinaryOp('=',Id('i'),BinaryOp('+',IntLiteral(1),Id('i')))
                                ],
                                BinaryOp('<',Id('epsilon'),FloatLiteral(0.e6))
                            )
                        ]
                    )
                )
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,330))
    
    def test_Break_Stml_No31(self):
        """Test break statement"""
        input = """
            boolean foo()
            {
                int i;
                for (i = 0;true;i=i+1)
                    {
                        if (i>100)
                            break;
                    }
            }
        """
        expect = str(
            Program(
                [
                    FuncDecl(Id('foo'),
                        [],
                        BoolType(),
                        Block(
                            [
                                VarDecl('i',IntType()),
                                For(
                                    BinaryOp('=',Id('i'),IntLiteral(0)),
                                    BooleanLiteral(True),
                                    BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
                                    Block(
                                        [
                                            If(
                                                BinaryOp('>',Id('i'),IntLiteral(100)),
                                                Break()
                                            )
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,331))
    
    def test_Continue_Stml_No32(self):
        """Test Continue statement"""
        input = """
            int[] foo(int a)
            {
                int n;
                for (n = 0; true; n = n+1)
                {
                    if (n>100)
                        break;
                    else
                        if (n%2==0 || n%5==0)
                            continue;
                }
            }
        """
        expect = str(
            Program(
                [
                    FuncDecl(Id('foo'),
                    [
                        VarDecl('a',IntType())
                    ],
                    ArrayPointerType(IntType()),
                    Block(
                        [
                            VarDecl('n',IntType()),
                            For(
                                BinaryOp('=',Id('n'),IntLiteral(0)),
                                BooleanLiteral('true'),
                                BinaryOp('=',Id('n'),BinaryOp('+',Id('n'),IntLiteral(1))),
                                Block(
                                    [
                                        If(
                                            BinaryOp('>',Id('n'),IntLiteral(100)),
                                            Break(),
                                            If(
                                                BinaryOp('||',BinaryOp('==',BinaryOp('%',Id('n'),IntLiteral(2)),IntLiteral(0)),BinaryOp('==',BinaryOp('%',Id('n'),IntLiteral(5)),IntLiteral(0))),
                                                Continue()
                                            )
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,332))
    
    def test_Return_void_Stml_No33(self):
        """Test Return statement"""
        input = """
           void printBinaryNumber(int a)
           {
                if (a == 0)
                    return;
                else
                {
                    printBinaryNumber(a/2);
                    print("%d",a%2);
                }
           }
        """
        expect = str(
           Program(
               [
                   FuncDecl(Id('printBinaryNumber'),
                   [
                       VarDecl('a',IntType())
                    ],
                    VoidType(),
                    Block(
                        [
                            If(
                                BinaryOp('==',Id('a'),IntLiteral(0)),
                                Return(),
                                Block(
                                    [
                                        CallExpr(
                                            Id('printBinaryNumber'),
                                            [
                                                BinaryOp('/',Id('a'),IntLiteral(2))
                                            ]
                                        ),
                                        CallExpr(
                                            Id('print'),
                                            [
                                                StringLiteral('%d'),
                                                BinaryOp('%',Id('a'),IntLiteral(2))
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,333))
    
    def test_Return_Stml_No34(self):
        """Test Return statement"""
        input = """
           int foo(float i)
           {
               if (i<10)
                    return 0;
                else
                    if (i<100)
                        return 10+(i/2+3);
                    else 
                        return (a&&b) || (a >= b) || (-10 > a) || !(a&&1); 
           }
        """
        expect = str(
           Program(
               [
                   FuncDecl(Id('foo'),
                        [
                            VarDecl('i',FloatType())
                        ],
                        IntType(),
                        Block(
                            [
                                If(
                                    BinaryOp('<',Id('i'),IntLiteral(10)),
                                    Return(IntLiteral(0)),
                                    If(
                                        BinaryOp('<',Id('i'),IntLiteral(100)),
                                        Return(BinaryOp('+',IntLiteral(10),BinaryOp('+',BinaryOp('/',Id('i'),IntLiteral(2)),IntLiteral(3)))),
                                        Return(
                                            BinaryOp('||',BinaryOp('||',BinaryOp('||',BinaryOp('&&',Id('a'),Id('b')),BinaryOp('>=',Id('a'),Id('b'))),BinaryOp('>',UnaryOp('-',IntLiteral(10)),Id('a'))),UnaryOp('!',BinaryOp('&&',Id('a'),IntLiteral(1))))
                                        )
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,334))
    
    def test_Comment_No35(self):
        """Test Comment"""
        input = """
           float main()
        {
             /*comment vui lam*/
             //tui vui lam chu bu 
             print("hahahaha!!!!!!");
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl(Id('main'),
                        [],
                        FloatType(),
                        Block(
                            [
                                CallExpr(
                                    Id('print'),
                                    [
                                        StringLiteral('hahahaha!!!!!!')
                                    ]
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,335))
    
    def test_Expression_No36(self):
        """Test Expression"""
        input = """
           int main(string u)
        {
            a = 7+8>=9+10-90--20+0;
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl(Id('main'),
                        [
                            VarDecl('u',StringType())
                        ],
                        IntType(),
                        Block(
                            [
                                BinaryOp(
                                    '=',
                                    Id('a'),
                                    BinaryOp(
                                        '>=',
                                        BinaryOp('+',IntLiteral(7),IntLiteral(8)),
                                        BinaryOp(
                                            '+',
                                            BinaryOp(
                                                '-',
                                                BinaryOp(
                                                    '-',
                                                    BinaryOp('+',IntLiteral(9),IntLiteral(10)),
                                                    IntLiteral(90)
                                                ),
                                                UnaryOp('-',IntLiteral(20))
                                            ),
                                            IntLiteral(0)
                                        )
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_Expression_No37(self):
        """Test Expression"""
        input = """
          int main()
        {
            khong_bit = (a+b)[2];
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl(Id('main'),
                        [],
                        IntType(),
                        Block(
                            [
                                BinaryOp(
                                    '=',
                                    Id("khong_bit"),
                                    ArrayCell(BinaryOp('+',Id('a'),Id('b')),IntLiteral(2)
                                    )
                                )
                            ]
                        )
                    )
                ]
            )    
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,337))
    
    def test_Expression_No38(self):
        """Test Expression"""
        input = """
          int foo(int a)
        {
            i = foo(2, foo(3,a[2]));
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl(Id('foo'),
                        [
                            VarDecl('a',IntType())
                        ],
                        IntType(),
                        Block(
                            [
                                BinaryOp(
                                    '=',
                                    Id('i'),
                                    CallExpr(
                                        Id('foo'),
                                        [
                                            IntLiteral(2),
                                            CallExpr(
                                                Id('foo'),
                                                [
                                                    IntLiteral(3),ArrayCell(Id('a'),IntLiteral(2))
                                                ]
                                            )
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,338))
    
    def test_Expression_No39(self):
        """Test Expression"""
        input = """
          int foo(int a)
        {
            int a[4];
            a[2] = foo(a+2)[2]-4+8;
        }
        """
        expect = str(
        Program(
            [
                FuncDecl(Id('foo'),
                    [
                        VarDecl('a',IntType())
                    ],
                    IntType(),
                    Block(
                        [
                            VarDecl('a',ArrayType(4,IntType())),
                            BinaryOp(
                                '=',
                                ArrayCell(Id('a'),IntLiteral(2)),
                                BinaryOp(
                                    '+',
                                    BinaryOp(
                                        '-',
                                        ArrayCell(
                                            CallExpr(
                                                Id('foo'),
                                                [
                                                    BinaryOp('+',Id('a'),IntLiteral(2))
                                                ]
                                            ),IntLiteral(2)),
                                        IntLiteral(4)
                                    ),
                                    IntLiteral(8)
                                )
                            )
                        ]
                    )
                )
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,339))
    
    def test_Expression_No40(self):
        """Test Expression"""
        input = """
          int foo(int a)
        {
            a=b=c=3;
            a=a&&b||c;
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl(Id('foo'),
                        [
                            VarDecl('a',IntType())
                        ],
                        IntType(),
                        Block(
                            [
                                BinaryOp(
                                    '=',
                                    Id('a'),
                                    BinaryOp(
                                        '=',
                                        Id('b'),
                                        BinaryOp('=',Id('c'), IntLiteral(3))
                                    )
                                ),
                                BinaryOp(
                                    '=',
                                    Id('a'),
                                    BinaryOp(
                                        '||',
                                        BinaryOp('&&',Id('a'),Id('b')),
                                        Id('c')
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,340))
    
    def test_Expression_No41(self):
        """Test expression statement"""
        input= """
        float[] foo(int a)
        {
            int x;
            foo(2,true)[3+x] = a[b[2]];
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl(Id('foo'),
                        [
                            VarDecl("a",IntType())
                        ],
                        ArrayPointerType(FloatType()),
                        Block(
                            [
                                VarDecl("x",IntType()),
                                BinaryOp(
                                    '=',
                                    ArrayCell(
                                        CallExpr(
                                            Id("foo"),
                                            [
                                                IntLiteral(2),
                                                BooleanLiteral(True)
                                            ]
                                        ),
                                        BinaryOp("+",IntLiteral(3),Id("x"))
                                    ),
                                    ArrayCell(
                                        Id("a"),
                                        ArrayCell(Id("b"),IntLiteral(2))
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,341))
    
    def test_Expression_No42(self):
        """Test expression statement"""
        input= """
            boolean test()
            {
                boolean b;
                b = ((a&&b)
                    ||(a>=c)
                    ||(d==e)
                    ||(a!=3));
           }
        """
        expect = str(
            Program(
                [
                    FuncDecl(Id("test"),
                        [],
                        BoolType(),
                        Block(
                            [
                                VarDecl('b',BoolType()),
                                BinaryOp(
                                    "=",
                                    Id("b"),
                                    BinaryOp(
                                        "||",
                                        BinaryOp(
                                            "||",
                                            BinaryOp(
                                                "||",
                                                BinaryOp("&&",Id("a"),Id("b")),
                                                BinaryOp(">=",Id("a"),Id("c"))
                                            ),
                                            BinaryOp("==",Id("d"),Id("e"))
                                        ),
                                        BinaryOp("!=",Id("a"),IntLiteral(3))
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_Expression_No43(self):
        """Test expression statement"""
        input= """
        int main(string u)
        {
            foo(foo(foo(foo(foo()))));
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl(Id('main'),
                        [
                            VarDecl('u',StringType())
                        ],
                        IntType(),
                        Block(
                            [
                                CallExpr(
                                    Id('foo'),
                                    [
                                        CallExpr(
                                            Id('foo'),
                                            [
                                                CallExpr(
                                                    Id('foo'),
                                                    [
                                                        CallExpr(
                                                            Id('foo'),
                                                            [
                                                                CallExpr(
                                                                    Id('foo'),
                                                                    []
                                                                )
                                                            ]
                                                        )
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_Expression_No44(self):
        """Test expression statement"""
        input= """
        int main(string u)
        {
            a[b[c[d[e[4]]]]]=0;
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl(Id('main'),
                        [
                            VarDecl('u',StringType())
                        ],
                        IntType(),
                        Block(
                            [
                                BinaryOp(
                                    '=',
                                    ArrayCell(
                                        Id('a'),
                                        ArrayCell(
                                            Id('b'),
                                            ArrayCell(
                                                Id('c'),
                                                ArrayCell(
                                                    Id('d'),
                                                    ArrayCell(
                                                        Id('e'),
                                                        IntLiteral(4)
                                                    )
                                                )
                                            )
                                        )
                                    ),
                                    IntLiteral(0)
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_Expression_No45(self):
        """Test expression statement"""
        input= """
        int main()
        {
             boo = (-4*7/6%1)+(8-9)>-1;
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl(Id('main'),
                        [],
                        IntType(),
                        Block(
                        [
                            BinaryOp(
                                '=',
                                Id('boo'),
                                BinaryOp(
                                    '>',
                                    BinaryOp(
                                        '+',
                                        BinaryOp(
                                            '%',
                                            BinaryOp(
                                                '/',
                                                BinaryOp('*',UnaryOp('-',IntLiteral(4)),IntLiteral(7)),
                                                IntLiteral(6)
                                            ),
                                            IntLiteral(1)
                                        ),
                                        BinaryOp(
                                            '-',
                                            IntLiteral(8),
                                            IntLiteral(9)
                                        )
                                    ),
                                    UnaryOp('-',IntLiteral(1))
                                )
                            )
                        ])
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,345))
    
    def test_Expression_No46(self):
        """Test expression statement"""
        input= """
        int main()
        {
             1.34[2]+5 - 1e4[42]%1.e5;
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl(Id('main'),
                        [],
                        IntType(),
                        Block(
                            [
                                BinaryOp(
                                    '-',
                                    BinaryOp('+',ArrayCell(FloatLiteral(1.34),IntLiteral(2)),IntLiteral(5)),
                                    BinaryOp('%',ArrayCell(FloatLiteral(1e4),IntLiteral(42)),FloatLiteral(1.e5))
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_Expression_No47(self):
        """Test expression statement"""
        input= """
        int main()
        {
            boolean b;
            b = true && "string" || false == (1e6 - 3);
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl(Id('main'),
                        [],
                        IntType(),
                        Block(
                            [
                                VarDecl('b',BoolType()),
                                BinaryOp(
                                    '=',
                                    Id('b'),
                                    BinaryOp(
                                        '||',
                                        BinaryOp('&&',BooleanLiteral(True),StringLiteral('string')),
                                        BinaryOp('==',BooleanLiteral(False),BinaryOp('-',FloatLiteral(1e6),IntLiteral(3)))
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,347))
    
    def test_Expression_No48(self):
        """Test expression statement"""
        input= """
        int main()
        {
             foo(2)+foo()-a[2]*foo((((2+3)-4)/7)-9,0.0,9.7);
            -!a[2] + a(a(a(a(2))))[2] - a / a * a % (a < a) + (a <= a) + (a >= a) + ((a > a) == a) + (a != a) && a || a = a;
            (((6)));
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl(Id('main'),
                        [],
                        IntType(),
                        Block(
                            [
                                BinaryOp(
                                    '-',
                                    BinaryOp(
                                        '+',
                                        CallExpr(
                                            Id('foo'),
                                            [
                                                IntLiteral(2)
                                                ]
                                            ),
                                        CallExpr(
                                            Id('foo'),
                                            []
                                        )
                                    ),
                                    BinaryOp(
                                        '*',
                                        ArrayCell(Id('a'),IntLiteral(2)),
                                        CallExpr(
                                            Id('foo'),
                                            [
                                                BinaryOp(
                                                    '-',
                                                    BinaryOp(
                                                        '/',
                                                        BinaryOp(
                                                            '-',
                                                            BinaryOp('+',IntLiteral(2),IntLiteral(3)),
                                                            IntLiteral(4)
                                                        ),
                                                        IntLiteral(7)
                                                    ),IntLiteral(9)
                                                ),
                                                FloatLiteral(0.0),
                                                FloatLiteral(9.7)
                                            ]
                                        )
                                    )
                                ),
                                BinaryOp(
                                    '=',
                                    BinaryOp(
                                        '||',
                                        BinaryOp(
                                            '&&',
                                            BinaryOp(
                                                '+',
                                                BinaryOp(
                                                    '+',
                                                    BinaryOp(
                                                        '+',
                                                        BinaryOp(
                                                            '+',
                                                            BinaryOp(
                                                                '-',
                                                                BinaryOp(
                                                                    '+',
                                                                    UnaryOp(
                                                                        '-',
                                                                        UnaryOp('!',ArrayCell(Id('a'),IntLiteral(2)))
                                                                    ),
                                                                    ArrayCell(
                                                                        CallExpr(
                                                                            Id('a'),
                                                                            [
                                                                                CallExpr(
                                                                                    Id('a'),
                                                                                    [
                                                                                        CallExpr(
                                                                                            Id('a'),
                                                                                            [
                                                                                                CallExpr(
                                                                                                    Id('a'),
                                                                                                    [
                                                                                                        IntLiteral(2)
                                                                                                    ]
                                                                                                )
                                                                                            ]
                                                                                        )
                                                                                    ]
                                                                                )
                                                                            ]
                                                                        ),
                                                                        IntLiteral(2)
                                                                    )
                                                                ),
                                                                BinaryOp(
                                                                    '%',
                                                                    BinaryOp(
                                                                        '*',
                                                                        BinaryOp('/',Id('a'),Id('a')),
                                                                        Id('a')
                                                                    ),
                                                                    BinaryOp('<',Id('a'),Id('a'))
                                                                )
                                                            ),
                                                            BinaryOp('<=',Id('a'),Id('a'))
                                                        ),
                                                        BinaryOp('>=',Id('a'),Id('a'))
                                                    ),
                                                    BinaryOp(
                                                        '==',
                                                        BinaryOp('>',Id('a'),Id('a')),
                                                        Id('a')
                                                    )
                                                ),
                                                BinaryOp('!=',Id('a'),Id('a'))
                                            ),
                                            Id('a')
                                        ),
                                        Id('a')
                                    ),
                                    Id('a')
                                ),
                                IntLiteral(6)
                            ]
                        )
                    )
                ]
            )  
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_Expression_No49(self):
        """Test expression statement"""
        input= """
        int main()
        {
             sum = (
                (2+3) ||
                (6-2) ||
                (6%4) ||
                (8/9) &&
                9>8 ||
                x>=0 ||
                y<=u ||
                (z < 0) ||
                (ui == 0) &&
                (7*9) ||
                !x!=9);
            
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl(Id('main'),
                        [],
                        IntType(),
                        Block(
                            [
                                BinaryOp(
                                    '=',
                                    Id('sum'),
                                    BinaryOp(
                                        '||',
                                        BinaryOp(
                                            '||',
                                            BinaryOp(
                                                '||',
                                                BinaryOp(
                                                    '||',
                                                    BinaryOp(
                                                        '||',
                                                        BinaryOp(
                                                            '||',
                                                            BinaryOp(
                                                                '||',
                                                                BinaryOp(
                                                                    '||',
                                                                    BinaryOp('+',IntLiteral(2),IntLiteral(3)),
                                                                    BinaryOp('-',IntLiteral(6),IntLiteral(2))
                                                                ),
                                                                BinaryOp('%',IntLiteral(6),IntLiteral(4))
                                                            ),
                                                            BinaryOp(
                                                               '&&',
                                                                BinaryOp('/',IntLiteral(8),IntLiteral(9)),
                                                                BinaryOp('>',IntLiteral(9),IntLiteral(8))
                                                            )
                                                        ),
                                                        BinaryOp('>=',Id('x'),IntLiteral(0))
                                                    ),
                                                    BinaryOp('<=',Id('y'),Id('u'))
                                                ),
                                                BinaryOp('<',Id('z'),IntLiteral(0))
                                            ),
                                            BinaryOp(
                                                '&&',
                                                BinaryOp('==',Id('ui'),IntLiteral(0)),
                                                BinaryOp('*',IntLiteral(7),IntLiteral(9))
                                            )
                                        ),
                                        BinaryOp(
                                            '!=',
                                            UnaryOp('!',Id('x')),
                                            IntLiteral(9)
                                        )
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,349))
    
    def test_Expression_No50(self):
        """Test expression statement"""
        input = """
            int foo(){
                call(1+3,a[3]);
            }
        """
        expect = str(
            Program(
                [
                    FuncDecl(Id('foo'),
                        [],
                        IntType(),
                        Block(
                            [
                                CallExpr(
                                    Id('call'),
                                    [
                                        BinaryOp('+',IntLiteral(1),IntLiteral(3)),
                                        ArrayCell(Id('a'),IntLiteral(3))
                                    ]
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,350))
    
    def test_Expression_No51(self):
        """Test expression statement"""
        input = """
            int foo(){
                a = 3 + call[3];
            }
        """
        expect = str(
            Program(
                [
                    FuncDecl(Id('foo'),
                        [],
                        IntType(),
                        Block(
                            [
                                BinaryOp(
                                    '=',
                                    Id('a'),
                                    BinaryOp(
                                        '+',
                                        IntLiteral(3),
                                        ArrayCell(Id('call'),IntLiteral(3))
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,351))
   
    def test_Expression_No52(self):
        """Test expression statement"""
        input = """
        void main(){
            A&&!B&&C||A&&!B&&!C = A&&!B;
            A&&B&&C||A&&B&&D||A&&B = A&&B;
            A=B=C=D=E=F=G;
            !(!A||!(B&&c))&&!A = false;

            return;
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl(Id('main'),
                        [],
                        VoidType(),
                        Block(
                            [
                                BinaryOp(
                                    '=',
                                    BinaryOp(
                                        '||',
                                        BinaryOp(
                                            '&&',
                                            BinaryOp('&&',Id('A'),UnaryOp('!',Id('B'))),
                                            Id('C')
                                        ),
                                        BinaryOp(
                                            '&&',
                                            BinaryOp('&&',Id('A'),UnaryOp('!',Id('B'))),
                                            UnaryOp('!',Id('C'))
                                        )
                                    ),
                                    BinaryOp('&&',Id('A'),UnaryOp('!',Id('B')))
                                ),
                                BinaryOp(
                                    '=',
                                    BinaryOp(
                                        '||',
                                        BinaryOp(
                                            '||',
                                            BinaryOp(
                                                '&&',
                                                BinaryOp('&&',Id('A'),Id('B')),
                                                Id('C')
                                            ),
                                            BinaryOp(
                                                '&&',
                                                BinaryOp('&&',Id('A'),Id('B')),
                                                Id('D')
                                            )
                                        ),
                                        BinaryOp('&&',Id('A'),Id('B'))
                                    ),
                                    BinaryOp('&&',Id('A'),Id('B'))
                                ),
                                BinaryOp(
                                    '=',
                                    Id('A'),
                                    BinaryOp(
                                        '=',
                                        Id('B'),
                                        BinaryOp(
                                            '=',
                                            Id('C'),
                                            BinaryOp(
                                                '=',
                                                Id('D'),
                                                BinaryOp(
                                                    '=',
                                                    Id('E'),
                                                    BinaryOp('=',Id('F'),Id('G'))
                                                )
                                            )
                                        )
                                    )
                                ),
                                BinaryOp(
                                    '=',
                                    BinaryOp(
                                        '&&',
                                        UnaryOp(
                                            '!',
                                            BinaryOp(
                                                '||',
                                                UnaryOp('!',Id('A')),
                                                UnaryOp(
                                                    '!',
                                                    BinaryOp('&&',Id('B'),Id('c'))
                                                )
                                            )
                                        ),
                                        UnaryOp('!',Id('A'))
                                    ),
                                    BooleanLiteral(False)
                                ),
                                Return()
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,352))
    
    def test_Expression_No53(self):
        """Test expression statement"""
        input = """
        void main()
        {
            //Some calculation for solving the logic equation
            A&&(!A||B) = A&&B;
            (A||B)&&(A||!B)= A;
            A || B&&C = (A||B)&&(A||C);
            A&&B || !A&&C || B&&C=A&&B || !A&&C(A||B)&&(!A||C)&&(B||C)=(A||B)&&(!A||C);
            return;
        }"""
        expect = str(
            Program(
                [
                    FuncDecl(Id('main'),
                        [],
                        VoidType(),
                        Block(
                            [
                                BinaryOp(
                                    '=',
                                    BinaryOp(
                                        '&&',
                                        Id('A'),
                                        BinaryOp('||',UnaryOp('!',Id('A')),Id('B'))
                                    ),
                                    BinaryOp('&&',Id('A'),Id('B'))
                                ),
                                BinaryOp(
                                    '=',
                                    BinaryOp(
                                        '&&',
                                        BinaryOp('||',Id('A'),Id('B')),
                                        BinaryOp('||',Id('A'),UnaryOp('!',Id('B')))
                                    ),
                                    Id('A')
                                ),
                                BinaryOp(
                                    '=',
                                    BinaryOp(
                                        '||',
                                        Id('A'),
                                        BinaryOp('&&',Id('B'),Id('C'))
                                    ),
                                    BinaryOp(
                                        '&&',
                                        BinaryOp('||',Id('A'),Id('B')),
                                        BinaryOp('||',Id('A'),Id('C'))
                                    )
                                ),
                                BinaryOp(
                                    '=',
                                    BinaryOp(
                                        '||',
                                        BinaryOp(
                                            '||',
                                            BinaryOp('&&',Id('A'),Id('B')),
                                            BinaryOp('&&',UnaryOp('!',Id('A')),Id('C'))
                                        ),
                                        BinaryOp('&&',Id('B'),Id('C'))
                                    ),
                                    BinaryOp(
                                        '=',
                                        BinaryOp(
                                            '||',
                                            BinaryOp('&&',Id('A'),Id('B')),
                                            BinaryOp(
                                                '&&',
                                                BinaryOp(
                                                    '&&',
                                                    BinaryOp(
                                                        '&&',
                                                        UnaryOp('!',Id('A')),
                                                        CallExpr(
                                                            Id('C'),
                                                            [
                                                                BinaryOp('||',Id('A'),Id('B'))
                                                            ]
                                                        )
                                                    ),
                                                    BinaryOp(
                                                        '||',
                                                        UnaryOp('!',Id('A')),Id('C')
                                                    )
                                                ),
                                                BinaryOp('||',Id('B'),Id('C'))
                                            )
                                        ),
                                        BinaryOp(
                                            '&&',
                                            BinaryOp('||',Id('A'),Id('B')),
                                            BinaryOp('||',UnaryOp('!',Id('A')),Id('C'))
                                        )
                                    )
                                ),
                                Return()
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,353))
    
    def test_Expression_No54(self):
        """Test expression statement"""
        input = """
        void main()
        {
            //Some calculation for solving the logic equation
            A = A &&(A||B);
            A = A || A&&B;
            A = A && B || A && !B;
            A || B = A || !A&&B;
            return;
        }"""
        expect = str(
            Program(
                [
                    FuncDecl(Id('main'),
                        [],
                        VoidType(),
                        Block(
                            [
                                BinaryOp(
                                    '=',
                                    Id('A'),
                                    BinaryOp(
                                        '&&',
                                        Id('A'),
                                        BinaryOp('||',Id('A'),Id('B'))
                                    )
                                ),
                                BinaryOp(
                                    '=',
                                    Id('A'),
                                    BinaryOp(
                                        '||',
                                        Id('A'),
                                        BinaryOp('&&',Id('A'),Id('B'))
                                    )
                                ),
                                BinaryOp(
                                    '=',
                                    Id('A'),
                                    BinaryOp(
                                        '||',
                                        BinaryOp('&&',Id('A'),Id('B')),
                                        BinaryOp('&&',Id('A'),UnaryOp('!',Id('B')))
                                    )
                                ),
                                BinaryOp(
                                    '=',
                                    BinaryOp('||',Id('A'),Id('B')),
                                    BinaryOp('||',Id('A'),BinaryOp('&&',UnaryOp('!',Id('A')),Id('B')))
                                ),
                                Return()
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_Expression_No55(self):
        """Test expression statement"""
        input = """
        void main()
        {
            Y = A&&B&&C || A&&B&&!C || A&&!B&&C;
            Y = A&&(B||C);
            return;
        }"""
        expect = str(
            Program(
                [
                    FuncDecl(Id('main'),
                        [],
                        VoidType(),
                        Block(
                            [
                                BinaryOp(
                                    '=',
                                    Id('Y'),
                                    BinaryOp(
                                        '||',
                                        BinaryOp(
                                            '||',
                                            BinaryOp(
                                                '&&',
                                                BinaryOp('&&',Id('A'),Id('B')),
                                                Id('C')
                                            ),
                                            BinaryOp(
                                                '&&',
                                                BinaryOp('&&',Id('A'),Id('B')),
                                                UnaryOp('!',Id('C'))
                                            )
                                        ),
                                        BinaryOp(
                                            '&&',
                                            BinaryOp('&&',Id('A'),UnaryOp('!',Id('B'))),
                                            Id('C')
                                        )
                                    )
                                ),
                                BinaryOp(
                                    '=',
                                    Id('Y'),
                                    BinaryOp(
                                        '&&',
                                        Id('A'),
                                        BinaryOp('||',Id('B'),Id('C'))
                                    )
                                ),
                                Return()
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,355))
    
    def test_Expression_No56(self):
        """Test expression statement"""
        input = """
        void main()
        {
            !A&&!B || !A&&C || B&&!C || A&&!B&&!C = !(A&&C);
            !A&&!B&&C || !A&&B&&!C || A&&!(B&&C);
            !(!(!A&&!B&&C)&&!(!A&&B&&!C)&&!(A&&!(B&&C)));
            return;
        }"""
        expect = str(
            Program(
                [
                    FuncDecl(Id('main'),
                        [],
                        VoidType(),
                        Block(
                            [
                                BinaryOp(
                                    '=',
                                    BinaryOp(
                                        '||',
                                        BinaryOp(
                                            '||',
                                            BinaryOp(
                                                '||',
                                                BinaryOp('&&',UnaryOp('!',Id('A')),UnaryOp('!',Id('B'))),
                                                BinaryOp('&&',UnaryOp('!',Id('A')),Id('C'))
                                            ),
                                            BinaryOp('&&',Id('B'),UnaryOp('!',Id('C')))
                                        ),
                                        BinaryOp(
                                            '&&',
                                            BinaryOp('&&',Id('A'),UnaryOp('!',Id('B'))),
                                            UnaryOp('!',Id('C'))
                                        )
                                    ),
                                    UnaryOp('!',BinaryOp('&&',Id('A'),Id('C')))
                                ),
                                BinaryOp(
                                    '||',
                                    BinaryOp(
                                        '||',
                                        BinaryOp(
                                            '&&',
                                            BinaryOp('&&',UnaryOp('!',Id('A')),UnaryOp('!',Id('B'))),
                                            Id('C')
                                        ),
                                        BinaryOp(
                                            '&&',
                                            BinaryOp('&&',UnaryOp('!',Id('A')),Id('B')),
                                            UnaryOp('!',Id('C'))
                                        )
                                    ),
                                    BinaryOp(
                                        '&&',
                                        Id('A'),
                                        UnaryOp('!',BinaryOp('&&',Id('B'),Id('C')))
                                    )
                                ),
                                UnaryOp(
                                    '!',
                                    BinaryOp(
                                        '&&',
                                        BinaryOp(
                                            '&&',
                                            UnaryOp(
                                                '!',
                                                BinaryOp(
                                                    '&&',
                                                    BinaryOp(
                                                        '&&',
                                                        UnaryOp('!',Id('A')),
                                                        UnaryOp('!',Id('B'))
                                                    ),
                                                    Id('C')
                                                )
                                            ),
                                            UnaryOp(
                                                '!',
                                                BinaryOp(
                                                    '&&',
                                                    BinaryOp(
                                                        '&&',
                                                        UnaryOp('!',Id('A')),
                                                        Id('B')
                                                    ),
                                                    UnaryOp('!',Id('C'))
                                                )
                                            )
                                        ),
                                        UnaryOp(
                                            '!',
                                            BinaryOp(
                                                '&&',
                                                Id('A'),
                                                UnaryOp('!',BinaryOp('&&',Id('B'),Id('C')))
                                            )
                                        )
                                    )
                                ),
                                Return()
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,356))
    
    def test_Expression_No57(self):
        """Test expression statement"""
        input = """
        void heapify(int arr[], int n, int i) 
        { 
            int largest;
            largest = i; // Initialize largest as root 
            int l ;l= 2*i + 1; // left = 2*i + 1 
            int r ;r= 2*i + 2; // right = 2*i + 2 

            if (l < n && arr[l] > arr[largest]) 
                largest = l; 
            if (r < n && arr[r] > arr[largest]) 
                largest = r; 
            if (largest != i) 
            { 
                swap(arr[i], arr[largest]); 
                heapify(arr, n, largest); 
            } 
        } 
        """
        expect = str(
            Program(
                [
                    FuncDecl(Id('heapify'),
                        [
                            VarDecl('arr',ArrayPointerType(IntType())),
                            VarDecl('n',IntType()),
                            VarDecl('i',IntType())
                        ],
                        VoidType(),
                        Block(
                            [
                                VarDecl('largest',IntType()),
                                BinaryOp('=',Id('largest'),Id('i')),
                                VarDecl('l',IntType()),
                                BinaryOp('=',Id('l'),BinaryOp('+',BinaryOp('*',IntLiteral(2),Id('i')),IntLiteral(1))),
                                VarDecl('r',IntType()),
                                BinaryOp('=',Id('r'),BinaryOp('+',BinaryOp('*',IntLiteral(2),Id('i')),IntLiteral(2))),
                                If(
                                    BinaryOp(
                                        '&&',
                                        BinaryOp('<',Id('l'),Id('n')),
                                        BinaryOp('>',ArrayCell(Id('arr'),Id('l')),ArrayCell(Id('arr'),Id('largest')))
                                    ),
                                    BinaryOp('=',Id('largest'),Id('l'))
                                ),
                                If(
                                    BinaryOp(
                                        '&&',
                                        BinaryOp('<',Id('r'),Id('n')),
                                        BinaryOp('>',ArrayCell(Id('arr'),Id('r')),ArrayCell(Id('arr'),Id('largest')))
                                    ),
                                    BinaryOp('=',Id('largest'),Id('r'))
                                ),
                                If(
                                    BinaryOp('!=',Id('largest'),Id('i')),
                                    Block(
                                        [
                                            CallExpr(
                                                Id('swap'),
                                                [
                                                    ArrayCell(Id('arr'),Id('i')),
                                                    ArrayCell(Id('arr'),Id('largest'))
                                                ]),
                                            CallExpr(
                                                Id('heapify'),
                                                [
                                                    Id('arr'),Id('n'),Id('largest')
                                                ]
                                            )
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,357))
    
    def test_FreeTest_No58(self):
        """Free test"""
        input= """
        void heapSort(int arr[], int n) 
        { 
            int i;
            for (i = n / 2 - 1; i >= 0; i=i-1) 
                    heapify(arr, n, i); 
            for (i=n-1; i>=0; i=i-1) 
            { 
                swap(arr[0], arr[i]); 
                heapify(arr, i, 0); 
            } 
        } 
        """
        expect = str(
            Program(
                [
                    FuncDecl(Id('heapSort'),
                        [
                            VarDecl('arr',ArrayPointerType(IntType())),
                            VarDecl('n',IntType())
                        ],
                        VoidType(),
                        Block(
                            [
                                VarDecl('i',IntType()),
                                For(
                                    BinaryOp('=',Id('i'),BinaryOp('-',BinaryOp('/',Id('n'),IntLiteral(2)),IntLiteral(1))),
                                    BinaryOp('>=',Id('i'),IntLiteral(0)),
                                    BinaryOp('=',Id('i'),BinaryOp('-',Id('i'),IntLiteral(1))),
                                    CallExpr(
                                        Id('heapify'),
                                        [
                                            Id('arr'),Id('n'),Id('i')
                                        ]
                                    )
                                ),
                                For(
                                    BinaryOp('=',Id('i'),BinaryOp('-',Id('n'),IntLiteral(1))),
                                    BinaryOp('>=',Id('i'),IntLiteral(0)),
                                    BinaryOp('=',Id('i'),BinaryOp('-',Id('i'),IntLiteral(1))),
                                    Block(
                                        [
                                            CallExpr(
                                                Id('swap'),
                                                [
                                                    ArrayCell(Id('arr'),IntLiteral(0)),
                                                    ArrayCell(Id('arr'),Id('i'))
                                                ]
                                            ),
                                            CallExpr(
                                                Id('heapify'),
                                                [
                                                    Id('arr'),Id('i'),IntLiteral(0)
                                                ]
                                            )
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,358))
    
    def test_FreeTest_No59(self):
        """Free test"""
        input = """
        void insertionSort(int arr[], int n) 
        { 
            int i, key, j; 
            for (i = 1; i < n; i=i+1) { 
                key = arr[i]; 
                j = i - 1; 
  
            /* Move elements of arr[0..i-1], that are 
            greater than key, to one position ahead 
            of their current position */
                arr[j + 1] = key; 
            } 
        } 
        """
        expect = str(
            Program(
                [
                    FuncDecl(
                        Id('insertionSort'),
                        [
                            VarDecl('arr',ArrayPointerType(IntType())),
                            VarDecl('n',IntType())
                        ],
                        VoidType(),
                        Block(
                            [
                                VarDecl('i',IntType()),
                                VarDecl('key',IntType()),
                                VarDecl('j',IntType()),
                                For(
                                    BinaryOp('=',Id('i'),IntLiteral(1)),
                                    BinaryOp('<',Id('i'),Id('n')),
                                    BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
                                    Block(
                                        [
                                            BinaryOp('=',Id('key'),ArrayCell(Id('arr'),Id('i'))),
                                            BinaryOp('=',Id('j'),BinaryOp('-',Id('i'),IntLiteral(1))),
                                        
                                            BinaryOp('=',ArrayCell(Id('arr'),BinaryOp('+',Id('j'),IntLiteral(1))),Id('key'))
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_FreeTest_No60(self):
        """Free test"""
        input= """ 
        void printArray(int arr[], int n) 
        { 
            int i; 
            for (i = 0; i < n; i=i+1) 
                printf("%d ", arr[i]); 
            printf("\\n"); 
        } 
  
        int main() 
        { 
            int arr[5]; //= { 12, 11, 13, 5, 6 }; 

            int n; n= sizeof(arr) / sizeof(arr[0]); 
  
            insertionSort(arr, n); 
            printArray(arr, n); 
  
            return 0; 
        } 
        """
        expect = str(
            Program(
                [
                    FuncDecl(Id('printArray'),
                        [
                            VarDecl('arr',ArrayPointerType(IntType())),
                            VarDecl('n',IntType())
                        ],
                        VoidType(),
                        Block(
                            [
                                VarDecl('i',IntType()),
                                For(
                                    BinaryOp('=',Id('i'),IntLiteral(0)),
                                    BinaryOp('<',Id('i'),Id('n')),
                                    BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
                                    CallExpr(
                                        Id('printf'),
                                        [
                                            StringLiteral('%d '),
                                            ArrayCell(Id('arr'),Id('i'))
                                        ]
                                    )
                                ),
                                CallExpr(
                                    Id('printf'),
                                    [
                                        StringLiteral('\\n')
                                    ]
                                )
                            ]
                        )
                    ),
                    FuncDecl(Id('main'),
                        [],
                        IntType(),
                        Block(
                            [
                                VarDecl('arr',ArrayType(5,IntType())),
                                VarDecl('n',IntType()),
                                BinaryOp(
                                    '=',
                                    Id('n'),
                                    BinaryOp(
                                        '/',
                                        CallExpr(
                                            Id('sizeof'),
                                            [
                                                Id('arr')
                                            ]
                                        ),
                                        CallExpr(
                                            Id('sizeof'),
                                            [
                                                ArrayCell(Id('arr'),IntLiteral(0))
                                            ]
                                        )
                                    )
                                ),
                                CallExpr(
                                    Id('insertionSort'),
                                    [
                                        Id('arr'),Id('n')
                                    ]
                                ),
                                CallExpr(
                                    Id('printArray'),
                                    [
                                        Id('arr'),Id('n')
                                    ]
                                ),
                                Return(IntLiteral(0))
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,360))
    
    def test_FreeTest_No61(self):
        """Free test"""
        input = """
        /* function to sort arr using shellSort */
        int shellSort(int arr[], int n) 
        {   
            int gap,i,j,temp;
            for (gap = n/2; gap > 0; gap = gap/ 2) 
            { 
                for (i = gap; i < n; i =i+ 1) 
                { 
                    temp = arr[i];          
                    for (j = i; j >= gap && arr[j - gap] > temp; j =j- gap) 
                        arr[j] = arr[j - gap]; 
                    arr[j] = temp; 
                } 
            } 
            return 0; 
        } 
        """
        expect = str(
            Program(
                [
                    FuncDecl(
                        Id('shellSort'),
                        [
                            VarDecl('arr',ArrayPointerType(IntType())),
                            VarDecl('n',IntType())
                        ],
                        IntType(),
                        Block(
                            [
                                VarDecl('gap',IntType()),
                                VarDecl('i',IntType()),
                                VarDecl('j',IntType()),
                                VarDecl('temp',IntType()),
                                For(
                                    BinaryOp('=',Id('gap'),BinaryOp('/',Id('n'),IntLiteral(2))),
                                    BinaryOp('>',Id('gap'),IntLiteral(0)),
                                    BinaryOp('=',Id('gap'),BinaryOp('/',Id('gap'),IntLiteral(2))),
                                    Block(
                                        [
                                            For(
                                                BinaryOp('=',Id('i'),Id('gap')),
                                                BinaryOp('<',Id('i'),Id('n')),
                                                BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
                                                Block(
                                                    [
                                                        BinaryOp('=',Id('temp'),ArrayCell(Id('arr'),Id('i'))),
                                                        For(
                                                            BinaryOp('=',Id('j'),Id('i')),
                                                            BinaryOp(
                                                                '&&',
                                                                BinaryOp('>=',Id('j'),Id('gap')),
                                                                BinaryOp('>',ArrayCell(Id('arr'),BinaryOp('-',Id('j'),Id('gap'))),Id('temp'))
                                                            ),
                                                            BinaryOp('=',Id('j'),BinaryOp('-',Id('j'),Id('gap'))),
                                                            BinaryOp(
                                                                '=',
                                                                ArrayCell(Id('arr'),Id('j')),
                                                                ArrayCell(Id('arr'),BinaryOp('-',Id('j'),Id('gap')))
                                                            )
                                                        ),
                                                        BinaryOp(
                                                            '=',
                                                            ArrayCell(Id('arr'),Id('j')),
                                                            Id('temp')
                                                        )
                                                    ]
                                                )
                                            )
                                        ]
                                    )
                                ),
                                Return(IntLiteral(0))
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,361))
   
    def test_FreeTest_No62(self):
        """Free test"""
        input= """
        void merge(int arr[], int l, int m, int r) 
        { 
            int i, j, k; int n1 ;n1= m - l + 1; 
            int n2 ;n2=  r - m; 
  
            int L[100], R[100]; 
            for (i = 0; i < n1; i=i+1) L[i] = arr[l + i]; 
            for (j = 0; j < n2; j=j+1) R[j] = arr[m + 1+ j]; 
            i = 0; j = 0; k = l; 
            do
            { 
                if (L[i] <= R[j]) 
                { 
                    arr[k] = L[i]; 
                    i=i+1; 
                } 
                else
                { 
                    arr[k] = R[j]; 
                    j=j+1; 
                } 
                k=k+1; 
            } while (i < n1 && j < n2) ;
            do
            { 
                arr[k] = L[i]; 
                i=i+1; 
                k=k+1; 
            } while (i < n1) ;
            do
            { 
                arr[k] = R[j]; 
                j=j+1; 
                k=k+1; 
            } while (j < n2) ;
        } 
        """
        expect = str(
            Program(
                [
                    FuncDecl(
                        Id('merge'),
                        [
                            VarDecl('arr',ArrayPointerType(IntType())),
                            VarDecl('l',IntType()),
                            VarDecl('m',IntType()),
                            VarDecl('r',IntType())
                        ],
                        VoidType(),
                        Block(
                            [
                                VarDecl('i',IntType()),
                                VarDecl('j',IntType()),
                                VarDecl('k',IntType()),
                                VarDecl('n1',IntType()),
                                BinaryOp('=',Id('n1'),BinaryOp('+',BinaryOp('-',Id('m'),Id('l')),IntLiteral(1))),
                                VarDecl('n2',IntType()),
                                BinaryOp('=',Id('n2'),BinaryOp('-',Id('r'),Id('m'))),
                                VarDecl('L',ArrayType(100,IntType())),
                                VarDecl('R',ArrayType(100,IntType())),
                                For(
                                    BinaryOp('=',Id('i'),IntLiteral(0)),
                                    BinaryOp('<',Id('i'),Id('n1')),
                                    BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
                                    BinaryOp('=',ArrayCell(Id('L'),Id('i')),ArrayCell(Id('arr'),BinaryOp('+',Id('l'),Id('i'))))
                                ),
                                For(
                                    BinaryOp('=',Id('j'),IntLiteral(0)),
                                    BinaryOp('<',Id('j'),Id('n2')),
                                    BinaryOp('=',Id('j'),BinaryOp('+',Id('j'),IntLiteral(1))),
                                    BinaryOp(
                                        '=',
                                        ArrayCell(Id('R'),Id('j')),
                                        ArrayCell(Id('arr'),BinaryOp('+',BinaryOp('+',Id('m'),IntLiteral(1)),Id('j'))))
                                ),
                                BinaryOp('=',Id('i'),IntLiteral(0)),
                                BinaryOp('=',Id('j'),IntLiteral(0)),
                                BinaryOp('=',Id('k'),Id('l')),
                                Dowhile(
                                    [
                                        Block(
                                            [
                                                If(
                                                    BinaryOp(
                                                        '<=',
                                                        ArrayCell(Id('L'),Id('i')),
                                                        ArrayCell(Id('R'),Id('j'))
                                                    ),
                                                    Block(
                                                        [
                                                            BinaryOp(
                                                                '=',
                                                                ArrayCell(Id('arr'),Id('k')),
                                                                ArrayCell(Id('L'),Id('i'))
                                                            ),
                                                            BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1)))
                                                        ]
                                                    ),
                                                    Block(
                                                        [
                                                            BinaryOp('=',ArrayCell(Id('arr'),Id('k')),ArrayCell(Id('R'),Id('j'))),
                                                            BinaryOp('=',Id('j'),BinaryOp('+',Id('j'),IntLiteral(1)))
                                                        ]
                                                    )
                                                ),
                                                BinaryOp('=',Id('k'),BinaryOp('+',Id('k'),IntLiteral(1)))
                                            ]
                                        )
                                    ],
                                    BinaryOp(
                                        '&&',
                                        BinaryOp('<',Id('i'),Id('n1')),
                                        BinaryOp('<',Id('j'),Id('n2'))
                                    )
                                ),
                                Dowhile(
                                    [
                                        Block(
                                            [
                                                BinaryOp(
                                                    '=',
                                                    ArrayCell(Id('arr'),Id('k')),
                                                    ArrayCell(Id('L'),Id('i'))
                                                ),
                                                BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
                                                BinaryOp('=',Id('k'),BinaryOp('+',Id('k'),IntLiteral(1)))
                                            ]
                                        )
                                    ],
                                    BinaryOp('<',Id('i'),Id('n1'))
                                ),
                                Dowhile(
                                    [
                                        Block(
                                            [
                                                BinaryOp(
                                                    '=',
                                                    ArrayCell(Id('arr'),Id('k')),
                                                    ArrayCell(Id('R'),Id('j'))
                                                ),
                                                BinaryOp('=',Id('j'),BinaryOp('+',Id('j'),IntLiteral(1))),
                                                BinaryOp('=',Id('k'),BinaryOp('+',Id('k'),IntLiteral(1)))
                                            ]
                                        )
                                    ],
                                    BinaryOp('<',Id('j'),Id('n2'))
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,362))
    
    def test_FreeTest_No63(self):
        """Free test"""
        input = """
        void mergeSort(int arr[], int l, int r) 
        { 
            if (l < r) 
            { 
                int m ;m= l+(r-l)/2; 
                mergeSort(arr, l, m); 
                mergeSort(arr, m+1, r); 
  
                merge(arr, l, m, r); 
            } 
        } 
        """
        expect = str(
            Program(
                [
                    FuncDecl(
                        Id('mergeSort'),
                        [
                            VarDecl('arr',ArrayPointerType(IntType())),
                            VarDecl('l',IntType()),
                            VarDecl('r',IntType())
                        ],
                        VoidType(),
                        Block(
                            [
                                If(
                                    BinaryOp('<',Id('l'),Id('r')),
                                    Block(
                                        [
                                            VarDecl('m',IntType()),
                                            BinaryOp(
                                                '=',
                                                Id('m'),
                                                BinaryOp(
                                                    '+',
                                                    Id('l'),
                                                    BinaryOp(
                                                        '/',
                                                        BinaryOp('-',Id('r'),Id('l')),
                                                        IntLiteral(2)
                                                    )
                                                )
                                            ),
                                            CallExpr(
                                                Id('mergeSort'),
                                                [
                                                    Id('arr'),Id('l'),Id('m')
                                                ]
                                            ),
                                            CallExpr(
                                                Id('mergeSort'),
                                                [
                                                    Id('arr'),
                                                    BinaryOp('+',Id('m'),IntLiteral(1)),
                                                    Id('r')
                                                ]
                                            ),
                                            CallExpr(
                                                Id('merge'),
                                                [
                                                    Id('arr'),Id('l'),Id('m'),Id('r')
                                                ]
                                            )
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,363))
    
    def test_FreeTest_No64(self):
        """Free test"""
        input= """
        int partition (int arr[], int low, int high) 
        { 
            int pivot ;pivot= arr[high];    // pivot 
            int i;i = (low - 1);  // Index of smaller element 
            int j;
            for (j = low; j <= high- 1; j=j+1) 
            { 
                // If current element is smaller than the pivot 
                if (arr[j] < pivot) 
                { 
                     i = i + 1;    // increment index of smaller element 
                    swap(arr[i], arr[j]); 
                } 
            } 
            swap(arr[i + 1], arr[high]); 
            return (i + 1); 
        } 
        """
        expect = str(
            Program(
                [
                    FuncDecl(
                        Id('partition'),
                        [
                            VarDecl('arr',ArrayPointerType(IntType())),
                            VarDecl('low',IntType()),
                            VarDecl('high',IntType())
                        ],
                        IntType(),
                        Block(
                            [
                                VarDecl('pivot',IntType()),
                                BinaryOp('=',Id('pivot'),ArrayCell(Id('arr'),Id('high'))),
                                VarDecl('i',IntType()),
                                BinaryOp('=',Id('i'),BinaryOp('-',Id('low'),IntLiteral(1))),
                                VarDecl('j',IntType()),
                                For(
                                    BinaryOp('=',Id('j'),Id('low')),
                                    BinaryOp('<=',Id('j'),BinaryOp('-',Id('high'),IntLiteral(1))),
                                    BinaryOp('=',Id('j'),BinaryOp('+',Id('j'),IntLiteral(1))),
                                    Block(
                                        [
                                            If(
                                                BinaryOp('<',ArrayCell(Id('arr'),Id('j')),Id('pivot')),
                                                Block(
                                                    [
                                                        BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
                                                        CallExpr(
                                                            Id('swap'),
                                                            [
                                                                ArrayCell(Id('arr'),Id('i')),
                                                                ArrayCell(Id('arr'),Id('j'))
                                                            ]
                                                        )
                                                    ]
                                                )
                                            )
                                        ]
                                    )
                                ),
                                CallExpr(
                                    Id('swap'),
                                    [
                                        ArrayCell(Id('arr'),BinaryOp('+',Id('i'),IntLiteral(1))),
                                        ArrayCell(Id('arr'),Id('high'))
                                    ]
                                ),
                                Return(BinaryOp('+',Id('i'),IntLiteral(1)))
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,364))
    
    def test_FreeTest_No65(self):
        """Free test"""
        input = """
        void quickSort(int arr[], int low, int high) 
        { 
            if (low < high) 
            { 
                int pi ;pi= partition(arr, low, high); 
  
        
                quickSort(arr, low, pi - 1); 
                quickSort(arr, pi + 1, high); 
            } 
        } 
        """
        expect = str(
            Program(
                [
                    FuncDecl(
                        Id('quickSort'),
                        [
                            VarDecl('arr',ArrayPointerType(IntType())),
                            VarDecl('low',IntType()),
                            VarDecl('high',IntType())
                        ],
                        VoidType(),
                        Block(
                            [
                                If(
                                    BinaryOp('<',Id('low'),Id('high')),
                                    Block(
                                        [
                                            VarDecl('pi',IntType()),
                                            BinaryOp(
                                                '=',
                                                Id('pi'),
                                                CallExpr(
                                                    Id('partition'),
                                                    [
                                                        Id('arr'),Id('low'),Id('high')
                                                    ]
                                                )
                                            ),
                                            CallExpr(
                                                Id('quickSort'),
                                                [
                                                    Id('arr'),Id('low'),
                                                    BinaryOp('-',Id('pi'),IntLiteral(1))
                                                ]
                                            ),
                                            CallExpr(
                                                Id('quickSort'),
                                                [
                                                    Id('arr'),
                                                    BinaryOp('+',Id('pi'),IntLiteral(1)),
                                                    Id('high')
                                                ]
                                            )
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,365))

    def test_FreeTest_No66(self):
        """Free test"""
        input = """
        int binarySearch(int arr[], int l, int r, int x) 
        { 
            if (r >= l) { 
                int mid ;
                mid= l + (r - l) / 2; 
                if (arr[mid] == x) return mid; 
                if (arr[mid] > x)  return binarySearch(arr, l, mid - 1, x); 
                return binarySearch(arr, mid + 1, r, x); 
            } 
            return -1; 
        } 
        """
        expect = str(
            Program(
                [
                    FuncDecl(
                        Id('binarySearch'),
                        [
                            VarDecl('arr',ArrayPointerType(IntType())),
                            VarDecl('l',IntType()),
                            VarDecl('r',IntType()),
                            VarDecl('x',IntType())
                        ],
                        IntType(),
                        Block(
                            [
                                If(
                                    BinaryOp('>=',Id('r'),Id('l')),
                                    Block(
                                        [
                                            VarDecl('mid',IntType()),
                                            BinaryOp(
                                                '=',
                                                Id('mid'),
                                                BinaryOp(
                                                    '+',
                                                    Id('l'),
                                                    BinaryOp(
                                                        '/',
                                                        BinaryOp('-',Id('r'),Id('l')),
                                                        IntLiteral(2)
                                                    )
                                                )
                                            ),
                                            If(
                                                BinaryOp(
                                                    '==',
                                                    ArrayCell(Id('arr'),Id('mid')),
                                                    Id('x')
                                                ),
                                                Return(Id('mid'))
                                            ),
                                            If(
                                                BinaryOp('>',ArrayCell(Id('arr'),Id('mid')),Id('x')),
                                                Return(
                                                    CallExpr(
                                                        Id('binarySearch'),
                                                        [
                                                            Id('arr'),Id('l'),BinaryOp('-',Id('mid'),IntLiteral(1)),
                                                            Id('x')
                                                        ]
                                                    )
                                                )
                                            ),
                                            Return(
                                                CallExpr(
                                                    Id('binarySearch'),
                                                    [
                                                        Id('arr'),
                                                        BinaryOp('+',Id('mid'),IntLiteral(1)),
                                                        Id('r'),Id('x')
                                                    ]
                                                )
                                            )
                                        ]
                                    )
                                ),
                                Return(UnaryOp('-',IntLiteral(1)))
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,366))
    
    def test_FreeTest_No67(self):
        """Free test"""
        input= """
        int parent(int i) { return (i-1)/2; } 
	    int left(int i) { return (2*i + 1); } 
	    int right(int i) { return (2*i + 2); } 
	    int getMin() { return harr[0]; }    
        void insertKey(int k) 
        { 
	        if (heap_size == capacity) return; 

	        heap_size=heap_size+1; 
	        int i ;i= heap_size - 1; 
	        harr[i] = k; 

	        do
	        { 
	            swap(harr[i], harr[parent(i)]); 
	            i = parent(i); 
	        } while(i != 0 && harr[parent(i)] > harr[i]) ;
        } 
        """
        expect = str(
            Program(
                [
                    FuncDecl(
                        Id('parent'),
                        [
                            VarDecl('i',IntType())
                        ],
                        IntType(),
                        Block(
                            [
                                Return(BinaryOp('/',BinaryOp('-',Id('i'),IntLiteral(1)),IntLiteral(2)))
                            ]
                        )
                    ),
                    
                    FuncDecl(
                        Id('left'),
                        [
                            VarDecl('i',IntType())
                        ],
                        IntType(),
                        Block(
                            [
                                Return(BinaryOp('+',BinaryOp('*',IntLiteral(2),Id('i')),IntLiteral(1)))
                            ]
                        )
                    ),
                    
                    FuncDecl(
                        Id('right'),
                        [
                            VarDecl('i',IntType())
                        ],
                        IntType(),
                        Block(
                            [
                                Return(BinaryOp('+',BinaryOp('*',IntLiteral(2),Id('i')),IntLiteral(2)))
                            ]
                        )
                    ),
                    
                    FuncDecl(
                        Id('getMin'),
                        [],
                        IntType(),
                        Block(
                            [
                                Return(ArrayCell(Id('harr'),IntLiteral(0)))
                            ]
                        )
                    ),
                    
                    FuncDecl(
                        Id('insertKey'),
                        [
                            VarDecl('k',IntType())
                        ],
                        VoidType(),
                        Block(
                            [
                                If(
                                    BinaryOp('==',Id('heap_size'),Id('capacity')),
                                    Return()
                                ),
                                BinaryOp('=',Id('heap_size'),BinaryOp('+',Id('heap_size'),IntLiteral(1))),
                                VarDecl('i',IntType()),
                                BinaryOp('=',Id('i'),BinaryOp('-',Id('heap_size'),IntLiteral(1))),
                                BinaryOp('=',ArrayCell(Id('harr'),Id('i')),Id('k')),
                                Dowhile(
                                    [
                                        Block(
                                            [
                                                CallExpr(
                                                    Id('swap'),
                                                    [
                                                        ArrayCell(Id('harr'),Id('i')),
                                                        ArrayCell(Id('harr'),CallExpr(Id('parent'),[Id('i')]))
                                                    ]
                                                ),
                                                BinaryOp('=',Id('i'),CallExpr(Id('parent'),[Id('i')]))
                                            ]
                                        )
                                    ],
                                    BinaryOp(
                                        '&&',
                                        BinaryOp('!=',Id('i'),IntLiteral(0)),
                                        BinaryOp(
                                            '>',
                                            ArrayCell(Id('harr'),
                                                CallExpr(
                                                    Id('parent'),
                                                    [
                                                        Id('i')
                                                    ]
                                                )
                                            ),
                                            ArrayCell(Id('harr'),Id('i'))))
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def test_FreeTest_No68(self):
        """Free test"""
        input = """
        void decreaseKey(int i, int new_val) 
        { 
	        harr[i] = new_val; 
	        do
	        { 
	            swap(harr[i], harr[parent(i)]); 
	            i = parent(i); 
	        } while (i != 0 && harr[parent(i)] > harr[i]) ;
        } 
        """
        expect = str(
            Program(
                [
                    FuncDecl(
                        Id('decreaseKey'),
                        [
                            VarDecl('i',IntType()),
                            VarDecl('new_val',IntType())
                        ],
                        VoidType(),
                        Block(
                            [
                                BinaryOp('=',ArrayCell(Id('harr'),Id('i')),Id('new_val')),
                                

                                Dowhile(
                                    [
                                        Block(
                                            [
                                                CallExpr(
                                                    Id('swap'),
                                                    [
                                                        ArrayCell(Id('harr'),Id('i')),
                                                        ArrayCell(Id('harr'),CallExpr(Id('parent'),[Id('i')]))
                                                    ]
                                                ),
                                                BinaryOp('=',Id('i'),CallExpr(Id('parent'),[Id('i')]))
                                            ]
                                        )
                                    ],
                                    BinaryOp(
                                        '&&',
                                        BinaryOp('!=',Id('i'),IntLiteral(0)),
                                        BinaryOp(
                                            '>',
                                            ArrayCell(Id('harr'),CallExpr(Id('parent'),[Id('i')])),
                                            ArrayCell(Id('harr'),Id('i'))
                                        )
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,368))
    
    def test_FreeTest_No69(self):
        """Free test"""
        input= """
        int extractMin() 
        { 
	        if (heap_size <= 0) 
		            return INT_MAX; 
	        if (heap_size == 1) 
	        { 
		        heap_size=heap_size-1; 
		        return harr[0]; 
	        } 

	        int root ;root= harr[0]; 
	        harr[0] = harr[heap_size-1]; 
	        heap_size=heap_size-1; 
	        MinHeapify(0); 

	        return root; 
        } 
        """
        expect = str(
            Program(
                [
                    FuncDecl(
                        Id('extractMin'),
                        [],
                        IntType(),
                        Block(
                            [
                                If(
                                    BinaryOp('<=',Id('heap_size'),IntLiteral(0)),
                                    Return(Id('INT_MAX'))
                                ),
                                
                                If(
                                    BinaryOp('==',Id('heap_size'),IntLiteral(1)),
                                    Block(
                                        [
                                            BinaryOp('=',Id('heap_size'),BinaryOp('-',Id('heap_size'),IntLiteral(1))),
                                            Return(ArrayCell(Id('harr'),IntLiteral(0)))
                                        ]
                                    )
                                ),
                                VarDecl('root',IntType()),
                                BinaryOp(
                                    '=',
                                    Id('root'),
                                    ArrayCell(Id('harr'),IntLiteral(0))
                                ),
                                BinaryOp(
                                    '=',
                                    ArrayCell(Id('harr'),IntLiteral(0)),
                                    ArrayCell(Id('harr'),BinaryOp('-',Id('heap_size'),IntLiteral(1)))
                                ),
                                BinaryOp(
                                    '=',
                                    Id('heap_size'),
                                    BinaryOp('-',Id('heap_size'),IntLiteral(1))
                                ),
                                CallExpr(Id('MinHeapify'),[IntLiteral(0)]),
                                Return(Id('root'))
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test_FreeTest_No70(self):
        """Free test"""
        input = """
    
        void deleteKey(int i) 
        { 
	        decreaseKey(i, INT_MIN); 
	        extractMin(); 
        } 
        void MinHeapify(int i) 
        { 
	        int l ;l= left(i); 
	        int r ;r= right(i); 
	        int smallest ;smallest= i; 
	        if (l < heap_size && harr[l] < harr[i]) smallest = l; 
	        if (r < heap_size && harr[r] < harr[smallest]) smallest = r; 
	        if (smallest != i) 
	        { 
		        swap(harr[i], harr[smallest]); 
		        MinHeapify(smallest); 
	        } 
        } 
        """
        expect = str(
            Program(
                [
                    FuncDecl(
                        Id('deleteKey'),
                        [
                            VarDecl('i',IntType())
                        ],
                        VoidType(),
                        Block(
                            [
                                CallExpr(Id('decreaseKey'),[Id('i'),Id('INT_MIN')]),
                                CallExpr(Id('extractMin'),[])
                            ]
                        )
                    ),
                    
                    FuncDecl(
                        Id('MinHeapify'),
                        [
                            VarDecl('i',IntType())
                        ],
                        VoidType(),
                        Block(
                            [
                                VarDecl('l',IntType()),
                                BinaryOp('=',Id('l'),CallExpr(Id('left'),[Id('i')])),
                                VarDecl('r',IntType()),BinaryOp('=',Id('r'),CallExpr(Id('right'),[Id('i')])),
                                VarDecl('smallest',IntType()),
                                BinaryOp('=',Id('smallest'),Id('i')),
                                If(
                                    BinaryOp(
                                        '&&',
                                        BinaryOp('<',Id('l'),Id('heap_size')),
                                        BinaryOp('<',ArrayCell(Id('harr'),Id('l')),ArrayCell(Id('harr'),Id('i')))
                                    ),
                                    BinaryOp('=',Id('smallest'),Id('l'))
                                ),

                                If(
                                    BinaryOp(
                                        '&&',
                                        BinaryOp('<',Id('r'),Id('heap_size')),
                                        BinaryOp('<',ArrayCell(Id('harr'),Id('r')),ArrayCell(Id('harr'),Id('smallest')))
                                    ),
                                    BinaryOp('=',Id('smallest'),Id('r'))
                                ),
                                
                                If(
                                    BinaryOp('!=',Id('smallest'),Id('i')),
                                    Block(
                                        [
                                            CallExpr(
                                                Id('swap'),
                                                [
                                                    ArrayCell(Id('harr'),Id('i')),
                                                    ArrayCell(Id('harr'),Id('smallest'))
                                                ]
                                            ),
                                            CallExpr(
                                                Id('MinHeapify'),
                                                [
                                                    Id('smallest')
                                                ]
                                            )
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,370))
    
    def test_FreeTest_No71(self):
        """Free test"""
        input= """
        int fib(int n) 
        { 
            int f[100000];   
            int i; 
            f[0] = 0; f[1] = 1; 
  
            for (i = 2; i <= n; i = i + 1) f[i] = f[i-1] + f[i-2]; 
            return f[n]; 
        } 
        """
        expect = str(
            Program(
                [
                    FuncDecl(
                        Id('fib'),
                        [
                            VarDecl('n',IntType())
                        ],
                        IntType(),
                        Block(
                            [
                                VarDecl('f',ArrayType(100000,IntType())),
                                VarDecl('i',IntType()),
                                BinaryOp('=',ArrayCell(Id('f'),IntLiteral(0)),IntLiteral(0)),
                                BinaryOp('=',ArrayCell(Id('f'),IntLiteral(1)),IntLiteral(1)),
                                For(
                                    BinaryOp('=',Id('i'),IntLiteral(2)),
                                    BinaryOp('<=',Id('i'),Id('n')),
                                    BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
                                    BinaryOp(
                                        '=',
                                        ArrayCell(Id('f'),Id('i')),
                                        BinaryOp(
                                            '+',
                                            ArrayCell(Id('f'),BinaryOp('-',Id('i'),IntLiteral(1))),
                                            ArrayCell(Id('f'),BinaryOp('-',Id('i'),IntLiteral(2)))
                                        )
                                    )
                                ),
                                Return(ArrayCell(Id('f'),Id('n')))
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_FreeTest_No72(self):
        """Free test"""
        input= """
        int fib(int n) 
        { 
            int a, b, c, i; a=0;b=1;
            if( n == 0) return a; 
            for (i = 2; i <= n; i = i + 1) 
            { 
                c = a + b; 
                a = b; 
                b = c; 
            } 
            return b; 
        } 
        """
        expect = str(
            Program(
                [
                    FuncDecl(
                        Id('fib'),
                        [
                            VarDecl('n',IntType())
                        ],
                        IntType(),
                        Block(
                            [
                                VarDecl('a',IntType()),
                                VarDecl('b',IntType()),
                                VarDecl('c',IntType()),
                                VarDecl('i',IntType()),
                                BinaryOp('=',Id('a'),IntLiteral(0)),
                                BinaryOp('=',Id('b'),IntLiteral(1)),
                                If(
                                    BinaryOp('==',Id('n'),IntLiteral(0)),
                                    Return(Id('a'))
                                ),
                                For(
                                    BinaryOp('=',Id('i'),IntLiteral(2)),
                                    BinaryOp('<=',Id('i'),Id('n')),
                                    BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
                                    Block(
                                        [
                                            BinaryOp('=',Id('c'),BinaryOp('+',Id('a'),Id('b'))),
                                            BinaryOp('=',Id('a'),Id('b')),
                                            BinaryOp('=',Id('b'),Id('c'))
                                        ]
                                    )
                                ),
                                Return(Id('b'))
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

    def test_FreeTest_No73(self):
        """Free test"""
        input= """
        int catalan(int n) 
        { 
            if (n <= 1) return 1; 
            int res;res= 0;
            int i; 
            for (i=0; i<n; i = i + 1) 
                res =res+ catalan(i)*catalan(n-i-1); 
            return res; 
        } 
        """
        expect = str(
            Program(
                [
                    FuncDecl(
                        Id('catalan'),
                        [
                            VarDecl('n',IntType())
                        ],
                        IntType(),
                        Block(
                            [
                                If(
                                    BinaryOp('<=',Id('n'),IntLiteral(1)),
                                    Return(IntLiteral(1))
                                ),
                                VarDecl('res',IntType()),
                                BinaryOp('=',Id('res'),IntLiteral(0)),
                                VarDecl('i',IntType()),
                                For(
                                    BinaryOp('=',Id('i'),IntLiteral(0)),
                                    BinaryOp('<',Id('i'),Id('n')),
                                    BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
                                    BinaryOp(
                                        '=',
                                        Id('res'),
                                        BinaryOp(
                                            '+',
                                            Id('res'),
                                            BinaryOp(
                                                '*',
                                                CallExpr(
                                                    Id('catalan'),
                                                    [
                                                        Id('i')
                                                    ]
                                                ),
                                                CallExpr(
                                                    Id('catalan'),
                                                    [
                                                        BinaryOp('-',BinaryOp('-',Id('n'),Id('i')),
                                                        IntLiteral(1))
                                                    ]
                                                )
                                            )
                                        )
                                    )
                                ),
                                Return(Id('res'))
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_FreeTest_No74(self):
        """Free test"""
        input= """
        int numberDays(int month,int year)
        { 

            if (year> MAX_YR || year < MIN_YR)  return 0;
	        if (month< 1 || month > 12) return 0;
            if (month == 2)
            {
                if (IsLeapYear(year)) return (29);
                else
                    return (28);
            }
	        else if (month == 4 || month == 6 || month == 9 || month== 11)
                        return (30);
		
            return 31;
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl(
                        Id('numberDays'),
                        [
                            VarDecl('month',IntType()),
                            VarDecl('year',IntType())
                        ],
                        IntType(),
                        Block(
                            [
                                If(
                                    BinaryOp(
                                        '||',
                                        BinaryOp('>',Id('year'),Id('MAX_YR')),
                                        BinaryOp('<',Id('year'),Id('MIN_YR'))
                                    ),
                                    Return(IntLiteral(0))
                                ),
                                
                                If(
                                    BinaryOp(
                                        '||',
                                        BinaryOp('<',Id('month'),IntLiteral(1)),
                                        BinaryOp('>',Id('month'),IntLiteral(12))
                                    ),
                                    Return(IntLiteral(0))
                                ),
                                
                                If(
                                    BinaryOp('==',Id('month'),IntLiteral(2)),
                                    Block(
                                        [
                                            If(
                                                CallExpr(Id('IsLeapYear'),[Id('year')]),
                                                Return(IntLiteral(29)),
                                                Return(IntLiteral(28))
                                            )
                                        ]
                                    ),
                                    
                                    If(
                                        BinaryOp(
                                            '||',
                                            BinaryOp(
                                                '||',
                                                BinaryOp(
                                                    '||',
                                                    BinaryOp('==',Id('month'),IntLiteral(4)),
                                                    BinaryOp('==',Id('month'),IntLiteral(6))
                                                ),
                                                BinaryOp('==',Id('month'),IntLiteral(9))
                                            ),
                                            BinaryOp('==',Id('month'),IntLiteral(11))
                                        ),
                                        Return(IntLiteral(30))
                                    )
                                ),
                                Return(IntLiteral(31))
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    def test_FreeTest_No75(self):
        """Free test"""
        input= """
        int  IsLeapYear(int year) 
        {
            return (((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0));
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl(
                        Id('IsLeapYear'),
                        [
                            VarDecl('year',IntType())
                        ],
                        IntType(),
                        Block(
                            [
                                Return(
                                    BinaryOp(
                                        '||',
                                        BinaryOp(
                                            '&&',
                                            BinaryOp(
                                                '==',
                                                BinaryOp('%',Id('year'),IntLiteral(4)),
                                                IntLiteral(0)
                                            ),
                                            BinaryOp(
                                                '!=',
                                                BinaryOp('%',Id('year'),IntLiteral(100)),
                                                IntLiteral(0)
                                            )
                                        ),
                                        BinaryOp(
                                            '==',
                                            BinaryOp('%',Id('year'),IntLiteral(400)),
                                            IntLiteral(0)
                                        )
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,375))

    def test_FreeTest_No76(self):
        """Free test"""
        input= """
        // Function to find the root 
        void newtonRaphson(float x) 
        { 
            float h ;
            h = func(x) / derivFunc(x); 
            do
            { 
                h = func(x)/derivFunc(x); 
                x = x - h; 
            } while (abs(h) >= EPSILON);
  
            print("The value of the root is : ",x); 
        } 
        """
        expect = str(
            Program(
                [
                    FuncDecl(
                        Id('newtonRaphson'),
                        [
                            VarDecl('x',FloatType())
                        ],
                        VoidType(),
                        Block(
                            [
                                VarDecl('h',FloatType()),
                                BinaryOp(
                                    '=',
                                    Id('h'),
                                    BinaryOp(
                                        '/',
                                        CallExpr(
                                            Id('func'),
                                            [
                                                Id('x')
                                            ]
                                        ),
                                        CallExpr(
                                            Id('derivFunc'),
                                            [
                                                Id('x')
                                            ]
                                        )
                                    )
                                ),
                                Dowhile(
                                    [
                                        Block(
                                            [
                                                BinaryOp(
                                                    '=',
                                                    Id('h'),
                                                    BinaryOp(
                                                        '/',
                                                        CallExpr(
                                                            Id('func'),
                                                            [
                                                                Id('x')
                                                            ]
                                                        ),
                                                        CallExpr(
                                                            Id('derivFunc'),
                                                            [
                                                                Id('x')
                                                            ]
                                                        )
                                                    )
                                                ),
                                                BinaryOp('=',Id('x'),BinaryOp('-',Id('x'),Id('h')))
                                            ]
                                        )
                                    ],
                                    BinaryOp(
                                        '>=',
                                        CallExpr(
                                            Id('abs'),
                                            [
                                                Id('h')
                                            ]
                                        ),
                                        Id('EPSILON')
                                    )
                                ),
                                CallExpr(
                                    Id('print'),
                                    [
                                        StringLiteral('The value of the root is : '),
                                        Id('x')
                                    ]
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,376))

    def test_FreeTest_No77(self):
        """Free test"""
        input= """
        int main()
        {
  
            int year ;year = 0; 
            int month ;month= 0;
            int ret ;ret= 0; 
            printf("\\n Enter the year: = "); scanf("%d",year);
            printf("\\n Enter the month: = ");scanf("%d",month);
            ret = numberDays(month,year); 
            if(0 == ret)
            {
  	            printf("\\n Enter valid month and year");
  	            return 0;
            }
  
            printf("\\n Number of days  = %d",ret);	
            return 0;
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl(
                        Id('main'),
                        [],
                        IntType(),
                        Block(
                            [
                                VarDecl('year',IntType()),
                                BinaryOp('=',Id('year'),IntLiteral(0)),
                                VarDecl('month',IntType()),
                                BinaryOp('=',Id('month'),IntLiteral(0)),
                                VarDecl('ret',IntType()),
                                BinaryOp('=',Id('ret'),IntLiteral(0)),
                                
                                CallExpr(
                                    Id('printf'),
                                    [
                                        StringLiteral('\\n Enter the year: = ')
                                    ]
                                ),
                                
                                CallExpr(Id('scanf'),[StringLiteral('%d'),Id('year')]),
                                CallExpr(
                                    Id('printf'),
                                    [
                                        StringLiteral('\\n Enter the month: = ')
                                    ]
                                ),
                                CallExpr(Id('scanf'),[StringLiteral('%d'),Id('month')]),
                                
                                BinaryOp('=',Id('ret'),CallExpr(Id('numberDays'),[Id('month'),Id('year')])),
                                If(
                                    BinaryOp('==',IntLiteral(0),Id('ret')),
                                    Block(
                                        [
                                            CallExpr(
                                                Id('printf'),
                                                [
                                                    StringLiteral('\\n Enter valid month and year')
                                                ]
                                            ),
                                            Return(IntLiteral(0))
                                        ]
                                    )
                                ),
                                CallExpr(
                                    Id('printf'),
                                    [
                                        StringLiteral('\\n Number of days  = %d'),Id('ret')
                                    ]
                                ),
                                Return(IntLiteral(0))
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,377))
 
    def test_FreeTest_No78(self):
        """Free test"""
        input = """
        int a;
        float b;
        string c;
        boolean d(){}
        int e(float f[]) {}
        string[] g(boolean h[]){}
        int i(float j[]){}
        int k;
        float l;
        string m;
        boolean n;
        int[] o(float p, string q[], boolean r){}
        int   s(string t[], boolean u[], float v){}
        float w(int x, string y[], boolean z){}"""
        expect = str(
            Program(
                [
                    VarDecl('a',IntType()),
                    VarDecl('b',FloatType()),
                    VarDecl('c',StringType()),
                    FuncDecl(
                        Id('d'),
                        [],
                        BoolType(),
                        Block([])
                    ),
                    FuncDecl(
                        Id('e'),
                        [
                            VarDecl('f',ArrayPointerType(FloatType()))
                        ],
                        IntType(),
                        Block([])
                    ),
                    FuncDecl(
                        Id('g'),
                        [
                            VarDecl('h',ArrayPointerType(BoolType()))
                        ],
                        ArrayPointerType(StringType()),
                        Block([])
                    ),
                    FuncDecl(
                        Id('i'),
                        [
                            VarDecl('j',ArrayPointerType(FloatType()))
                        ],
                        IntType(),
                        Block([])
                    ),
                    VarDecl('k',IntType()),
                    VarDecl('l',FloatType()),
                    VarDecl('m',StringType()),
                    VarDecl('n',BoolType()),
                    FuncDecl(
                        Id('o'),
                        [
                            VarDecl('p',FloatType()),
                            VarDecl('q',ArrayPointerType(StringType())),
                            VarDecl('r',BoolType())
                        ],
                        ArrayPointerType(IntType()),
                        Block([])
                    ),
                    FuncDecl(
                        Id('s'),
                        [
                            VarDecl('t',ArrayPointerType(StringType())),
                            VarDecl('u',ArrayPointerType(BoolType())),
                            VarDecl('v',FloatType())
                        ],
                        IntType(),
                        Block([])
                    ),
                    FuncDecl(
                        Id('w'),
                        [
                            VarDecl('x',IntType()),
                            VarDecl('y',ArrayPointerType(StringType())),
                            VarDecl('z',BoolType())
                        ],
                        FloatType(),Block([])
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,378))

    def test_FreeTest_No79(self):
        """Free test"""
        input= """
        int main()
        {
            int x, y;
 
            scanf("%d%d", x, y);
 
            printf("x = %d\\ny = %d\\n", x, y);
 
            x = xor(x,y);
            y = xor(x,y);
            x = xor(x,y);
 
 
            printf("x = %d\\ny = %d\\n", x, y);
 
            return 0;
        }
        """
        expect = str(\
            Program(
                [
                    FuncDecl(
                        Id('main'),
                        [],
                        IntType(),
                        Block(
                            [
                                VarDecl('x',IntType()),
                                VarDecl('y',IntType()),
                                CallExpr(
                                    Id('scanf'),
                                    [
                                        StringLiteral('%d%d'),
                                        Id('x'),Id('y')
                                    ]
                                ),
                                CallExpr(
                                    Id('printf'),
                                    [
                                        StringLiteral('x = %d\\ny = %d\\n'),
                                        Id('x'),Id('y')
                                    ]
                                ),
                                BinaryOp(
                                    '=',
                                    Id('x'),
                                    CallExpr(
                                        Id('xor'),
                                        [
                                            Id('x'),Id('y')
                                        ]
                                    )
                                ),
                                BinaryOp(
                                    '=',
                                    Id('y'),
                                    CallExpr(
                                        Id('xor'),
                                        [
                                            Id('x'),Id('y')
                                        ]
                                    )
                                ),
                                BinaryOp(
                                    '=',
                                    Id('x'),
                                    CallExpr(
                                        Id('xor'),
                                        [
                                            Id('x'),Id('y')
                                        ]
                                    )
                                ),
                                CallExpr(
                                    Id('printf'),
                                    [
                                        StringLiteral('x = %d\\ny = %d\\n'),
                                        Id('x'),Id('y')
                                    ]
                                ),
                                Return(IntLiteral(0))
                            ]
                        )
                    )
                ]
            )    
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,379))
    
    def test_FreeTest_No80(self):
        """Free test"""
        input = """
        int main()
        {
            int a, b;
   
            printf("Input two integers (a & b) to swap\\n");
            scanf("%d%d", a, b);
   
            a = a + b;
            b = a - b;
            a = a - b;
 
            printf("a = %d\\nb = %d\\n",a,b);
            return 0;
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl(
                        Id('main'),
                        [],
                        IntType(),
                        Block(
                            [
                                VarDecl('a',IntType()),
                                VarDecl('b',IntType()),
                                CallExpr(
                                    Id('printf'),
                                    [
                                        StringLiteral('Input two integers (a & b) to swap\\n')
                                    ]
                                ),
                                CallExpr(
                                    Id('scanf'),
                                    [
                                        StringLiteral('%d%d'),Id('a'),Id('b')
                                    ]
                                ),
                                BinaryOp('=',Id('a'),BinaryOp('+',Id('a'),Id('b'))),
                                BinaryOp('=',Id('b'),BinaryOp('-',Id('a'),Id('b'))),
                                BinaryOp('=',Id('a'),BinaryOp('-',Id('a'),Id('b'))),
                                CallExpr(
                                    Id('printf'),
                                    [
                                        StringLiteral('a = %d\\nb = %d\\n'),
                                        Id('a'),Id('b')
                                    ]
                                ),
                                Return(IntLiteral(0))
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,380))

    def test_FreeTest_No81(self):
        """Free test"""
        input = """
        int main()
        {
            int array[100], n, c, d, swap;
 
            printf("Enter number of elements\\n");
            scanf("%d", n);
 
            printf("Enter %d integers\\n", n);
 
            for (c = 0; c < n; c= c +1)
            scanf("%d", array[c]);
 
            for (c = 0 ; c < n - 1; c= c + 1)
            {
                for (d = 0 ; d < n - c - 1; d=d+1)
                {
                    if (array[d] > array[d+1]) /* For decreasing order use < */
                    {
                        swap       = array[d];
                        array[d]   = array[d+1];
                        array[d+1] = swap;
                    }
                }
            }
 
            printf("Sorted list in ascending order:\\n");
 
            for (c = 0; c < n; c=c+1)
                 printf("%d\\n", array[c]);
 
             return 0;
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl(
                        Id('main'),
                        [],
                        IntType(),
                        Block(
                            [
                                VarDecl('array',ArrayType(100,IntType())),
                                VarDecl('n',IntType()),
                                VarDecl('c',IntType()),
                                VarDecl('d',IntType()),
                                VarDecl('swap',IntType()),
                                CallExpr(
                                    Id('printf'),
                                    [
                                        StringLiteral('Enter number of elements\\n')
                                    ]
                                ),
                                CallExpr(
                                    Id('scanf'),
                                    [
                                        StringLiteral('%d'),Id('n')
                                    ]
                                ),
                                CallExpr(
                                    Id('printf'),
                                    [
                                        StringLiteral('Enter %d integers\\n'),
                                        Id('n')
                                    ]
                                ),
                                For(
                                    BinaryOp('=',Id('c'),IntLiteral(0)),
                                    BinaryOp('<',Id('c'),Id('n')),
                                    BinaryOp('=',Id('c'),BinaryOp('+',Id('c'),IntLiteral(1))),
                                    CallExpr(
                                        Id('scanf'),
                                        [
                                            StringLiteral('%d'),ArrayCell(Id('array'),Id('c'))
                                        ]
                                    )
                                ),
                                For(
                                    BinaryOp('=',Id('c'),IntLiteral(0)),
                                    BinaryOp('<',Id('c'),BinaryOp('-',Id('n'),IntLiteral(1))),
                                    BinaryOp('=',Id('c'),BinaryOp('+',Id('c'),IntLiteral(1))),
                                    Block(
                                        [
                                            For(
                                                BinaryOp('=',Id('d'),IntLiteral(0)),
                                                BinaryOp('<',Id('d'),BinaryOp('-',BinaryOp('-',Id('n'),Id('c')),IntLiteral(1))),
                                                BinaryOp('=',Id('d'),BinaryOp('+',Id('d'),IntLiteral(1))),
                                                Block(
                                                    [
                                                        If(
                                                            BinaryOp(
                                                                '>',
                                                                ArrayCell(Id('array'),Id('d')),
                                                                ArrayCell(Id('array'),BinaryOp('+',Id('d'),IntLiteral(1)))
                                                            ),
                                                            Block(
                                                                [
                                                                    BinaryOp('=',Id('swap'),ArrayCell(Id('array'),Id('d'))),
                                                                    BinaryOp('=',ArrayCell(Id('array'),Id('d')),ArrayCell(Id('array'),BinaryOp('+',Id('d'),IntLiteral(1)))),
                                                                    BinaryOp('=',ArrayCell(Id('array'),BinaryOp('+',Id('d'),IntLiteral(1))),Id('swap'))
                                                                ]
                                                            )
                                                        )
                                                    ]
                                                )
                                            )
                                        ]
                                    )
                                ),
                                CallExpr(
                                    Id('printf'),
                                    [
                                        StringLiteral('Sorted list in ascending order:\\n')
                                    ]
                                ),
                                For(
                                    BinaryOp('=',Id('c'),IntLiteral(0)),
                                    BinaryOp('<',Id('c'),Id('n')),
                                    BinaryOp('=',Id('c'),BinaryOp('+',Id('c'),IntLiteral(1))),
                                    CallExpr(
                                        Id('printf'),
                                        [
                                            StringLiteral('%d\\n'),ArrayCell(Id('array'),Id('c'))
                                        ]
                                    )
                                ),
                                Return(IntLiteral(0))
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,381))
    
    def test_FreeTest_No82(self):
        """Free test"""
        input= """
        int main() 
        { 
            int arr[5]; 
            arr[0] = 5; 
            arr[2] = -10; 
            arr[3 / 2] = 2; 
            arr[3] = arr[0]; 
  
            printf("%d %d %d %d", arr[0], arr[1], arr[2], arr[3]); 
            return 0; 
        } 
        """
        expect = str(
            Program(
                [
                    FuncDecl(
                        Id('main'),
                        [],
                        IntType(),
                        Block(
                            [
                                VarDecl('arr',ArrayType(5,IntType())),
                                BinaryOp('=',ArrayCell(Id('arr'),IntLiteral(0)),IntLiteral(5)),
                                BinaryOp('=',ArrayCell(Id('arr'),IntLiteral(2)),UnaryOp('-',IntLiteral(10))),
                                BinaryOp('=',ArrayCell(Id('arr'),BinaryOp('/',IntLiteral(3),IntLiteral(2))),IntLiteral(2)),
                                BinaryOp('=',ArrayCell(Id('arr'),IntLiteral(3)),ArrayCell(Id('arr'),IntLiteral(0))),
                                CallExpr(
                                    Id('printf'),
                                    [
                                        StringLiteral('%d %d %d %d'),
                                        ArrayCell(Id('arr'),IntLiteral(0)),
                                        ArrayCell(Id('arr'),IntLiteral(1)),
                                        ArrayCell(Id('arr'),IntLiteral(2)),
                                        ArrayCell(Id('arr'),IntLiteral(3))
                                    ]
                                ),
                                Return(IntLiteral(0))
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,382))
    
    def test_FreeTest_No83(self):
        """Free test"""
        input = """
        float func(float x) 
        { 
            return x*x*x - x*x + 2; 
        } 
        float derivFunc(float x) 
        { 
            return 3*x*x - 2*x; 
        }  
        int main() 
        { 
            float x0; x0= -20; 
            newtonRaphson(x0); 
            return 0; 
        } 
        """
        expect = str(
            Program(
                [
                    FuncDecl(
                        Id('func'),
                        [
                            VarDecl('x',FloatType())
                        ],
                        FloatType(),
                        Block(
                            [
                                Return(
                                    BinaryOp(
                                        '+',
                                        BinaryOp(
                                            '-',
                                            BinaryOp(
                                                '*',
                                                BinaryOp('*',Id('x'),Id('x')),
                                                Id('x')
                                            ),
                                            BinaryOp('*',Id('x'),Id('x'))
                                        ),
                                        IntLiteral(2)
                                    )
                                )
                            ]
                        )
                    ),
                    FuncDecl(
                        Id('derivFunc'),
                        [
                            VarDecl('x',FloatType())
                        ],
                        FloatType(),
                        Block(
                            [
                                Return(
                                    BinaryOp(
                                        '-',
                                        BinaryOp(
                                            '*',
                                            BinaryOp('*',IntLiteral(3),Id('x')),
                                            Id('x')
                                        ),
                                        BinaryOp('*',IntLiteral(2),Id('x'))
                                    )
                                )
                            ]
                        )
                    ),
                    FuncDecl(
                        Id('main'),
                        [],
                        IntType(),
                        Block(
                            [
                                VarDecl('x0',FloatType()),
                                BinaryOp('=',Id('x0'),UnaryOp('-',IntLiteral(20))),
                                CallExpr(
                                    Id('newtonRaphson'),
                                    [
                                        Id('x0')
                                    ]
                                ),
                                Return(IntLiteral(0))
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,383))

    def test_FreeTest_No84(self):
        """Free test"""
        input = """
        int main()
        {// giai pt bac 3	
	        float a, b, c, d, delta, k, x1, x2, x3, x0, x, X;
 	        delta = pow(b,2) - 3*a*c;
	        k = (9*a*b*c - 2*pow(b,3) - 27*pow(a,2)*d)/ (2*sqrt(abs(pow(delta,3))));
	
	        if(delta>0){
		        if(abs(k)<=1) {
		                x1 = (2*sqrt(delta)*cos((acos(k)/3)) - b)/ (3*a);
		                x2 = (2*sqrt(delta)*cos((acos(k)/3 - (2*PI/3))) - b)/(3*a);
		                x3 = (2*sqrt(delta)*cos((acos(k)/3 + (2*PI/3))) - b)/(3*a);
		        }
                else{
		                float x0;
                        x0 = ((sqrt(delta)*abs(k))/(3*a*k))*(pow(abs(k) + sqrt(pow(k,2) - 1),1/3) + pow(abs(k) - sqrt(pow(k,2) - 1),1/3)) - (b/(3*a));
		        }
		    }
	        if(delta=0){
		        X = (-b + pow(pow(b,3) - 27*pow(a,2)*d,1/3))/(3*a);
		        
	        }
	        if(delta<0){
		        x = (sqrt(abs(delta))/(3*a))*(pow(k + sqrt(pow(k,2) + 1),1/3) + pow(k - sqrt(pow(k,2) + 1),1/3)) - (b/(3*a));
	        }
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl(
                        Id('main'),
                        [],
                        IntType(),
                        Block(
                            [
                                VarDecl('a',FloatType()),
                                VarDecl('b',FloatType()),
                                VarDecl('c',FloatType()),
                                VarDecl('d',FloatType()),
                                VarDecl('delta',FloatType()),
                                VarDecl('k',FloatType()),
                                VarDecl('x1',FloatType()),
                                VarDecl('x2',FloatType()),
                                VarDecl('x3',FloatType()),
                                VarDecl('x0',FloatType()),
                                VarDecl('x',FloatType()),
                                VarDecl('X',FloatType()),
                                BinaryOp(
                                    '=',
                                    Id('delta'),
                                    BinaryOp(
                                        '-',
                                        CallExpr(Id('pow'),[Id('b'),IntLiteral(2)]),
                                        BinaryOp(
                                            '*',
                                            BinaryOp('*',IntLiteral(3),Id('a')),
                                            Id('c')
                                        )
                                    )
                                ),
                                BinaryOp(
                                    '=',
                                    Id('k'),
                                    BinaryOp(
                                        '/',
                                        BinaryOp(
                                            '-',
                                            BinaryOp(
                                                '-',
                                                BinaryOp(
                                                    '*',
                                                    BinaryOp(
                                                        '*',
                                                        BinaryOp('*',IntLiteral(9),Id('a')),
                                                        Id('b'))
                                                    ,
                                                    Id('c')
                                                ),
                                                BinaryOp(
                                                    '*',
                                                    IntLiteral(2),
                                                    CallExpr(Id('pow'),[Id('b'),IntLiteral(3)])
                                                )
                                            ),
                                            BinaryOp(
                                                '*',
                                                BinaryOp('*',IntLiteral(27),CallExpr(Id('pow'),[Id('a'),IntLiteral(2)])),
                                                Id('d')
                                            )
                                        ),
                                        BinaryOp(
                                            '*',
                                            IntLiteral(2),
                                            CallExpr(
                                                Id('sqrt'),
                                                [
                                                    CallExpr(
                                                        Id('abs'),
                                                        [
                                                            CallExpr(
                                                                Id('pow'),
                                                                [
                                                                    Id('delta'),IntLiteral(3)
                                                                ]
                                                            )
                                                        ]
                                                    )
                                                ]
                                            )
                                        )
                                    )
                                ),
                                If(
                                    BinaryOp('>',Id('delta'),IntLiteral(0)),
                                    Block(
                                        [
                                            If(
                                                BinaryOp('<=',CallExpr(Id('abs'),[Id('k')]),IntLiteral(1)),
                                                Block(
                                                    [
                                                        BinaryOp(
                                                            '=',
                                                            Id('x1'),
                                                            BinaryOp(
                                                                '/',
                                                                BinaryOp(
                                                                    '-',
                                                                    BinaryOp(
                                                                        '*',
                                                                        BinaryOp(
                                                                            '*',
                                                                            IntLiteral(2),
                                                                            CallExpr(Id('sqrt'),[Id('delta')])
                                                                        ),
                                                                        CallExpr(
                                                                            Id('cos'),
                                                                            [
                                                                                BinaryOp('/',CallExpr(Id('acos'),[Id('k')]),IntLiteral(3))
                                                                            ]
                                                                        )
                                                                    ),
                                                                    Id('b')
                                                                ),
                                                                BinaryOp('*',IntLiteral(3),Id('a'))
                                                            )
                                                        ),
                                                        BinaryOp(
                                                            '=',
                                                            Id('x2'),
                                                            BinaryOp(
                                                                '/',
                                                                BinaryOp(
                                                                    '-',
                                                                    BinaryOp(
                                                                        '*',
                                                                        BinaryOp('*',IntLiteral(2),CallExpr(Id('sqrt'),[Id('delta')])),
                                                                        CallExpr(
                                                                            Id('cos'),
                                                                            [
                                                                                BinaryOp(
                                                                                    '-',
                                                                                    BinaryOp('/',CallExpr(Id('acos'),[Id('k')]),IntLiteral(3)),
                                                                                    BinaryOp('/',BinaryOp('*',IntLiteral(2),Id('PI')),IntLiteral(3))
                                                                                )
                                                                            ]
                                                                        )
                                                                    ),
                                                                    Id('b')
                                                                ),
                                                                BinaryOp('*',IntLiteral(3),Id('a'))
                                                            )
                                                        ),
                                                        BinaryOp(
                                                            '=',
                                                            Id('x3'),
                                                            BinaryOp(
                                                                '/',
                                                                BinaryOp(
                                                                    '-',
                                                                    BinaryOp(
                                                                        '*',
                                                                        BinaryOp('*',IntLiteral(2),CallExpr(Id('sqrt'),[Id('delta')])),
                                                                        CallExpr(
                                                                            Id('cos'),
                                                                            [
                                                                                BinaryOp(
                                                                                    '+',
                                                                                    BinaryOp('/',CallExpr(Id('acos'),[Id('k')]),IntLiteral(3)),
                                                                                    BinaryOp('/',BinaryOp('*',IntLiteral(2),Id('PI')),IntLiteral(3))
                                                                                )
                                                                            ]
                                                                        )
                                                                    ),
                                                                    Id('b')
                                                                ),
                                                                BinaryOp('*',IntLiteral(3),Id('a'))
                                                            )
                                                        )
                                                    ]
                                                ),
                                                Block(
                                                    [
                                                        VarDecl('x0',FloatType()),
                                                        BinaryOp(
                                                            '=',
                                                            Id('x0'),
                                                            BinaryOp(
                                                                '-',
                                                                BinaryOp(
                                                                    '*',
                                                                    BinaryOp(
                                                                        '/',
                                                                        BinaryOp(
                                                                            '*',
                                                                            CallExpr(Id('sqrt'),[Id('delta')]),
                                                                            CallExpr(Id('abs'),[Id('k')])
                                                                        ),
                                                                        BinaryOp('*',BinaryOp('*',IntLiteral(3),Id('a')),Id('k'))
                                                                    ),
                                                                    BinaryOp(
                                                                        '+',
                                                                        CallExpr(
                                                                            Id('pow'),
                                                                            [
                                                                                BinaryOp(
                                                                                    '+',
                                                                                    CallExpr(Id('abs'),[Id('k')]),
                                                                                    CallExpr(
                                                                                        Id('sqrt'),
                                                                                        [
                                                                                            BinaryOp('-',CallExpr(Id('pow'),[Id('k'),IntLiteral(2)]),IntLiteral(1))
                                                                                        ]
                                                                                    )
                                                                                ),
                                                                                BinaryOp('/',IntLiteral(1),IntLiteral(3))
                                                                            ]
                                                                        ),
                                                                        CallExpr(
                                                                            Id('pow'),
                                                                            [
                                                                                BinaryOp(
                                                                                    '-',
                                                                                    CallExpr(Id('abs'),[Id('k')]),
                                                                                    CallExpr(
                                                                                        Id('sqrt'),
                                                                                        [
                                                                                            BinaryOp('-',CallExpr(Id('pow'),[Id('k'),IntLiteral(2)]),IntLiteral(1))
                                                                                        ]
                                                                                    )
                                                                                ),
                                                                                BinaryOp('/',IntLiteral(1),IntLiteral(3))
                                                                            ]
                                                                        )
                                                                    )
                                                                ),
                                                                BinaryOp(
                                                                    '/',
                                                                    Id('b'),
                                                                    BinaryOp('*',IntLiteral(3),Id('a'))
                                                                )
                                                            )
                                                        )
                                                    ]
                                                )
                                            )
                                        ]
                                    )
                                ),
                                If(
                                    BinaryOp('=',Id('delta'),IntLiteral(0)),
                                    Block(
                                        [
                                            BinaryOp(
                                                '=',
                                                Id('X'),
                                                BinaryOp(
                                                    '/',
                                                    BinaryOp(
                                                        '+',
                                                        UnaryOp('-',Id('b')),
                                                        CallExpr(
                                                            Id('pow'),
                                                            [
                                                                BinaryOp(
                                                                    '-',
                                                                    CallExpr(Id('pow'),[Id('b'),IntLiteral(3)]),
                                                                    BinaryOp(
                                                                        '*',
                                                                        BinaryOp('*',IntLiteral(27),CallExpr(Id('pow'),[Id('a'),IntLiteral(2)])),
                                                                        Id('d')
                                                                    )
                                                                ),
                                                                BinaryOp('/',IntLiteral(1),IntLiteral(3))
                                                            ]
                                                        )
                                                    ),
                                                    BinaryOp('*',IntLiteral(3),Id('a'))
                                                )
                                            )
                                        ]
                                    )
                                ),
                                If(
                                    BinaryOp('<',Id('delta'),IntLiteral(0)),
                                    Block(
                                        [
                                            BinaryOp(
                                                '=',
                                                Id('x'),
                                                BinaryOp(
                                                    '-',
                                                    BinaryOp(
                                                        '*',
                                                        BinaryOp(
                                                            '/',
                                                            CallExpr(
                                                                Id('sqrt'),
                                                                [
                                                                    CallExpr(Id('abs'),[Id('delta')])
                                                                ]
                                                            ),
                                                            BinaryOp('*',IntLiteral(3),Id('a'))
                                                        ),
                                                        BinaryOp(
                                                            '+',
                                                            CallExpr(
                                                                Id('pow'),
                                                                [
                                                                    BinaryOp(
                                                                        '+',
                                                                        Id('k'),
                                                                        CallExpr(
                                                                            Id('sqrt'),
                                                                            [
                                                                                BinaryOp(
                                                                                    '+',
                                                                                    CallExpr(Id('pow'),[Id('k'),IntLiteral(2)]),
                                                                                    IntLiteral(1)
                                                                                )
                                                                            ]
                                                                        )
                                                                    ),
                                                                    BinaryOp('/',IntLiteral(1),IntLiteral(3))
                                                                ]
                                                            ),
                                                            CallExpr(
                                                                Id('pow'),
                                                                [
                                                                    BinaryOp(
                                                                        '-',
                                                                        Id('k'),
                                                                        CallExpr(
                                                                            Id('sqrt'),
                                                                            [
                                                                                BinaryOp(
                                                                                    '+',
                                                                                    CallExpr(Id('pow'),[Id('k'),IntLiteral(2)]),
                                                                                    IntLiteral(1)
                                                                                )
                                                                            ]
                                                                        )
                                                                    ),
                                                                    BinaryOp('/',IntLiteral(1),IntLiteral(3))
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    BinaryOp(
                                                        '/',
                                                        Id('b'),
                                                        BinaryOp('*',IntLiteral(3),Id('a'))
                                                    )
                                                )
                                            )
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,384))
    
    def test_FreeTest_No85(self):
        """Free test"""
        input= """
        int giaiPT(float a, float b, float c,float x1, float x2){
            float delta ; delta= b*b - 4*a*c;
            if(delta<0){
                x1=x2=0.0;
                return 0;
            }
            else if(delta==0){
                x1 = x2 = -b/(2*a);
                return 1;
            }
            else{
                delta = sqrt(delta);
                x1 = (-b + delta) / (2*a);
                x2 = (-b - delta) / (2*a);
                return 2;
            }
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl(
                        Id('giaiPT'),
                        [
                            VarDecl('a',FloatType()),
                            VarDecl('b',FloatType()),
                            VarDecl('c',FloatType()),
                            VarDecl('x1',FloatType()),
                            VarDecl('x2',FloatType())
                        ],
                        IntType(),
                        Block(
                            [
                                VarDecl('delta',FloatType()),
                                BinaryOp(
                                    '=',
                                    Id('delta'),
                                    BinaryOp(
                                        '-',
                                        BinaryOp('*',Id('b'),Id('b')),
                                        BinaryOp('*',BinaryOp('*',IntLiteral(4),Id('a')),Id('c'))
                                    )
                                ),
                                If(
                                    BinaryOp('<',Id('delta'),IntLiteral(0)),
                                    Block(
                                        [
                                            BinaryOp(
                                                '=',
                                                Id('x1'),
                                                BinaryOp('=',Id('x2'),FloatLiteral(0.0))
                                            ),
                                            Return(IntLiteral(0))
                                        ]
                                    ),
                                    If(
                                        BinaryOp('==',Id('delta'),IntLiteral(0)),
                                        Block(
                                            [
                                                BinaryOp(
                                                    '=',
                                                    Id('x1'),
                                                    BinaryOp(
                                                        '=',
                                                        Id('x2'),
                                                        BinaryOp(
                                                            '/',
                                                            UnaryOp('-',Id('b')),
                                                            BinaryOp('*',IntLiteral(2),Id('a'))
                                                        )
                                                    )
                                                ),
                                                Return(IntLiteral(1))
                                            ]
                                        ),
                                        Block(
                                            [
                                                BinaryOp(
                                                    '=',
                                                    Id('delta'),
                                                    CallExpr(
                                                        Id('sqrt'),
                                                        [
                                                            Id('delta')
                                                        ]
                                                    )
                                                ),
                                                BinaryOp(
                                                    '=',
                                                    Id('x1'),
                                                    BinaryOp(
                                                        '/',
                                                        BinaryOp('+',UnaryOp('-',Id('b')),Id('delta')),
                                                        BinaryOp('*',IntLiteral(2),Id('a'))
                                                    )
                                                ),
                                                BinaryOp(
                                                    '=',
                                                    Id('x2'),
                                                    BinaryOp(
                                                        '/',
                                                        BinaryOp('-',UnaryOp('-',Id('b')),Id('delta')),
                                                        BinaryOp('*',IntLiteral(2),Id('a'))
                                                    )
                                                ),
                                                Return(IntLiteral(2))
                                            ]
                                        )
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,385))
    
    def test_FreeTest_No86(self):
        """Free test"""
        input = """
        int Sin(int x){
            int t,sum,n;
            n = 1000;
            for(i=1;i<=n;i=i+1)
            {
                t=(t*(-1)*x*x)/(2*i*(2*i+1));
                sum=sum+t;
            }
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl(
                        Id('Sin'),
                        [
                            VarDecl('x',IntType())
                        ],
                        IntType(),
                        Block(
                            [
                                VarDecl('t',IntType()),
                                VarDecl('sum',IntType()),
                                VarDecl('n',IntType()),
                                BinaryOp('=',Id('n'),IntLiteral(1000)),
                                For(
                                    BinaryOp('=',Id('i'),IntLiteral(1)),
                                    BinaryOp('<=',Id('i'),Id('n')),
                                    BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
                                    Block(
                                        [
                                            BinaryOp(
                                                '=',
                                                Id('t'),
                                                BinaryOp(
                                                    '/',
                                                    BinaryOp(
                                                        '*',
                                                        BinaryOp(
                                                            '*',
                                                            BinaryOp('*',Id('t'),UnaryOp('-',IntLiteral(1))),
                                                            Id('x')
                                                        ),
                                                        Id('x')
                                                    ),
                                                    BinaryOp(
                                                        '*',
                                                        BinaryOp('*',IntLiteral(2),Id('i')),
                                                        BinaryOp('+',BinaryOp('*',IntLiteral(2),Id('i')),IntLiteral(1))
                                                    )
                                                )
                                            ),
                                            BinaryOp('=',Id('sum'),BinaryOp('+',Id('sum'),Id('t')))
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_FreeTest_No87(self):
        """Free test"""
        input = """
        int xor(int a,int b)
        {
            return (!a && b) || (a && !b);
        }

        int min(int x, int y) 
        { 
            return xor(y,(xor(x,y) && -(x < y))); 
        } 

        int max(int x, int y) 
        { 
            return xor(x,(xor(x,y) && -(x < y)));  
        } 
        int main() 
        { 
            int x ; x = 15; 
            int y ; y = 6; 
            printf("Minimum of ",x," and ",y," is ",min(x,y)); 
            printf("Maximum of ",x," and ",y," is ",max(x,y)); 
        } 
        """
        expect = str(
            Program(
                [
                    FuncDecl(
                        Id('xor'),
                        [
                            VarDecl('a',IntType()),
                            VarDecl('b',IntType())
                        ],
                        IntType(),
                        Block(
                            [
                                Return(
                                    BinaryOp(
                                        '||',
                                        BinaryOp('&&',UnaryOp('!',Id('a')),Id('b')),
                                        BinaryOp('&&',Id('a'),UnaryOp('!',Id('b')))
                                    )
                                )
                            ]
                        )
                    ),
                    FuncDecl(
                        Id('min'),
                        [
                            VarDecl('x',IntType()),
                            VarDecl('y',IntType())
                        ],
                        IntType(),
                        Block(
                            [
                                Return(
                                    CallExpr(
                                        Id('xor'),
                                        [
                                            Id('y'),
                                            BinaryOp(
                                                '&&',
                                                CallExpr(
                                                    Id('xor'),
                                                    [
                                                        Id('x'),Id('y')
                                                    ]
                                                ),
                                                UnaryOp('-',BinaryOp('<',Id('x'),Id('y')))
                                            )
                                        ]
                                    )
                                )
                            ]
                        )
                    ),
                    FuncDecl(
                        Id('max'),
                        [
                            VarDecl('x',IntType()),
                            VarDecl('y',IntType())
                        ],
                        IntType(),
                        Block(
                            [
                                Return(
                                    CallExpr(
                                        Id('xor'),
                                        [
                                            Id('x'),
                                            BinaryOp(
                                                '&&',
                                                CallExpr(
                                                    Id('xor'),
                                                    [
                                                        Id('x'),Id('y')
                                                    ]
                                                ),
                                                UnaryOp('-',BinaryOp('<',Id('x'),Id('y')))
                                            )
                                        ]
                                    )
                                )
                            ]
                        )
                    ),
                    FuncDecl(
                        Id('main'),
                        [],
                        IntType(),
                        Block(
                            [
                                VarDecl('x',IntType()),
                                BinaryOp('=',Id('x'),IntLiteral(15)),
                                VarDecl('y',IntType()),
                                BinaryOp('=',Id('y'),IntLiteral(6)),
                                CallExpr(
                                    Id('printf'),
                                    [
                                        StringLiteral('Minimum of '),
                                        Id('x'),
                                        StringLiteral(' and '),
                                        Id('y'),
                                        StringLiteral(' is '),
                                        CallExpr(
                                            Id('min'),
                                            [
                                                Id('x'),Id('y')
                                            ]
                                        )
                                    ]
                                ),
                                CallExpr(
                                    Id('printf'),
                                    [
                                        StringLiteral('Maximum of '),
                                        Id('x'),
                                        StringLiteral(' and '),
                                        Id('y'),
                                        StringLiteral(' is '),
                                        CallExpr(
                                            Id('max'),
                                            [
                                                Id('x'),Id('y')
                                            ]
                                        )
                                    ]
                                ),
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,387))
    
    def test_FreeTest_No88(self):
        """Free test"""
        input= """
        int max(int a[], int n)
        {
            int max ;max = a[0];
            int i;
            for (i = 1; i < n; i=i+1)
                if (max < a[i]) max = a[i];
            return max;
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl(
                        Id('max'),
                        [
                            VarDecl('a',ArrayPointerType(IntType())),
                            VarDecl('n',IntType())
                        ],
                        IntType(),
                        Block(
                            [
                                VarDecl('max',IntType()),
                                BinaryOp('=',Id('max'),ArrayCell(Id('a'),IntLiteral(0))),
                                VarDecl('i',IntType()),
                                For(
                                    BinaryOp('=',Id('i'),IntLiteral(1)),
                                    BinaryOp('<',Id('i'),Id('n')),
                                    BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
                                    If(
                                        BinaryOp('<',Id('max'),ArrayCell(Id('a'),Id('i'))),
                                        BinaryOp('=',Id('max'),ArrayCell(Id('a'),Id('i')))
                                    )
                                ),
                                Return(Id('max'))
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,388))
    
    def test_FreeTest_No89(self):
        """Free test"""
        input = """
        int gcd(int a, int b) {
            int tmp;
            do{
                tmp = a % b;
                a = b;
                b = tmp;
            }while(b != 0);
            return a;
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl(
                        Id('gcd'),
                        [
                            VarDecl('a',IntType()),
                            VarDecl('b',IntType())
                        ],
                        IntType(),
                        Block(
                            [
                                VarDecl('tmp',IntType()),
                                Dowhile(
                                    [
                                        Block(
                                            [
                                                BinaryOp('=',Id('tmp'),BinaryOp('%',Id('a'),Id('b'))),
                                                BinaryOp('=',Id('a'),Id('b')),
                                                BinaryOp('=',Id('b'),Id('tmp'))
                                            ]
                                        )
                                    ],
                                    BinaryOp('!=',Id('b'),IntLiteral(0))
                                ),
                                Return(Id('a'))
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_FreeTest_No90(self):
        """Free test"""
        input = """
        float F(float x,int n) {
            int a,i;
            if (n % 2 == 0)
                a = 1;
            else
                a = -1;
            float temp ;temp= 1;
            for (i = 1; i <= 2 * n + 1; i=i+1)
                temp = temp * x / i;
            return a * temp;
        }
        int main()
        {   
            float x, sin;sin =0;
            print("Nhap gia tri sin can tinh(radian): ");
            scan(x);
            int n ;n= 0;
            do{
                sin = sin+ F(x, n);
                n=n+1;
            }while (abs(F(x, n)) > 0.00001) ;
            print("Gia tri can tinh: ",sin);
            return 0;
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl(
                        Id('F'),
                        [
                            VarDecl('x',FloatType()),
                            VarDecl('n',IntType())
                        ],
                        FloatType(),
                        Block(
                            [
                                VarDecl('a',IntType()),
                                VarDecl('i',IntType()),
                                If(
                                    BinaryOp('==',BinaryOp('%',Id('n'),IntLiteral(2)),IntLiteral(0)),
                                    BinaryOp('=',Id('a'),IntLiteral(1)),
                                    BinaryOp('=',Id('a'),UnaryOp('-',IntLiteral(1)))
                                ),
                                VarDecl('temp',FloatType()),
                                BinaryOp('=',Id('temp'),IntLiteral(1)),
                                For(
                                    BinaryOp('=',Id('i'),IntLiteral(1)),
                                    BinaryOp('<=',Id('i'),BinaryOp('+',BinaryOp('*',IntLiteral(2),Id('n')),IntLiteral(1))),
                                    BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
                                    BinaryOp('=',Id('temp'),BinaryOp('/',BinaryOp('*',Id('temp'),Id('x')),Id('i')))
                                ),
                                Return(BinaryOp('*',Id('a'),Id('temp')))
                            ]
                        )
                    ),
                    FuncDecl(
                        Id('main'),
                        [],
                        IntType(),
                        Block(
                            [
                                VarDecl('x',FloatType()),
                                VarDecl('sin',FloatType()),
                                BinaryOp('=',Id('sin'),IntLiteral(0)),
                                CallExpr(
                                    Id('print'),
                                    [
                                        StringLiteral('Nhap gia tri sin can tinh(radian): ')
                                    ]
                                ),
                                CallExpr(
                                    Id('scan'),
                                    [
                                        Id('x')
                                    ]
                                ),
                                VarDecl('n',IntType()),
                                BinaryOp('=',Id('n'),IntLiteral(0)),
                                Dowhile(
                                    [
                                        Block(
                                            [
                                                BinaryOp(
                                                    '=',
                                                    Id('sin'),
                                                    BinaryOp(
                                                        '+',
                                                        Id('sin'),
                                                        CallExpr(Id('F'),[Id('x'),Id('n')])
                                                    )
                                                ),
                                                BinaryOp(
                                                    '=',
                                                    Id('n'),
                                                    BinaryOp('+',Id('n'),IntLiteral(1))
                                                )
                                            ]
                                        )
                                    ],
                                    BinaryOp(
                                        '>',
                                        CallExpr(
                                            Id('abs'),
                                            [
                                                CallExpr(Id('F'),[Id('x'),Id('n')])
                                            ]
                                        ),
                                        FloatLiteral(0.00001)
                                    )
                                ),
                                CallExpr(Id('print'),[StringLiteral('Gia tri can tinh: '),Id('sin')]),
                                Return(IntLiteral(0))
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,390))
    
    def test_FreeTest_No91(self):
        """Free test"""
        input= """
        int gcd(int a, int b) {
            if (b == 0) return a;
                return gcd(b, a % b);
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl(
                        Id('gcd'),
                        [
                            VarDecl('a',IntType()),
                            VarDecl('b',IntType())
                        ],
                        IntType(),
                        Block(
                            [
                                If(
                                    BinaryOp('==',Id('b'),IntLiteral(0)),
                                    Return(Id('a'))
                                ),
                                Return(
                                    CallExpr(
                                        Id('gcd'),
                                        [
                                            Id('b'),
                                            BinaryOp('%',Id('a'),Id('b'))
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,391))
    
    def test_FreeTest_No92(self):
        """Free test"""
        input = """
        int gcd(int a, int b){
            if (a*b==0)
                return 0 ;
            do{ 
                if (a > b)
                    a = a % b;
                else
                    b = b % a;
            
            }while (a*b != 0); 
            return a + b;
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl(Id('gcd'),
                        [
                            VarDecl('a',IntType()),
                            VarDecl('b',IntType())
                        ],
                        IntType(),
                        Block(
                            [
                                If(
                                    BinaryOp(
                                        '==',
                                        BinaryOp('*',Id('a'),Id('b')),
                                        IntLiteral(0)
                                    ),
                                    Return(IntLiteral(0))
                                ),
                                Dowhile(
                                    [
                                        Block(
                                            [
                                                If(
                                                    BinaryOp('>',Id('a'),Id('b')),
                                                    BinaryOp('=',Id('a'),BinaryOp('%',Id('a'),Id('b'))),
                                                    BinaryOp('=',Id('b'),BinaryOp('%',Id('b'),Id('a')))
                                                )
                                            ]
                                        )
                                    ],
                                    BinaryOp(
                                        '!=',
                                        BinaryOp('*',Id('a'),Id('b')),
                                        IntLiteral(0))
                                ),
                                Return(BinaryOp('+',Id('a'),Id('b')))
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_FreeTest_No93(self):
        """Free test"""
        input = """
        int gcd(int a, int b){
            if (a == 0 || b == 0){
                    return a + b;
            }
            do{
                if (a > b){
                    a = a - b; 
                }else{
                    b = b - a;
                }
            }while (a != b);
            return a; 
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl(Id('gcd'),
                        [
                            VarDecl('a',IntType()),
                            VarDecl('b',IntType())
                        ],
                        IntType(),
                        Block(
                            [
                                If(
                                    BinaryOp(
                                        '||',
                                        BinaryOp('==',Id('a'),IntLiteral(0)),
                                        BinaryOp('==',Id('b'),IntLiteral(0))
                                    ),
                                    Block(
                                        [
                                            Return(
                                                BinaryOp('+',Id('a'),Id('b'))
                                            )
                                        ]
                                    )
                                ),
                                Dowhile(
                                    [
                                        Block(
                                            [
                                                If(
                                                    BinaryOp('>',Id('a'),Id('b')),
                                                    Block(
                                                        [
                                                            BinaryOp('=',Id('a'),BinaryOp('-',Id('a'),Id('b')))
                                                        ]
                                                    ),
                                                    Block(
                                                        [
                                                            BinaryOp('=',Id('b'),BinaryOp('-',Id('b'),Id('a')))
                                                        ]
                                                    )
                                                )
                                            ]
                                        )
                                    ],
                                    BinaryOp('!=',Id('a'),Id('b'))
                                ),
                                Return(Id('a'))
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,393))

    def test_FreeTest_No94(self):
        """Free test"""
        input = """
        //find sum of numbers in range [a,b] by using recursive
        int sum(int a, int b)
        {
            if (b<a) return 0;
            else
                return b + sum(a,b-1);
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl(Id('sum'),
                        [
                            VarDecl('a',IntType()),
                            VarDecl('b',IntType())
                        ],
                        IntType(),
                        Block(
                            [
                                If(
                                    BinaryOp('<',Id('b'),Id('a')),
                                    Return(IntLiteral(0)),
                                    Return(
                                        BinaryOp(
                                            '+',
                                            Id('b'),
                                            CallExpr(
                                                Id('sum'),
                                                [
                                                    Id('a'),
                                                    BinaryOp('-',Id('b'),IntLiteral(1))
                                                ]
                                            )
                                        )
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test_FreeTest_No95(self):
        """Free test"""
        input = """
        //find sum of numbers in range [a,b] by using recursive
        int sum(int a, int b)
        {
            if (a > b)
                return 0;
            return a+sum(a+1,b);
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl(Id('sum'),
                        [
                            VarDecl('a',IntType()),
                            VarDecl('b',IntType())
                        ],
                        IntType(),
                        Block(
                            [
                                If(
                                    BinaryOp('>',Id('a'),Id('b')),
                                    Return(IntLiteral(0))
                                ),
                                Return(
                                    BinaryOp(
                                        '+',
                                        Id('a'),
                                        CallExpr(
                                            Id('sum'),
                                            [
                                                BinaryOp('+',Id('a'),IntLiteral(1)),Id('b')
                                            ]
                                        )
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test_FreeTest_No96(self):
        """Free test"""
        input = """
        int save;
        float dump;
        string str;
        boolean isPrime(int num)
        {
            if((num <= 1) || (num % 2 ==0 && num != 2))
                return false;
            int square, i;
            square = sqrt(num);
            for (i=2;i<=square+1;i = i+1)
             {
                if (num % i == 0) return false;
             }
            return true;
        }
        int main()
        {
            scrand(time(0));
            int a[100],i;
            for (i=0;i<length(a);i=i+1)
            {
                a[i]=rand();
                if (isPrime(a[i]))
                 printf(a[i] + "\\t");
            }
            return 1;
        }
        """
        expect = str(
            Program(
            [
                VarDecl('save',IntType()),
                VarDecl('dump',FloatType()),
                VarDecl('str',StringType()),
                FuncDecl(Id('isPrime'),
                    [
                        VarDecl('num',IntType())
                    ],
                    BoolType(),
                    Block(
                    [
                        If(
                            BinaryOp(
                                '||',
                                BinaryOp(
                                    '<=',
                                    Id('num'),
                                    IntLiteral(1)
                                ),
                                BinaryOp(
                                    '&&',
                                    BinaryOp('==',
                                        BinaryOp('%',Id('num'),IntLiteral(2)),IntLiteral(0)
                                    ),
                                    BinaryOp('!=',Id('num'),IntLiteral(2))
                                )),
                            Return(BooleanLiteral('false'))
                        ),
                        VarDecl('square',IntType()),
                        VarDecl('i',IntType()),
                        BinaryOp('=',Id('square'),CallExpr(Id('sqrt'),[Id('num')])),
                        For(
                            BinaryOp('=',Id('i'),IntLiteral(2)),
                            BinaryOp('<=',Id('i'),BinaryOp('+',Id('square'),IntLiteral(1))),
                            BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
                            Block(
                            [
                                If(
                                    BinaryOp('==',BinaryOp('%',Id('num'),Id('i')),IntLiteral(0)),
                                    Return(
                                        BooleanLiteral('false')
                                        )
                                )
                            ])),
                            Return(BooleanLiteral('true'))
                    ])),
                FuncDecl(Id('main'),
                    [],
                    IntType(),
                    Block(
                    [
                        CallExpr(
                            Id('scrand'),
                            [
                                CallExpr(
                                    Id('time'),
                                    [
                                        IntLiteral(0)
                                    ]
                                )
                            ]
                        ),
                        VarDecl('a',
                        ArrayType(100,IntType())),
                        VarDecl('i',IntType()),
                        For(
                            BinaryOp('=',Id('i'),IntLiteral(0)),
                            BinaryOp('<',Id('i'),CallExpr(
                                                    Id('length'),
                                                    [
                                                        Id('a')
                                                    ])),
                            BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
                            Block(
                            [
                                BinaryOp('=',ArrayCell(Id('a'),Id('i')),CallExpr(Id('rand'),[])),
                                If(
                                    CallExpr(Id('isPrime'),
                                        [
                                            ArrayCell(Id('a'),Id('i'))
                                        ]
                                    ),
                                    CallExpr(Id('printf'),
                                        [
                                            BinaryOp('+',ArrayCell(Id('a'),Id('i')),
                                            StringLiteral('\\t'))
                                        ]
                                    )
                                )
                            ])
                        ),
                        Return(IntLiteral(1))
                    ])
                )
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,396))
    
    def test_FreeTest_No97(self):
        """Free test"""
        input = """
        int a; float d; boolean b, c[2]; 
        void example(string a)
        {
            int i;
            for (i=1;i<=9;i=i+1)
                print("trung");
            do 
                scandf("Nhap n",n);
                if (n<=0)
                    printf("Nhap sai roi \\n Moi nhap lai : ");
            while(n>0);
            for (i=0; i<length(a);i=i+1)
            {
                    if (i%2!=0)
                        continue;
                    if (a[i]=="2")
                        return;
            }
        }
        """
        expect = str(
            Program(
            [
                VarDecl('a',IntType()),
                VarDecl('d',FloatType()),
                VarDecl('b',BoolType()),
                VarDecl('c',ArrayType(2,BoolType())),
                FuncDecl(Id('example'),
                [
                    VarDecl('a',StringType())
                ],
                VoidType(),
                Block(
                [
                    VarDecl('i',IntType()),
                    For(
                        BinaryOp('=',Id('i'),IntLiteral(1)),
                        BinaryOp('<=',Id('i'),IntLiteral(9)),
                        BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
                        CallExpr(
                            Id('print'),
                            [
                                StringLiteral('trung')
                            ])
                    ),
                    Dowhile(
                    [
                        CallExpr(
                            Id('scandf'),
                            [
                                StringLiteral('Nhap n'),
                                Id('n')
                            ]),
                        If(
                            BinaryOp('<=',Id('n'),IntLiteral(0)),
                            CallExpr(
                                Id('printf'),
                                [
                                    StringLiteral('Nhap sai roi \\n Moi nhap lai : ')
                                ])
                        )
                    ],
                    BinaryOp('>',Id('n'),IntLiteral(0))
                    ),
                    For(
                        BinaryOp('=',Id('i'),IntLiteral(0)),
                        BinaryOp('<',Id('i'),CallExpr(
                                                Id('length'),
                                                [
                                                    Id('a')
                                                ]
                                            )),
                        BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
                        Block(
                        [
                            If(
                                BinaryOp('!=',BinaryOp('%',Id('i'),IntLiteral(2)),IntLiteral(0)),
                                Continue()
                            ),
                            If(
                                BinaryOp('==',ArrayCell(Id('a'),Id('i')),StringLiteral('2')),
                                Return())
                        ])
                    )
                ]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,397))
    
    def test_FreeTest_No98(self):
        """Free test"""
        input = """
        int gcd(int x, int y){
            if (x==0) return y;
            else if (x<0) return gcd(-x,y);
            else if (y<0) return -gcd(x,-y);
            else return gcd(y%x,x);
        }
        """
        test = """successful"""
        expect = str(
            Program(
            [
                FuncDecl(Id('gcd'),
                [
                    VarDecl('x',IntType()),
                    VarDecl('y',IntType())
                ],
                IntType(),
                Block(
                [
                    If(
                        BinaryOp('==',Id('x'),IntLiteral(0)),
                        Return(Id('y')),
                        If(
                            BinaryOp('<',Id('x'),IntLiteral(0)),
                            Return(CallExpr(Id('gcd'),
                                    [
                                        UnaryOp('-',Id('x')),Id('y')
                                    ])),
                            If(
                                BinaryOp('<',Id('y'),IntLiteral(0)),
                                Return(UnaryOp('-',CallExpr(Id('gcd'),
                                                        [
                                                            Id('x'),
                                                            UnaryOp('-',Id('y'))
                                                        ])
                                                )
                                        ),
                                Return(CallExpr(Id('gcd'),
                                    [
                                        BinaryOp('%',Id('y'),Id('x')),
                                        Id('x')
                                    ])
                                )
                            )
                        )
                    )
                ]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_FreeTest_No99(self):
        """Free test"""
        input = """
        int giai_thua(int n){
            if (n<=1) 
                return 1;
            else 
                return n*giai_thua(n-1);
        }
        int main() {
            int a,b,c;
            float ku;
            a = 4;
            print(giai_thua(a));
        }
        """
        expect = str(
            Program(
            [
                FuncDecl(Id('giai_thua'),
                [
                    VarDecl('n',IntType())
                ],IntType(),
                Block(
                [
                    If(
                        BinaryOp('<=',Id('n'),IntLiteral(1)),
                        Return(IntLiteral(1)),
                        Return(
                            BinaryOp('*',Id('n'),CallExpr(Id('giai_thua'),
                                                [
                                                    BinaryOp('-',Id('n'),IntLiteral(1))
                                                ])
                                    )
                            )
                    )
                ])),
                
                FuncDecl(
                    Id('main'),[],IntType(),
                    Block(
                    [
                        VarDecl('a',IntType()),
                        VarDecl('b',IntType()),
                        VarDecl('c',IntType()),
                        VarDecl('ku',FloatType()),
                        BinaryOp('=',Id('a'),IntLiteral(4)),
                        CallExpr(Id('print'),[
                                                CallExpr(Id('giai_thua'),
                                                [
                                                    Id('a')
                                                ])
                                            ]
                        )
                    ])
                )
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,399))
    
    def test_FreeTest_No100(self):
        """Free test"""
        input = """
        int main()
        {
        
            int a;
            if (a >= 0)
                do 
                    print(a);
                    a = a-1;
                while (a<0);
            else
                for(0;9;0)
                    {
                        print(a);
                        a = a + 1;
                    }
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl(Id('main'),
                        [],
                        IntType(),
                        Block(
                            [
                                VarDecl('a',IntType()),
                                If(
                                    BinaryOp('>=',Id('a'),IntLiteral(0)),
                                    Dowhile(
                                        [
                                            CallExpr(
                                                Id('print'),
                                                [
                                                    Id('a')
                                                ]
                                            ),
                                            BinaryOp('=',Id('a'),BinaryOp('-',Id('a'),IntLiteral(1)))
                                        ],
                                        BinaryOp('<',Id('a'),IntLiteral(0))
                                    ),
                                    For(
                                        IntLiteral(0),
                                        IntLiteral(9),
                                        IntLiteral(0),
                                        Block(
                                            [
                                                CallExpr(
                                                    Id('print'),
                                                    [
                                                        Id('a')
                                                    ]
                                                ),
                                                BinaryOp('=',Id('a'),BinaryOp('+',Id('a'),IntLiteral(1)))
                                            ]
                                        )
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,400))
