import heapq
from heapq import heappush

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

        self._insert(new_node, word[1:])

    def is_word(self, node, word):
        if not word:
            return node.is_word

        c = word[0]
        try:
            return self.is_word(node.children[c], word[1:])
        except KeyError:
            return False

    def traverse_to_word(self, node, word):
        if not word:
            return node

        c = word[0]
        try:
            return self.traverse_to_word(node.children[c], word[1:])
        except KeyError:
            return None

    def closest_word(self, word):
        node = self.traverse_to_word(self.root, word)
        result = []
        if not node:
            return 'Could not find any words'

        priority = (0 , '')
        hq = []
        heappush(hq, (priority, node))

        while hq:
            priority, next_node = heapq.heappop(hq)

            if next_node.is_word:
                result.append(word + priority[1])
                if len(result) == 3:
                    return 'Did you mean ', result

            for child in next_node.children.values():
                heappush(hq, ((priority[0] + 1, priority[1] + child.letter), child))


        return "Did you mean ", result


class Autocomplete(object):
    def __init__(self, filename):
        self.tree = Trie(filename)

    def is_word(self, word):
        return self.tree.is_word(self.tree.root, word)

    def closest_word(self, word):
        return self.tree.closest_word(word)
