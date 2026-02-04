"""
Lexer test cases for TyC compiler
TODO: Implement 100 test cases for lexer
"""

import pytest
from tests.utils import Tokenizer

#this is keyword test
def test_keyword_auto():
    """1. Keyword"""
    tokenizer = Tokenizer("auto")
    assert tokenizer.get_tokens_as_string() == "auto,<EOF>"

def test_keyword_break():
    """2. Keyword"""
    tokenizer = Tokenizer("break")
    assert tokenizer.get_tokens_as_string() == "break,<EOF>"

def test_keyword_case():
    """3. Keyword"""
    tokenizer = Tokenizer("case")
    assert tokenizer.get_tokens_as_string() == "case,<EOF>"

def test_keyword_continue():
    """4. Keyword"""
    tokenizer = Tokenizer("continue")
    assert tokenizer.get_tokens_as_string() == "continue,<EOF>"

def test_keyword_default():
    """5. Keyword"""
    tokenizer = Tokenizer("default")
    assert tokenizer.get_tokens_as_string() == "default,<EOF>"

def test_keyword_else():
    """6. Keyword"""
    tokenizer = Tokenizer("else")
    assert tokenizer.get_tokens_as_string() == "else,<EOF>"

def test_keyword_float():
    """7. Keyword"""
    tokenizer = Tokenizer("float")
    assert tokenizer.get_tokens_as_string() == "float,<EOF>"

def test_keyword_for():
    """8. Keyword"""
    tokenizer = Tokenizer("for")
    assert tokenizer.get_tokens_as_string() == "for,<EOF>"

def test_keyword_if():
    """9. Keyword"""
    tokenizer = Tokenizer("if")
    assert tokenizer.get_tokens_as_string() == "if,<EOF>"

def test_keyword_int():
    """10. Keyword"""
    tokenizer = Tokenizer("int")
    assert tokenizer.get_tokens_as_string() == "int,<EOF>"

def test_keyword_return():
    """11. Keyword"""
    tokenizer = Tokenizer("return")
    assert tokenizer.get_tokens_as_string() == "return,<EOF>"

def test_keyword_string():
    """12. Keyword"""
    tokenizer = Tokenizer("string")
    assert tokenizer.get_tokens_as_string() == "string,<EOF>"

def test_keyword_struct():
    """13. Keyword"""
    tokenizer = Tokenizer("struct")
    assert tokenizer.get_tokens_as_string() == "struct,<EOF>"

def test_keyword_switch():
    """14. Keyword"""
    tokenizer = Tokenizer("switch")
    assert tokenizer.get_tokens_as_string() == "switch,<EOF>"

def test_keyword_void():
    """15. Keyword"""
    tokenizer = Tokenizer("void")
    assert tokenizer.get_tokens_as_string() == "void,<EOF>"

def test_keyword_while():
    """16. Keyword"""
    tokenizer = Tokenizer("while")
    assert tokenizer.get_tokens_as_string() == "while,<EOF>"

#this is operator test
def test_operator_add():
    """17. Operator"""
    tokenizer = Tokenizer("+")
    assert tokenizer.get_tokens_as_string() == "+,<EOF>"

def test_operator_sub():
    """18. Operator"""
    tokenizer = Tokenizer("-")
    assert tokenizer.get_tokens_as_string() == "-,<EOF>"

def test_operator_mul():
    """19. Operator"""
    tokenizer = Tokenizer("*")
    assert tokenizer.get_tokens_as_string() == "*,<EOF>"

def test_operator_div():
    """20. Operator"""
    tokenizer = Tokenizer("/")
    assert tokenizer.get_tokens_as_string() == "/,<EOF>"

def test_operator_mod():
    """21. Operator"""
    tokenizer = Tokenizer("%")
    assert tokenizer.get_tokens_as_string() == "%,<EOF>"

def test_operator_equal():
    """22. Operator"""
    tokenizer = Tokenizer("==")
    assert tokenizer.get_tokens_as_string() == "==,<EOF>"

