from sqlalchemy.orm import Session

from models import Movie


def get_movies(db: Session) -> list[Movie]:
    try:
        movies = (
            db.query(Movie)
            .filter(Movie.is_deleted.is_(False))
            .order_by(Movie.release_date)
            .all()
        )
        return movies
    except Exception as e:
        raise e
