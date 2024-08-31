from sqlalchemy.orm import Session
from data.db import get_db_session

from data.counterModel import Counter


def increment_counter(user_id: int) -> int:
    with get_db_session() as db:
        counter = get_or_create_user_counter(db, user_id)
        counter.counter += 1
        db.commit()
    return counter.counter


def get_or_create_user_counter(db: Session, user_id: int) -> Counter:
    counter = db.query(Counter).filter(Counter.user_id == user_id).first()
    if counter is None:
        counter = Counter(user_id=user_id, counter=0)
        db.add(counter)
        db.commit()
        db.refresh(counter)
    return counter





