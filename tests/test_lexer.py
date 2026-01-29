"""
Lexer test cases for TyC compiler
TODO: Implement 100 test cases for lexer
"""

import pytest
from tests.utils import Tokenizer
from build.TyCLexer import UncloseString, IllegalEscape, ErrorToken

def test_lexer_placeholder():
    """Placeholder test - replace with actual test cases"""
    source = "// This is a placeholder test"
    tokenizer = Tokenizer(source)
    # TODO: Add actual test assertions
    assert True

def test_keyword_int():
    """Test that 'int' keyword is recognized"""
    source = "int"
    tokenizer = Tokenizer(source)
    result = tokenizer.get_tokens_as_string()
    # Expected format: "TOKEN_NAME,token_text,TOKEN_NAME,token_text,...,EOF"
    assert result == "INT,int,EOF"


def test_simple_expression():
    """Test a simple arithmetic expression: 10 + 20"""
    source = "10 + 20"
    tokenizer = Tokenizer(source)
    result = tokenizer.get_tokens_as_string()
    # Should tokenize as: INTLIT(10), ADD(+), INTLIT(20), EOF
    assert result == "INTLIT,10,ADD,+,INTLIT,20,EOF"


def test_identifier():
    """Test that identifiers are recognized"""
    source = "myVariable"
    tokenizer = Tokenizer(source)
    result = tokenizer.get_tokens_as_string()
    assert result == "ID,myVariable,EOF"


def test_valid_string():
    """Test a valid string literal with escape sequence"""
    source = '"Hello\\nWorld"'
    tokenizer = Tokenizer(source)
    result = tokenizer.get_tokens_as_string()
    # The quotes should be stripped, but escape sequences remain
    assert result == "STRINGLIT,Hello\\nWorld,EOF"

#test valid and invalid tokens 

def test_valid_float1():
    source = "0.0"
    tokenizer = Tokenizer(source)
    result = tokenizer.get_tokens_as_string()
    assert result == "FLOATLIT,0.0,EOF"

def test_valid_float2():
    source = "3.14"
    tokenizer = Tokenizer(source)
    result = tokenizer.get_tokens_as_string()
    assert result == "FLOATLIT,3.14,EOF"

def test_valid_float3():
    source = "1.23e4"
    tokenizer = Tokenizer(source)
    result = tokenizer.get_tokens_as_string()
    assert result == "FLOATLIT,1.23e4,EOF"

def test_valid_float4():
    source = "5.67E-2"
    tokenizer = Tokenizer(source)
    result = tokenizer.get_tokens_as_string()
    assert result == "FLOATLIT,5.67E-2,EOF"

def test_valid_float5():
    source = "1."
    tokenizer = Tokenizer(source)
    result = tokenizer.get_tokens_as_string()
    assert result == "FLOATLIT,1.,EOF"

def test_valid_float6():
    source = ".5"
    tokenizer = Tokenizer(source)
    result = tokenizer.get_tokens_as_string()
    assert result == "FLOATLIT,.5,EOF"

def test_valid_float7():
    source = "1e4"
    tokenizer = Tokenizer(source)
    result = tokenizer.get_tokens_as_string()
    assert result == "FLOATLIT,1e4,EOF"

def test_valid_float8():
    source = "2E-3"
    tokenizer = Tokenizer(source)
    result = tokenizer.get_tokens_as_string()
    assert result == "FLOATLIT,2E-3,EOF"

#test error handling
#test edge cases and boundary conditions

def test_unclosed_string_message():
    source = '"Hello'
    tokenizer = Tokenizer(source)
    
    with pytest.raises(UncloseString) as excinfo:
        tokenizer.get_tokens_as_string()
    
    # Kiểm tra tin nhắn trong ngoại lệ
    assert "Unclosed String: Hello" in str(excinfo.value)

