import openai as OpenAI
import os 
import data as data
SECRET_KEY = os.environ.get('OPENAI_API_KEY')

OpenAI.api_key = SECRET_KEY


def query(prompt):
    response = OpenAI.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {
                "role":"system",
                "content":"Your are a skilled cybersecurity analyst with expertice to detect phishing content."
            },
            {
                "role":"user",
                "content": prompt
            }
        ]
    )
    #choose the first generated response[choices][0], extracts the content of it [message][content]
    queryResponse,likelihood,classification, = data.apiHandler(response.model_dump()['choices'][0]['message']['content'])
    print(classification, likelihood)
    return queryResponse, likelihood, classification 
    