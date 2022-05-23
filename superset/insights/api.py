import logging
from typing import Any

from flask import g, request, Response
from flask_appbuilder.api import expose, BaseApi, ModelRestApi, permission_name, protect, rison, safe

from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_babel import ngettext
from marshmallow import ValidationError
from flask_appbuilder.security.decorators import protect

from superset.models.insights import InsightsModels
from superset.views.base_api import (
    BaseSupersetModelRestApi,
    requires_json,
    statsd_metrics,
)

# from . import appbuilder

greeting_schema = {"type": "object", "properties": {"name": {"type": "string"}}}


# BaseSupersetModelRestApi
# ModelRestApi
class InsightsLayerRestApi(BaseSupersetModelRestApi):
    resource_name = 'insights'    
    datamodel = SQLAInterface(InsightsModels)
    
    # route_base = '/api/v1'
    # route_base = '/newapi/v2/nice'

    # @expose('/greeting')
    # def greeting(self):
    #     """Send a greeting
    #     ---
    #     get:
    #         description: >-
    #             Returns the user object corresponding to the agent making the request,
    #             or returns a 401 error if the user is unauthenticated.
    #         responses:
    #             200:
    #                 description: Greet the user
    #                 content:
    #                     application/json:
    #                         schema:
    #                             type: object
    #                             properties:
    #                                 message:
    #                                     type: string
    #             401:
    #                 $ref: '#/components/responses/401'

    #     """
    #     return self.response(200, message="Hello")    
    
    
    # @expose('/greeting1', methods=['POST', 'GET'])
    # def greeting1(self):
    #     """Send a Greeting
    #     ---
    #     get:
    #         responses:
    #             200:
    #                 description: Greet the user
    #                 content:
    #                     application/json:
    #                         schema:
    #                             type: object
    #                             properties:
    #                                 message:
    #                                     type: string
    #     post:
    #         responses:
    #             201:
    #                 description: Greet the user
    #                 content:
    #                     application/json:
    #                         schema:
    #                             type: object
    #                             properties:
    #                                 message:
    #                                     type: string
    #     """
    #     if request.method == 'GET':
    #         return self.response(200, message="Hello (GET)")
    #     return self.response(201, message="Hello (POST)")

    
    # @expose('/greeting_param')
    # @rison()
    # def greeting_param(self, **kwargs):
    #     if 'name' in kwargs['rison']:
    #         return self.response(
    #             200,
    #             message=f"Hello {kwargs['rison']['name']}"
    #         )
    #     return self.response_400(message="Please send your name")     


    # @expose("/add", methods=["POST"])
    # @protect()
    # @safe
    # @statsd_metrics
    # @permission_name("post")
    # @event_logger.log_this_with_context(
    #     action=lambda self, *args, **kwargs: f"{self.__class__.__name__}.post",
    #     log_to_statsd=False,
    # )
    # @requires_json
    # def post(self) -> Response:
    #     """Creates a new Insight 
    #     ---
    #     post:
    #       description: >-
    #         Create a new Insight
    #       requestBody:
    #         description: Insight schema
    #         required: true
    #         content:
    #           application/json:
    #             schema:
    #               $ref: '#/components/schemas/{{self.__class__.__name__}}.post'
    #       responses:
    #         201:
    #           description: Insight added
    #           content:
    #             application/json:
    #               schema:
    #                 type: object
    #                 properties:
    #                   id:
    #                     type: number
    #                   result:
    #                     $ref: '#/components/schemas/{{self.__class__.__name__}}.post'
    #         400:
    #           $ref: '#/components/responses/400'
    #         401:
    #           $ref: '#/components/responses/401'
    #         404:
    #           $ref: '#/components/responses/404'
    #         500:
    #           $ref: '#/components/responses/500'
    #     """
    #     try:
    #         item = self.add_model_schema.load(request.json)
    #     # This validates custom Schema with custom validations
    #     except ValidationError as error:
    #         return self.response_400(message=error.messages)
    #     try:
    #         new_model = CreateAnnotationLayerCommand(g.user, item).run()
    #         return self.response(201, id=new_model.id, result=item)
    #     except AnnotationLayerNotFoundError as ex:
    #         return self.response_400(message=str(ex))
    #     except AnnotationLayerInvalidError as ex:
    #         return self.response_422(message=ex.normalized_messages())
    #     except AnnotationLayerCreateFailedError as ex:
    #         logger.error(
    #             "Error creating annotation %s: %s",
    #             self.__class__.__name__,
    #             str(ex),
    #             exc_info=True,
    #         )
    #         return self.response_422(message=str(ex))

# appbuilder.add_api(ExampleApi)