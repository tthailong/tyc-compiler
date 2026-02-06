"""
Parser test cases for TyC compiler
TODO: Implement 100 test cases for parser
"""

import pytest
from tests.utils import Parser


# ========== Simple Test Cases (10 types) ==========
def test_empty_program():
    """1. Empty program"""
    assert Parser("").parse() == "success"


def test_program_with_only_main():
    """2. Program"""
    assert Parser("void main() {}").parse() == "success"

#this is struct test
def test_struct_simple():
    """3. test_struct_multiple_vars"""""
    source = "struct Point { int x; int y; };"
    assert Parser(source).parse() == "success"
""
def test_struct_empty():
    """4. Struct"""
    source = "struct Empty {};"
    assert Parser(source).parse() == "success"

def test_struct_auto_member():
    """5. Struct"""
    source = """struct Point {
                    int x;
                    abc z;
                    auto y;
                };"""
    assert Parser(source).parse() == "Error on line 4 col 20: auto"

def test_struct_var_no_init():
    """6. Struct"""
    source = "struct Point { int x; }; void main() { Point p; }"
    assert Parser(source).parse() == "success"

def test_struct_var_with_init():
    """7. Struct"""
    source = "struct Point { int x; int y; }; void main() { Point p = {10, 20}; }"
    assert Parser(source).parse() == "success"

def test_struct_var_empty_init():
    """8. Struct"""
    source = "struct Empty {}; void main() { Empty e = {}; }"
    assert Parser(source).parse() == "success"

def test_struct_var_multiple_types():
    """9. Struct"""
    source = """struct Person { string name; int age; float height; };
                void main() { Person p = {"John", 25, 1.75}; }"""
    assert Parser(source).parse() == "success"

def test_struct_var_nested_init():
    """10. Struct"""
    source = """struct Point { int x; int y; };
                struct Circle { Point center; int radius; };
                void main() { Circle c = {{10, 20}, 5}; }"""
    assert Parser(source).parse() == "success"

def test_struct_literal_as_arg():
    """11. Struct"""
    source = """struct Point { int x; int y; };
                void usePoint(Point p) { printInt(p.x); }
                void main() { usePoint({3, 4}); }"""
    assert Parser(source).parse() == "success"

def test_struct_var_expression_init():
    """12. Struct"""
    source = """struct Point { int x; int y; };
                void main() { int a = 10; Point p = {a + 5, a * 2}; }"""
    assert Parser(source).parse() == "success"

def test_struct_var_function_call_init():
    """13. Struct"""
    source = """struct Point { int x; };
                int getValue() { return 5; }
                void main() { Point p = {getValue()}; }"""
    assert Parser(source).parse() == "success"

def test_struct_multiple_vars():
    """14. Struct"""
    source = """struct Point { int x; };
                void main() { Point p1; Point p2 = {5}; Point p3 = {10}; }"""
    assert Parser(source).parse() == "success"

#this is member access test
def test_member_access_simple():
    """15. Member Access"""
    source = """struct Point { int x; int y; };
                void main() { Point p; auto val = p.x; }"""
    assert Parser(source).parse() == "success"

def test_member_access_assign():
    """16. Member Access"""
    source = """struct Point { int x; int y; };
                void main() { Point p; p.x = 30; }"""
    assert Parser(source).parse() == "success"

def test_member_access_read():
    """17. Member Access"""
    source = """struct Point { int x; };
                void main() { Point p = {10}; auto x_coord = p.x; }"""
    assert Parser(source).parse() == "success"

def test_member_access_in_expression():
    """18. Member Access"""
    source = """struct Point { int x; };
                void main() { Point p = {10}; printInt(p.x); }"""
    assert Parser(source).parse() == "success"

def test_member_access_increment():
    """19. Member Access"""
    source = """struct Point { int x; };
                void main() { Point p; p.x++; }"""
    assert Parser(source).parse() == "success"

def test_member_access_decrement():
    """20. Member Access"""
    source = """struct Point { int x; };
                void main() { Point p; p.x--; }"""
    assert Parser(source).parse() == "success"

