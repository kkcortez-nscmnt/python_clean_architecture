"""Cria o Handler de conexão com a DataBase"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    """Conexao com a base de dados da SqlAlchemy"""

    def __init__(self) -> None:
        self.__connection_string = "sqlite:///storage.db"
        self.session = None

    def get_engine(self):
        """
        Return engine necessaria para a conexão com a DataBase
        :param - None
        :return - engine
        """
        engine = create_engine(self.__connection_string)
        return engine

    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
