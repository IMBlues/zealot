"""{{cookiecutter.license_header}}"""
from blue_krill.web.drf_utils import inject_serializer
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.template.response import TemplateResponse
from rest_framework import mixins, viewsets

from {{cookiecutter.api_name}}.common.error_codes import error_codes


class WebPageViewSet(viewsets.ViewSet):

    serializer_class = None

    permission_classes: list = []

    @inject_serializer(auto_schema=None, config={"remain_request": True})
    def index(self, request):
        """首页"""
        try:
            return TemplateResponse(request=request, template=get_template("index.html"))
        except TemplateDoesNotExist:
            raise error_codes.CANNOT_FIND_TEMPLATE
