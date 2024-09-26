import requests
from serpapi import GoogleSearch

import requests

def fetch_youtube_videos(query):
    api_key = 'AIzaSyDlssb4kS9yfLm7K1sqAa16Wil3Vp8wF7M'
    
    # First, search for videos
    search_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=20&q={query}&key={api_key}&type=video"
    search_response = requests.get(search_url)

    videos = []
    if search_response.status_code == 200:
        videos = search_response.json().get('items', [])
    
    results = []
    for video in videos:
        video_id = video['id']['videoId']
        
        
        video_details_url = f"https://www.googleapis.com/youtube/v3/videos?part=statistics&id={video_id}&key={api_key}"
        details_response = requests.get(video_details_url)

        views, likes = 0, 0 
        if details_response.status_code == 200:
            stats = details_response.json().get('items', [])
            if stats:
                views = int(stats[0]['statistics'].get('viewCount', 0))
                likes = int(stats[0]['statistics'].get('likeCount', 0))

        video_data = {
            'title': video['snippet']['title'],
            'url': f"https://www.youtube.com/watch?v={video_id}",
            'views': views,  
            'likes': likes,  
            'thumbnail_url': video['snippet'].get('thumbnails', {}).get('default', {}).get('url', '')
        }
        results.append(video_data)

   
    results.sort(key=lambda x: (x['views'], x['likes']), reverse=True)

    return results


def fetch_google_articles(query):
    api_key = 'AIzaSyCLRj_IlhgEpgCVJhjwNSfyChFIC1akhKg'
    cx = 'YOUR_CUSTOM_SEARCH_ENGINE_ID'
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&cx={cx}&key={api_key}&num=5"
    response = requests.get(url)
    
    if response.status_code == 200:
        articles = response.json().get('items', [])
    else:
        articles = []
    
    results = []
    for article in articles:
        article_data = {
            'title': article['title'],
            'url': article['link'],
            'snippet': article.get('snippet', 'No description available')
        }
        results.append(article_data)
    return results


def fetch_academic_papers(query):
    api_key = 'fe5b504e6dd5859709bc2b835fe088c6f4413a5a0e4d752be21d43400b10711d'
    search = GoogleSearch({
        "q": query,
        "tbm": "scholar",  
        "api_key": api_key
    })
    response = search.get_dict()
    
    if response:
        results = response.get('organic_results', [])
    else:
        results = []
    
    papers = []
    for result in results:
        paper_data = {
            'title': result['title'],
            'url': result.get('link'),
            'snippet': result.get('snippet', 'No description available')
        }
        papers.append(paper_data)
    return papers
