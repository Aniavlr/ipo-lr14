from django.shortcuts import render, HttpResponse
import json

# Create your views here.

def main_page(request):
    return render(request, 'index.html')

def about(request):
    return render(request,'about.html')

def ofiston(request):
    return render(request, 'ophiston.html')

def load_qualifications():
    with open('dump.json', encoding='utf-8') as file:
        return json.load(file)

def spec_list(request):
    data = load_qualifications()
    qualifications = []
    
    for item in data:
        if item["model"] == "data.skill":
            qualifications.append({
                "id": item["pk"],
                "type": "skill",
                "code": item["fields"]["code"],
                "title": item["fields"]["title"],
                "description": item["fields"].get("description", "")
            })
        elif item["model"] == "data.specialty":
            qualifications.append({
                "id": item["pk"],
                "type": "specialty",
                "code": item["fields"]["code"],
                "title": item["fields"]["title"],
                "description": item["fields"].get("description", ""),
                "c_type": item["fields"]["c_type"]
            })
    
    return render(request, 'spec_list.html', {
        'qualifications': qualifications
    })
              
def spec_detail(request, id):
    data = load_qualifications()
    qualification = None
    
    for item in data:
        if str(item["pk"]) == str(id):
            if item["model"] == "data.skill":
                qualification = {
                    "id": item["pk"],
                    "type": "skill",
                    "code": item["fields"]["code"],
                    "title": item["fields"]["title"],
                    "description": item["fields"].get("description", "")
                }
            elif item["model"] == "data.specialty":
                qualification = {
                    "id": item["pk"],
                    "type": "specialty",
                    "code": item["fields"]["code"],
                    "title": item["fields"]["title"],
                    "description": item["fields"].get("description", ""),
                    "c_type": item["fields"]["c_type"]
                }
            break
    
    if not qualification:
        return render(request, 'spec_detail.html', {
            'error': True,
            'message': f'Квалификация с ID {id} не найдена'
        })
    
    return render(request, 'spec_detail.html', {
        'qualification': qualification,
        'error': False
    })
    