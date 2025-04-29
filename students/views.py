from django.http import JsonResponse

# بيانات الطلاب الثابتة
STUDENTS_DATA = [
    {"id": 1, "name": "رغد الجباوي", "age": 25, "major": "ذكاء اصطناعي"},
    {"id": 2, "name": "سارة علي", "age": 21, "major": "هندسة برمجيات"},
    {"id": 3, "name": "خالد عبدالله", "age": 22, "major": "ذكاء اصطناعي"},
    {"id": 4, "name": "نورا حسن", "age": 19, "major": "أمن معلومات"},
    {"id": 5, "name": "عمر كمال", "age": 20, "major": "علم البيانات"}
]


def welcome_page(request):
    """عرض الصفحة الترحيبية"""
    return JsonResponse({
        "message": "مرحباً بك في نظام إدارة الطلاب",
        "endpoints": {
            "قائمة_الطلاب": "/students/",
            "لوحة_التحكم": "/admin/"
        },
        "instructions": "قم بزيارة /students/ للحصول على قائمة الطلاب"
    }, status=200, json_dumps_params={'ensure_ascii': False})


def student_list(request):
    """عرض قائمة الطلاب"""
    return JsonResponse(STUDENTS_DATA, safe=False, json_dumps_params={'ensure_ascii': False})
