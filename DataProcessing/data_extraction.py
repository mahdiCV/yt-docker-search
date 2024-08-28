import requests
import json
import polars as pl


def getVideoRecord(response: requests.models.Response) -> list:
    """ Function to get Youtube video data """
    video_record_list = []
    for raw_item in json.loads(response.text)['items']:
        
        if raw_item['id']['kind'] != "youtube#video":
            continue
        video_title = raw_item['snippet']['title']
        if "docker" not in video_title.lower():
            continue

        video_record = {}
        video_record['video_id'] = raw_item['id']['videoId']
        video_record['datetime'] = raw_item['snippet']['publishedAt']
        video_record['title'] = video_title

        video_record_list.append(video_record)

    return video_record_list



channel_id = 'UCdngmbVKX1Tgre699-XLlUA'
url = 'https://www.googleapis.com/youtube/v3/search'
myApi_key = "AIzaSyCPvibhjK8Beja2CeSlW6Q7RwndhLcDZwU"
page_token = None
video_record_list = []

while page_token != 0:
    params = {'key': myApi_key,
              'channelId': channel_id,
              'part': ["snippet", "id"],
              'order': "date",
              'maxResults':50,
              'pageToken': page_token}
    response = requests.get(url, params=params)
    video_record_list += getVideoRecord(response)

    try:
        page_token = json.loads(response.text)['nextPageToken']
    except:
        page_token = 0


pl.DataFrame(video_record_list).write_parquet('data/video-ids.parquet')
pl.DataFrame(video_record_list).write_csv('data/video-ids.csv')


 




