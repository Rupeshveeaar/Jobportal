from rest_framework import serializers
from auth_app.models import *



class JobSerliazer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"
 