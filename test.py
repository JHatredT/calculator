from parser import Parser
from unittest import (
    TestCase,
    main
)
from math import (
    sin,
    cos,
    tan
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
        self.assertEqual(
            parser.parse('((3+2)×(9−8)+1)+5÷2'),
            eval('((3+2)*(9-8)+1)+5/2')
        )
        self.assertEqual(
            parser.parse('sin(1)+cos(1)×tan(1)÷sin(2)'),
            eval('sin(1)+cos(1)*tan(1)/sin(2)')
        )
        self.assertEqual(
            parser.parse('cos(1)×sin(1)−tan(1)÷cos(2)×sin(3)'),
            eval('cos(1)*sin(1)-tan(1)/cos(2)*sin(3)')
        )
        self.assertEqual(
            parser.parse('sin(1)+cos(2)÷tan(1)×sin(3)−cos(4)×sin(5)'),
            eval('sin(1)+cos(2)/tan(1)*sin(3)-cos(4)*sin(5)')
        )
        self.assertEqual(
            parser.parse('tan(1)×sin(1)÷cos(2)−sin(3)×cos(1)+tan(4)÷sin(5)'),
            eval('tan(1)*sin(1)/cos(2)-sin(3)*cos(1)+tan(4)/sin(5)')
        )

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