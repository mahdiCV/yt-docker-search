# A YouTube search approach in a specific category
In this repository, as I started to learn Docker, I tried to build a search method in TechWorld with Nana's YouTube channel. 
## Result
![Result:](img/result.png) 

## Steps
**1.** Get all video Id's \
**2.** Filtering videos base on **Docker** topic, and Extracting its transcript \
**3.** Embedding texts with the Sbert pre-trained model [(all-MiniLM-L6-v2)](https://sbert.net/docs/sentence_transformer/pretrained_models.html#)\
**4.** Find the best video to texts and transcripts based on the input query
