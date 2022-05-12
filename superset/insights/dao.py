from superset.dao.base import BaseDAO
from superset.insights.models import Insight
from superset.insights.filters import InsightFilter
from superset.extensions import db


class InsightDAO(BaseDAO):
    model_cls = Insight
    base_filter = InsightFilter

    @staticmethod
    def save(ins: Insight, commit: bool = True) -> None:
        db.session.add(ins)
        if commit:
            db.session.commit()

    @staticmethod
    def overwrite(ins: Insight, commit: bool = True) -> None:
        db.session.merge(ins)
        if commit:
            db.session.commit()
