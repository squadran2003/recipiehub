from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .models import Recipie
from .serializers import RecipieSerialier, RecipieDetailSerialier


class RecipieList(APIView):
    """
    List all recipies, or create a new recipie.
    """

    def get(self, request, format=None):
        recipies = Recipie.objects.all()
        serializer = RecipieSerialier(recipies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        request.data.update({'user': request.user.id})
        serializer = RecipieSerialier(
            data=request.data,
            context={
                'user_id': request.user.id,
                'ingredients': request.data.get('ingredients'),
                'instructions': request.data.get('instructions')
            }

        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecipieDetail(APIView):
    """
    Retrieve, update or delete a recipie instance.
    """

    def get_object(self, pk):
        try:
            return Recipie.objects.get(pk=pk)
        except Recipie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = RecipieDetailSerialier(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        request.data.update({'user':request.user.id})
        recipie = self.get_object(pk)
        serializer = RecipieSerialier(
            recipie, data=request.data,
            context={'user_id': request.user.id}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        recipie = self.get_object(pk)
        recipie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
