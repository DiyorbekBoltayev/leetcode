class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        for i in range(len(sentences)):
            sentences[i] = sentences[i].count(' ') + 1

        return max(sentences)
