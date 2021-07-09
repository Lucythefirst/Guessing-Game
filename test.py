import unittest
import guessing_game

class TestGame(unittest.TestCase):
    def test_input(self):
        result = guessing_game.run_guess(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = guessing_game.run_guess(0, 5)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = guessing_game.run_guess(11, 5)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = guessing_game.run_guess('a', 5)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()

