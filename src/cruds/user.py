from sqlalchemy.orm import Session

from models import User


def get_user_by_id(db: Session, user_id: str) -> User:
    try:
        user = db.query(User).filter(User.user_id == user_id).first()
        if user is None:
            raise Exception("ユーザは削除済です")
        else:
            return user
    except Exception as e:
        raise e
