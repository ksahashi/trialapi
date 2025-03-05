from sqlalchemy import Column
from sqlalchemy.types import Boolean, Date, DateTime, Integer, String

from database import Base

from .mixin import BaseMixin


class Movie(Base):
    __tablename__ = "movies"
    movie_code = Column(String(6), primary_key=True, nullable=False, comment="映画コード")
    title = Column(String(255), nullable=False, comment="タイトル")
    release_date = Column(Date, nullable=False, comment="公開日")
    recommendation = Column(Integer, nullable=True, comment="おすすめ")
    is_deleted = Column(Boolean, nullable=False, comment="削除フラグ")
    deleted_at = Column(DateTime, nullable=True, comment="削除日時")
