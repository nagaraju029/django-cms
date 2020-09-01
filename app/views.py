from django.shortcuts import render
from app.models import EmployeeModel
from django.http import JsonResponse
from django.views.generic import View

# Create your views here.
def check(request):
    x=request.GET.get("employee_id")
    try:
        EmployeeModel.objects.get(eid=x)
        message={"k1":"IDno is Taken"}
    except EmployeeModel.DoesNotExist:
        message={"k1":""}
    return JsonResponse(message)


class ProductDeatils(View):
    pass