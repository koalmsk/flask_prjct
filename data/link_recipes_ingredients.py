import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class RecipesToIngredients(SqlAlchemyBase):
    __tablename__ = 'recipes_to_ingredients'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    recipes_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("recipes.id"))
    ingredients_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("ingredients.id"))
    count = sqlalchemy.Column(sqlalchemy.Float)
    mesure = sqlalchemy.Column(sqlalchemy.String)

    recipes_rel = orm.relationship("Recipes", back_populates='link_rel')
    ingredients_rel = orm.relationship("Ingredients", back_populates='link_rel')