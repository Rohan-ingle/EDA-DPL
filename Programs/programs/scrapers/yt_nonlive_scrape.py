import googleapiclient.discovery
import pandas as pd
import time

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyAw1-i3tNmJR3RkPE3arIbXVIUwrW-e9xA"

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY)

comments = []

def scrape(api_service_name, api_version, DEVELOPER_KEY, youtube, comments, next_page_token=None, count=0):
    while True:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId="",
            maxResults=100,
            pageToken=next_page_token
        )
        response = request.execute()

        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']
            comments.append([
                comment['authorDisplayName'],
                comment['publishedAt'],
                comment['updatedAt'],
                comment['likeCount'],
                comment['textDisplay']
            ])
        next_page_token = response.get('nextPageToken')
        count += 1

        if not next_page_token:
            break

        print(count)
        #time.sleep(5)

    df = pd.DataFrame(comments, columns=['author', 'published_at', 'updated_at', 'like_count', 'text'])
    df.to_csv('dataframe.csv')

scrape(api_service_name, api_version, DEVELOPER_KEY, youtube, comments)
