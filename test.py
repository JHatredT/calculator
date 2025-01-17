from parser import Parser
from unittest import (
    TestCase,
    main
)


class TestParseFunction(TestCase):
    def test_parse_valid(self) -> None:
        parser = Parser()

        self.assertEqual(parser.parse('3+5−2×4÷2'), 4)
        self.assertEqual(parser.parse('6×3÷2+7−1'), 15)
        self.assertEqual(parser.parse('9−4+8×2÷5'), eval('9-4+8*2/5'))
        self.assertEqual(parser.parse('2×7−5÷3+6'), eval('2*7-5/3+6'))
        self.assertEqual(parser.parse('5−3+6×2÷7'), eval('5-3+6*2/7'))
        self.assertEqual(parser.parse('4×5−2÷6+3'), eval('4*5-2/6+3'))
        self.assertEqual(parser.parse('7+8÷4×3−2'), 11)
        self.assertEqual(parser.parse('6×2−3÷1+5'), 14)
        self.assertEqual(parser.parse('2+8÷(2×4)−2'), 1)
        self.assertEqual(parser.parse('3+(5−1)÷2'), 5)
        self.assertEqual(parser.parse('7+(2÷5)×(4−6)'), eval('7+(2/5)*(4-6)'))
        self.assertEqual(parser.parse('((3+2)×(9−8)+1)+5÷2'), eval('((3+2)*(9-8)+1)+5/2'))

    def test_parse_invalid(self) -> None:
        parser = Parser()
        
        self.assertRaises(ValueError, parser.parse, '3+−5×2')
        self.assertRaises(ValueError, parser.parse, '6×÷4−2')
        self.assertRaises(ValueError, parser.parse, '−7+8÷')
        self.assertRaises(ValueError, parser.parse, '4×+3−1')
        self.assertRaises(ValueError, parser.parse, '8÷2×−3+4')
        self.assertRaises(ValueError, parser.parse, '5+×6−2÷')
        self.assertRaises(ValueError, parser.parse, '2×−5÷3+')
        self.assertRaises(ValueError, parser.parse, '+7−4×8÷2')
        self.assertRaises(ValueError, parser.parse, '(+2×7)-8÷2')
        self.assertRaises(ValueError, parser.parse, ')9-3(−2×3÷1')
        self.assertRaises(ValueError, parser.parse, '3−5×((7÷6)+1')
        self.assertRaises(ValueError, parser.parse, '+7−4×8÷2')


if __name__ == '__main__':
    main()