def test_member_access_chained():
    """21. Member Access"""
    source = """struct Point { int x; };
                struct Circle { Point center; };
                void main() { Circle c; auto x = c.center.x; }"""
    assert Parser(source).parse() == "success"

def test_member_access_function_call():
    """22. Member Access"""
    source = """struct Point { int x; };
                Point getPoint() { Point p; return p; }
                void main() { auto x = getPoint().x; }"""
    assert Parser(source).parse() == "success"

def test_member_modify_after_assign():
    """23. Member Access"""
    source = """struct Point { int x; };
                void main() { Point p1 = {10}; Point p2; p2 = p1; p2.x = 30; }"""
    assert Parser(source).parse() == "success"

def test_member_access_complex():
    """24. Member Access"""
    source = """struct Point { int x; };
                Point getPoint() { Point p; return p; }
                void main() { getPoint().x++; }"""
    assert Parser(source).parse() == "success"

def test_member_in_arithmetic():
    """25. Member Access"""
    source = """struct Point { int x; int y; };
                void main() { Point p = {10, 20}; auto sum = p.x + p.y; }"""
    assert Parser(source).parse() == "success"

def test_member_prefix_increment():
    """26. Member Access"""
    source = """struct Point { int x; };
                void main() { Point p; ++p.x; }"""
    assert Parser(source).parse() == "success"

def test_assignment_member_access():
    """27. Member Access"""
    source = """struct Point { int x; int y; };
                void main() { Point p; p.x = 10; p.y = p.x + 5; }"""
    assert Parser(source).parse() == "success"

#this is function test
def test_function_no_params():
    """28. Function"""
    source = "void greet() { printString(\"superlongblue\"); }"
    assert Parser(source).parse() == "success"

def test_function_no_type():
    """29. Function"""
    source = "greet() { printString(\"superlongblue\"); }"
    assert Parser(source).parse() == "success"

def test_function_struct_type():
    """30. Function"""
    source = "Point greet() { printString(\"superlongblue\"); }"
    assert Parser(source).parse() == "success"

def test_function_auto_type():
    """31. Function"""
    source = "auto greet() { printString(\"superlongblue\"); }"
    assert Parser(source).parse() == "Error on line 1 col 0: auto"

def test_function_with_params():
    """32. Function"""
    source = "string greet(int x, int y) { int cur = x + y; return cur; }"
    assert Parser(source).parse() == "success" #still success because this is parser check, not semantic check

def test_function_multiple_params():
    """33. Function"""
    source = "void process(int a, float b, string c, Point d) {}"
    assert Parser(source).parse() == "success"

def test_function_params_type_auto():
    """34. Function"""
    source = "string greet(auto z) { return 1; }"
    assert Parser(source).parse() == "Error on line 1 col 13: auto"
    
def test_function_no_body():
    """35. Function"""
    source = "string greet() {}"
    assert Parser(source).parse() == "success"

def test_function_nested_call():
    """36. Function"""
    source = """int add(int x, int y) { return x + y; }
                void main() { auto result = add(add(1, 2), 3); }"""
    assert Parser(source).parse() == "success"

def test_function_call_as_arg():
    """37. Function"""
    source = """int getValue() { return 5; }
                void process(int x) { printInt(x); }
                void main() { process(getValue()); }"""
    assert Parser(source).parse() == "success"   

def test_function_multiple_returns():
    """38. Function"""
    source = """int check(int x) { 
                    if (x) { return 1; } 
                    return 0; 
                }"""
    assert Parser(source).parse() == "success"

#this is var test
def test_var_missing_semicolon():
    """39. Variable"""
    source = "void main() { auto x = 10 }"
    assert Parser(source).parse() == "Error on line 1 col 26: }"

def test_var_decl_outside():
    """40. Variable"""
    source = "int x = 5;" # only allow struct and function in program
    assert Parser(source).parse() == "Error on line 1 col 6: ="

def test_var_auto_without_init():
    """41. Variable"""
    source = "void main() { auto x; }"
    assert Parser(source).parse() == "success"

def test_var_int_with_init():
    """42. Variable"""
    source = "void main() { int x = 10; }"
    assert Parser(source).parse() == "success"

