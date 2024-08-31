from sqlalchemy import Column, Integer, BigInteger

from .db import Base


class Counter(Base):
    __tablename__ = "counter"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(BigInteger, nullable=False)
    counter = Column(Integer, nullable=False)
