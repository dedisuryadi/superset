from typing import Any, Dict

from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, Text

from superset.models.helpers import AuditMixin


class Insight(Model, AuditMixin):

    """Map Insight"""

    __tablename__ = "insights"
    id = Column(Integer, primary_key=True)
    title = Column(String(500), nullable=False)
    description = Column(Text, default="")
    meta = Column(Text, nullable=False, default="{}")

    @property
    def data(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "meta": self.meta,
        }

    def __repr__(self) -> str:
        return str(self.description)
