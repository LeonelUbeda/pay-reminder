from rest_framework.routers import DefaultRouter
from .views import PaymentsViewSet, PaymentGroupViewSet, PaymentTrackingViewSet

router = DefaultRouter()

router.register('payments', PaymentsViewSet, basename='payments')
router.register('groups', PaymentGroupViewSet, basename='groups')
router.register('tracking', PaymentTrackingViewSet, basename='tracking')


urlpatterns = router.urls