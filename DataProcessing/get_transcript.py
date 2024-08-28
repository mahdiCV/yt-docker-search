import polars as pl
from youtube_transcript_api import YouTubeTranscriptApi


def extract_text(transcript: list) -> str:
    """
    Extracting text from transcript dictionary
    """
    text_list = [transcript[i]['text'] for i in range(len(transcript))]
    return ' '.join(text_list)

df = pl.read_parquet('data/video-ids.parquet')

transcript_text_list = []

for i in range(len(df)):

    try:
        transcript = YouTubeTranscriptApi.get_transcript(df['video_id'][i])
        transcript_text = extract_text(transcript)
    except:
        transcript_text = "n/a"
    
    transcript_text_list.append(transcript_text)


# add transcrpits to dataframe
df = df.with_columns(pl.Series(name="transcript", values=transcript_text_list))

df.write_parquet('data/video-transcripts.parquet')
df.write_csv('data/video-transcripts.csv')