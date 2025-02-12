class TrieNode:
    def __init__(self, value, n_id=None):
        self.children = {}
        self.n_id = n_id
        self.value = value

    def set_id(self, n_id):
        self.n_id = n_id


class Trie:
    def __init__(self, jms_client):
        self.root = TrieNode('root')
        self.node_mapping = {}
        self.jms_client = jms_client
        self.init_node()

    def init_node(self):
        for n in self.jms_client.node.list():
            self.insert(n)

    def insert(self, node):
        trie_node = self.root
        for sub_name in node.full_value.split('/'):
            if not sub_name:
                continue
            if sub_name not in trie_node.children:
                trie_node.children[sub_name] = TrieNode(sub_name, node.id)
            trie_node = trie_node.children[sub_name]
            self.node_mapping[node.full_value] = node.id

    def create_node_by_full_name(self, node_full_name):
        n_id, trie_node = None, self.root
        for sub_name in node_full_name.split('/'):
            if not sub_name:
                continue
            if sub_name not in trie_node.children:
                node = self.jms_client.node.create_node_by_id(
                    trie_node.n_id, {'value': sub_name}
                )
                trie_node.children[sub_name] = TrieNode(sub_name, n_id=node.id)
                n_id = node.id
            trie_node = trie_node.children[sub_name]
        return n_id

    def get_node_id(self, full_value):
        n_id = self.node_mapping.get(full_value)
        if not n_id:
            n_id = self.create_node_by_full_name(full_value)
            self.node_mapping[full_value] = n_id
        return n_id

    def print(self):
        print(self.node_mapping)
