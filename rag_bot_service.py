from openai import AzureOpenAI
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
import os
# import logging

OPENAI_ENDPOINT = os.getenv("OPENAI_ENDPOINT")
OPENAI_DEPLOYMENT = os.getenv("OPENAI_DEPLOYMENT")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SEARCH_ENDPOINT = os.getenv("SEARCH_ENDPOINT")
SEARCH_API_KEY = os.getenv("SEARCH_API_KEY")
SEARCH_INDEX = os.getenv("SEARCH_INDEX")

openai_client = AzureOpenAI(
    azure_endpoint=OPENAI_ENDPOINT,
    api_key=OPENAI_API_KEY,
    api_version="2024-08-01-preview"
)

search_client = SearchClient(
     SEARCH_ENDPOINT,
     SEARCH_INDEX,
     AzureKeyCredential(SEARCH_API_KEY)
 )


GROUNDED_PROMPT = """
Context:\n{context},
This Provided context above is search results from Azure AI Search.

Now, Process the following query below and just return the most relevant URL below in form of JSON like "URL" : "www.google.com"
Query: {query}
"""
# GROUNDED_PROMPT = """
# Context:\n{context},
# This Provided context above is search results from Azure AI Search.

# Now, answer the following query below. 
# Query: {query}
# """

def vector_search(query):
    search_results = search_client.search(
        # //semantic_query=
                search_text=query,
                top=5,
                select="chunk"
                #chunk_id, title, chunk, @search.score, @search.reranker_score, @search.highlights, @search.captions
            )
    # logging.error(f"type: {type(search_results)}")
    search_results = list(search_results)

    # logging.error(f"type: {type(search_results)}")
    
    return search_results


def openai_chat(query, sources_formatted):
     response = openai_client.chat.completions.create(
            messages=[{
                "role": "user",
                "content": GROUNDED_PROMPT.format(query=query, context=sources_formatted)
            }],
            model=OPENAI_DEPLOYMENT
        )
     res = response.choices[0].message.content
     
     return res