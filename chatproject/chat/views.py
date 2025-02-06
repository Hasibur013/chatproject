# chat/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm

@login_required
def chat_room(request):
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
            return redirect('chat_room')
    else:
        form = MessageForm()
    
    messages = Message.objects.all().order_by('-timestamp')[:50]
    return render(request, 'chat/chat_room.html', {
        'form': form,
        'messages': messages
    })