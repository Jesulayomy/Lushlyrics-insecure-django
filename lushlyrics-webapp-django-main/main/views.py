import json

from django.contrib.auth import (
    login,
    logout,
)
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from youtube_search import YoutubeSearch

from .models import playlist_user


f = open("card.json", "r")
CONTAINER = json.load(f)


def default(request):
    global CONTAINER

    if request.method == "POST":
        add_playlist(request)
        return HttpResponse("")

    song = "kSFJGEHDCrQ"
    return render(
        request,
        "player.html",
        {"CONTAINER": CONTAINER, "song": song}
    )


def playlist(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    cur_user = playlist_user.objects.get(username=request.user)
    try:
        song = request.GET.get("song")
        song = cur_user.playlist_song_set.get(song_title=song)
        song.delete()
    except Exception:
        pass
    if request.method == "POST":
        add_playlist(request)
        return HttpResponse("")
    song = "kSFJGEHDCrQ"
    user_playlist = cur_user.playlist_song_set.all()
    return render(
        request,
        "playlist.html",
        {"song": song, "user_playlist": user_playlist}
    )


def search(request):
    if request.method == "POST":
        add_playlist(request)
        return HttpResponse("")
    try:
        search = request.GET.get("search")
        song = YoutubeSearch(search, max_results=10).to_dict()
        song_li = [song[:10:2], song[1:10:2]]
    except Exception:
        return redirect("/")

    return render(
        request,
        "search.html",
        {"CONTAINER": song_li, "song": song_li[0][0]["id"]}
    )


def add_playlist(request):
    cur_user = playlist_user.objects.get(username=request.user)

    if (request.POST["title"],) not in cur_user.playlist_song_set.values_list(
        "song_title",
    ):
        songdic = (
            YoutubeSearch(
                request.POST["title"],
                max_results=1
            ).to_dict()
        )[0]
        song__albumsrc = songdic["thumbnails"][0]
        cur_user.playlist_song_set.create(
            song_title=request.POST["title"],
            song_dur=request.POST["duration"],
            song_albumsrc=song__albumsrc,
            song_channel=request.POST["channel"],
            song_date_added=request.POST["date"],
            song_youtube_id=request.POST["songid"],
        )


def login_user(request):
    if request.method == "POST":
        try:
            user = User.objects.get(username=request.POST["username"])
        except User.DoesNotExist:
            try:
                user = User.objects.get(email=request.POST['username'])
            except User.DoesNotExist:
                return render(
                    request,
                    "login.html",
                    {"errors": "User does not exist"}
                )
        if user.check_password(request.POST["password"]):
            login(request, user)
            return redirect("/")
        else:
            return render(
                request,
                "login.html",
                {"errors": "Password incorrect"}
            )
    else:
        return render(request, "login.html", {})


def logout_user(request):
    logout(request)
    return redirect("/")


def signup(request):
    if request.method == "POST":
        try:
            user = User.objects.get(username=request.POST["username"])
            return render(
                request,
                "signup.html",
                {"errors": {"username": "Username already exists"}},
            )
        except User.DoesNotExist:
            try:
                user = User.objects.get(email=request.POST["email"])
                return render(
                    request,
                    "signup.html",
                    {"errors": {"email": "Email already exists"}},
                )
            except User.DoesNotExist:
                pass
        user = User.objects.create(
            username=request.POST["username"], email=request.POST["email"]
        )
        user.set_password(request.POST["password"])
        user.save()
        playlist_user.objects.create(username=user.username)
        login(request, user)
        return redirect("/")
    else:
        return render(request, "signup.html", {})


def reset(request):
    if request.method == "POST":
        try:
            user = User.objects.get(
                username=request.POST["username"], email=request.POST["email"]
            )
        except User.DoesNotExist:
            return render(
                request,
                "reset.html",
                {"errors": "Username does not exist or Email is incorrect"},
            )
        user.set_password(request.POST["password"])
        user.save()
        login(request, user)
        return redirect("/")
    else:
        return render(request, "reset.html", {})
