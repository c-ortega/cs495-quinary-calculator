import unittest
from quinary import Calc

def enter(calc, s):
    for ch in s:
        calc.push_digit(ch)

class TestQuinaryCalculator(unittest.TestCase):
    def setUp(self):
        self.c = Calc()

    def test_add(self):
        enter(self.c, "13"); self.c.set_operation("+"); enter(self.c, "3"); self.c.equal()
        self.assertEqual(self.c.get_display_quinary(), "21")  # 8+3=11 -> 21

    def test_sub(self):
        enter(self.c, "13"); self.c.set_operation("-"); enter(self.c, "3"); self.c.equal()
        self.assertEqual(self.c.get_display_quinary(), "10")  # 8-3=5 -> 10

    def test_mul(self):
        enter(self.c, "13"); self.c.set_operation("*"); enter(self.c, "3"); self.c.equal()
        self.assertEqual(self.c.get_display_quinary(), "44")  # 8*3=24 -> 44

    def test_div(self):
        enter(self.c, "13"); self.c.set_operation("/"); enter(self.c, "3"); self.c.equal()
        self.assertEqual(self.c.get_display_quinary(), "2")   # 8//3=2 -> 2

    def test_sq(self):
        enter(self.c, "4"); self.c.set_operation("sq")
        self.assertEqual(self.c.get_display_quinary(), "31")  # 4^2=16 -> 31

    def test_sqrt(self):
        enter(self.c, "31"); self.c.set_operation("sqrt")
        self.assertEqual(self.c.get_display_quinary(), "4")   # sqrt(16)=4 -> 4

if __name__ == "__main__":
    unittest.main()