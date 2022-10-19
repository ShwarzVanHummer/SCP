
from django.db.models import QuerySet
from urllib.request import Request
from rest_framework.response import Response

from rest_framework.viewsets import ViewSet

from abstracts.mixins import ValidationMixin, ResponseMixin
from .serializers import (
    ScpSafeSerializer,
    ScpEuclidSerializer,
    ScpKeterSerializer,
    ScpThaumielSerializer,
    ScpAllSerializer
)
from .models import (
    SCPSafe,
    SCPEuclid,
    SCPKeter,
    SCPThaumiel,
    SCPAllClasses
)
from abstracts.permissions import ScpBasePermissons


class ScpSafeViewSet(ValidationMixin, ResponseMixin, ViewSet):

    queryset: QuerySet = SCPSafe.objects.all()

    permission_classes = (
        ScpBasePermissons,
    )
    serializer_class = ScpSafeSerializer

    def list(self, request: Request):
        serializer: ScpSafeSerializer = \
            ScpSafeSerializer(
                self.queryset,
                many=True
            )
        return self.get_json_response(
            serializer.data
        )

    def create(self, request: Request):
        serializer: ScpSafeSerializer = \
            ScpSafeSerializer(
                data=request.data
            )

        if not serializer.is_valid():
            return self.get_json_response(
                {
                    'message': 'Объект не был создан',
                    'playload': {}
                }
            )
        serializer.save()

        return self.get_json_response(
            {
                'message': 'Объект был создан',
            }
        )

    def update(self, request: Request, pk: str) -> Response:

        obj: SCPSafe = self.get_obj_or_raise(
            pk
        )
        serializer: ScpSafeSerializer = \
            ScpSafeSerializer(
                obj,
                data=request.data
            )
        request.data['obj_id'] = obj.pk
        breakpoint()
        if not serializer.is_valid():
            return self.get_json_response(
                {
                    'message': 'Объект не был обновлен',
                    'payload': request.data
                }
            )
        
        serializer.save()

        return self.get_json_response(
            {
                'message': 'Объект был обновлен',
                'payload': request.data
            }
        )

    def partial_update(self, request: Request, pk: str) -> Response:

        obj: SCPSafe = self.get_obj_or_raise(
            self.queryset,
            pk
        )
        serializer: ScpSafeSerializer = \
            ScpSafeSerializer(
                obj,
                data=request.data,
                partial=True
            )
        request.data['obj_id'] = obj.id

        if not serializer.is_valid():
            return self.get_json_response(
                {
                    'message': 'Объект не был частично-обновлен',
                    'payload': request.data
                }
            )

        serializer.save()

        return self.get_json_response(
            {
                'message': 'Объект был частично-обновлен',
                'payload': request.data
            }
        )

    def destroy(self, request: Request, pk: str) -> Response:

        obj: SCPSafe = self.get_obj_or_raise(
            self.queryset,
            pk
        )

        obj.delete()

        return self.get_json_response(
            {
                'message': 'Объект был удален',
                'payload': {
                    'obj_id': f'{obj.pk}',
                    'obj_deleted': f'{obj}',
                }
            }
        )