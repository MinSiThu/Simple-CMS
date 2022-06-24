from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Content

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContentSerializer
# Create your views here.

class ContentListView(ListView):
    model = Content
    context_object_name = "contents"
    template_name = 'blog/content_list.html'

class ContentDetailView(DetailView):
    model = Content
    context_object_name = "content"
    template_name = 'blog/content_detail.html'

class ContentApiView(APIView):
    def get(self,request,id=None):
        if id:    
            content = Content.objects.get(id=id)
            serializer = ContentSerializer(content)
            return Response({'status':'success','data':serializer.data},status=status.HTTP_200_OK)            

        contents = Content.objects.all()
        serializer = ContentSerializer(contents,many=True)
        return Response({'status':'success','data':serializer.data},status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = ContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({'status':'error','data':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
            