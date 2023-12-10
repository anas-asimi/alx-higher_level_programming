import unittest
from models.rectangle import Rectangle


class TestStringMethods(unittest.TestCase):

    def test_id_increment(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        index = r1.id

        self.assertEqual(r2.id, index + 1)
        self.assertEqual(r3.id, 12)

    def test_height_must_be_an_integer(self):
        with self.assertRaises(Exception) as context:
            Rectangle(10, "2")
        self.assertEqual(
            'height must be an integer', str(context.exception))

    def test_width_must_be_an_integer(self):
        with self.assertRaises(Exception) as context:
            Rectangle('10', 2)
        self.assertEqual(
            'width must be an integer', str(context.exception))

    def test_width_must_be_positive(self):
        with self.assertRaises(Exception) as context:
            r = Rectangle(10, 2)
            r.width = -10
        self.assertEqual(
            'width must be > 0', str(context.exception))

    def test_x_must_be_an_integer(self):
        with self.assertRaises(Exception) as context:
            r = Rectangle(10, 2)
            r.x = {}
        self.assertEqual(
            'x must be an integer', str(context.exception))

    def test_y_must_not_be_negative(self):
        with self.assertRaises(Exception) as context:
            Rectangle(10, 2, 3, -1)
        self.assertEqual(
            'y must be >= 0', str(context.exception))

    def test_area(self):
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)

        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        pass

    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r1), '[Rectangle] (12) 2/1 - 4/6')
        self.assertEqual(str(r2), '[Rectangle] ({}) 1/0 - 5/5'.format(r2.id))

    def test_update_with_args(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.id = 1
        self.assertEqual(str(r1), '[Rectangle] (1) 10/10 - 10/10')
        r1.update(89)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 10/10')
        r1.update(89, 2)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 2/10')
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 2/3')
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), '[Rectangle] (89) 4/10 - 2/3')
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), '[Rectangle] (89) 4/5 - 2/3')

    def test_update_with_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.id = 1
        self.assertEqual(str(r1), '[Rectangle] (1) 10/10 - 10/10')
        r1.update(height=1)
        self.assertEqual(str(r1), '[Rectangle] (1) 10/10 - 10/1')
        r1.update(width=1, x=2)
        self.assertEqual(str(r1), '[Rectangle] (1) 2/10 - 1/1')
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), '[Rectangle] (89) 3/1 - 2/1')
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), '[Rectangle] (89) 1/3 - 4/2')


if __name__ == '__main__':
    unittest.main()