def test_operator_notequal():
    """23. Operator"""
    tokenizer = Tokenizer("!=")
    assert tokenizer.get_tokens_as_string() == "!=,<EOF>"

def test_operator_lessthan():
    """24. Operator"""
    tokenizer = Tokenizer("<")
    assert tokenizer.get_tokens_as_string() == "<,<EOF>"

def test_operator_greaterthan():
    """25. Operator"""
    tokenizer = Tokenizer(">")
    assert tokenizer.get_tokens_as_string() == ">,<EOF>"

def test_operator_lessthan_equal():
    """26. Operator"""
    tokenizer = Tokenizer("<=")
    assert tokenizer.get_tokens_as_string() == "<=,<EOF>"

def test_operator_greaterthan_equal():
    """27. Operator"""
    tokenizer = Tokenizer(">=")
    assert tokenizer.get_tokens_as_string() == ">=,<EOF>"

def test_operator_or():
    """28. Operator"""
    tokenizer = Tokenizer("||")
    assert tokenizer.get_tokens_as_string() == "||,<EOF>"

def test_operator_and():
    """29. Operator"""
    tokenizer = Tokenizer("&&")
    assert tokenizer.get_tokens_as_string() == "&&,<EOF>"

def test_operator_not():
    """30. Operator"""
    tokenizer = Tokenizer("!")
    assert tokenizer.get_tokens_as_string() == "!,<EOF>"

def test_operator_increment():
    """31. Operator"""
    tokenizer = Tokenizer("++")
    assert tokenizer.get_tokens_as_string() == "++,<EOF>"

def test_operator_decrement():
    """32. Operator"""
    tokenizer = Tokenizer("--")
    assert tokenizer.get_tokens_as_string() == "--,<EOF>"

def test_operator_assign():
    """33. Operator"""
    tokenizer = Tokenizer("=")
    assert tokenizer.get_tokens_as_string() == "=,<EOF>"

def test_operator_access():
    """34. Operator"""
    tokenizer = Tokenizer(".")
    assert tokenizer.get_tokens_as_string() == ".,<EOF>"

#this is separator test
def test_seperator_leftparatheses():
    """35. Separator"""
    tokenizer = Tokenizer("(")
    assert tokenizer.get_tokens_as_string() == "(,<EOF>"

def test_seperator_rightparatheses():
    """36. Separator"""
    tokenizer = Tokenizer(")")
    assert tokenizer.get_tokens_as_string() == "),<EOF>"

def test_seperator_leftbrace():
    """37. Separator"""
    tokenizer = Tokenizer("{")
    assert tokenizer.get_tokens_as_string() == "{,<EOF>"

def test_seperator_rightbrace():
    """38. Separator"""
    tokenizer = Tokenizer("}")
    assert tokenizer.get_tokens_as_string() == "},<EOF>"

def test_separator_comma():
    """39. Separator"""
    tokenizer = Tokenizer(",")
    assert tokenizer.get_tokens_as_string() == ",,<EOF>"

def test_separator_semi():
    """40. Separator"""
    tokenizer = Tokenizer(";")
    assert tokenizer.get_tokens_as_string() == ";,<EOF>"

def test_separator_colon():
    """41. Separator"""
    tokenizer = Tokenizer(":")
    assert tokenizer.get_tokens_as_string() == ":,<EOF>"

#this is integer test
def test_integer_single_digit():
    """42. Integer literal"""
    tokenizer = Tokenizer("5")
    assert tokenizer.get_tokens_as_string() == "5,<EOF>"

def test_integer_start_with_zero():
    """43. Integer literal"""
    tokenizer = Tokenizer("05")
    assert tokenizer.get_tokens_as_string() == "05,<EOF>"

def test_integer_long_digits():
    """44. Integer literal"""
    tokenizer = Tokenizer("12345678901234567890")
    assert tokenizer.get_tokens_as_string() == "12345678901234567890,<EOF>"

