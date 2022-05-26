from src.infra.config import Base, DBConnectionHandler
from src.infra.entities import *

if __name__ == '__main__':
    engine = DBConnectionHandler().get_engine()
    Base.metadata.create_all(bind=engine)
