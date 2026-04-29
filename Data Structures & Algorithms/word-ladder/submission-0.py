class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wset = set(wordList) # convert list to set for O(1) lookup

        if endWord not in wordList:
            return 0

        q = deque([(beginWord, 1)])

        while q:
            word,length = q.popleft()

            if word == endWord:
                return length

            for i in range(len(word)):
                for k in 'abcdefghijklmnopqrstuvwxyz':

                    new_word = word[:i] + k + word[i+1:]

                    if new_word in wset:
                        wset.remove(new_word)
                        q.append((new_word, length + 1))

        return 0
