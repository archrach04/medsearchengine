import streamlit as st
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer


indexName = "is"

try:
    es = Elasticsearch("https://localhost:9200", basic_auth=("elastic", "UDdjs5w=6siS3emjl=Y5"),
                       ca_certs="C:/Users/C4/Downloads/elasticsearch-8.16.1/config/certs/http_ca.crt")
except ConnectionError as e:
    print("Connection Error:", e)

if es.ping():
    print("Successfully connected to Elasticsearch!!")
else:
    print("Oops!! Cannot connect to Elasticsearch!")


def search(input_keyword):
    model = SentenceTransformer('all-mpnet-base-v2')
    vector_of_input_keyword = model.encode(input_keyword)

    query = {
        "field": "AbstractVector",
        "query_vector": vector_of_input_keyword,
        "k": 10,
        "num_candidates": 500
    }
    res = es.knn_search(index="is", knn=query, source=["Title", "Abstract", "DOI"])
    results = res.get("hits", {}).get("hits", [])
    return results


def main():
    st.title("Medical Scholarly Article Search Engine")


    search_query = st.text_input("Enter your search query")

 
    if st.button("Search"):
        if search_query:
            
            results = search(search_query)

           
            st.subheader("Search Results")
            if results:
                for result in results:
                    with st.container():
                        title = result['_source'].get('Title', 'No Title Available')
                        abstract = result['_source'].get('Abstract', 'No Abstract Available')
                        doi = result['_source'].get('DOI', 'N/A')
                        
                        st.header(title)
                        
                        
                        if doi != 'N/A':
                            st.markdown(f"[DOI Link](https://doi.org/{doi})")
                        else:
                            st.write("DOI not available.")

                        st.write(f"Abstract: {abstract}")
                        st.divider()
            else:
                st.write("No results found.")



def main():
    st.title("Research Papers at Your Fingertips")

    
    search_query = st.text_input("Enter your search query")

   
    if st.button("Search"):
        if search_query:
            
            results = search(search_query)

            
            st.subheader("Search Results")
            for result in results:
                with st.container():
                    title = result['_source']['Title']
                    abstract = result['_source']['Abstract']
                    doi = result['_source'].get('DOI', 'N/A')  
                    
                    st.header(title)
                    
                 
                    if doi != 'N/A':
                        st.markdown(f"[DOI Link](https://doi.org/{doi})")
                    else:
                        st.write("DOI not available.")

                    st.write(f"Abstract: {abstract}")
                    st.divider()

if __name__ == "__main__":
    main()
