from tree.binary_tree.Huffman.main import HuffmanCoding


def test_huffman_coding():
    string = "AAABBCCDBBAAAABCBA"
    HuffmanCoding.encode(string)
    assert HuffmanCoding.decode(string) == "00010101101101111010000010110100"
