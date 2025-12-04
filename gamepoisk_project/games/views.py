from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Game
from .forms import CommentForm

def game_list(request):
    query = request.GET.get('q', '').strip()
    games = Game.objects.all()
    if query:
        games = Game.objects.filter(
            Q(title__icontains=query) |
            Q(genre__icontains=query) |
            Q(developer__icontains=query) |
            Q(publisher__icontains=query)
        )
    return render(request, 'games/game_list.html', {'games': games, 'query': query})

def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    comments = game.comments.all().order_by('-created_at')
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.game = game
                comment.save()
            return redirect('games:game_detail', pk=game.pk)

        else:
            return redirect('users:login')
    else:
        form = CommentForm()
    return render(request, 'games/game_detail.html', {'game': game, 'comments': comments, 'form': form})
