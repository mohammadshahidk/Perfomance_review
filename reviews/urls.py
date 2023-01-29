from rest_framework.routers import SimpleRouter
from reviews.views import ReviewView

router = SimpleRouter()

router.register(r'review', ReviewView, basename='reviews')

urlpatterns = router.urls
