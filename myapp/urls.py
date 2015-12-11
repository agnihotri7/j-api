"""
"""
from django.conf.urls import patterns, url
from rest_framework.routers import SimpleRouter

from myapp import views


router = SimpleRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = patterns('',
    url(r'^register/', 'myapp.views.create_auth'),
)

urlpatterns += router.urls
