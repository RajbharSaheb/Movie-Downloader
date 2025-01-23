import requests
from bs4 import BeautifulSoup

def get_movie_download_link(movie_name):
    # Search for the movie on a website (example: a public domain movie website)
    search_url = f"https://example-movie-search.com/search?q={movie_name}"
    response = requests.get(search_url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # This would depend on the structure of the website you're scraping
        movie_link = soup.find('a', {'class': 'download-link'})
        
        if movie_link:
            return movie_link['href']
    return None
