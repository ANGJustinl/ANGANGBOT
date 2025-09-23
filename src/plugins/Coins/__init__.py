"""Coins plugin for managing user currency"""

from .database import CoinsDatabase

class Coins:
    """Main class for Coins plugin"""
    
    @staticmethod
    def get_balance(userid: int) -> float:
        """Get user's current balance
        
        Args:
            userid (int): User ID to check
            
        Returns:
            float: Current balance
        """
        return CoinsDatabase.get_balance(userid)
    
    @staticmethod
    def add_coins(userid: int, amount: float, reason: str = "") -> float:
        """Add coins to user's balance
        
        Args:
            userid (int): User ID to modify
            amount (float): Amount to add (can be negative)
            reason (str, optional): Transaction reason. Defaults to ""
            
        Returns:
            float: New balance after modification
        """
        return CoinsDatabase.add_coins(userid, amount, reason)
    
    @staticmethod
    def claim_daily(userid: int, amount: float = 100.0) -> bool:
        """Try to claim daily coins
        
        Args:
            userid (int): User ID to claim for
            amount (float, optional): Amount to claim. Defaults to 100.0
            
        Returns:
            bool: True if claimed successfully, False if already claimed today
        """
        return CoinsDatabase.claim_daily(userid, amount)
    
    @staticmethod
    def get_history(userid: int, limit: int = 10) -> list:
        """Get user's transaction history
        
        Args:
            userid (int): User ID to check
            limit (int, optional): Number of records to return. Defaults to 10
            
        Returns:
            list: List of transaction records
        """
        return CoinsDatabase.get_transaction_history(userid, limit)