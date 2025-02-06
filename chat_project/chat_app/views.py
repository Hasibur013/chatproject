from django.shortcuts import render
from django.http import JsonResponse
from .models import ChatMessage

def chat_view(request):
    messages = ChatMessage.objects.all().order_by('-timestamp')
    return render(request, "chat.html", {"messages": messages})

def send_message(request):
    if request.method == "POST":
        text = request.POST.get("text", "")
        image = request.FILES.get("image", None)
        audio = request.FILES.get("audio", None)

        message = ChatMessage.objects.create(text=text, image=image, audio=audio)
        return JsonResponse({"status": "success", "message_id": message.id})

    return JsonResponse({"status": "error"}, status=400)
