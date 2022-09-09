import io
import json
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Coder 
from django.views.decorators.csrf import csrf_exempt
from .serializers import CoderSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.
@csrf_exempt
def get_coders(request):
    # get Data
    # check request 
    if request.method=='GET':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id = pythondata.get('id',None)
        if id is not None:
            coder=Coder.objects.get(id=id)
            serializer = CoderSerializer(coder)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        coder = Coder.objects.all()
        serializer = CoderSerializer(coder,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')

        # create Data
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=CoderSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={
                'msg':'data created'
            }
            json_data=JSONRenderer().render(res)
            # return JsonResponse(serializer.data , status=201)
            return HttpResponse(json_data,content_type='application/json')
        # return JsonResponse(serializer.errors,status=400)
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method=='PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id = pythondata.get('id')
        # get the coder to update using id
        coder=Coder.objects.get(id=id)
        # partial update with serializer
        serializer=CoderSerializer(coder,data=pythondata,partial=True)
        # complete update 
        # serializer=CoderSerializer(coder,data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={
                'msg':'Data updated'
            }
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    # delete coder

    if request.method=='DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id = pythondata.get('id')
        # get the coder to update using id
        coder=Coder.objects.get(id=id)
        coder.delete()
        res={
            'msg':'data deleted succesfully'
        }                                   
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')                                                                                                       



        

        