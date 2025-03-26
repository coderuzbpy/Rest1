from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView
from .models import Mirror
from .serializers import MirrorSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.


class MirrorList(APIView):
    def get(self, request):
        books = Mirror.objects.all()
        serializer = MirrorSerializer(books, many=True)
        rpns = {
            'data': serializer.data,
            'status': status.HTTP_200_OK,
            "message": 'Mirror List'
        }
        return Response(rpns)


class MirrorCreate(APIView):
    def post(self, request, *args, **kwargs):
        serializer = MirrorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            rpns = {
                'data': serializer.data,
                'status': status.HTTP_201_CREATED,
                "message": 'Mirror Created'
            }
            return Response(rpns)
        else:
            rpns = {
                'data': serializer.errors,
                'status': status.HTTP_400_BAD_REQUEST,
                "message": 'Invalid Data'
            }
            return Response(rpns)


class MirrorUpdate(APIView):
    def put(self, request, pk, *args, **kwargs):
        book = Mirror.objects.get(pk=pk)
        serializer = MirrorSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            rpns = {
                'data': serializer.data,
                'status': status.HTTP_200_OK,
                "message": 'Mirror Updated'
            }

        else:
            rpns = {
                'data': serializer.errors,
                'status': status.HTTP_400_BAD_REQUEST,
                "message": 'Invalid Data'
            }
        return Response(rpns)

    def patch(self, request, pk, *args, **kwargs):
        book = Mirror.objects.get(pk=pk)
        serializer = MirrorSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            rpns = {
                'data': serializer.data,
                'status': status.HTTP_200_OK,
                "message": 'Mirror Updated'
            }

        else:
            rpns = {
                'data': serializer.errors,
                'status': status.HTTP_400_BAD_REQUEST,
                "message": 'Invalid Data'
            }
        return Response(rpns)

class MirrorDelete(APIView):
    def delete(self, request, pk, *args, **kwargs):
        try:
            book = Mirror.objects.get(pk=pk)
        except Mirror.DoesNotExist:
            return Response({"message": "Mirror not found"}, status=status.HTTP_404_NOT_FOUND)

        book.delete()
        return Response({"message": "Mirror Deleted"}, status=status.HTTP_204_NO_CONTENT)


# class MirrorViewSet(viewsets.ModelViewSet):
#     queryset = Mirror.objects.all()
#     serializer_class = MirrorSerializer
#     lookup_field = 'pk'

# class MirrorList(ListAPIView):
#     queryset = Mirror.objects.all()
#     serializer_class = MirrorSerializer


# class MirrorCreate(CreateAPIView):
#     queryset = Mirror.objects.all()
#     serializer_class = MirrorSerializer


# class MirrorDelete(DestroyAPIView):
#     queryset = Mirror.objects.all()
#     serializer_class = MirrorSerializer
#     lookup_field = 'pk'


# class MirrorUpdate(UpdateAPIView):
#     queryset = Mirror.objects.all()
#     serializer_class = MirrorSerializer
#     lookup_field = 'pk'


# class MirrorListCreate(ListCreateAPIView):
#     queryset = Mirror.objects.all()
#     serializer_class = MirrorSerializer


# class MirrorRetrieveDestroy(RetrieveUpdateDestroyAPIView):
#     queryset = Mirror.objects.all()
#     serializer_class = MirrorSerializer
#     lookup_field = 'pk'