def test_integer_negative():
    """45. Integer literal"""
    tokenizer = Tokenizer("-123")
    assert tokenizer.get_tokens_as_string() == "-123,<EOF>"

#this is float test
def test_float_decimal_point():
    """46. Float literal"""
    tokenizer = Tokenizer("0.0")
    assert tokenizer.get_tokens_as_string() == "0.0,<EOF>"

def test_float_decimal_one_digit_before_point():
    """47. Float literal"""
    tokenizer = Tokenizer("1.")
    assert tokenizer.get_tokens_as_string() == "1.,<EOF>"

def test_float_decimal_one_digit_after_point():
    """48. Float literal"""
    tokenizer = Tokenizer(".5")
    assert tokenizer.get_tokens_as_string() == ".5,<EOF>"

def test_float_decimal_e():
    """49. Float literal"""
    tokenizer = Tokenizer("1e4")
    assert tokenizer.get_tokens_as_string() == "1e4,<EOF>"

def test_float_decimal_e_negative():
    """50. Float literal"""
    tokenizer = Tokenizer("1e-4")
    assert tokenizer.get_tokens_as_string() == "1e-4,<EOF>"

def test_float_decimal_e_positive():
    """51. Float literal"""
    tokenizer = Tokenizer("1e+4")
    assert tokenizer.get_tokens_as_string() == "1e+4,<EOF>"

def test_float_decimal_E_negative():
    """52. Float literal"""
    tokenizer = Tokenizer("2E-3")
    assert tokenizer.get_tokens_as_string() == "2E-3,<EOF>"

def test_float_decimal_E_positive():
    """53. Float literal"""
    tokenizer = Tokenizer("2E+3")
    assert tokenizer.get_tokens_as_string() == "2E+3,<EOF>"

def test_float_decimal_point_e():
    """54. Float literal"""
    tokenizer = Tokenizer("1.23e4")
    assert tokenizer.get_tokens_as_string() == "1.23e4,<EOF>"

def test_float_decimal_point_E():
    """55. Float literal"""
    tokenizer = Tokenizer("5.67E-200")
    assert tokenizer.get_tokens_as_string() == "5.67E-200,<EOF>"

def test_float_decimal_two_point():
    """56. Float literal"""
    tokenizer = Tokenizer("5.67.8")
    assert tokenizer.get_tokens_as_string() == "5.67,.8,<EOF>"

def test_float_decimal_two_e():
    """57. Float literal"""
    tokenizer = Tokenizer("5e6e7") # floatlit + id
    assert tokenizer.get_tokens_as_string() == "5e6,e7,<EOF>"

#this is string test
def test_string_empty():
    """58. String literal"""
    tokenizer = Tokenizer('""')
    assert tokenizer.get_tokens_as_string() == ",<EOF>"

def test_string_simple():
    """59. String literal"""
    tokenizer = Tokenizer('"hello"')
    assert tokenizer.get_tokens_as_string() == "hello,<EOF>"

def test_string_with_spaces():
    """60. String literal"""
    tokenizer = Tokenizer('"hello world"')
    assert tokenizer.get_tokens_as_string() == "hello world,<EOF>"

def test_string_escape_backspace():
    """61. String literal"""
    tokenizer = Tokenizer('"test\\bbackspace"')
    assert tokenizer.get_tokens_as_string() == "test\\bbackspace,<EOF>"

def test_string_escape_formfeed():
    """62. String literal"""
    tokenizer = Tokenizer('"test\\fformfeed"')
    assert tokenizer.get_tokens_as_string() == "test\\fformfeed,<EOF>"

def test_string_escape_carriage_return():
    """63. Unclosed string"""
    tokenizer = Tokenizer('"test \\\r')
    assert tokenizer.get_tokens_as_string() == 'Unclosed String: test '

def test_string_escape_newline():
    """64. String literal"""
    tokenizer = Tokenizer('"test\\nnewline"')
    assert tokenizer.get_tokens_as_string() == "test\\nnewline,<EOF>"

