import pandas as pd
import joblib
import ollama
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import json
from dotenv import load_dotenv
import os
import math

load_dotenv()

df=joblib.load("embeddings.joblib")
# input_query=input("Enter your query: ")
def get_response(input_query):
    response = ollama.embed(
            model='bge-m3',
            input=[input_query],
            )
    input_embds=np.array(response.embeddings).reshape(1,-1)
    similarity_scores = cosine_similarity(input_embds, np.vstack(df['embedding']))
    top_results=np.argsort(similarity_scores)[0][::-1][:3]
    for i in top_results:
        for j in range(i-5,i+5):
            top_results=np.append(top_results,j)
            top_results=np.sort(top_results)

    relevant_data=df.iloc[top_results]
    relevant_data['start']=relevant_data['start'].apply(lambda x:(x/60))
    relevant_data['end']=relevant_data['end'].apply(lambda x:(x/60))
    # print(type(relevant_data))

    prompt= f"""

    The user has asked the following question:
    "{input_query}"
    This is in the context of this data:
    {relevant_data[['text','title','start','end']]} 

    generate a response for the question asked by the user and mention the video title and timestamps at which the user can find the relevant information.
    Act like you are the agent which is answering questions directly to the user and not like a chatbot.
    Do not mention anything else other the given context
    give a humainsed response to the user.
    In your response do not just mention the video numbers always mention the video title and timestamps.

    

    """
    # from openai import OpenAI
    # client = OpenAI()

    # response = client.responses.create(
    #     model="gpt-5-mini-2025-08-07",
    #     input=prompt
    # )

    # return response.output_text

    from google import genai

    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
    )

    return response.text


# res=get_response(input_query)
# print(res)

   
    
