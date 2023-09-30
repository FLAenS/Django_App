from django.http import JsonResponse
from django.contrib.auth import login
from django.contrib.auth.models import User
from game.models.player.player import Player



def register(request):
    data = request.GET
    username = data.get("username", "").strip()
    password = data.get("password", "").strip()
    password_confirm = data.get("password_confirm", "").strip()
    if not username or not password:
        return JsonResponse({
            'result': "username/password cannot be empty",
        })
    if password != password_confirm:
        return JsonResponse({
            'result': "confirmed password do not match",
        })
    if User.objects.filter(username=username).exists():
        return JsonResponse({
            'result': "username already existed",
        })
    user = User(username=username)
    user.set_password(password)
    user.save()
    Player.objects.create(user=user, photo="https://i.stack.imgur.com/gMbrL.jpg")
    login(request, user)
    return JsonResponse({
        'result': "success",
    })
