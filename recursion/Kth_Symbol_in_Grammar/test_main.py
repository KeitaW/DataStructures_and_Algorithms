from recursion.Kth_Symbol_in_Grammar.main import Solution


def test_main():
    solution = Solution()
    assert solution.kthGrammar(N=1, K=1) == '0'
    assert solution.kthGrammar(N=2, K=1) == '0'
    assert solution.kthGrammar(N=2, K=2) == '1'
    assert solution.kthGrammar(N=4, K=5) == '1'