def test_var_int_without_init():
    """43. Variable"""
    source = "void main() { int x; }"
    assert Parser(source).parse() == "success"

def test_var_float_with_init():
    """44. Variable"""
    source = "void main() { float x = 3.14; }"
    assert Parser(source).parse() == "success"

def test_var_float_without_init():
    """45. Variable"""
    source = "void main() { float x; }"
    assert Parser(source).parse() == "success"

def test_var_string_with_init():
    """46. Variable"""
    source = "void main() { string s = \"hello\"; }"
    assert Parser(source).parse() == "success"

def test_var_string_without_init():
    """47. Variable"""
    source = "void main() { string s; }"
    assert Parser(source).parse() == "success"

def test_var_expression_init():
    """48. Variable"""
    source = "void main() { auto sum = 1 + 2 * 3; }"
    assert Parser(source).parse() == "success"

def test_var_nested_scopes():
    """49. Variable"""
    source = "void main() { int x; { int y; { int z; } } }"
    assert Parser(source).parse() == "success"

#this is block statement test
def test_block_empty():
    """50. Block"""
    source = "void main() { {} }"
    assert Parser(source).parse() == "success"

def test_block_single_var():
    """51. Block"""
    source = "void main() { { auto x = 10; } }"
    assert Parser(source).parse() == "success"

def test_block_multiple_vars():
    """52. Block"""
    source = """void main() { 
                    { 
                        auto x = 10; 
                        auto y = 20; 
                        auto sum = x + y; 
                    } 
                }"""
    assert Parser(source).parse() == "success"

def test_block_with_statement():
    """53. Block"""
    source = """void main() { 
                    { 
                        auto x = 10; 
                        printInt(x); 
                    } 
                }"""
    assert Parser(source).parse() == "success"

def test_block_nested():
    """54. Block"""
    source = """void main() { 
                    { 
                        auto x = 10; 
                        { 
                            auto y = 20; 
                            { 
                                auto z = 30; 
                            } 
                        } 
                    } 
                }"""
    assert Parser(source).parse() == "success"

def test_block_in_if():
    """55. Block"""
    source = """void main() { 
                    if (1) { 
                        auto x = 10; 
                        printInt(x); 
                    } 
                }"""
    assert Parser(source).parse() == "success"

def test_block_in_while():
    """56. Block"""
    source = """void main() { 
                    while (1) { 
                        auto x = 10; 
                        break; 
                    } 
                }"""
    assert Parser(source).parse() == "success"

def test_block_sequential():
    """57. Block"""
    source = """void main() { 
                    { auto x = 1; } 
                    { auto y = 2; } 
                    { auto z = 3; } 
                }"""
    assert Parser(source).parse() == "success"

def test_block_mixed_content():
    """58. Block"""
    source = """void main() { 
                    { 
                        int a; 
                        auto b = 5; 
                        a = 10; 
                        printInt(a + b); 
                    } 
                }"""
    assert Parser(source).parse() == "success"

#this is if statement test
def test_if_simple():
    """59. If"""
    source = "void main() { if (1) printInt(1); }"
    assert Parser(source).parse() == "success"


def test_if_simple_with_braces():
    """60. If"""
    source = "void main() { int x = 2; if (x == 3) { printInt(1); } }"
    assert Parser(source).parse() == "success"

def test_if_else():
    """61. If"""
    source = """void main() { 
                    if (flag) { 
                        printInt(1); 
                    } else { 
                        printInt(0); 
                    } 
                }"""
    assert Parser(source).parse() == "success"

def test_if_nested():
    """62. If"""
    source = """void main() { 
                    if (x) { 
                        if (y) { 
                            printInt(1); 
                        } 
                    } 
                }"""
    assert Parser(source).parse() == "success"

def test_if_else_if():
    """63. If"""
    source = """void main() { 
                    if (x) { 
                        printInt(1); 
                    } else if (y) { 
                        printInt(2); 
                    } else { 
                        printInt(3); 
                    } 
                }"""
    assert Parser(source).parse() == "success"

def test_if_dangling_else():
    """64. If"""
    source = "void main() { if (x) if (y) a; else b; }"
    assert Parser(source).parse() == "success"

