from .db import Base, engine
from .counterModel import Counter


def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Tables created")


if __name__ == "__main__":
    create_tables()
