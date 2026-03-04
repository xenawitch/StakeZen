# test_stakezen.py
"""
Tests for StakeZen module.
"""

import unittest
from stakezen import StakeZen

class TestStakeZen(unittest.TestCase):
    """Test cases for StakeZen class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = StakeZen()
        self.assertIsInstance(instance, StakeZen)
        
    def test_run_method(self):
        """Test the run method."""
        instance = StakeZen()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
