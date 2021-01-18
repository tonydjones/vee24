from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import json, urllib.request
from django.http import JsonResponse
from datetime import datetime

from .models import Song, Date

def refresh(request):
    for song in Song.objects.all():
        song.delete()

    with urllib.request.urlopen("https://itunes.apple.com/us/rss/topalbums/limit=100/json") as response:
        data = json.loads(response.read())
        rank = 1
        for song in (data['feed']['entry']):
            try:
                album = song["im:name"]["label"]
            except:
                album = None
            
            try:
                album_link = song["link"]["attributes"]["href"]
            except:
                album_link = None
            
            try:
                song_count = song["im:itemCount"]["label"]
            except:
                song_count = None
            
            try:
                price = song["im:price"]["label"]
            except:
                price = None
            
            try:
                artist = song["im:artist"]["label"]
            except:
                artist = None
            
            try:
                artist_link = song["im:artist"]["attributes"]["href"]
            except:
                artist_link = None
            
            try:
                category = song["category"]["attributes"]["label"]
            except:
                category = None
            
            try:
                category_link = song["category"]["attributes"]["scheme"]
            except:
                category_link = None

            try:
                release_date = song["im:releaseDate"]["attributes"]["label"]
            except:
                release_date = None

            try:
                image_url = song["im:image"][2]["label"]
            except:
                image_url = None

            new_album = Song(album=album, album_link=album_link, song_count=song_count, price=price, artist=artist, 
            artist_link=artist_link, category=category, category_link=category_link, release_date=release_date, 
            rank=rank, image_url=image_url)
            new_album.save()
            rank += 1

    return HttpResponse(status=204)

def index(request):
    date = Date.objects.all()
    if len(date) == 0 or datetime.now().date() != date[0].timestamp.date():
        refresh(request)
        if len(date) == 0:
            new_date = Date(timestamp=datetime.now().date())
            new_date.save()
        else:
            date[0].timestamp = datetime.now().date()
            date[0].save()
    else:
        refresh(request)

    albums = Song.objects.all()
    return render(request, "top100/index.html", {
        "albums" : albums
    })

def search(request):
    date = Date.objects.all()
    if len(date) == 0 or datetime.now().date() != date[0].timestamp.date():
        refresh(request)
        if len(date) == 0:
            new_date = Date(timestamp=datetime.now().date())
            new_date.save()
        else:
            date[0].timestamp = datetime.now().date()
            date[0].save()
    else:
        refresh(request)

    albums = Song.objects.all()
    search_terms = request.GET['search_terms'].lower()
    print(search_terms)
    filtered_albums = []
    for album in albums:
        if search_terms in album.album.lower():
            filtered_albums.append(album)
        elif search_terms in album.artist.lower():
            filtered_albums.append(album)
        elif search_terms == album.rank:
            filtered_albums.append(album)
    return render(request, "top100/index.html", {
        "albums" : filtered_albums,
        "message" : "Search results for '" + request.GET['search_terms'] + "'"
    })