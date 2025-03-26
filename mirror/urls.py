from django.urls import path
from .views import MirrorList, MirrorCreate,  MirrorUpdate#, MirrorListCreate, MirrorRetrieveDestroy, MirrorDelete

urlpatterns = [
    path('', MirrorList.as_view(), name='mirror_list'),
    path('create/', MirrorCreate.as_view(), name='create_mirror'),
    # path('delete/<int:pk>/', MirrorDelete.as_view(), name='delete_mirror'),
    path('update/<int:pk>/', MirrorUpdate.as_view(), name='update_mirror'),
    # path('lstcrt/', MirrorListCreate.as_view()),
    # path('dstdltupt/<int:pk>/', MirrorRetrieveDestroy.as_view()),
]




# from .views import MirrorViewSet
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'mirrors', MirrorViewSet, basename='mirror')
# urlpatterns = router.urls