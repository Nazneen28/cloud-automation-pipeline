"""Tests for GitFlow Portfolio app"""
from src.app import greet, add, get_status

def test_greet_returns_correct_message():
    assert greet("Nazneen") == "Hello, Nazneen! Welcome to Cloud Engineering."

def test_greet_works_with_any_name():
    assert "Cloud Engineering" in greet("Anyone")

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -1) == -2

def test_get_status_returns_dict():
    status = get_status()
    assert isinstance(status, dict)
    assert status["author"] == "Nazneen"
    assert status["status"] == "active"