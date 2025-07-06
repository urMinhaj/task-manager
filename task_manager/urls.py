from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def root_view(request):
    if request.user.is_authenticated:
        return redirect('task_list')  # Redirect to tasks if logged in
    return redirect('login')  # Redirect to login if not logged in

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root_view, name='root'),  # Add root path
    path('', include('tasks.urls')),  # Existing include
]