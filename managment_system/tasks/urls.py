from rest_framework import routers

from managment_system.tasks.api.views import TeamViewSet, TaskViewSet

app_name = "team"

router = routers.SimpleRouter()
router.register("team", TeamViewSet, basename="team")
router.register("task", TaskViewSet, basename="task")
urlpatterns = router.urls
