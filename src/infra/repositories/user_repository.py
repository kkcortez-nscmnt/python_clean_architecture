from src.domain.models import Users
from src.infra.config import DBConnectionHandler
from src.infra.entities import Users as UsersModel


class UserRepository:
    """Implementação do repositorio da entidade Users"""

    def insert_user(self, name: str, password: str) -> Users:
        """
        Insere data na entidade User
        :param - name: person name
               - password: user password
        :return - nameduple InsertedData
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_user = UsersModel(name=name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()

                return Users(
                    id=new_user.id, name=new_user.name, password=new_user.password
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None
