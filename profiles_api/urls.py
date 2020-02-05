from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('books-viewset',views.BookViewset,'books')

urlpatterns = [
    path('',views.ProfilesView.as_view()),
    path('books/', include(router.urls)),
]
