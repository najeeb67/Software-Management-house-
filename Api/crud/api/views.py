from django.shortcuts import render
from django.http import HttpResponse , JsonResponse , HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Employee , Projects
from django.shortcuts import get_object_or_404 

@csrf_exempt
def add_employee(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        field = data.get('field')
        phone_no = data.get('phone_no')
        location = data.get('location')
        date_of_joining = data.get('date_of_joining')
        
        if Employee.objects.filter(email = email).exists():
            return JsonResponse({"error":"Employee already Exist"} , status = 404)
        
        user = Employee.objects.create(name=name , email = email , field = field , phone_no = phone_no , location = location , date_of_joining = date_of_joining)
        user.save()
        return JsonResponse({"Message":"Employee add SucessFully..!"} , status= 201)
    return HttpResponseBadRequest("Invaild Request Method")
        
@csrf_exempt

def get_employee_data(request , employee_id):
    if request.method == "GET":
        try:
            employee = get_object_or_404(Employee , id=employee_id)
            employee_data = {
                "name": employee.name,
                "email":employee.email,
                "field":employee.field,
                "phone_no":employee.phone_no,
                "location":employee.location,
                "date_of_joining":employee.date_of_joining,
            }
            return JsonResponse(employee_data, status = 200)
        except Employee.DoesNotExist:
            return JsonResponse({"error": "Employee Not Found"}, status=404)
    return HttpResponseBadRequest("Invaild Request Method")




@csrf_exempt
def update_employe(request, employee_id):
    if request.method == "PUT":
        try:
            employee = get_object_or_404(Employee, id= employee_id)
            data = json.loads(request.body)
            if 'name' in data:
                employee.name = data['name']
            if "email" in data:
                employee.email = data["email"]
            if "field" in  data:
                employee.email = data["field"]
            if "phone_no" in data:
                employee.phone_no = data["phone_no"]
            if "location" in data:
                employee.location = data["location"]
            if "date_of_joining" in data:
                employee.date_of_joining = data["date_of_joining"]
                
            employee.save()
            return JsonResponse({"Message": "Employee Data Updated Successfully"}, status=200)
        except Employee.DoesNotExist:
            return JsonResponse({"error": "Employee Not Found"}, status=404)
        
    return HttpResponseBadRequest("Method invaild")



@csrf_exempt
def delete_employe(request, employee_id):
    if request.method == "DELETE":
        try:
            employee = get_object_or_404(Employee, id = employee_id)
            employee.delete()
            return JsonResponse({"message":"Dalete Employee Data Sucessfully..!"})
        except Employee.DoesNotExist:
            return JsonResponse({"error": "Employee Not Found"}, status=404)
    return HttpResponseBadRequest("Method invaild")


@csrf_exempt
def add_project(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("project_name")
        description = data.get("project_description")
        manager = data.get("project_manager")
        start_date = data.get("project_start_date")
        end_date = data.get("project_end_date")
        
        if Projects.objects.filter(name = name).exists():
            return JsonResponse({"message":"Project Already exists"}, status = 201)
        
        user = Projects.objects.create(name = name , description = description , manager = manager , start_project = start_date , end_project = end_date)
        user.save()
        return JsonResponse({"message":"Project Added Sucessfully"}, status = 400)
    return HttpResponse("invaild methods")


def get_object(request, project_id):
    if request.method == "GET":
        try:
            data = get_object_or_404(Projects, id = project_id)
            project_data = {
            "name" : data.project_name,
            "description":data.project_description,
            "manager":data.project_manager,
            "start_date": data.project_start_date,
            "end_date": data.project_end_date,
            }
            return JsonResponse(project_data, status = 201)
        except Projects.DoesNotExist:
            return JsonResponse({"message":"Project not found"})
        
    return HttpResponse("invaild methods")