import logging
from typing import Any, Optional
from flask import g, redirect, request, Response, url_for
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelRestApi
from flask_appbuilder.api import expose, protect, rison, safe

from superset.insights.dao import InsightDAO
from superset.insights.models import Insight
from superset.insights.filters import InsightFilter
from superset.views.base_api import (
    BaseSupersetModelRestApi,
    RelatedFieldFilter
)
from superset.constants import MODEL_API_RW_METHOD_PERMISSION_MAP
from superset.views.filters import FilterRelatedOwners

logger = logging.getLogger(__name__)


class InsightRestApi(ModelRestApi):
    datamodel = SQLAInterface(Insight)

    resource_name = "insight"
    allow_browser_login = True

    class_permission_name = "Insight"
    method_permission_name = MODEL_API_RW_METHOD_PERMISSION_MAP

    base_order = ("changed_on", "desc")
    base_filters = [["id", InsightFilter, lambda: []]]

    related_field_filters = {
        "owners": RelatedFieldFilter("first_name", FilterRelatedOwners),
        "created_by": RelatedFieldFilter("first_name", FilterRelatedOwners),
    }

    allowed_rel_fields = {"owners", "created_by"}

    openapi_spec_tag = "Insights"
    # openapi_spec_methods = openapi_spec_methods_override

    # @protect
    # @safe
    @expose("/", methods=["POST"])
    def post(self) -> Response:
        item = self.add_model_schema.load(request.json)
        try:
            new_model = InsightDAO.create(item.copy())
            return self.response(201, id=new_model.id, result=item)
        except Exception as ex:
            logger.error(
                "Error creating model %s: %s",
                self.__class__.__name__,
                str(ex),
                exc_info=True,
            )
            return self.response_422(message=str(ex))
