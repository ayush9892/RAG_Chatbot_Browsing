import azure.functions as func
import logging
import json
from rag_bot_service import openai_chat, vector_search

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)
@app.route(route="rag_chatbot_aisearch", methods=["POST"])
def rag_chatbot_aisearch(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing request...")

    try:
        # Parse the request JSON
        req_body = req.get_json()
        query = req_body.get("query")
        if not query:
            return func.HttpResponse(
                "Please provide a 'query' in the request body.",
                status_code=400
            )
        logging.error("Going for Vector Search")
        search_results = vector_search(query)
        if not search_results:
            logging.error("No search results returned!")

        sources_formatted = "\n".join([
            f'{document["chunk"]}' 
            # f'{document["chunk_id"]}: {document["chunk"]}: {document["title"]}' 
            for document in search_results
        ])

        # logging.error(f"sources_formatted: {sources_formatted}")
        response = openai_chat(query, sources_formatted)
        response = json.loads(response)
        return func.HttpResponse(
            json.dumps({"response": response}),
            mimetype="application/json",
            status_code=200
        )

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            mimetype="application/json",
            status_code=500
        )
