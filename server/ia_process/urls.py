from ia_process import views
from django.urls import path

urlpatterns = [
    # path('reviews/', views.reviewAPIView.as_view()),
    # path('reviews/<int:pk>', views.reviewApiView.as_view()),
    path('review/', views.into_text),
]

