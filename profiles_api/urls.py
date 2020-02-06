from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('books',views.BookViewset)
router.register('users',views.UserProfilesViewset)

urlpatterns = [
    path('',views.UserLoginView.as_view()),
    path('profiles/', include(router.urls)),
]
