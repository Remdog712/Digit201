import requests
from bs4 import BeautifulSoup

# replace the url with the Genius link you want to scrape
url = "https://genius.com/James-arthur-say-you-wont-let-go-lyrics"

# send a GET request to the URL
response = requests.get(url)

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# find the span element that contains the lyrics
lyrics_span = soup.find('span', class_='lyrics')

# get the text content of the span element
lyrics = lyrics_span.get_text()

# print the lyrics
print(lyrics)
