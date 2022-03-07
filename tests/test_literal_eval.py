import unittest
from tocode import literal_eval


class MyTestCase(unittest.TestCase):
    def test_literal_eval(self):
        assert literal_eval("[    this    is a cool lib     ,{'e':     k, 4:2},j, 5, ([v    r, f,[4]], 4)]",
                            no_string_quotation=True) == \
               ['this    is a cool lib', {'e': 'k', 4: 2}, 'j', 5, (['v    r', 'f', [4]], 4)]

        assert literal_eval("['hello', 5, 4,'f','r','f','r','e','f',{'e': 4}]") == ['hello', 5, 4, 'f', 'r', 'f', 'r',
                                                                                    'e', 'f', {'e': 4}]

        assert literal_eval("['ABC', 5, ('d', 4)]") == ['ABC', 5, ('d', 4)]
        assert literal_eval("(['ABC', 5, ('d', 4)], ddd)", no_string_quotation=True) == (['ABC', 5, ('d', 4)], 'ddd')
        assert literal_eval("{'ABC 9': 5, 'd':  l44455    }", no_string_quotation=True) == {'ABC 9': 5,
                                                                                            'd': 'l44455   '}
        assert literal_eval("{'d':  4     }", no_string_quotation=True) == {'d': 4}
        assert literal_eval("{(('ABC',2), 'ddd'): 5}", no_string_quotation=True) == {(('ABC', 2), 'ddd'): 5}
        assert literal_eval("['this  ,  is a cool lib', 'j', 5, {'e': 4}, (['v    r', 'f', [4]], 4)]") == [
            'this  ,  is a cool lib', 'j', 5, {'e': 4}, (['v    r', 'f', [4]], 4)]


if __name__ == '__main__':
    unittest.main()
