# Weather-Based Outfit Recommender

### Overview
Weather Wear is an application that suggests outfits based on the weather conditions of a specified location. 
Users can get outfit recommendations, save their favorite outfits, and view saved favorites. 
The application uses OpenAI's GPT-3.5 for outfit recommendations and a weather API to fetch real-time weather data.

### Features
1. ***Get Outfit Recommendation***: Fetches weather data for a specified location and provides outfit recommendations based on the weather conditions.
2. ***Save to Favorites***: Users can save their favorite outfit recommendations to their profile.
3. ***View Favorite Outfits***: Users can view their saved outfit recommendations.
4. ***User Authentication***:Users need to create an account or log in to save and view favorite outfits.

### Project Structure
- ***main.py***: runs the application. 
- ***gptapi***: contains the code to interact with the OpenAI API to get outfit recommendations based on weather data.
- ***sql.py***: handles database operations. It includes functions to create new users, authenticate users, save favorite outfits, and view favorite outfits.
- ***weatherAPI.py***: fetches real-time weather data from the Tomorrow.io weather API.

### Setup
#### Prerequisites
- Python 3.6 or higher
- OpenAI API key
- [Tomorrow.io Weather API key](https://www.tomorrow.io/a/faq/weather-api/how-to-get-a-weather-api-key/)

#### Installation
1. Clone the repository
2. Install required packages:
   - pip install openai
   - pip install requests
   - pip install python-dotenv
3. Create a `.env` file in the root directory and add your API keys:
   - OPENAI_KEY=your_openai_api_key
   - API_KEY=your_weather_api_key

### Usage
Run main script:
- python main.py
