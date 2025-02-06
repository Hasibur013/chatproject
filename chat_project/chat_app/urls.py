from django.urls import path
from .views import chat_view, send_message

urlpatterns = [
    path('', chat_view, name="chat"),        # Chat view at /chat/
    path('send/', send_message, name="send_message"),
]