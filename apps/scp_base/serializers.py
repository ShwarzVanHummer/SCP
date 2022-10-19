from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    ImageField
)
from .models import (
    SCPSafe,
    SCPEuclid,
    SCPKeter,
    SCPThaumiel,
    SCPAllClasses
)


class ScpSafeSerializer(ModelSerializer):
    title_object = CharField(required=False)
    description = CharField(required=False)
    image = ImageField()
    content = CharField(required=False)

    class Meta:
        model = SCPSafe
        fields = (
            '__all__'
        )


class ScpEuclidSerializer(ModelSerializer):
    title_object = CharField(required=False)
    description = CharField(required=False)
    image = CharField(required=False)
    content = CharField(required=False)

    class Meta:
        model = SCPSafe
        fields = (
            '__all__'
        )


class ScpKeterSerializer(ModelSerializer):
    title_object = CharField(required=False)
    description = CharField(required=False)
    image = CharField(required=False)
    content = CharField(required=False)

    class Meta:
        model = SCPSafe
        fields = (
            '__all__'
        )


class ScpThaumielSerializer(ModelSerializer):
    title_object = CharField(required=False)
    description = CharField(required=False)
    image = CharField(required=False)
    content = CharField(required=False)

    class Meta:
        model = SCPSafe
        fields = (
            '__all__'
        )


class ScpAllSerializer(ModelSerializer):
    scp_safe = CharField(required=False)
    scp_euclid = CharField(required=False)
    scp_keter = CharField(required=False)
    scp_thaumiel = CharField(required=False)

    class Meta:
        model = SCPSafe
        fields = (
            '__all__'
        )
