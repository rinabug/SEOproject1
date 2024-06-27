import os 
import openai
from dotenv import load_dotenv
from openai import OpenAI


# Load environment variables from a .env file
load_dotenv()


# Set environment variables
my_api_key = os.getenv("OPENAI_KEY")

openai.api_key = my_api_key
# WRITE YOUR CODE HERE
client = OpenAI(
    api_key=my_api_key,
)
def recomendation(info):
# Specify the model to use and the messages to send
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are giving outfit recomendation to the client based on this weather informetion."},
            {"role": "user", "content": f'The Weather is : {info} What outfit should I wear? Also, output the temperature in fahrenheit and celcius and output the outfit recomendation as a list.'}
        ]
    )   
    return completion.choices[0].message.content

#if __name__ == "__main__":
#    recomendation('{"data":{"time":"2024-06-26T16:13:00Z","values":{"cloudBase":0.29,"cloudCeiling":0.29,"cloudCover":68,"dewPoint":18,"freezingRainIntensity":0,"humidity":71,"precipitationProbability":0,"pressureSurfaceLevel":1014.15,"rainIntensity":0,"sleetIntensity":0,"snowIntensity":0,"temperature":23.5,"temperatureApparent":23.5,"uvHealthConcern":0,"uvIndex":0,"visibility":16,"weatherCode":1102,"windDirection":6.88,"windGust":1,"windSpeed":1}},"location":{"lat":35.72515106201172,"lon":139.76300048828125,"name":"NEWYORK, 不忍通り, 千駄木三丁目, 文京区, 東京都, 113-0022, 日本","type":"yes"}')