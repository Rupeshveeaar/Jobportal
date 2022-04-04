
# from jobBunny.auth_app.models import Job
# from jobBunny.auth_app.seriealzers import JobSerliazer
from rest_framework.viewsets import ModelViewSet
# from auth_app import seriealzers JobSerliazer
from auth_app.seriealzers import JobSerliazer
from .models import Job

class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()     
    serializer_class  = JobSerliazer
 