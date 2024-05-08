from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Animal
from .serializers import AnimalSerializer

@csrf_exempt
def get_all_animals(request):
    if request.method == 'GET':
        animals = Animal.objects.all()
        serializer = AnimalSerializer(animals, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def get_animal(request, animal_id):
    try:
        animal = Animal.objects.get(id=animal_id)
    except Animal.DoesNotExist:
        return JsonResponse({'error': 'Animal not found'}, status=404)

    if request.method == 'GET':
        serializer = AnimalSerializer(animal)
        return JsonResponse(serializer.data)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def add_animal(request):
    if request.method == 'POST':
        data = request.POST
        serializer = AnimalSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
