"""Database module for Coins plugin"""

import os
from typing import Dict, List, Optional
from datetime import datetime

from sqlalchemy import (
    Column,
    Engine,
    Integer,
    Float,
    String,
    create_engine,
    orm,
)
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Database path configuration
DATA_PATH = "data/coins"

# Create directories if not exist
os.makedirs(DATA_PATH, exist_ok=True)

class DatabaseError(Exception):
    """Base exception for database operations"""
    pass

class BaseModel(orm.declarative_base()):
    """Base model with common methods"""
    __abstract__ = True

    @classmethod
    def create(cls, session: Session, **kwargs):
        """Create a new record"""
        instance = cls(**kwargs)
        session.add(instance)
        return instance

    def update(self, session: Session, **kwargs):
        """Update record with given fields"""
        for key, value in kwargs.items():
            setattr(self, key, value)
        session.add(self)

class UserData(BaseModel):
    """User coins data table"""
    __tablename__: str = "user_coins"

    userid = Column(Integer, primary_key=True, index=True)
    coins = Column(Float, nullable=False, default=0.0)
    last_daily = Column(String(20), nullable=True)

    def __str__(self) -> str:
        return f"User(id={self.userid}, coins={self.coins})"

    def __repr__(self) -> str:
        return f"UserData(userid={self.userid}, coins={self.coins}, last_daily={self.last_daily})"

class TransactionData(BaseModel):
    """Transaction history table"""
    __tablename__: str = "transactions"

    id = Column(Integer, primary_key=True)
    userid = Column(Integer, nullable=False, index=True)
    amount = Column(Float, nullable=False)
    description = Column(String(100), nullable=False)
    timestamp = Column(String(20), nullable=False)

    def __str__(self) -> str:
        return f"Transaction(user={self.userid}, amount={self.amount}, desc={self.description})"

class CoinsDatabase:
    """Database manager with singleton pattern and context management"""
    _instance = None
    _engine: Optional[Engine] = None
    _session_maker = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._engine = create_engine(f"sqlite:///{DATA_PATH}/coins.db")
            cls._session_maker = sessionmaker(cls._engine)
            BaseModel.metadata.create_all(cls._engine)
        return cls._instance

    def __enter__(self) -> Session:
        self.session = self._session_maker()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.session.rollback()
            self.session.close()
            raise DatabaseError(f"Database operation failed: {str(exc_val)}")
        try:
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise DatabaseError(f"Failed to commit: {str(e)}")
        finally:
            self.session.close()

    @classmethod
    def get_user(cls, userid: int) -> Optional[UserData]:
        """Get user data, create if not exists"""
        with cls() as session:
            user = session.query(UserData).filter(UserData.userid == userid).first()
            if not user:
                user = UserData.create(
                    session,
                    userid=userid,
                    coins=0.0
                )
            return user

    @classmethod
    def add_coins(cls, userid: int, amount: float, description: str = "") -> float:
        """Add coins to user and record transaction"""
        with cls() as session:
            user = cls.get_user(userid)
            new_balance = round(user.coins + amount, 2)
            user.update(session, coins=new_balance)
            
            TransactionData.create(
                session,
                userid=userid,
                amount=amount,
                description=description,
                timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
            return new_balance

    @classmethod
    def get_balance(cls, userid: int) -> float:
        """Get user's current balance"""
        user = cls.get_user(userid)
        return user.coins

    @classmethod
    def claim_daily(cls, userid: int, amount: float) -> bool:
        """Try to claim daily coins"""
        today = datetime.now().strftime("%Y-%m-%d")
        
        with cls() as session:
            user = cls.get_user(userid)
            if user.last_daily == today:
                return False
                
            user.update(session, 
                coins=user.coins + amount,
                last_daily=today
            )
            
            TransactionData.create(
                session,
                userid=userid,
                amount=amount,
                description="Daily claim",
                timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
            return True

    @classmethod
    def get_transaction_history(cls, userid: int, limit: int = 10) -> List[Dict]:
        """Get user's recent transactions"""
        with cls() as session:
            transactions = session.query(TransactionData)\
                .filter(TransactionData.userid == userid)\
                .order_by(TransactionData.id.desc())\
                .limit(limit)\
                .all()
            
            return [{
                "amount": t.amount,
                "description": t.description,
                "timestamp": t.timestamp
            } for t in transactions]

    def __str__(self) -> str:
        return "CoinsDatabase(singleton instance)"

    def __repr__(self) -> str:
        return f"CoinsDatabase(engine={self._engine})"