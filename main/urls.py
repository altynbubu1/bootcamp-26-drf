from rest_framework.routers import SimpleRouter
from main.views import PostViewSet, EmployViewSet

router = SimpleRouter()
router.register('posts', PostViewSet, basename='posts')  # Changed from '' to 'posts'
router.register('employ', EmployViewSet, basename='employ')

urlpatterns = router.urls
