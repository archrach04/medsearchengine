indexMapping = {

    "mappings": {
        "properties": {
            "doc_id": {"type": "integer"},
            "Title": {"type": "text"},
            "Abstract": {"type": "text"},
            "AbstractVector": {
                "type": "dense_vector",
                "index": True,
                "similarity": "l2_norm",

            }
        }
    }
}


