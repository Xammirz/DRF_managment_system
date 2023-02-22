from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from managment_system.users.api.views import UserViewSet

from managment_system.tasks.urls import router as tasks_router

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.registry.extend(tasks_router.registry)

app_name = "api"
urlpatterns = router.urls
