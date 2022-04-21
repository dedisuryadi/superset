from .base import BaseSupersetView
from flask_appbuilder import expose
from superset.superset_typing import FlaskResponse


class Lab(BaseSupersetView):
    @expose("/visualanalytic/")
    def visualanalytic(self) -> FlaskResponse:
        return super().render_app_template()
