from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Menyu, Comment
from .serializer import MenyuSerializer, CommentSerializer, DeleteManyuSerializer, UpdateManyuSerializer
from .filters import MenyuFilter
from rest_framework import status

# Create your views here.


class MenuAPIView(ListAPIView):
    queryset = Menyu.objects.all()
    serializer_class = MenyuSerializer
    # filter_backends = MenyuFilter


class CommentAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ProductDetailView(APIView):

    def get(self, request, pk):
        menyu = Menyu.objects.get(id=pk)
        serializer = MenyuSerializer(menyu).data
        data = {
            'status': status.HTTP_200_OK,
            'data': serializer
        }

        return Response(data)


class DeleteView(APIView):
    def delete(self, request, pk):
        menyu = Menyu.objects.get(id=pk)
        menyu.delete()
        return Response({
            "status": status.HTTP_204_NO_CONTENT
        })


class UpdateView(APIView):

    def put(self, request, pk):
        menyu = Menyu.objects.get(id=pk)
        serializer = UpdateManyuSerializer(menyu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": status.HTTP_200_OK
            })
        else:
            return Response({
                "status": status.HTTP_400_BAD_REQUEST
            })

