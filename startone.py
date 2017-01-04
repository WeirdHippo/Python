from apiclient.discovery import build


DEVELOPER_KEY = "AIzaSyDngQv_cVeUuk1LMrqwvP0M-8s6XfgqpGs"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,  developerKey=DEVELOPER_KEY)
search_response = youtube.search().list(
    q='asmr 귀',
    part="id,snippet",
    maxResults=25
  ).execute()

print(search_response)