class Anagram:
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def is_anagram(self):
        if sorted(self.s1) == sorted(self.s2):
            return True
        return False


print("Give me string 1:")
s1 = str(input())
print("Give me string 2:")
s2 = str(input())

if Anagram(s1, s2).is_anagram():
    print("The two strings are anagrams!!")
else:
    print("The two strings are not anagrams!!")
