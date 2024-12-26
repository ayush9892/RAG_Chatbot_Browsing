# RAG_Chatbot_Browsing

## Introduction
This project implements a Retrieval Augmented Generation (RAG) chatbot that integrates Azure OpenAI and Azure Cognitive Search. The chatbot processes user queries by retrieving relevant information from a search index and generating context-aware responses. By combining embedding-based retrieval and natural language generation, it ensures accurate and contextual answers.

## Features
- **Vector Search**: Leverages Azure Cognitive Search to retrieve highly relevant data chunks based on the user’s query.
- **Contextual Responses**: Combines retrieved data with Azure OpenAI’s language model to provide grounded and accurate answers.
- **Serverless Deployment**: Utilizes Azure Functions for scalability and ease of management.
- **JSON Response Format**: Outputs responses in JSON for easy integration into other applications or workflows.


## Architecture
1. **User Input**: A user submits a question or query via the chatbot.
2. **Vector Search**: The query is sent to Azure Cognitive Search, which retrieves the most relevant chunks of data from a configured search index.
3. **Azure OpenAI Interaction**: The retrieved search results are combined and passed to Azure OpenAI, which processes the context and generates a response.
4. **Response Generation**: The chatbot returns either the most relevant URL in JSON format.

The system diagram below outlines the RAG process:

![image](https://github.com/user-attachments/assets/0bb07a3c-a025-4a3b-a8dc-c8e4b58294ea)


---

## File Structure
### Main Files
- **`rag_bot_service.py`**:
  - Contains logic to interact with Azure Cognitive Search and Azure OpenAI.
  - Implements the `vector_search` function for retrieving search results and `openai_chat` for generating contextual responses.

- **`function_app.py`**:
  - Implements an HTTP-triggered Azure Function that acts as the API endpoint for the chatbot.
  - Handles user queries, processes search results, and integrates them with Azure OpenAI responses.


## Setup Instructions

### Prerequisites
1. **Azure Resources**:
   - Azure OpenAI resource with a deployed GPT model and text_embedded model.
   - Azure Cognitive Search resource with a properly configured search index [Upload Book.xlsx file in blob storage while Importing and vectorizing data].
     ![image](https://github.com/user-attachments/assets/dcdbbd39-dd24-413f-85ca-f18c1c430df4)

     

2. **Development Tools**:
   - Azure Functions Core Tools.
   - Python 3.9 or later.

### Environment Variables
Define the following variables in a `.env` file or configure them in Azure Function App settings:

- `OPENAI_ENDPOINT`: The endpoint for your Azure OpenAI resource.
- `DEPLOYMENT_NAME`: The name of your OpenAI deployment.
- `OPENAI_API_KEY`: API key for accessing Azure OpenAI.
- `SEARCH_ENDPOINT`: Endpoint for your Azure Cognitive Search resource.
- `SEARCH_API_KEY`: API key for Azure Cognitive Search.
- `SEARCH_INDEX`: Name of the Azure Cognitive Search index.


## API Usage
### Endpoint
The chatbot is exposed via the following HTTP POST endpoint:
`POST /rag-chatbot-aisearch`

### Request Format
Send a JSON payload containing the user query:
```json
{
  "query": "<user_query>"
}
```

### Response Format
The API returns a JSON response containing the relevant URL or answer:
```json
{
  "response": {
    "URL": "www.example.com"
  }
}
```

---

## Example Usage
### Request
```json
{
  "query": "Take me to about section"
}
```

### Response
```json
{
    "response": {
        "URL": "https://www.rsystems.com/about-us/"
    }
}
```

## Hands-on
![image](https://github.com/user-attachments/assets/9a7eabfd-cbde-430f-a901-b9584ca786aa)

### [Deployed function URL](https://auto-browsing-llm.azurewebsites.net/api/rag_chatbot_aisearch?code=K6L20I5_x6NXcs63ge9a0ECOscAJp-RAQsj6D8nBwtEBAzFuJunorg%3D%3D)

Use this link in Postman application, for hands-on:
![image](https://github.com/user-attachments/assets/df62dbd2-8dd9-4abb-bb48-c9e1acb710cc)


## Requirements:
### Platforms
- Azure Open AI Studio
- Azure AI Search
- Function App
- VS Code

### Language
- Python 

### Vector Database SDKs
- Azure AI Search

## Acknowledgments
This project leverages the following technologies:
- [Azure OpenAI](https://azure.microsoft.com/en-us/services/openai/): For natural language processing and chat completions.
- [Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/): For indexing and retrieving relevant content.


