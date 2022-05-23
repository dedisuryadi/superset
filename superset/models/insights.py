"""a collection of Annotation-related models"""
from typing import Any, Dict

from flask_appbuilder import Model
from sqlalchemy import Column, DateTime, ForeignKey, Index, Integer, String, Text
from sqlalchemy.orm import relationship

from superset.models.helpers import AuditMixinNullable

# class InsightsModels(Model, AuditMixinNullable):
class InsightsModels(Model):
    """A logical namespace for a set of annotations"""
    __tablename__ = "insights"
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    descr = Column(Text)

    def __repr__(self) -> str:
        return str(self.name)
