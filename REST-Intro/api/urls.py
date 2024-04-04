from django.urls import path
from .views import PostListCreateView, PostDetailRetrieveDestroyAPIView, PostUpdateAPIView

urlpatterns = [
    path('', PostListCreateView.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetailRetrieveDestroyAPIView.as_view(), name='retrieve'),
    path('post/update/<int:pk>/', PostUpdateAPIView.as_view(), name='update')
]
