from core.tokenizer import Tokenizer
from core.parser import Parser
from core.evaluator import Evaluator
from unittest import TestCase, main
from math import sin, cos, tan


tokenizer = Tokenizer()
parser = Parser()
evaluator = Evaluator()


def calc(expr: str):
    seq = tokenizer.tokenize(expr)
    tree = parser.parse(seq)
    result = evaluator.evaluate(tree)

    return result


class TestParser(TestCase):
    def test_parse_valid(self) -> None:
        self.assertEqual(calc('3+5−2×4÷2'), 4)
        self.assertEqual(calc('6×3÷2+7−1'), 15)
        self.assertEqual(calc('9−4+8×2÷5'), eval('9-4+8*2/5'))
        self.assertEqual(calc('2×7−5÷3+6'), eval('2*7-5/3+6'))
        self.assertEqual(calc('5−3+6×2÷7'), eval('5-3+6*2/7'))
        self.assertEqual(calc('4×5−2÷6+3'), eval('4*5-2/6+3'))
        self.assertEqual(calc('7+8÷4×3−2'), 11)
        self.assertEqual(calc('6×2−3÷1+5'), 14)
        self.assertEqual(calc('2+8÷(2×4)−2'), 1)
        self.assertEqual(calc('3+(5−1)÷2'), 5)
        self.assertEqual(calc('7+(2÷5)×(4−6)'), eval('7+(2/5)*(4-6)'))
        self.assertEqual(
            calc('((3+2)×(9−8)+1)+5÷2'),
            eval('((3+2)*(9-8)+1)+5/2')
        )
        self.assertEqual(
            calc('sin(1)+cos(1)×tan(1)÷sin(2)'),
            eval('sin(1)+cos(1)*tan(1)/sin(2)')
        )
        self.assertEqual(
            calc('cos(1)×sin(1)−tan(1)÷cos(2)×sin(3)'),
            eval('cos(1)*sin(1)-tan(1)/cos(2)*sin(3)')
        )
        self.assertEqual(
            calc('sin(1)+cos(2)÷tan(1)×sin(3)−cos(4)×sin(5)'),
            eval('sin(1)+cos(2)/tan(1)*sin(3)-cos(4)*sin(5)')
        )
        self.assertEqual(
            calc('tan(1)×sin(1)÷cos(2)−sin(3)×cos(1)+tan(4)÷sin(5)'),
            eval('tan(1)*sin(1)/cos(2)-sin(3)*cos(1)+tan(4)/sin(5)')
        )

    def test_parse_invalid(self) -> None:
        parser = Parser()
        
        self.assertRaises(ValueError, calc, '6×÷4−2')
        self.assertRaises(ValueError, calc, '−7+8÷')
        self.assertRaises(ValueError, calc, '5+×6−2÷')
        self.assertRaises(ValueError, calc, '2×−5÷3+')
        self.assertRaises(ValueError, calc, ')9-3(−2×3÷1')
        self.assertRaises(ValueError, calc, '3−5×((7÷6)+1')


if __name__ == '__main__':
    main()