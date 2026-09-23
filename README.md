# TripMate AI

AI-powered travel planner built with Streamlit and Google Gemini.

This app asks a few trip details, creates a custom travel prompt, and generates a practical itinerary with destinations, activities, food suggestions, transport ideas, and budget-aware guidance.

## Features

- Destination-based trip planning
- Custom itinerary based on:
  - number of days
  - traveler type
  - interests
  - budget level
  - season
- AI-generated day-by-day recommendations
- Modern glassmorphism UI with animated travel styling
- Built-in loading state while Gemini generates the response

## Tech Stack

- Python
- Streamlit
- Google GenAI SDK
- python-dotenv

## Project Files

- `main.py` — Streamlit app and Gemini integration
- `.env` — environment variables (API key)

## Requirements

Install the required Python packages:

```bash
pip install streamlit python-dotenv google-genai
```

## Environment Setup

Create a `.env` file in the project root or in the location your environment loader expects, and add your Google API key:

```env
GOOGLE_API_KEY=your_api_key_here
```

> Note: the current app loads the environment from a fixed path in `main.py` using `load_dotenv(...)`. If you are running this on another machine, update that path to match your local `.env` file.

## Run the App

From the `travel_assistant` folder:

```bash
streamlit run main.py
```

## How It Works

1. Enter the destination.
2. Add the trip duration.
3. Choose traveler type and interests.
4. Select budget and season.
5. Click the planning button.
6. The app builds a prompt and sends it to Gemini.
7. The generated itinerary is displayed in the app.

## Example Prompt Inputs

- Destination: Bali
- Days: 5
- Travelers: Couple
- Interests: Relaxation, Food, Nature
- Budget: Mid-range comfort
- Season: Summer

The app generates a response like:

- destination overview
- daily itinerary
- sightseeing spots
- local food recommendations
- transportation suggestions
- approximate budget guidance
- useful travel tips

## Notes

- The app does not check live flight, hotel, or weather data.
- It gives practical suggestions based on the information you provide.
- It is designed for itinerary planning and travel inspiration rather than real-time booking or price verification.

## License

This project is for learning and personal use.

