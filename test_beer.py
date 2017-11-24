from contextlib import contextmanager

try:
    from StringIO import StringIO
except ImportError:
    # This is neccessary for Python 3.x which moves StringIO into io.
    from io import StringIO

import unittest, sys

from beer import pluralize, bottle_beer, _beer_printer


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class TestBeer(unittest.TestCase):
    def test_pluralize(self):
        self.assertEqual(pluralize(100**100), 's')
        self.assertEqual(pluralize(2), 's')
        self.assertEqual(pluralize(1), '')
        self.assertEqual(pluralize(0), 's')
        self.assertEqual(pluralize(-1), 's')

    def test_bottle_beer(self):
        self.assertEqual(bottle_beer(100), '100 bottles of beer')
        self.assertEqual(bottle_beer(2), '2 bottles of beer')
        self.assertEqual(bottle_beer(1), '1 bottle of beer')
        self.assertEqual(bottle_beer(0), '0 bottles of beer')
        self.assertEqual(bottle_beer(-1), '-1 bottles of beer')

    def test_beer_printer_with_100_beers(self):
        expected = ('100 bottles of beer on the wall. 100 bottles of beer.\n'
                    'Take one down, pass it around, 99 bottles of beer on the wall.\n--')
        with captured_output() as (out, err):
            _beer_printer(100)
            self.assertEqual(out.getvalue().strip(), expected)

    def test_beer_printer_with_2_beers(self):
        expected = ('2 bottles of beer on the wall. 2 bottles of beer.\n'
                    'Take one down, pass it around, 1 bottle of beer on the wall.\n--')
        with captured_output() as (out, err):
            _beer_printer(2)
            self.assertEqual(out.getvalue().strip(), expected)

    def test_beer_printer_with_1_beer(self):
        expected = ('1 bottle of beer on the wall. 1 bottle of beer.\n'
                    'Take one down, pass it around, no more bottles of beer on the wall.')
        with captured_output() as (out, err):
            _beer_printer(1)
            self.assertEqual(out.getvalue().strip(), expected)

    def test_beer_printer_with_0_beers(self):
        expected = ('0 bottles of beer on the wall. 0 bottles of beer.\n'
                    'Take one down, pass it around, no more bottles of beer on the wall.')
        with captured_output() as (out, err):
            _beer_printer(0)
            self.assertEqual(out.getvalue().strip(), expected)


if __name__ == '__main__':
    unittest.main()
