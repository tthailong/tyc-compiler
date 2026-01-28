"""
Lexer test cases for TyC compiler
TODO: Implement 100 test cases for lexer
"""

import pytest
from tests.utils import Tokenizer
from src.lexererr import UncloseString, IllegalEscape, ErrorToken

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


def test_unclosed_string_error():
    """Test that unclosed string raises UncloseString error"""
    source = '"Hello'  # Missing closing quote
    tokenizer = Tokenizer(source)
    
    # This should raise UncloseString exception
    with pytest.raises(UncloseString) as exc_info:
        tokenizer.get_tokens_as_string()
    
    # The error message should contain "Hello" (without the opening quote)
    assert exc_info.value.args[0] == "Hello"
