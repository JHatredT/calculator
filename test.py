from main import parse
from unittest import (
    TestCase,
    main
)


class TestParseFunction(TestCase):
    def test_parse_valid(self) -> None:
        self.assertEqual(parse("3+5−2×4÷2"), 4),
        self.assertEqual(parse("6×3÷2+7−1"), 15),
        self.assertEqual(parse("9−4+8×2÷5"), eval('9-4+8*2/5')),
        self.assertEqual(parse("2×7−5÷3+6"), eval('2*7-5/3+6')),
        self.assertEqual(parse("5−3+6×2÷7"), eval('5-3+6*2/7')),
        self.assertEqual(parse("4×5−2÷6+3"), eval('4*5-2/6+3')),
        self.assertEqual(parse("7+8÷4×3−2"), 11),
        self.assertEqual(parse("6×2−3÷1+5"), 14)

    def test_parse_invalid(self) -> None:
        for expr in (
            '3+−5×2',
            '6×÷4−2',
            '−7+8÷',
            '4×+3−1',
            '8÷2×−3+4',
            '5+×6−2÷',
            '2×−5÷3+',
            '+7−4×8÷2'
        ):
            with self.assertRaises(ValueError):
                parse(expr)


if __name__ == '__main__':
    main()