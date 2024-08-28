import numpy as np
import polars
import sentence_transformers
import sklearn


def returnSearchResultIndex(query: str, 
                            df: polars.lazyframe.frame.LazyFrame,
                            model,
                            dist: sklearn.metrics.pairwise.manhattan_distances) -> np.ndarray:
    
    query_embedding = model.encode(query).reshape(1, -1)

    # compute distance betwenn query and titles and transcripts
    dist_arr = dist.pairwise(df.select(df.columns[4:388]).collect(), query_embedding) + dist.pairwise(df.select(df.columns[388:]).collect(), query_embedding)

    # search params
    threshold = 40 # threshold for manhatten distance
    top_k = 5

    # evaluate videos close to query based on threshold
    idx_below_threshold = np.argwhere(dist_arr.flatten()<threshold).flatten()

    # keep top k closest videos
    idx_stored = np.argsort(dist_arr[idx_below_threshold], axis=0).flatten()

    # return indexes of search results
    return idx_below_threshold[idx_stored][:top_k]