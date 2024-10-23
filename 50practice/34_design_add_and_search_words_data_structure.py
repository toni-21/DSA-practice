# class TrieNode:
#     def __init__(self):
#         self.links = [None] * 26
#         self.is_end = False

#     def ind(self, ch: str) -> int:
#         return ord(ch) - ord("a")

#     def put(self, ch: str, node: "TrieNode") -> None:
#         self.links[self.ord(ch)] = node

#     def containsKey(self, ch: str) -> bool:
#         return self.links[self.ord(ch)] is not None

#     def get(self, ch: str) -> "TrieNode":
#         return self.links[self.ord(ch)]

#     def setEnd(self) -> None:
#         self.isEnd = True

#     def isEnd(self) -> bool:
#         return self.isEnd


# class Trie:
#     def __init__(self) -> None:
#         self.root = TrieNode()

#     def addWord(self, word: str) -> None:
#         node = self.root
#         for ch in word:
#             if not node.containsKey(ch):
#                 node.put(ch, TrieNode())
#             node = node.get(ch)
#         node.setEnd()

#     def searchPrefix(self, node: TrieNode, word: str, index: int) -> bool:
#         if index == len(word):
#             return node.isEnd()
#         ch = word[index]
#         if ch == ".":
#             for i in range(len(node.links)):
#                 link = node.links[i]
#                 if link is not None and self.searchPrefix(link, word, index + 1):
#                     return True
#             return False
#         else:
#             if node.containsKey(ch):
#                 return self.searchPrefix(node.get(ch), word, index + 1)
#             else:
#                 return False

#     def search(self, word: str) -> bool:
#         return self.searchPrefix(self.root, word, 0)


# BETTER SOLUTION
class TrieNode:
    def __init__(self) -> None:
        self.links = {}
        self.is_end = False


class WordDictionary:
    def __init__(self) -> None:
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.links:
                node.links[ch] = TrieNode()
            node = node.links[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        def preSearch(word: str, node: TrieNode, index: int) -> bool:
            if index == len(word):
                return node.is_end
            ch = word[index]
            if ch == ".":
                for link in node.links.values():
                    if preSearch(word, link, index + 1):
                        return True
            elif ch in node.links:
                return preSearch(word, node.links[ch], index + 1)
            return False

        return preSearch(word, self.root, 0)


node = WordDictionary()
node.addWord("bad")
node.addWord("dad")
node.addWord("mad")
print(node.search("pad"))
print(node.search("bad"))
print(node.search(".ad"))
print(node.search("b.."))
