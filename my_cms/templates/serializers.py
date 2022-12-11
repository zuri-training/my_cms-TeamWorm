from rest_framework import serializers
from .models import AllTemplates
from .models import UserTemplate


class AllTemplatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllTemplates
        fields = "__all__"

class UserTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTemplate
        fields = "__all__"