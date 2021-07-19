from django.shortcuts import render
from music.models import Song, Listenlater, History, Channel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.db.models import Case, When


def history(request):
    if request.method == "POST":
        user = request.user
        music_id = request.POST['music_id']
        # if History.objects.filter(user=user).exists() and History.objects.filter(music_id=music_id).exists():
        #     emp = Employee.objects.get(pk = emp_id)
        hist = History.objects.filter(user=request.user)
        for i in hist:
            if i.music_id == music_id:
                i.delete()
                break
        history = History(user=user, music_id=music_id)
        history.save()

        return redirect(f"/music/songs/{music_id}")

    history = History.objects.filter(user=request.user)
    ids = []
    for i in history:
        ids.append(i.music_id)
    
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    song = Song.objects.filter(song_id__in=ids).order_by(preserved)

    return render(request, 'music/history.html', {"song": song})

def songs(request):
    wl = Song.objects.all()
    ids = []
    for i in wl:
        ids.append(i.song_id)
    
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    song = Song.objects.filter(song_id__in=ids).order_by(preserved)   
    return render(request, 'music/songs.html',  {'song': song})

def songpost(request, id):
    if request.method == "POST":
        user = request.user
        video_id = request.POST['video_id']

        watch = Listenlater.objects.filter(user=user)
        
        for i in watch:
            if video_id == i.video_id:
                message = "This Song is Already Added"
                break
        else:
            watchlater = Listenlater(user=user, video_id=video_id)
            watchlater.save()
            message = "This Song is Succesfully Added to Listen Later"

        song = Song.objects.filter(song_id=video_id).first()
        return render(request, f"music/songpost.html", {'song': song, "message": message})
    song = Song.objects.filter(song_id=id).first()
    return render(request, 'music/songpost.html', {'song': song})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
#none => galat hai
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'music/login.html')

    # if request.method == "POST":
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(username=username, password=password)
    #     from django.contrib.auth import login
    #     login(request, user)   
    #     redirect("/")

    # return render(request, 'music/login.html')

def signup(request): 
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 != pass2:
            messages.error(request, 'Passwords donot Match!!')
            return redirect('signup')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username Taken')
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email Taken')
            return redirect('signup')

        else:
            
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = first_name
            myuser.last_name = last_name
            myuser.save()
            user = authenticate(username=username, password=pass1)
            from django.contrib.auth import login
            login(request, user)

            channel = Channel(name=username)
            channel.save()

            return redirect('/')

    return render(request, 'music/signup.html')

def logout_user(request):
    logout(request)
    return redirect("/")

def delete_song(request):
    # delete(request)
    # return redirect("/")
    if request.method == "POST":
        song = Song.objects.get(id=song_id)
        print(song)
        song.file.delete()  # File delete
        song.delete() # object delete
        return redirect("/")
    return render(request, 'music/channel.html')

    
# def listenlater(request):
#     if request.method == "POST":
#         user = request.user
#         video_id = request.POST['video_id']

#         watch = Listenlater.objects.filter(user=user)
        
#         for i in watch:
#             if video_id == i.video_id:
#                 message = "Your Video is Already Added"
#                 break
#         else:
#             watchlater = Listenlater(user=user, video_id=video_id)
#             watchlater.save()
#             message = "Your Video is Succesfully Added"

#         song = Song.objects.filter(song_id=video_id).first()
#         return render(request, "music/songpost.html", {'song': song, "message": message})
#     wl = Listenlater.objects.filter(user=request.user)
#     ids = []
#     for i in wl:
#         ids.append(i.video_id)
    
#     preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
#     song = Song.objects.filter(song_id__in=ids).order_by(preserved)

#     return render(request, "music/listenlater.html", {'song': song})

def listenlater(request):
    # if request.method == "POST":
    #     user = request.user
    #     video_id = request.POST['video_id']

    #     watch = Listenlater.objects.filter(user=user)
        
    #     for i in watch:
    #         if video_id == i.video_id:
    #             message = "Your Video is Already Added"
    #             break
    #     else:
    #         watchlater = Listenlater(user=user, video_id=video_id)
    #         watchlater.save()
    #         message = "Your Video is Succesfully Added"

    #     song = Song.objects.filter(song_id=video_id).first()
    #     return render(request, f"music/songpost.html", {'song': song, "message": message})

    wl = Listenlater.objects.filter(user=request.user)
    ids = []
    for i in wl:
        ids.append(i.video_id)
    
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    song = Song.objects.filter(song_id__in=ids).order_by(preserved)

    return render(request, "music/listenlater.html", {'song': song})

def channel(request, channel):
    chan = Channel.objects.filter(name=channel).first()
    video_ids = str(chan.music).split(" ")[1:]

    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(video_ids)])
    song = Song.objects.filter(song_id__in=video_ids).order_by(preserved)    

    return render(request, "music/channel.html", {"channel": chan, "song": song})

def upload(request):
    if request.method == "POST":
        name = request.POST['name']
        singer = request.POST['singer']
        tag = request.POST['tag']
        image = request.FILES['img']
        movie = request.POST['movie']
        credit = request.POST['credit']
        song1 = request.FILES['file']
        genre = request.POST['genre']

        song_model = Song(name=name, singer=singer, tags=tag, image=image, movie=movie, credit=credit, song=song1, genre=genre)
        song_model.save()

        music_id = song_model.song_id
        channel_find = Channel.objects.filter(name=str(request.user))
        print(channel_find)

        for i in channel_find:
            i.music += f" {music_id}"
            i.save()
        message = "Your Innovation is Succesfully Uploaded"
        return render(request, f"music/upload.html", {"message": message})
    return render(request, "music/upload.html")
    
def search(request):
    query = request.GET.get("query")
    song = Song.objects.all()
    qs1 = song.filter(name__icontains=query)
    qs2 = song.filter(singer__icontains=query)
    qs3 = song.filter(movie__icontains=query)
    return render(request, "music/search.html", {"song1" : qs1, "song2" : qs2, "movie" : qs3, "query" : query })

def acoustics(request):
    wl = Song.objects.filter(genre='acoustic')
    ids = []
    for i in wl:
        ids.append(i.song_id)
    
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    song = Song.objects.filter(song_id__in=ids).order_by(preserved)
    return render(request, "music/acoustic.html",  {'song': song})

def old_days(request):
    wl = Song.objects.filter(genre='old days')
    ids = []
    for i in wl:
        ids.append(i.song_id)
    
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    song = Song.objects.filter(song_id__in=ids).order_by(preserved)  
    return render(request, "music/old_days.html",  {'song': song})

def country(request):
    wl = Song.objects.filter(genre='country')
    ids = []
    for i in wl:
        ids.append(i.song_id)
    
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    song = Song.objects.filter(song_id__in=ids).order_by(preserved)
    return render(request, "music/country.html",  {'song': song})

def bangers(request):
    wl = Song.objects.filter(genre='banger')
    ids = []
    for i in wl:
        ids.append(i.song_id)
    
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    song = Song.objects.filter(song_id__in=ids).order_by(preserved)
    return render(request, "music/bangers.html",  {'song': song})

def bollywood(request):
    wl = Song.objects.filter(genre='bollywood')
    ids = []
    for i in wl:
        ids.append(i.song_id)
    
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    song = Song.objects.filter(song_id__in=ids).order_by(preserved)
    return render(request, "music/bollywood.html",  {'song': song})
