import doctest
import unittest


optionflags = doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE


def bprint(s):
    print(s.strip())


def test_suite():
    return unittest.TestSuite(
        [
            doctest.DocFileSuite(
                "README.rst",
                globs={"bprint": bprint},
                encoding="utf-8",
                optionflags=optionflags,
            )
        ]
    )
