# -*- coding: utf-8 -*-
import doctest
import unittest

optionflags = (doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)


def bprint(s):
    if not isinstance(s, str):
        s = s.decode()
    print(s.strip())


def test_suite():
    return unittest.TestSuite([
        doctest.DocFileSuite(
            'README.rst',
            globs={'bprint': bprint},
            encoding='utf-8',
            optionflags=optionflags,
        )
    ])