def test_if_expression_condition():
    """65. If"""
    source = "void main() { if (x + y > 10) { printInt(1); } }"
    assert Parser(source).parse() == "success"

def test_if_function_call_condition():
    """66. If"""
    source = "int getValue() { return 1; } void main() { if (getValue()) { printInt(1); } }"
    assert Parser(source).parse() == "success"

def test_if_member_access_condition():
    """67. If"""
    source = """struct Point { int x; };
                void main() { Point p; if (p.x) { printInt(1); } }"""
    assert Parser(source).parse() == "success"

def test_if_logical_condition():
    """68. If"""
    source = "void main() { if (x && y || z) { printInt(1); } }"
    assert Parser(source).parse() == "success"

#this is while statement test
def test_while_simple():
    """69. While"""
    source = "void main() { while (1) printInt(1); }"
    assert Parser(source).parse() == "success"

def test_while_with_block_and_break():
    """70. While"""
    source = """void main() { 
                    auto i = 0;
                    auto j = 1;
                    while (i < 10) {
                        j = j/2 + i/2;
                        if (i>j) break;
                        printInt(i);
                        ++i;
                    }
                }"""
    assert Parser(source).parse() == "success"

def test_while_function_call_condition():
    """71. While"""
    source = "int getValue() { return 1; } void main() { while (getValue()) { break; } }"
    assert Parser(source).parse() == "success"

def test_while_logical_condition():
    """72. While"""
    source = "void main() { while (x && y || z) { break; } }"
    assert Parser(source).parse() == "success"

def test_while_with_continue():
    """73. While"""
    source = "void main() { while (1) { continue; } }"
    assert Parser(source).parse() == "success"

def test_while_nested():
    """74. While"""
    source = """void main() { 
                    while (x) { 
                        while (y) { 
                            printInt(1); 
                        } 
                    } 
                }"""
    assert Parser(source).parse() == "success"

def test_while_member_access_condition():
    """75. While"""
    source = """struct Point { int x; };
                void main() { Point p; while (p.x) { break; } }"""
    assert Parser(source).parse() == "success"   

def test_while_empty_body():
    """76. While"""
    source = "void main() { while (1) {} }"
    assert Parser(source).parse() == "success"

#this is for statement test
def test_for_simple():
    """77. For"""
    source = "void main() { for (auto i = 0; i < 10; ++i) printInt(i); }"
    assert Parser(source).parse() == "success"

def test_for_with_block():
    """78. For"""
    source = """void main() { 
                    for (auto i = 0; i < 10; ++i) {
                        printInt(i);
                    }
                }"""
    assert Parser(source).parse() == "success"

def test_for_no_init():
    """79. For"""
    source = "void main() { int i = 0; for (; i < 10; ++i) { printInt(i); } }"
    assert Parser(source).parse() == "success"

def test_for_no_condition():
    """80. For"""
    source = "void main() { for (auto i = 0; ; ++i) { break; } }"
    assert Parser(source).parse() == "success"

def test_for_no_update():
    """81. For"""
    source = "void main() { for (auto i = 0; i < 10; ) { i++; } }"
    assert Parser(source).parse() == "success"

def test_for_all_empty():
    """82. For"""
    source = "void main() { for (;;) { break; } }"
    assert Parser(source).parse() == "success"

def test_for_complex_condition():
    """83. For"""
    source = "void main() { for (auto i = 0; i < 10 && i != 5; ++i) { printInt(i); } }"
    assert Parser(source).parse() == "success"

def test_for_complex_update():
    """84. For"""
    source = "void main() { for (auto i = 0; i < 10; i = i + 2) { printInt(i); } }"
    assert Parser(source).parse() == "success"

def test_for_nested():
    """85. For"""
    source = """void main() { 
                    for (auto i = 0; i < 10; ++i) { 
                        for (auto j = 0; j < 10; ++j) { 
                            printInt(i + j); 
                        } 
                    } 
                }"""
    assert Parser(source).parse() == "success"

