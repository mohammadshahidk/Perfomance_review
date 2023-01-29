from django.urls import path, include
from rest_framework.routers import SimpleRouter
from accounts import views as user_views
router = SimpleRouter()

router.register(r'employee', user_views.EmployeeView, basename='Employee')

urlpatterns = [
    path('login/', user_views.Login.as_view()),
    path('', include(router.urls))
]
