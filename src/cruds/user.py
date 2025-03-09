from sqlalchemy.orm import Session

from models import User


def get_users(db: Session) -> list[User]:
    try:
        users = db.query(User).all()
        return users
    except Exception as e:
        raise e


def get_user_by_id(db: Session, user_id: str) -> User:
    try:
        if user_id is None:
            raise Exception("user_idは必須です")
        else:
            user = db.query(User).filter(User.user_id == user_id).first()
            if user is None:
                raise Exception("ユーザは削除済です")
            else:
                return user
    except Exception as e:
        raise e
