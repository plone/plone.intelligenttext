import unittest
import doctest

optionflags = (doctest.ELLIPSIS |
               doctest.NORMALIZE_WHITESPACE)


def test_suite():
    return unittest.TestSuite([
        doctest.DocFileSuite('README.txt', 
                             optionflags=optionflags,)
        ])


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
