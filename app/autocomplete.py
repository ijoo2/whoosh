class TrieNode(object):
    def __init__(self, letter=''):
        self.letter = letter
        self.children = {}
        self.is_word = False


class Trie(object):
    def __init__(self, filename):
        self.root = None
        with open(filename, "r") as f:
            words = [line.replace('\n', '') for line in f]
        self.build_trie(words)

    def build_trie(self, words):
        self.root = TrieNode()
        for word in words:
            self.insert(word)

    def insert(self, word):
        self._insert(self.root, word)

    def _insert(self, node, word):
        if not word:
            node.is_word = True
            return

        c = word[0]

        try:
            new_node = node.children[c]
        except:
            new_node = TrieNode(c)
            node.children[c] = new_node

        self._insert(new_node, word[1::])
