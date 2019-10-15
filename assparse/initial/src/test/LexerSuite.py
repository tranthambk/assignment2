# import unittest
# from TestUtils import TestLexer 

# class LexerSuite(unittest.TestCase):
#     """test identifiers"""
#     def test_case_ID(self):
#         """ID"""
#         self.assertTrue(TestLexer.checkLexeme("aBc","aBc,<EOF>",100))
#     def test_case_ID_1(self):
#         self.assertTrue(TestLexer.checkLexeme("abc_09","abc_09,<EOF>",101))
#     def test_case_ID_2(self):
#         self.assertTrue(TestLexer.checkLexeme("_abc3","_abc3,<EOF>",102))
#     def test_case_ID_3(self):
#         self.assertTrue(TestLexer.checkLexeme("_a_abc3","_a_abc3,<EOF>",180))
#     def test_case_ID_4(self):
#         self.assertTrue(TestLexer.checkLexeme("int_abc3","int_abc3,<EOF>",181))
#     def test_ambigous_ID(self):
#         """ID with digit"""
#         self.assertTrue(TestLexer.checkLexeme("57a7","57,a7,<EOF>",103))
#     def test_ambigous_ID_1(self):
#         self.assertTrue(TestLexer.checkLexeme("5_a7","5,_a7,<EOF>",104))
#     def test_ambigous_ID_2(self):
#         self.assertTrue(TestLexer.checkLexeme("5int_a7","5,int_a7,<EOF>",182))
#     def test_ambigous_ID_3(self):
#         self.assertTrue(TestLexer.checkLexeme("5float _a7","5,float,_a7,<EOF>",183))
#     def test_ambigous_ID_4(self):
#         self.assertTrue(TestLexer.checkLexeme("5_a 7","5,_a,7,<EOF>",184))
#     def test_ID_with_character_set(self):
#         """ID with character set"""
#         self.assertTrue(TestLexer.checkLexeme("abc\nbca","abc,bca,<EOF>",105))
#     def test_ID_with_character_set_1(self):
#         self.assertTrue(TestLexer.checkLexeme("abc\tbca","abc,bca,<EOF>",106))
#     def test_ID_with_character_set_2(self):
#         self.assertTrue(TestLexer.checkLexeme("abc\fbc\ta","abc,bc,a,<EOF>",107))
#     def test_ID_with_character_set_3(self):
#         self.assertTrue(TestLexer.checkLexeme("abc\fbc\t0a","abc,bc,0,a,<EOF>",108))
#     def test_ID_with_character_set_4(self):
#         self.assertTrue(TestLexer.checkLexeme("\rabc\fbc\t0a","abc,bc,0,a,<EOF>",109))
#     def test_ID_with_error_token(self):
#         """Error Token"""
#         self.assertTrue(TestLexer.checkLexeme("abc\aca","abc,Error Token ",110))
#     def test_ID_with_error_token_1(self):
#         self.assertTrue(TestLexer.checkLexeme("abc@ca","abc,Error Token @",111))
#     def test_ID_with_error_token_2(self):
#         self.assertTrue(TestLexer.checkLexeme("abc@ca/","abc,Error Token @",112))
#     def test_ID_with_error_token_3(self):
#         self.assertTrue(TestLexer.checkLexeme("1abc@ca/","1,abc,Error Token @",113))
#     def test_ID_with_error_token_4(self):
#         self.assertTrue(TestLexer.checkLexeme("1\t_abc@\fca/","1,_abc,Error Token @",114))
#     """Comments"""
#     def test_comment_block(self):
#         """Block comment"""
#         self.assertTrue(TestLexer.checkLexeme("""/*abc*/""","""<EOF>""",115))
#     def test_comment_block_1(self):
#         self.assertTrue(TestLexer.checkLexeme("""in main(){/*abc}""","""in,main,(,),{,/,*,abc,},<EOF>""",116))
#     def test_comment_block_2(self):
#         self.assertTrue(TestLexer.checkLexeme("""flo a(){/*abc//abc*/}""","""flo,a,(,),{,},<EOF>""",117))
#     def test_comment_block_3(self):
#         self.assertTrue(TestLexer.checkLexeme("""xn dz(){/*abc/*man/abc*/}""","""xn,dz,(,),{,},<EOF>""",118))
#     def test_comment_block_4(self):
#         self.assertTrue(TestLexer.checkLexeme("""xn dz(){/*abc/**/man/abc*/}""","""xn,dz,(,),{,man,/,abc,*,/,},<EOF>""",119))
#     def test_comment_line(self):
#         """Line comment"""
#         self.assertTrue(TestLexer.checkLexeme("""//abc
#         bc
#         /*abc*/
#         c""","""bc,c,<EOF>""",120))
#     def test_comment_line_1(self):
#         self.assertTrue(TestLexer.checkLexeme("""tt\tent//abc""","""tt,ent,<EOF>""",121))
#     def test_comment_line_2(self):
#         self.assertTrue(TestLexer.checkLexeme("""tt\rent//abc/*abc""","""tt,ent,<EOF>""",122))
#     def test_comment_line_3(self):
#         self.assertTrue(TestLexer.checkLexeme("""tt\fent xuhi//abc/*abc*/""","""tt,ent,xuhi,<EOF>""",123))
#     def test_comment_line_4(self):
#         self.assertTrue(TestLexer.checkLexeme("""tt\fent\txuhi//abc//
#         /*abc*/""","""tt,ent,xuhi,<EOF>""",124))
#     """Keyword"""
#     def test_keyword(self):
#         self.assertTrue(TestLexer.checkLexeme("""int main(){}""","""int,main,(,),{,},<EOF>""",125))
#     def test_keyword_1(self):
#         self.assertTrue(TestLexer.checkLexeme("""int main(float a, string b, boolean c){}""","""int,main,(,float,a,,,string,b,,,boolean,c,),{,},<EOF>""",126))
#     def test_keyword_2(self):
#         self.assertTrue(TestLexer.checkLexeme("""int main(){
#             //that's comment
#             foo(true);
#             return foo(false);
#         }""","""int,main,(,),{,foo,(,true,),;,return,foo,(,false,),;,},<EOF>""",127))
#     def test_keyword_3(self):
#         self.assertTrue(TestLexer.checkLexeme("""int main(){
#             /*that's comment*/
#             float a;
#             a = 10
#             do {
#                 a = a - 1;
#                 if (a < 10) break;
#                 //that's comment
#             } while (a > 0);
#         }""","""int,main,(,),{,float,a,;,a,=,10,do,{,a,=,a,-,1,;,if,(,a,<,10,),break,;,},while,(,a,>,0,),;,},<EOF>""",128))
#     def test_keyword_4(self):
#         self.assertTrue(TestLexer.checkLexeme("""void main(){
#             int i, a;
#             i = 20;
#             for(i, i >= 10, --i){
#                 a = i * i;
#                 if (a <= 0) continue;
#             }
#         }""","""void,main,(,),{,int,i,,,a,;,i,=,20,;,for,(,i,,,i,>=,10,,,-,-,i,),{,a,=,i,*,i,;,if,(,a,<=,0,),continue,;,},},<EOF>""",129))   
#     """Operand"""
#     def test_operand(self):
#         self.assertTrue(TestLexer.checkLexeme("boolean is true || false","boolean,is,true,||,false,<EOF>",130))
#     def test_operand_1(self):
#         self.assertTrue(TestLexer.checkLexeme("if (>=) else (<)","if,(,>=,),else,(,<,),<EOF>",131))
#     def test_operand_2(self):
#         self.assertTrue(TestLexer.checkLexeme("2 >>= 1","2,>,>=,1,<EOF>",132))
#     def test_operand_3(self):
#         self.assertTrue(TestLexer.checkLexeme("""do {a = a % b;} while (a != b);""","do,{,a,=,a,%,b,;,},while,(,a,!=,b,),;,<EOF>",133))
#     def test_operand_4(self):
#         self.assertTrue(TestLexer.checkLexeme("if !(a==b) return a/b ","if,!,(,a,==,b,),return,a,/,b,<EOF>",134))
#     def test_operand_5(self):
#         self.assertTrue(TestLexer.checkLexeme("1 => 2 so false","1,=,>,2,so,false,<EOF>",135))
#     def test_operand_6(self):
#         self.assertTrue(TestLexer.checkLexeme("2 >=> 1 so true","2,>=,>,1,so,true,<EOF>",136))
#     def test_operand_7(self):
#         self.assertTrue(TestLexer.checkLexeme("///abc","<EOF>",137))
#     def test_operand_8(self):
#         self.assertTrue(TestLexer.checkLexeme("/a//abc","/,a,<EOF>",138))
#     def test_operand_9(self):
#         self.assertTrue(TestLexer.checkLexeme("a&&&b","a,&&,Error Token &",139))
#     """Separator"""
#     def test_separator(self):
#         self.assertTrue(TestLexer.checkLexeme("int a[5]","int,a,[,5,],<EOF>",140))
#     def test_separator_1(self):
#         self.assertTrue(TestLexer.checkLexeme("FLOAT foo(x+3,x)[x]","FLOAT,foo,(,x,+,3,,,x,),[,x,],<EOF>",141))
#     def test_separator_2(self):
#         self.assertTrue(TestLexer.checkLexeme("int STRING(){boolean TRUE = 0}","int,STRING,(,),{,boolean,TRUE,=,0,},<EOF>",142))
#     def test_separator_3(self):
#         self.assertTrue(TestLexer.checkLexeme("""a'b""","""a,Error Token '""",143))
#     def test_separator_4(self):
#         self.assertTrue(TestLexer.checkLexeme("{[(xnhh)]}","{,[,(,xnhh,),],},<EOF>",144))
#     """Integer Literal"""
#     def test_intlit(self):
#         self.assertTrue(TestLexer.checkLexeme("0777525661","0777525661,<EOF>",145))
#     def test_intlit_1(self):
#         self.assertTrue(TestLexer.checkLexeme("-0777525661","-,0777525661,<EOF>",146))
#     def test_intlit_2(self):
#         self.assertTrue(TestLexer.checkLexeme("07775.25661","07775.25661,<EOF>",147))
#     def test_intlit_3(self):
#         self.assertTrue(TestLexer.checkLexeme("07775_25661","07775,_25661,<EOF>",148))
#     def test_intlit_4(self):
#         self.assertTrue(TestLexer.checkLexeme("07775===25661","07775,==,=,25661,<EOF>",149))
#     """Float Literal"""
#     def test_floatlit(self):
#         self.assertTrue(TestLexer.checkLexeme("1.2","1.2,<EOF>",150))
#     def test_floatlit_1(self):
#         self.assertTrue(TestLexer.checkLexeme("1.a","1.,a,<EOF>",151))
#     def test_floatlit_2(self):
#         self.assertTrue(TestLexer.checkLexeme(".1a",".1,a,<EOF>",152))
#     def test_floatlit_3(self):
#         self.assertTrue(TestLexer.checkLexeme("1e2","1e2,<EOF>",153))
#     def test_floatlit_4(self):
#         self.assertTrue(TestLexer.checkLexeme("1e21E2","1e21,E2,<EOF>",154))
#     def test_floatlit_5(self):
#         self.assertTrue(TestLexer.checkLexeme("1.2E-2","1.2E-2,<EOF>",155))
#     def test_floatlit_6(self):
#         self.assertTrue(TestLexer.checkLexeme("1.2e-2-1.2E-2","1.2e-2,-,1.2E-2,<EOF>",156))
#     def test_floatlit_7(self):
#         self.assertTrue(TestLexer.checkLexeme(".1E2",".1E2,<EOF>",157))
#     def test_floatlit_8(self):
#         self.assertTrue(TestLexer.checkLexeme("a1.1E2","a1,.1E2,<EOF>",158))
#     def test_floatlit_9(self):
#         self.assertTrue(TestLexer.checkLexeme("0.33E-3e-42","0.33E-3,e,-,42,<EOF>",159))
#     def test_floatlit_10(self):
#         self.assertTrue(TestLexer.checkLexeme("143e.1","143,e,.1,<EOF>",160))
#     def test_floatlit_11(self):
#         self.assertTrue(TestLexer.checkLexeme("1.e2","1.e2,<EOF>",161))
#     def test_floatlit_12(self):
#         self.assertTrue(TestLexer.checkLexeme("1.a2e2","1.,a2e2,<EOF>",162))
#     def test_floatlit_13(self):
#         self.assertTrue(TestLexer.checkLexeme("-a1e2","-,a1e2,<EOF>",163))
#     def test_floatlit_14(self):
#         self.assertTrue(TestLexer.checkLexeme("-1e-2ab2","-,1e-2,ab2,<EOF>",164))
#     """Boolean literal"""
#     def test_boolit(self):
#         self.assertTrue(TestLexer.checkLexeme("true : TRUE","true,Error Token :",165))
#     def test_boolit_1(self):
#         self.assertTrue(TestLexer.checkLexeme("FALSE:false","FALSE,Error Token :",166))
#     def test_boolit_2(self):
#         self.assertTrue(TestLexer.checkLexeme("truefalse","truefalse,<EOF>",167))
#     def test_boolit_3(self):
#         self.assertTrue(TestLexer.checkLexeme("True_true true","True_true,true,<EOF>",168))
#     def test_boolit_4(self):
#         self.assertTrue(TestLexer.checkLexeme("tRue","tRue,<EOF>",169))
#     """String literal"""
#     def test_stringlit(self):
#         self.assertTrue(TestLexer.checkLexeme('''"abc"''','''abc,<EOF>''',170))
#     def test_stringlit_1(self):
#         self.assertTrue(TestLexer.checkLexeme('''"""''',''',Unclosed String: ''',171))
#     def test_stringlit_2(self):
#         self.assertTrue(TestLexer.checkLexeme(""""'""","""Illegal Escape In String: '""",172))
#     def test_stringlit_3(self):
#         self.assertTrue(TestLexer.checkLexeme('''"abc\nabc"''',"""Unclosed String: abc""",173))
#     def test_stringlit_4(self):
#         self.assertTrue(TestLexer.checkLexeme('''"abc abc"''','''abc abc,<EOF>''',174))
#     def test_stringlit_5(self):
#         self.assertTrue(TestLexer.checkLexeme('''"abc\\t\\r"''','''abc\\t\\r,<EOF>''',175))
#     def test_stringlit_6(self):
#         self.assertTrue(TestLexer.checkLexeme('''"abc\ta\n"''','''Illegal Escape In String: abc	''',176))
#     def test_stringlit_7(self):
#         self.assertTrue(TestLexer.checkLexeme('''"ab\tc\\t"''','''Illegal Escape In String: ab	''',177))
#     def test_stringlit_8(self):
#         self.assertTrue(TestLexer.checkLexeme('''"abc\\\\"''','''abc\\\\,<EOF>''',178))
#     def test_stringlit_9(self):
#         """\t is illegal escape"""
#         self.assertTrue(TestLexer.checkLexeme('''"\\b\\r\\n\\f\\t\t"''','''Illegal Escape In String: \\b\\r\\n\\f\\t	''',179))
#     """Though Exception"""
#     def test_though_exception(self):
#         """ILLEGAL ESCAPE"""
#         self.assertTrue(TestLexer.checkLexeme('''"ab\\ac\\t"''','''Illegal Escape In String: ab\\a''',185))
#     def test_though_exception_1(self):
#         """STRINGLIT"""
#         self.assertTrue(TestLexer.checkLexeme('''"ab\a"''','''ab,<EOF>''',186))
#     def test_though_exception_2(self):
#         """UNCLOSED STRING"""
#         self.assertTrue(TestLexer.checkLexeme('''"ab\a''','''Unclosed String: ab''',187))
#     def test_though_exception_3(self):
#         """ILLEGAL + UNCLOSED"""
#         self.assertTrue(TestLexer.checkLexeme('''"ab\\\t"''','''Illegal Escape In String: ab\	''',188))
#     def test_though_exception_4(self):
#         """ILLEGAL + ERROR CHAR + UNCLOSED"""
#         self.assertTrue(TestLexer.checkLexeme('''"ab\t\\"''','''Illegal Escape In String: ab	''',189))
#     def test_though_exception_5(self):
#         """ILLEGAL + STRINGLIT"""
#         self.assertTrue(TestLexer.checkLexeme('''"abc\t"a\\n"''','''Illegal Escape In String: abc	''',190))
#     def test_though_exception_6(self):
#         """ILLEGAL + UNCLOSEDx2"""
#         self.assertTrue(TestLexer.checkLexeme('''"abc\t"a\n"''','''Illegal Escape In String: abc	''',191))
#     def test_though_exception_7(self):
#         """ILLEGALx2 + UNCLOSED"""
#         self.assertTrue(TestLexer.checkLexeme('''"abc\t"a\b"''','''Illegal Escape In String: abc	''',192))
#     def test_though_exception_8(self):
#         """ILLEGAL + .*?"""
#         self.assertTrue(TestLexer.checkLexeme('''"abc\t28a\\n''','''Illegal Escape In String: abc	''',193))
#     def test_though_exception_9(self):
#         """.*? + UNCLOSED STRING"""
#         self.assertTrue(TestLexer.checkLexeme('''"ab\a"ab\t"''','''ab,ab,Unclosed String: ''',194))
#     def test_though_exception_10(self):
#         """.*? + UNCLOSED STRING + ERROR CHAR"""
#         self.assertTrue(TestLexer.checkLexeme('''"ab\\n"ab\a"''','''ab\\n,ab,Error Token \a''',195))
#     def test_though_exception_11(self):
#         """ILLEGALx2"""
#         self.assertTrue(TestLexer.checkLexeme('''"ab\\a"ab\t''','''Illegal Escape In String: ab\\a''',196))
#     def test_though_exception_12(self):
#         """ILLEGAL + STRINGLIT"""
#         self.assertTrue(TestLexer.checkLexeme('''"ab\a\t"ab\a"''','''Illegal Escape In String: ab	''',197))
#     def test_though_exception_13(self):
#         """STRINGLIT"""
#         self.assertTrue(TestLexer.checkLexeme('''8"8ab\a"''','''8,8ab,<EOF>''',198))
#     def test_though_exception_14(self):
#         """UNCLOSED STRINGx2"""
#         self.assertTrue(TestLexer.checkLexeme('''"ab\r"''','''Unclosed String: ab''',199))

