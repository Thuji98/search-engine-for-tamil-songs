# search-engine-for-tamil-songs

Steps followed to implement this application
1.  I have collected data from various websites and built corpus.
2.  I preprocessed corpus and converted into json format and created index.
    (curl -X POST "localhost:9200/lyrics_metaphor_db/_bulk?pretty" -H "Content-Type: application/json" --data-binary @180482C_corpus.json)
3.  Implemented queries for the search application.
