from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.infra.config import Base


class Users(Base):
    """Implementação da entidade Users"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    id_pet = relationship("Pets")

    def __repr__(self):
        return f"<User name={self.name}>"
