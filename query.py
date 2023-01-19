from elasticsearch import Elasticsearch

client = Elasticsearch(HOST="http://localhost", PORT=9200)
INDEX = 'lyrics_metaphor_db'

def search(list_):
    query_body = process_query(list_)
    response = client.search(index=INDEX, body=query_body)
    return response

def process_query(list_):
    if (list_[0] == 1):
        query_body = multi_match_query(list_[1])
    elif (list_[0] == 2):
        query_body = term_query(list_[1])
    else:
        query_body = basic_search(list_[1])
    return query_body


# Basic Search Query
def basic_search(query):
    q = {
        "query": {
            "query_string": {
                "query": query
            }
        }
    }
    return q

# Multi Match Query
def multi_match_query(target):
    q = {
            "query": {
                "multi_match" : {
                    "query": target,
                    "type": "most_fields",
                    "fields": [ "இலக்கு_1", "இலக்கு_2", "இலக்கு_3", "இலக்கு_4", "இலக்கு_5", "இலக்கு_6"]
                }
            }
        }
    return q

# Term query
def term_query(query):
    q = {
        "query": {
            "term": {
                "வருடம்": {
                    "value": query
                }
            }
        }
    }
    return q

