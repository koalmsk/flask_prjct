import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Ingredients(SqlAlchemyBase):
    __tablename__ = 'ingredients'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.Text, default="Тут пусто")

    # link_rel = orm.relationship("RecipesToIngredients", back_populates='ingredients_rel')