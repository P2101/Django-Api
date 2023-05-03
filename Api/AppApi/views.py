from typing import Any
from django import http
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Company
import json
# Create your views here.

# MÉTODOS RESTful
# POST: crear un recurso nuevo.
# PUT: modificar un recurso existente.
# GET: consultar información de un recurso.
# DELETE: eliminar un recurso determinado.
# PATCH: modificar solamente un atributo de un recurso.
class CompanyView(View):

    # MÉTODO PARA CADA PETICIÓN
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if (id>0):
            # diferencia entre filter y get, filter si no existe no peta, get sí
            companies = list(Company.objects.filter(id=id).values())
            if len(companies) > 0:
                company = companies[0]
                datos={'message':'Success', 'company':company}
            else:
                datos={'message':'Company Not Found'}
            return JsonResponse(datos)
        else:
            # HACEMOS UN CASTING PARA SERIALIZARLO A UN JSON
            companies = list(Company.objects.values())
            if len(companies) > 0:
                datos={'message':'Success', 'companies':companies}
            else:
                datos={'message':'Companies Not Found'}
            return JsonResponse(datos)
            

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Company.objects.create(name=jd['name'], url=jd['url'], foundation=jd['foundation'])
        datos={'message':'Success'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        companies = list(Company.objects.filter(id=id).values())
        if len(companies) > 0:
            company = Company.objects.get(id=id)
            company.name = jd['name']
            company.url = jd['url']
            company.foundation = jd['foundation']
            company.save()
            datos = {'message': 'Success'}
        else:
            datos={'message':'Company Not Found'}
        return JsonResponse(datos)

    def delete(self, request, id):
        companies = list(Company.objects.filter(id=id).values())
        if len(companies) > 0:
            companies = list(Company.objects.filter(id=id).delete())
            datos = {'message': 'Success'}
        else:
            datos={'message':'Company Not Found'}
        return JsonResponse(datos)