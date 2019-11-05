from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializer import LeadSerializer
# viewset


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()  # define model
    permission_classes = [  # permission
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer  # serializer class
