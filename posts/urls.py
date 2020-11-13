from django.urls import path
from posts.views import posts, post_details

app_name = 'post'

urlpatterns = [
    path('', posts),
    path('details/', post_details, name='post_details')
]
