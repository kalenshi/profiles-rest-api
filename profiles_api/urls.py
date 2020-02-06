from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('books',views.BookViewset)
router.register('users',views.UserProfilesViewset)

urlpatterns = [
    #path('',views.ProfilesView.as_view()),
    path('', include(router.urls)),
]
