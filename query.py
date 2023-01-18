from elasticsearch import Elasticsearch

client = Elasticsearch(HOST="http://localhost", PORT=9200)
INDEX = 'lyrics_metaphor_db'

def search(query):
    query_body = process_query(query)
    response = client.search(index=INDEX, body=query_body)
    return response

def process_query(query):
    query_body = basic_search(query)
    return query_body

def basic_search(query):
    query = {
        "query": {
            "query_string": {
                "query": query
            }
        }
    }
    return query

def exact_search(query):
    q = {
        "query": {
            "multi_match": {
                "query": query,
                "type": "phrase"
            }
        }
    }
    return q