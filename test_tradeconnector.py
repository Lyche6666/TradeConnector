# test_tradeconnector.py
"""
Tests for TradeConnector module.
"""

import unittest
from tradeconnector import TradeConnector

class TestTradeConnector(unittest.TestCase):
    """Test cases for TradeConnector class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TradeConnector()
        self.assertIsInstance(instance, TradeConnector)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TradeConnector()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
