class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()      # Create new TrieNode from there and insert value
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
            
        return node.is_end

    def start_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def delete(self, word):
        if not self.search(word):
            return
        
        node = self.root
        stack = []

        for char in word:
            stack.append((node, char))
            node = node.children[char]

        node.is_end = False
        for curr_node, char in reversed(stack):
            if len(curr_node.children[char].children) == 0 and not curr_node.children[char].is_end:
                del curr_node.children[char]

            else:
                break


    def print_trie(self):
        words = []
        self._traverse(self.root, "", words)
        for word in words:
            print(word)

    def _traverse(self, node, prefix, words):
        if node.is_end:
            words.append(prefix)
        for char, child_node in node.children.items():
            self._traverse(child_node, prefix + char, words)



trie = Trie()

trie.insert("Orange")
trie.insert("Oracle")

trie.delete("Oracle")

trie.print_trie()