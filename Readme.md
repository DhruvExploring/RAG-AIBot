# RAG-AIBot-3B1B probability

This is a RAG (retrieval augmented generation) based AI bot which can answer questions based on the popular youtube playlist of 3 Blue 1 Brown on probability. 

## features

1) It can answer questions based on the popular youtube playlist of 3 Blue 1 Brown on probability. 
2) The response generated is based on the context of the video and the timestamps of the video are also mentioned in the response.
3) clean chatbot interface enables a smooth user experience.

## techstack

1) React
2) FastAPI
3) Ollama - Bge-m3
4) Whisper 
5) Python
6) OpenAI GPT - 5 - mini
7) Google GenAI - Gemini 3 Flash preview

## Installing 

1) clone the repository
2) cd into the repository
3) ```pip install -r requirements.txt```

## Running the project
1) cd into the backend folder

    
   ``` uvicorn main:app```

2) cd into the frontend folder

    ```npm install```
    ```npm start```



## How it works
1) The user enters a question in the chatbot interface.
2) The question is sent to the backend server where the top 5 relevant videos are fetched from the youtube playlist using cosine similarity.
3) The backend server uses the OpenAI GPT-5 Mini model (or any LLM model) to generate a response.
4) The response is sent back to the frontend server.
5) The frontend server sends the response to the user.


# Future scope
1) The model can be build upon all the videos of 3Blue1Brown.
2) The time required to generate the response can be reduced by a more optimal method of embedding traversal.
3) The model can be deployed on a cloud platform.
4) The chat interface can be memory enabled and can remember the previous conversation.
5) The model can be used again for other purposes with a better transcription model.

# Author
**Dhruv Pandey**