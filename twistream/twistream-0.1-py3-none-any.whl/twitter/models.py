from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Status(Base):
    """
    SQLAlchemy model to represent a status. Can be used with any backend that is supported by SQLAlchemy: i.e sqlite,
    MySQL or PostgreSQL
    """
    __tablename__ = "status"

    id = Column(Integer, primary_key=True)
    tweet = Column(String(140))
    created_at = Column(DateTime(timezone=True))
    user_handle = Column(String(100))
    user_id = Column(String(40))
    followers_count = Column(Integer)

    def __init__(self, tweet_id, tweet, created_at, user_handle, followers_count):
        self.id = tweet_id
        self.tweet = tweet
        self.created_at = created_at
        self.user_handle = user_handle
        self.followers_count = followers_count

    def __repr__(self):
        return f'<{self.user_handle}: {self.tweet}>'
