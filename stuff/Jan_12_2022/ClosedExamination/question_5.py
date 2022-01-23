import copy


class Encoding:
    def __init__(self, tree: list):
        """Deep copies a tree list to instance attribute _encoding.
        """
        self._encoding = copy.deepcopy(tree)

    def decodeText(self, coded: str):
        """Decodes a binary string using the instance attribute _encoding.

        Args:
            coded: A binary string consisting of 0s and 1s, e.g. '1011010'

        Returns:
            A plain text string decoded.

        Raises:
            ValueError: Occurred when
                - string ``coded`` contains symbols other than 0s and 1s,
                - the code is corrupted.
        """
        for x in coded:
            if x != '0' and x != '1':
                raise ValueError("Invalid encoded string")

        dct = self.build_dict()
        dct_kv_reverse = {}
        for key, val in dct.items():
            dct_kv_reverse[val] = key

        def is_prefix(substr, string):
            n = len(substr)
            for i in range(n):
                if string[i] != substr[i]:
                    return False
            return True

        def remove_prefix(prefix, text):
            if text.startswith(prefix):
                return text[len(prefix):]
            return text

        decoded = ''
        while len(coded) > 0:
            max_prefix_len = 0
            max_prefix = ''
            for bstr in dct_kv_reverse:
                if is_prefix(bstr, coded) and len(bstr) > max_prefix_len:
                    max_prefix_len = len(bstr)
                    max_prefix = bstr

            if len(max_prefix) > len(coded):
                raise ValueError("Corrupted data")
            coded = remove_prefix(max_prefix, coded)
            decoded = decoded + dct_kv_reverse[max_prefix]

        return decoded


    def encodeText(self, text: str):
        """Decodes a binary string using the instance attribute _encoding.

        Args:
            text: A text string to be encoded

        Returns:
            An encoded binary string based on the instance attribute _encoding.

        Raises:
            ValueError: Occurred when string ``text`` contains symbol(s)
                not in the _encoding tree.
        """

        encoded = ''
        dct = self.build_dict()
        for c in text:
            if c not in dct:
                raise ValueError("Invalid symbol(s)")
            encoded = encoded + dct[c]

        return encoded

    def build_dict(self) -> dict:
        """Builds a dictionary representation of the binary tree _encoding.
        """
        dct = {}
        N = len(self._encoding)
        if N == 0:
            return {}

        def recursively_build_tree_and_dict(index: int, prefix: str) -> TreeNode:
            if index >= N or self._encoding[index] is None:
                return None

            char = self._encoding[index]
            if char != '':
                dct[char] = prefix
            node = TreeNode(char)
            node.left = recursively_build_tree_and_dict(2 * index + 1, prefix + '0')
            node.right = recursively_build_tree_and_dict(2 * index + 2, prefix + '1')
            return node

        root = recursively_build_tree_and_dict(0, '')
        # use root if possible ...

        return dct


# Binary tree node representation
class TreeNode:
    def __init__(self, val: str, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# a useful routine
def list_to_binary_tree(lst: list) -> TreeNode:
    """Converts a list to a binary tree.
    """
    N = len(lst)
    if N == 0:
        return None

    # use a nested function for convenience
    def recursively_build_tree(index: int) -> TreeNode:
        if index >= N or lst[index] is None:
            return None

        node = TreeNode(lst[index])
        node.left = recursively_build_tree(2 * index + 1)
        node.right = recursively_build_tree(2 * index + 2)
        return node

    return recursively_build_tree(0)


if __name__ == '__main__':
    try:
        l = 1

    except ValueError as verr:
        print(verr)
