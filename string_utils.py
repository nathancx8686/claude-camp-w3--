

#reverse_words(s)：反转单词顺序（"hello world" → "world hello"）
import re
def reverse_words(s):
    words = re.findall(r"[a-zA-Z]+|[^a-zA-Z\s]+", s)
    reversed_words=words[::-1]
    return " ".join(reversed_words)
                    

#count_vowels(s)：统计元音字母数量
def count_vowels(s):
    vowels="aeiouAEIOU"
    count=0
    for char in s:
        if char in vowels:
            count+=1
    return count



#is_palindrome(s)：判断是否回文,↓ 不删空格翻转,← 空格位置变了，判断错误！

def is_palindrome(s):
    ops=s.replace(" ","").lower()
    return ops==ops[::-1]


