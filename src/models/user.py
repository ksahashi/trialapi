from sqlalchemy import Column
from sqlalchemy.types import String
from sqlalchemy_utils import EmailType

from database import Base

from .mixin import BaseMixin


class User(Base):
    __tablename__ = "users"

    user_id = Column(String(15), primary_key=True, nullable=False, comment="ユーザID")
    user_name = Column(String(50), nullable=True, comment="ユーザ名")
    email_address = Column(EmailType, nullable=True, comment="メールアドレス")