#     def test_lower_identifier(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",501))
#     def test_lower_upper_id(self):
#         self.assertTrue(TestLexer.checkLexeme("aCBbdc","aCBbdc,<EOF>",502))
#     def test_wrong_token(self):
#         self.assertTrue(TestLexer.checkLexeme("aA?sVN","aA,Error Token ?",503))
#     def test_integer(self):
#         """test integers"""
#         self.assertTrue(TestLexer.checkLexeme("123a123","123,a123,<EOF>",504))
#     def test_string(self):
#         """test string"""
#         self.assertTrue(TestLexer.checkLexeme(""" "123a\\n123" ""","""123a\\n123,<EOF>""",505))
#     def test_unclose_string(self):
#         """test integers"""
#         self.assertTrue(TestLexer.checkLexeme(""" "123a\\n123 ""","""Unclosed String: 123a\\n123 """,506))
#     def test_illegal_escape(self):
#         self.assertTrue(TestLexer.checkLexeme(""" 123 "123a\\m123" ""","""123,Illegal Escape In String: 123a\\m""",507))
#     def test_double_slash(self):
#         self.assertTrue(TestLexer.checkLexeme(""" 123 "123a\\\\123" ""","""123,123a\\\\123,<EOF>""",508))

import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):



    #====================TEST COMMENTS====================   
    def test_comment1(self):
        self.assertTrue(TestLexer.checkLexeme("First line// Comments \n Second line","First,line,Second,line,<EOF>",101))
    def test_comment2(self):
        self.assertTrue(TestLexer.checkLexeme("First line/* Comments \n\n\n */ Second //line","First,line,Second,<EOF>",102))
    def test_comment3(self):
        self.assertTrue(TestLexer.checkLexeme("First line/* Comments \n\n\t\r *// Second line","First,line,/,Second,line,<EOF>",103))
    #=====================================================



    #====================TEST IDENTIFIERSS====================
    def test_identifier1(self):
        self.assertTrue(TestLexer.checkLexeme("Operand1+Operand2","Operand1,+,Operand2,<EOF>",104))
    def test_identifie2(self):
        self.assertTrue(TestLexer.checkLexeme("4321Happy_New_Year","4321,Happy_New_Year,<EOF>",105))
    def test_identifier3(self):
        self.assertTrue(TestLexer.checkLexeme("_number_1 is greater than _number_2, isn't it?","_number_1,is,greater,than,_number_2,,,isn,Error Token '",106))
    def test_identifier4(self):
        self.assertTrue(TestLexer.checkLexeme("Your password (123_345_myname) is INVALID","Your,password,(,123,_345_myname,),is,INVALID,<EOF>",107))
    def test_identifier5(self):
        self.assertTrue(TestLexer.checkLexeme("Te3nc0D3 hUR7s mY 3Yes O__0","Te3nc0D3,hUR7s,mY,3,Yes,O__0,<EOF>",108))
    def test_identifier6(self):
        self.assertTrue(TestLexer.checkLexeme("____________<3____________","____________,<,3,____________,<EOF>",109))
    def test_identifier7(self):
        self.assertTrue(TestLexer.checkLexeme("Array_[_infinity_]","Array_,[,_infinity_,],<EOF>",110))
    #=========================================================



    #====================TEST INTEGERS====================
    def test_integer1(self):
        self.assertTrue(TestLexer.checkLexeme("1234f","1234,f,<EOF>",111))
    def test_integer2(self):
        self.assertTrue(TestLexer.checkLexeme("[000000000000000001] Numbers of 0s is 17","[,000000000000000001,],Numbers,of,0,s,is,17,<EOF>",112))
    def test_integer3(self):
        self.assertTrue(TestLexer.checkLexeme("567891O111213","567891,O111213,<EOF>",113))
    #=====================================================



    #====================TEST FLOATING-POINTS====================
    def test_float1(self):
        self.assertTrue(TestLexer.checkLexeme("0.3e-2+423","0.3e-2,+,423,<EOF>",114))
    def test_float2(self):
        self.assertTrue(TestLexer.checkLexeme(".3E is not a number",".3,E,is,not,a,number,<EOF>",115))
    def test_float3(self):
        self.assertTrue(TestLexer.checkLexeme("0000.0E-0000 is a number","0000.0E-0000,is,a,number,<EOF>",116))
    def test_float4(self):
        self.assertTrue(TestLexer.checkLexeme("128e...Well...","128,e,.,.,.,Well,.,.,.,<EOF>",117))
    def test_float5(self):
        self.assertTrue(TestLexer.checkLexeme("196.25.25.3 is an address","196.25,.25,.3,is,an,address,<EOF>",118))
    def test_float6(self):
        self.assertTrue(TestLexer.checkLexeme("1e1.2E2.3e3.4E4.5e5.6E6.7e7.8E8.9e9.Ezzz","1e1,.2E2,.3e3,.4E4,.5e5,.6E6,.7e7,.8E8,.9e9,.,Ezzz,<EOF>",119))
    def test_float7(self):
        self.assertTrue(TestLexer.checkLexeme("0.e-2pi","0.e-2,pi,<EOF>",120))
    def test_float8(self):
        self.assertTrue(TestLexer.checkLexeme("33E-33.33E-33.33","33E-33,.33E-33,.33,<EOF>",121))
    def test_float9(self):
        self.assertTrue(TestLexer.checkLexeme("My number is 0345.234.835(VietNam)","My,number,is,0345.234,.835,(,VietNam,),<EOF>",122))
    def test_float10(self):
        self.assertTrue(TestLexer.checkLexeme("Is 1234E56.78 a number???","Is,1234E56,.78,a,number,Error Token ?",123))
    def test_float11(self):
        self.assertTrue(TestLexer.checkLexeme("New ID is E356-99","New,ID,is,E356,-,99,<EOF>",124))
    def test_float12(self):
        self.assertTrue(TestLexer.checkLexeme("Oxygen has 8electrons","Oxygen,has,8,electrons,<EOF>",125))
    def test_float13(self):
        self.assertTrue(TestLexer.checkLexeme("200IQ or 200EQ?","200,IQ,or,200,EQ,Error Token ?",126))
    def test_float14(self):
        self.assertTrue(TestLexer.checkLexeme("0123.4E+56","0123.4,E,+,56,<EOF>",127))
    def test_float15(self):
        self.assertTrue(TestLexer.checkLexeme("The length is 13.4e+-3.5 cm","The,length,is,13.4,e,+,-,3.5,cm,<EOF>",128))
    def test_float16(self):
        self.assertTrue(TestLexer.checkLexeme("-123.456 is invalid","-,123.456,is,invalid,<EOF>",129))
    def test_float17(self):
        self.assertTrue(TestLexer.checkLexeme("325.432e---3","325.432,e,-,-,-,3,<EOF>",130))
    #============================================================



    #====================TEST STRINGS====================
    def test_string1(self):
        self.assertTrue(TestLexer.checkLexeme("\"This is a string\"","This is a string,<EOF>",131))
    def test_string2(self):
        self.assertTrue(TestLexer.checkLexeme("\"This is a string!\"","This is a string!,<EOF>",132))
    def test_string3(self):
        self.assertTrue(TestLexer.checkLexeme("\"There is a weird symbol(\\n) in the string\"","There is a weird symbol(\\n) in the string,<EOF>",133))
    def test_string4(self):
        self.assertTrue(TestLexer.checkLexeme("""\"This is the first string!""This is the second string!\"""","This is the first string!,This is the second string!,<EOF>",134))
    def test_string5(self):
        self.assertTrue(TestLexer.checkLexeme("\"My email is anh.phan2017_2021@hcmut.edu.vn\"","My email is anh.phan2017_2021@hcmut.edu.vn,<EOF>",135))
    def test_string6(self):
        self.assertTrue(TestLexer.checkLexeme("\"Can we have a string\"[string]\"inside a string\"","Can we have a string,[,string,],inside a string,<EOF>",136))
    def test_string7(self):
        self.assertTrue(TestLexer.checkLexeme("\"We are having a string\\\"[string]\\\"inside a string\"","We are having a string\\\"[string]\\\"inside a string,<EOF>",137))
    def test_string8(self):
        self.assertTrue(TestLexer.checkLexeme("Here is a string_ \"@#$&^@!&(!^#&*\"","Here,is,a,string_,@#$&^@!&(!^#&*,<EOF>",138))
    def test_string9(self):
        self.assertTrue(TestLexer.checkLexeme("\"Count the slash: \\\\\\\\\"","Count the slash: \\\\\\\\,<EOF>",139))
    def test_string10(self):
        self.assertTrue(TestLexer.checkLexeme("Empty string \"\"","Empty,string,,<EOF>",140))
    def test_string11(self):
        self.assertTrue(TestLexer.checkLexeme("List testcase \"\\b\"","List,testcase,\\b,<EOF>",141))
    def test_string12(self):
        self.assertTrue(TestLexer.checkLexeme("List testcase \"\n\" ","List,testcase,Unclosed String: ",142))
    def test_string13(self):
        self.assertTrue(TestLexer.checkLexeme("List testcase: \"\\t\"","List,testcase,Error Token :",143))
    def test_string14(self):
        self.assertTrue(TestLexer.checkLexeme("List testcase \"\\f\\b\n\"","List,testcase,Unclosed String: \\f\\b",144))
    def test_string15(self):
        self.assertTrue(TestLexer.checkLexeme("List testcase \"\" \"\\ \"","List,testcase,,Illegal Escape In String: \\ ",145))
    def test_string16(self):
        self.assertTrue(TestLexer.checkLexeme("Let's test some weird symbols: @#$ \"@#$\"","Let,Error Token '",146))
    def test_string17(self):
        self.assertTrue(TestLexer.checkLexeme("Let us test some weird symbols &&!= \"&&!=\"","Let,us,test,some,weird,symbols,&&,!=,&&!=,<EOF>",147))
    def test_string18(self):
        self.assertTrue(TestLexer.checkLexeme("Let us test some weird symbols ||=! \"||=!\"","Let,us,test,some,weird,symbols,||,=,!,||=!,<EOF>",148))
    def test_string19(self):
        self.assertTrue(TestLexer.checkLexeme("How about {brackets} and \"{brackets}\"?","How,about,{,brackets,},and,{brackets},Error Token ?",149))
    def test_string20(self):
        self.assertTrue(TestLexer.checkLexeme("Well...\" the\" last\" [string]\" testcase\"?\"","Well,.,.,., the,last, [string],testcase,?,<EOF>",150))
    #====================================================



    #====================TEST OPERATORS AND BRACKETS====================
    def test_opebrack1(self):
        self.assertTrue(TestLexer.checkLexeme("(Egg1),(Egg2);","(,Egg1,),,,(,Egg2,),;,<EOF>",151))
    def test_opebrack2(self):
        self.assertTrue(TestLexer.checkLexeme("[{{}}],[[[]]]","[,{,{,},},],,,[,[,[,],],],<EOF>",152))
    def test_opebrack3(self):
        self.assertTrue(TestLexer.checkLexeme("array[array[array[3.56e-2]]]","array,[,array,[,array,[,3.56e-2,],],],<EOF>",153))
    def test_opebrack4(self):
        self.assertTrue(TestLexer.checkLexeme("\"Hello [[{<3}]] World\"","Hello [[{<3}]] World,<EOF>",154))
    def test_opebrack5(self):
        self.assertTrue(TestLexer.checkLexeme("[The wall] ||||||","[,The,wall,],||,||,||,<EOF>",155))
    def test_opebrack6(self):
        self.assertTrue(TestLexer.checkLexeme("A+-B != C, logic!!!","A,+,-,B,!=,C,,,logic,!,!,!,<EOF>",156))
    def test_opebrack7(self):
        self.assertTrue(TestLexer.checkLexeme("infinity >>>>>>>>> 0.","infinity,>,>,>,>,>,>,>,>,>,0.,<EOF>",157))
    def test_opebrack8(self):
        self.assertTrue(TestLexer.checkLexeme("*_* >_< ^_^","*,_,*,>,_,<,Error Token ^",158))
    def test_opebrack9(self):
        self.assertTrue(TestLexer.checkLexeme("\" A \" + \" B \" == \" A\"&\"B\""," A ,+, B ,==, A,Error Token &",159))
    def test_opebrack10(self):
        self.assertTrue(TestLexer.checkLexeme("A * B // C ","A,*,B,<EOF>",160))
    def test_opebrack11(self):
        self.assertTrue(TestLexer.checkLexeme("Day * -Night[30]","Day,*,-,Night,[,30,],<EOF>",161))
    def test_opebrack12(self):
        self.assertTrue(TestLexer.checkLexeme("If(A|B)","If,(,A,Error Token |",162))
    def test_opebrack13(self):
        self.assertTrue(TestLexer.checkLexeme("If(A|B)","If,(,A,Error Token |",163))
    def test_opebrack14(self):
        self.assertTrue(TestLexer.checkLexeme("1234*(3.4e-5-3)","1234,*,(,3.4e-5,-,3,),<EOF>",164))
    def test_opebrack15(self):
        self.assertTrue(TestLexer.checkLexeme("\"STRING+string\" != \"STRING\"+\"string\"","STRING+string,!=,STRING,+,string,<EOF>",165))
    def test_opebrack16(self):
        self.assertTrue(TestLexer.checkLexeme("\"Name \"[3(2)9]","Name ,[,3,(,2,),9,],<EOF>",166))
    def test_opebrack17(self):
        self.assertTrue(TestLexer.checkLexeme("\"Close the door (*)\n\"","Unclosed String: Close the door (*)",167))
    def test_opebrack18(self):
        self.assertTrue(TestLexer.checkLexeme("\"Close the damn doorrrr {\\b*\\f}","Unclosed String: Close the damn doorrrr {\\b*\\f}",168))
    def test_opebrack19(self):
        self.assertTrue(TestLexer.checkLexeme("\"\"+-*//*-+",",+,-,*,<EOF>",169))
    def test_opebrack20(self):
        self.assertTrue(TestLexer.checkLexeme("Welcome to <=PPL=>","Welcome,to,<=,PPL,=,>,<EOF>",170))
    # #===================================================================



    #====================TEST OVERALL====================
    def test_overall1(self):
        self.assertTrue(TestLexer.checkLexeme("ID[\"str \"+\" str\"*123-34.e]","ID,[,str ,+, str,*,123,-,34.,e,],<EOF>",171))
    def test_overall2(self):
        self.assertTrue(TestLexer.checkLexeme("\"     \"(0.f%abc[5])","     ,(,0.,f,%,abc,[,5,],),<EOF>",172))
    def test_overall3(self):
        self.assertTrue(TestLexer.checkLexeme("printf(\"%f\",325e-13);","printf,(,%f,,,325e-13,),;,<EOF>",173))
    def test_overall4(self):
        self.assertTrue(TestLexer.checkLexeme("ABC,.0;\"00\",{list};","ABC,,,.0,;,00,,,{,list,},;,<EOF>",174))
    def test_overall5(self):
        self.assertTrue(TestLexer.checkLexeme("[Math] != \"is\" == [beautiful]!","[,Math,],!=,is,==,[,beautiful,],!,<EOF>",175))
    def test_overall6(self):
        self.assertTrue(TestLexer.checkLexeme("Your password [34.e\"BKU\"] is too weak;","Your,password,[,34.,e,BKU,],is,too,weak,;,<EOF>",176))
    def test_overall7(self):
        self.assertTrue(TestLexer.checkLexeme("There's something (wrong) \"Yes \\a\n\"","There,Error Token '",177))
    def test_overall8(self):
        self.assertTrue(TestLexer.checkLexeme("There is something (wrong) \"Yes \\a\n\"","There,is,something,(,wrong,),Illegal Escape In String: Yes \\a",178))
    def test_overall9(self):
        self.assertTrue(TestLexer.checkLexeme("There is something (wrong) \"Yes \\b\n\"","There,is,something,(,wrong,),Unclosed String: Yes \\b",179))
    def test_overall10(self):
        self.assertTrue(TestLexer.checkLexeme("The price(\"of the meal\") is 3.4e12$","The,price,(,of the meal,),is,3.4e12,Error Token $",180))
    def test_overall11(self):
        self.assertTrue(TestLexer.checkLexeme("\"You spent 413$ for those shoes!?!\",Unbelievable!","You spent 413$ for those shoes!?!,,,Unbelievable,!,<EOF>",181))
    def test_overall12(self):
        self.assertTrue(TestLexer.checkLexeme("-34.e12 is not a \"float(%f)\" number!","-,34.e12,is,not,a,float(%f),number,!,<EOF>",182))
    def test_overall13(self):
        self.assertTrue(TestLexer.checkLexeme("-34.e12 IS a \"float(%f)\" number, you \"DUMMY\n\"","-,34.e12,IS,a,float(%f),number,,,you,Unclosed String: DUMMY",183))
    def test_overall14(self):
        self.assertTrue(TestLexer.checkLexeme("Who cares about \"float numbers\", \"you \\idiots\"","Who,cares,about,float numbers,,,Illegal Escape In String: you \\i",184))
    def test_overall15(self):
        self.assertTrue(TestLexer.checkLexeme("\"Don't talk about math\", \"123.4e-3+234{answer}\"","Don't talk about math,,,123.4e-3+234{answer},<EOF>",185))
    def test_overall16(self):
        self.assertTrue(TestLexer.checkLexeme("\"SV1:\" \"PPL\" is a great subject!","SV1:,PPL,is,a,great,subject,!,<EOF>",186))
    def test_overall17(self):
        self.assertTrue(TestLexer.checkLexeme("\"SV2:\" No it's not :)))","SV2:,No,it,Error Token '",187))
    def test_overall18(self):
        self.assertTrue(TestLexer.checkLexeme("\"SV3:\" Yes, it is! \"But you're not gonna pass it :)\"","SV3:,Yes,,,it,is,!,But you're not gonna pass it :),<EOF>",188))
    def test_overall19(self):
        self.assertTrue(TestLexer.checkLexeme("\"SV4:\" [forum, 3PM] \"How can i run run.py???????\"","SV4:,[,forum,,,3,PM,],How can i run run.py???????,<EOF>",189))
    def test_overall20(self):
        self.assertTrue(TestLexer.checkLexeme("\"SV5 replied SV4\"*Haizzzz*\"You know there's only 0.9 week, right?\\u\"","SV5 replied SV4,*,Haizzzz,*,Illegal Escape In String: You know there's only 0.9 week, right?\\u",190))
    def test_overall21(self):
        self.assertTrue(TestLexer.checkLexeme("\"SV4: \";{silence in 333.3seconds};\"Yeah, i know, and where can i find MC.g4?\n\"","SV4: ,;,{,silence,in,333.3,seconds,},;,Unclosed String: Yeah, i know, and where can i find MC.g4?",191))
    def test_overall22(self):
        self.assertTrue(TestLexer.checkLexeme("\"SV5: *thinking\\\" $%#@!#%$\\\"\" replied \"R.I.P my friend...\"","SV5: *thinking\\\" $%#@!#%$\\\",replied,R.I.P my friend...,<EOF>",192))
    def test_overall23(self):
        self.assertTrue(TestLexer.checkLexeme("{Reddit} has \"\\rnosleep\"","{,Reddit,},has,\\rnosleep,<EOF>",193))
    def test_overall24(self):
        self.assertTrue(TestLexer.checkLexeme("3.4e-2*35(abc[5],AV)","3.4e-2,*,35,(,abc,[,5,],,,AV,),<EOF>",194))
    def test_overall25(self):
        self.assertTrue(TestLexer.checkLexeme("\"Teacher1: \",\"\\b\\f\\rMy students are too lazy\"","Teacher1: ,,,\\b\\f\\rMy students are too lazy,<EOF>",195))
    def test_overall26(self):
        self.assertTrue(TestLexer.checkLexeme("\"Teacher2: \",\"Just be harder!, like this: \\\\\\\\\\b\\f\\r\\\\\\\\\"","Teacher2: ,,,Just be harder!, like this: \\\\\\\\\\b\\f\\r\\\\\\\\,<EOF>",196))
    def test_overall27(self):
        self.assertTrue(TestLexer.checkLexeme("\"Teacher1: \"OK, you are right!{(The next assignment will be done in two days!)}","Teacher1: ,OK,,,you,are,right,!,{,(,The,next,assignment,will,be,done,in,two,days,!,),},<EOF>",197))
    def test_overall28(self):
        self.assertTrue(TestLexer.checkLexeme("\"Teacher2: ........\"Did i just create a monster?","Teacher2: ........,Did,i,just,create,a,monster,Error Token ?",198))
    def test_overall29(self):
        self.assertTrue(TestLexer.checkLexeme("+-*/My name is {Gia Anh}\"These are my testcases\\\\\\o\"","+,-,*,/,My,name,is,{,Gia,Anh,},Illegal Escape In String: These are my testcases\\\\\\o",199))
    def test_overall30(self):
        self.assertTrue(TestLexer.checkLexeme("\"Good luck with 100 testcases passed","Unclosed String: Good luck with 100 testcases passed",200))
    #===================================================