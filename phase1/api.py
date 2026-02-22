from .models import Product
from rest_framework import viewsets, permissions
from .serializers import serializerProduct

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializerProduct