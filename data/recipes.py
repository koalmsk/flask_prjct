import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Recipes(SqlAlchemyBase):
    __tablename__ = 'recipes'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    servings = sqlalchemy.Column(sqlalchemy.Integer, default=1)
    instructions = sqlalchemy.Column(sqlalchemy.Text, nullable=True)

    link_rel = orm.relationship("Recipes_to_Ingredients", back_populates='recipes_rel')