def test_string_escape_tab():
    """65. String literal"""
    tokenizer = Tokenizer('"test\\ttab"')
    assert tokenizer.get_tokens_as_string() == "test\\ttab,<EOF>"

def test_string_escape_quote():
    """66. String literal"""
    tokenizer = Tokenizer('"He said: \\"Hello\\""')
    assert tokenizer.get_tokens_as_string() == 'He said: \\"Hello\\",<EOF>'

def test_string_escape_backslash():
    """67. String literal"""
    tokenizer = Tokenizer('"path\\\\to\\\\file"')
    assert tokenizer.get_tokens_as_string() == "path\\\\to\\\\file,<EOF>"

def test_string_with_numbers():
    """68. String literal"""
    tokenizer = Tokenizer('"abc123def456"')
    assert tokenizer.get_tokens_as_string() == "abc123def456,<EOF>"

def test_string_with_special_chars():
    """69. String literal"""
    tokenizer = Tokenizer('"!@#$%^&*()_+-=[]{}|;:,.<>?/"')
    assert tokenizer.get_tokens_as_string() == "!@#$%^&*()_+-=[]{}|;:,.<>?/,<EOF>"

def test_string_single_char():
    """70. String literal"""
    tokenizer = Tokenizer('"a"')
    assert tokenizer.get_tokens_as_string() == "a,<EOF>"

def test_string_long():
    """71. String literal"""
    tokenizer = Tokenizer('"This is a very long string with many words and characters"')
    assert tokenizer.get_tokens_as_string() == "This is a very long string with many words and characters,<EOF>"

def test_string_in_expression():
    """72. String literal"""
    tokenizer = Tokenizer('auto msg = "Hello";')
    assert tokenizer.get_tokens_as_string() == 'auto,msg,=,Hello,;,<EOF>'

def test_string_illegal_escape():
    """73. Illegal escape"""
    tokenizer = Tokenizer('"Hi \\a Long"') 
    assert tokenizer.get_tokens_as_string() == 'Illegal Escape In String: Hi \\a'

def test_string_illegal_escape_enter():
    """74. Unclosed string"""
    tokenizer = Tokenizer('"Hi \\\n') 
    assert tokenizer.get_tokens_as_string() == 'Unclosed String: Hi '

def test_string_unclose():
    """75. Unclosed string"""
    tokenizer = Tokenizer('"Hi Long')
    assert tokenizer.get_tokens_as_string() == 'Unclosed String: Hi Long'

def test_string_unclose_enter():
    """76. Unclosed string"""
    input_text = """
    "Hi
    Long"
    """
    tokenizer = Tokenizer(input_text) 
    assert tokenizer.get_tokens_as_string() == 'Unclosed String: Hi'

def test_string_illegal_unclose():
    """77. Illegal escape"""
    tokenizer = Tokenizer('"Hi \\a Long')
    assert tokenizer.get_tokens_as_string() == 'Illegal Escape In String: Hi \\a'

#this is identifier test
def test_identifier_simple():
    """78. Identifier"""
    tokenizer = Tokenizer("x")
    assert tokenizer.get_tokens_as_string() == "x,<EOF>"

def test_identifier_uppercase():
    """79. Identifier"""
    tokenizer = Tokenizer("X")
    assert tokenizer.get_tokens_as_string() == "X,<EOF>"

def test_identifier_underscore():
    """80. Identifier"""
    tokenizer = Tokenizer("_aZ9")
    assert tokenizer.get_tokens_as_string() == "_aZ9,<EOF>"

def test_identifier_error_start_with_number():
    """81. Identifier error"""
    tokenizer = Tokenizer("1a")
    assert tokenizer.get_tokens_as_string() == "1,a,<EOF>"

def test_identifier_four_ID():
    """82. Identifier"""
    tokenizer = Tokenizer("MyVar myvar MYVAR _myVar")
    assert tokenizer.get_tokens_as_string() == "MyVar,myvar,MYVAR,_myVar,<EOF>"

