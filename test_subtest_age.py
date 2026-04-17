import unittest
from age import categorize_by_age


class TestAgeCategories(unittest.TestCase):
    
    def test_child_category(self):
        """Test all ages in the child category (0-9)"""
        for age in range(0, 10):
            with self.subTest(age=age):
                result = categorize_by_age(age)
                self.assertEqual(result, "Child", f"Age {age} should be categorized as Child")
    
    def test_adolescent_category(self):
        """Test all ages in the adolescent category (10-18)"""
        for age in range(10, 19):
            with self.subTest(age=age):
                result = categorize_by_age(age)
                self.assertEqual(result, "Adolescent", f"Age {age} should be categorized as Adolescent")
    
    def test_adult_category(self):
        """Test all ages in the adult category (19-65)"""
        for age in range(19, 66):
            with self.subTest(age=age):
                result = categorize_by_age(age)
                self.assertEqual(result, "Adult", f"Age {age} should be categorized as Adult")


if __name__ == "__main__":
    unittest.main()
