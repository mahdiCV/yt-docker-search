from fastapi import FastAPI
import polars as pl
from sentence_transformers import SentenceTransformer
from sklearn.metrics import DistanceMetric
import numpy as np
from app.functions import returnSearchResultIndex

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

df = pl.scan_csv('app/data/video-index.csv')

dist_name = 'manhattan'
dist = DistanceMetric.get_metric(dist_name)

app = FastAPI()

@app.get("/")
def health_check():
    return {'health_check': 'ok'}

@app.get("/info")
def info():
    return {'name': 'yt-search', 'description': "Search API for Nana's YouTube videos."}

@app.get("/search")
def search(query: str):
    idx_result = returnSearchResultIndex(query, df, model, dist)
    return df.select(['title', 'video_id']).collect()[idx_result].to_dict(as_series=False)  