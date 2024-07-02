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
        manager_id = data.get("project_manager")
        
        if Projects.objects.filter(project_name = name).exists():
            return JsonResponse({"message":"Project Already exists"}, status = 201)
        
        manager = get_object_or_404(Employee, id=manager_id)
        
        project = Projects.objects.create(
            project_name=name,
            project_description=description,
            project_manager=manager,
            project_start_date=data.get("project_start_date"),
            project_end_date=data.get("project_end_date")
        )
        project.save()
        return JsonResponse({"message":"Project Added Sucessfully"}, status = 400)
    return HttpResponse("invaild methods")

@csrf_exempt
def get_project(request, project_id):
    if request.method == "GET":
        try:
            project = get_object_or_404(Projects, id = project_id)
            project_data = {
                "project_name": project.project_name,
                "project_description": project.project_description,
                "project_manager": project.project_manager.name, 
                "project_start_date": project.project_start_date,
                "project_end_date": project.project_end_date,
            }

            return JsonResponse(project_data, status = 201)
        except Projects.DoesNotExist:
            return JsonResponse({"message":"Project not found"})
        
    return HttpResponse("invaild methods")

@csrf_exempt
def update_project(request, project_id):
    if request.method == "PUT":
        try:
            project = get_object_or_404(Projects, id=project_id)
            data = json.loads(request.body)
            if "project_name" in data:
                project.project_name = data['project_name']
            if 'project_description' in data:
                project.project_description = data['project_description']
            if 'project_manager' in data:
                project.project_manager = data['project_manager']
            if 'project_start_date' in data:
                project.project_start_date = data["project_start_date"]
            if 'project_end_date' in data:
                project.project_end_date = data["project_end_date"]
            project.save()
            return JsonResponse({"message": "Project data update succesfuuly"}, status = 200)
        except Projects.DoesNotExist:
            return JsonResponse({"message":"Something error"}, status = 401)
    return HttpResponse("invaild method")


@csrf_exempt
def delete_project(request, project_id):
    if request.method == "DELETE":
        try:
            project = get_object_or_404(Projects, id= project_id)
            project.delete()
            return JsonResponse({"message":"Project Delete succesfully"}, status=200)
        except Projects.DoesNotExist:
            return JsonResponse({"message":"Something issue"}, status = 401)
    return HttpResponse("invaild method")