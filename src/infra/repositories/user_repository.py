from typing import List

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

    def select_user(self, user_id: int = None, name: str = None) -> List[Users]:
        """
        Seleciona dados na entidade de usuario pelo id ou pelo nome
        :Param - user_id: Id do registro
               - name: User name
        :return - Lista com os dados selecionados
        """
        try:
            query_data = None

            if user_id and not name:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(UsersModel)
                        .filter_by(id=user_id)
                        .one()
                    )
                    query_data = [data]

            elif not user_id and name:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(UsersModel)
                        .filter_by(name=name)
                        .one()
                    )
                    query_data = [data]

            elif user_id and name:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(UsersModel)
                        .filter_by(id=user_id, name=name)
                        .one()
                    )
                    query_data = [data]
            return query_data

        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()

        return None
