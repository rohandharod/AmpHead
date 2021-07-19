from django.shortcuts import render
from music.models import Song, Listenlater
from django.db.models import Case, When


# def index(request):
#     song =.all()
#     return render(request, 'index.html', {'song': song})

def index(request):
    # wl = Song.objects.all()
    # ids = []
    # for i in wl:
    #     ids.append(i.song_id)
    
    # preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    # song1 = Song.objects.filter(song_id__in=ids).order_by(preserved)[0:4]
    # song2 = Song.objects.filter(song_id__in=ids).order_by(preserved)[4:7]  

    
    song_old1 = Song.objects.filter(genre = 'old days')[0:4]
    song_old2 = Song.objects.filter(genre = 'old days')[4:7]

    song_aco1 = Song.objects.filter(genre = 'acoustic')[0:4]
    song_aco2 = Song.objects.filter(genre = 'acoustic')[4:7]

    song_count1 = Song.objects.filter(genre = 'country')[0:4]
    song_count2 = Song.objects.filter(genre = 'country')[4:7]

    song_bolly1 = Song.objects.filter(genre = 'bollywood')[0:4]
    song_bolly2 = Song.objects.filter(genre = 'bollywood')[4:7]   
    song_banger1 = Song.objects.filter(genre = 'banger')[0:4]
    song_banger2 = Song.objects.filter(genre = 'banger')[4:7]   
    # wl = Listenlater.objects.filter(user=request.user)
    # ids = []
    # for i in wl:
    #     ids.append(i.video_id)
    
    # preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    # song_ll = Song.objects.filter(song_id__in=ids).order_by(preserved)

    return render(request, 'index.html', {'song_old_1': song_old1, 'song_old_2': song_old2, 'song_aco_1': song_aco1, 'song_aco_2': song_aco2, 'song_count_1': song_count1, 'song_count_2': song_count2, 'song_bolly_1': song_bolly1, 'song_bolly_2': song_bolly2, 'song_banger_1': song_banger1, 'song_banger_2': song_banger2})