#this is comment test
def test_line_comment():
    """83. Line comment"""
    tokenizer = Tokenizer("// This is a comment")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_block_comment():
    """84. Block comment"""
    tokenizer = Tokenizer("/* This is a comment */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_line_comment_in_block_comment():
    """85. Line comment"""
    tokenizer = Tokenizer("/* // This is a comment */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_block_comment_enter():
    """86. Block comment"""
    input_text = """
    /* This is
        super
        Long
    */
    """
    tokenizer = Tokenizer(input_text)
    assert tokenizer.get_tokens_as_string() == "<EOF>"

#this is mixed test
def test_operators_mixed_in_expression():
    """87. Mixed"""
    tokenizer = Tokenizer("a + b * c - d / e % f == g != h < i <= j > k >= l && m || n ! o ++ p -- q a++ b--")
    assert tokenizer.get_tokens_as_string() == "a,+,b,*,c,-,d,/,e,%,f,==,g,!=,h,<,i,<=,j,>,k,>=,l,&&,m,||,n,!,o,++,p,--,q,a,++,b,--,<EOF>"

def test_increment_decrement_operators():
    """88. Mixed"""
    tokenizer = Tokenizer("++a -- b a++ b--")
    assert tokenizer.get_tokens_as_string() == "++,a,--,b,a,++,b,--,<EOF>"

def test_expression_adjacent_operators():
    """89. Mixed"""
    tokenizer = Tokenizer("a++---10") 
    assert tokenizer.get_tokens_as_string() == "a,++,--,-10,<EOF>"

def test_expression_nested_parentheses():
    """90. Mixed"""
    tokenizer = Tokenizer("((a + b) * c)")
    assert tokenizer.get_tokens_as_string() == "(,(,a,+,b,),*,c,),<EOF>"

def test_expression_member_access():
    """91. Mixed"""
    tokenizer = Tokenizer("person.name.length")
    assert tokenizer.get_tokens_as_string() == "person,.,name,.,length,<EOF>"

def test_expression_function_call():
    """92. Mixed"""
    tokenizer = Tokenizer("add(5, 10)")
    assert tokenizer.get_tokens_as_string() == "add,(,5,,,10,),<EOF>"

def test_expression_chained_function_calls():
    """93. Mixed"""
    tokenizer = Tokenizer("f(g(h(x)))")
    assert tokenizer.get_tokens_as_string() == "f,(,g,(,h,(,x,),),),<EOF>"

def test_expression_with_line_comment():
    """94. Mixed"""
    tokenizer = Tokenizer("x + y // add them")
    assert tokenizer.get_tokens_as_string() == "x,+,y,<EOF>"

#this is complex test
def test_complex_expression():
    """95. Complex"""
    tokenizer = Tokenizer("auto x = 5 + 3 * 2;")
    assert tokenizer.get_tokens_as_string() == "auto,x,=,5,+,3,*,2,;,<EOF>"

def test_complex_expression_2():
    """96. Complex"""
    tokenizer = Tokenizer("--45")
    assert tokenizer.get_tokens_as_string() == "--,45,<EOF>"

#this is expression test
def test_expression_for_loop():
    """97. Expression"""
    tokenizer = Tokenizer("for (auto i = 0; i < 10; ++i)")
    assert tokenizer.get_tokens_as_string() == "for,(,auto,i,=,0,;,i,<,10,;,++,i,),<EOF>"

def test_expression_switch_case():
    """98. Expression"""
    tokenizer = Tokenizer("case 1+2: break;")
    assert tokenizer.get_tokens_as_string() == "case,1,+,2,:,break,;,<EOF>"

def test_expression_whitespace_variants():
    """99. Expression"""
    input_text = "a  +\tb\n*\r\nc"
    tokenizer = Tokenizer(input_text)
    assert tokenizer.get_tokens_as_string() == "a,+,b,*,c,<EOF>"

def test_expression_struct_init():
    """100. Expression"""
    tokenizer = Tokenizer('Point p = {10, 20};')
    assert tokenizer.get_tokens_as_string() == "Point,p,=,{,10,,,20,},;,<EOF>"