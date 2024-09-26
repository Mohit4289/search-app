from django.shortcuts import render
from .utils import fetch_youtube_videos, fetch_google_articles, fetch_academic_papers

def home(request):
    return render(request, 'home.html')

def search_results(request):
    query = request.GET.get('query', '')
    
    if query:
        youtube_videos = fetch_youtube_videos(query)
        articles = fetch_google_articles(query)
        academic_papers = fetch_academic_papers(query)
    else:
        
        youtube_videos, articles, academic_papers = [], [], []
    
    return render(request, 'search/results.html', {
        'query': query,
        'youtube_videos': youtube_videos,
        'articles': articles,
        'academic_papers': academic_papers
    })
