from string_utils import reverse_words, count_vowels, is_palindrome

# 测试 reverse_words
def test_reverse_words_normal():
    assert reverse_words("hello world") == "world hello"

def test_reverse_words_single():
    assert reverse_words("hello") == "hello"

def test_reverse_words_empty():
    assert reverse_words("") == ""

def test_reverse_words_more():
    assert reverse_words("world hello!!!") == "!!! hello world"

def test_reverse_words_more1():
    assert reverse_words("world,hello!") == "! hello , world"


# 测试 count_vowels
def test_count_vowels_normal():
    assert count_vowels("hello") == 2

def test_count_vowels_no_vowels():
    assert count_vowels("gym") == 0

def test_count_vowels_uppercase():
    assert count_vowels("APPLE") == 2

# 测试 is_palindrome
def test_is_palindrome_true():
    assert is_palindrome("racecar") == True

def test_is_palindrome_false():
    assert is_palindrome("hello") == False

def test_is_palindrome_spaces():
    assert is_palindrome("race car") == True