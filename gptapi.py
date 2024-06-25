import os 
import openai
from dotenv import load_dotenv
from openai import OpenAI


# Load environment variables from a .env file
load_dotenv()


# Set environment variables
my_api_key = os.getenv("OPENAI_KEY")

openai.api_key = my_api_key
print(my_api_key)
# WRITE YOUR CODE HERE
client = OpenAI(
    api_key=my_api_key,
)

# Specify the model to use and the messages to send
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a university instructor and can explain programming concepts clearly in a few words."},
        {"role": "user", "content": "What are the advantages of pair programming?"}
    ]
)
print(completion.choices[0].message.content)