"""Tests for the Hero class"""
import unittest
from hero import Hero
class TestHero(unittest.TestCase):
    # Do test setup
    def setUp(self):
        # Create a Hero instance for testing
        self.hero = Hero()

# Run the tests
unittest.main()