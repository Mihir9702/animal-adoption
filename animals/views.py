from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Animal
from .serializers import AnimalSerializer

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    # permission_classes = [IsAuthenticated]  # Only authenticated users can access

    def list(self, request):
        animals = self.get_queryset()
        serializer = AnimalSerializer(animals, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        animal = self.get_object()
        serializer = AnimalSerializer(animal)
        return Response(serializer.data)

    def update(self, request, pk=None, partial=False):
        # Update animal details (modify based on your needs)
        animal = self.get_object()
        serializer = AnimalSerializer(animal, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Add an endpoint for adoption functionality (e.g., POST request with animal ID)
    def adopt(self, request, pk=None):
        user = request.user  # Get the authenticated user
        animal = self.get_object()

        if animal.adopted:
            return Response({'error': 'Animal is already adopted.'}, status=status.HTTP_400_BAD_REQUEST)

        animal.adopted = True
        animal.adopted_by = user
        animal.save()

        serializer = AnimalSerializer(animal)
        return Response(serializer.data)