def test_for_postfix_increment_update():
    """86. For"""
    source = "void main() { for (auto i = 0; i < 10; i++) { printInt(i); } }"
    assert Parser(source).parse() == "success"

def test_for_decrement_update():
    """87. For"""
    source = "void main() { for (auto i = 10; i > 0; --i) { printInt(i); } }"
    assert Parser(source).parse() == "success"

#this is switch statement test
def test_switch_simple():
    """88. Switch"""
    source = "void main() { switch (1) { case 1: printInt(1); break; } }"
    assert Parser(source).parse() == "success"

def test_switch_multiple_cases():
    """89. Switch"""
    source = """void main() { 
                    auto day = 2;
                    switch (day) {
                        case 1:
                            printInt(1);
                            break;
                        case 2:
                            printInt(2);
                            break;
                        case 3:
                            printInt(3);
                            break;
                    }
                }"""
    assert Parser(source).parse() == "success"

def test_switch_with_default():
    """90. Switch"""
    source = """void main() { 
                    switch (x) {
                        case 1:
                            printInt(1);
                            break;
                        default:
                            printInt(0);
                    }
                }"""
    assert Parser(source).parse() == "success"

def test_switch_fall_through():
    """91. Switch"""
    source = """void main() { 
                    switch (day) {
                        case 1:
                        case 2:
                        case 3:
                            printInt(2);
                            break;
                        default:
                            printInt(0);
                    }
                }"""
    assert Parser(source).parse() == "success"   

def test_switch_empty_body():
    """92. Switch"""
    source = "void main() { switch (x) { } }"
    assert Parser(source).parse() == "success"

def test_switch_constant_expression():
    """93. Switch"""
    source = """void main() { 
                    switch (x) {
                        case 1+2:
                            printInt(3);
                            break;
                        case 4*5:
                            printInt(20);
                            break;
                    }
                }"""
    assert Parser(source).parse() == "success"

def test_switch_parenthesized_case():
    """94. Switch"""
    source = """void main() { 
                    switch (x) {
                        case (4):
                            printInt(4);
                            break;
                        case (2+3):
                            printInt(5);
                            break;
                    }
                }"""
    assert Parser(source).parse() == "success"

def test_switch_unary_case():
    """95. Switch"""
    source = """void main() { 
                    switch (x) {
                        case +5:
                            printInt(5);
                            break;
                        case -6:
                            printInt(6);
                            break;
                    }
                }"""
    assert Parser(source).parse() == "success"

def test_switch_no_break():
    """96. Switch"""
    source = """void main() { 
                    switch (x) {
                        case 1:
                            printInt(1);
                        case 2:
                            printInt(2);
                    }
                }"""
    assert Parser(source).parse() == "success"

def test_switch_nested():
    """97. Switch"""
    source = """void main() { 
                    switch (x) {
                        case 1:
                            switch (y) {
                                case 2:
                                    printInt(2);
                                    break;
                            }
                            break;
                    }
                }"""
    assert Parser(source).parse() == "success"

#this is return statement test
def test_return_void():
    """98. Return"""
    source = "void doSomething() { return; }"
    assert Parser(source).parse() == "success"

#this is expression statement test
def test_expression_statement_increment():
    """99. Expression statement"""
    source = "void main() { int x = 0; x++; }"
    assert Parser(source).parse() == "success"

#this is one for all
def test_complete_program_example():
    """100. Complete program with multiple features combined"""
    source = """
        struct Point {
            int x;
            int y;
        };
        
        Point createPoint(int a, int b) {
            Point p = {a, b};
            return p;
        }
        
        int calculateSum(Point p) {
            return p.x + p.y;
        }
        
        void main() {
            auto p1 = createPoint(10, 20);
            auto sum = calculateSum(p1);
            
            for (auto i = 0; i < sum; i++) {
                if (i % 2 == 0) {
                    printInt(i);
                } else {
                    printInt(i * 2);
                }
            }
            
            Point p2;
            p2.x = 5;
            p2.y = 15;
            
            switch (p2.x) {
                case 5:
                    printString("Five");
                    break;
                default:
                    printString("Other");
            }
            
            return;
        }
    """
    assert Parser(source).parse() == "success"
