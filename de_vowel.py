vowels = list("aeiou")
no_vowels = list("rcls")
def de_vowel(string):
    for n in string:
        if n != "a" and n != "e" and n != "i" and n != "o" and n != "u":
            return n

print de_vowel("Testing vowels")

