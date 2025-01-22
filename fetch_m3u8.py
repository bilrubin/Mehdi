import requests
import re

# URL of the website to fetch
url = "https://yodaplayer.yodacdn.net/qafqazwebsite/index.php"

# Send a request to the website
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Regular expression to find .m3u8 URLs on the page
    m3u8_urls = re.findall(r'https://[^"\']+\.m3u8', response.text)
    
    # Create and write the .m3u8 playlist to a file
    with open("qafqaz_playlist.m3u8", "w", encoding="utf-8") as file:
        file.write("#EXTM3U\n")  # Header for M3U playlist
        for i, url in enumerate(m3u8_urls, start=1):
            file.write(f"#EXTINF:-1, Stream {i}\n")
            file.write(url + "\n")
    
    print(f"Playlist generated and saved as 'qafqaz_playlist.m3u8' with {len(m3u8_urls)} streams.")
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
