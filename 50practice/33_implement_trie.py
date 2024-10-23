class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.isEnd = False

    def ind(self, ch: str) -> int:
        return ord(ch) - ord("a")

    def put(self, ch: str, node: "TrieNode") -> None:
        self.links[self.ord(ch)] = node

    def contains_key(self, ch: str) -> bool:
        return self.links[self.ord(ch)] is not None

    def get(self, ch: str) -> "TrieNode":
        return self.links[self.ord(ch)]

    def set_end(self) -> None:
        self.isEnd = True

    def is_end(self) -> bool:
        return self.isEnd


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if not node.contains_key(ch):
                node.put(ch, TrieNode())
            node = node.get(ch)
        node.set_end()

    def search_prefix(self, word: str) -> TrieNode:
        node = self.root
        for ch in word:
            if not node.contains_key(ch):
                node = node.get(ch)
            else:
                return None
        return node

    def search(self, word: str) -> bool:
        node = self.search_prefix(word)
        return node is not None and node.is_end()

    def starts_with(self, prefix: str) -> bool:
        node = self.search_prefix(prefix)
        return node is not None
