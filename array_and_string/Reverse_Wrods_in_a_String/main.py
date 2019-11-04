class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([word for word in s.split(" ") if len(word) >= 1][::-1])
