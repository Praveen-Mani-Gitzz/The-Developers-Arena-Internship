
# 🌤️ Weather Dashboard Application

## 📌 Project Overview

The Weather Dashboard Application is a console-based Python application that integrates with the OpenWeatherMap API to fetch and display real-time weather information.

This project demonstrates professional software development practices including API integration, JSON parsing, environment variable management, modular architecture, caching mechanisms, and structured error handling.

The system allows users to search for weather conditions in any city worldwide and interact through a clean command-line interface.

---

## 🎯 Project Objectives

- Integrate a third-party weather API
- Make HTTP requests using the requests library
- Parse complex JSON responses
- Implement API response caching
- Securely manage API keys using environment variables
- Build a modular and maintainable application structure
- Implement comprehensive error handling
- Follow professional Python development practices

---

## 🚀 Features

✔ Current weather for any city worldwide  
✔ Temperature display with color-coded output  
✔ Weather condition icons  
✔ Wind speed, humidity, pressure information  
✔ Sunrise and sunset details  
✔ API response caching (10-minute cache system)  
✔ Refresh option to force new API call  
✔ Search functionality for multiple cities  
✔ Secure API key management using .env  
✔ Robust error handling for API failures  
✔ Clean modular project architecture  

---

## 🏗️ System Architecture

The application is divided into multiple modules for clear separation of concerns:

### 🔹 config.py
- Loads API key from environment variables
- Defines API base URL
- Sets cache duration configuration

### 🔹 weather_api.py
- Handles HTTP requests using requests
- Implements caching logic
- Manages API status code handling
- Handles network and timeout errors

### 🔹 weather_parser.py
- Extracts relevant fields from raw JSON responses
- Formats timestamps
- Converts temperature units
- Structures data into clean dictionaries

### 🔹 weather_display.py
- Formats and prints weather information
- Adds weather icons
- Implements color-coded temperature output
- Presents user-friendly dashboard layout

### 🔹 main.py
- Handles interactive command-line interface
- Coordinates all modules
- Manages user commands (search, refresh, help, quit)

This layered architecture ensures maintainability and scalability.

---

## 📂 Project Structure

```

week6-weather-dashboard/
│
├── weather_app/
│   ├── **init**.py
│   ├── config.py
│   ├── weather_api.py
│   ├── weather_parser.py
│   ├── weather_display.py
│   └── main.py
│
├── data/
│   ├── cache/
│   └── favorites.json
│
├── tests/
│   ├── test_api.py
│   ├── test_parser.py
│   └── test_display.py
│
├── requirements.txt
├── .env.example
├── README.md
└── .gitignore

```

---

## 🔧 Installation & Setup

### Step 1: Clone the Repository

```

git clone [https://github.com/yourusername/week6-weather-dashboard.git](https://github.com/yourusername/week6-weather-dashboard.git)

```

### Step 2: Navigate to Project Directory

```

cd week6-weather-dashboard

```

### Step 3: Create Virtual Environment

```

python -m venv venv

```

Activate environment:

Windows:
```

venv\Scripts\activate

```

### Step 4: Install Dependencies

```

pip install -r requirements.txt

```

### Step 5: Configure API Key

Create a `.env` file in the project root:

```

WEATHER_API_KEY=your_api_key_here

```

You can obtain a free API key from:

https://openweathermap.org

### Step 6: Run the Application

```

python -m weather_app.main

```

---

## 📊 Example Output

```

# 🌤️  WEATHER DASHBOARD

📍 Location: London, GB
🕐 Last Updated: 2024-01-25 10:15:00

## Current Weather

Temperature:   8°C
Feels Like:    5°C
Condition:     Light rain 🌧️
Humidity:      87%
Wind Speed:    22 m/s
Pressure:      1009 hPa
Sunrise:       07:45
Sunset:        16:30

```

---

## 💾 Caching Mechanism

- Weather data is cached locally for 10 minutes.
- If a request is made within cache duration, cached data is used.
- This reduces API calls and improves performance.
- Users can force refresh to retrieve updated data.

---

## ⚠️ Error Handling

The system handles:

- Invalid API key (401)
- City not found (404)
- API rate limit exceeded (429)
- Network timeout errors
- Connection errors
- Unexpected exceptions

Graceful messages are displayed to the user.

---

## 📦 Required Libraries

- requests
- python-dotenv
- colorama

All dependencies are listed in requirements.txt.

---

## 🧠 What I Learned

- Integrating external APIs
- Making HTTP requests using requests
- Parsing nested JSON structures
- Implementing caching mechanisms
- Managing environment variables securely
- Designing modular applications
- Handling real-world network errors
- Writing clean, maintainable code

---

## ✅ Conclusion

The Weather Dashboard Application demonstrates professional Python development practices, including API integration, modular architecture, structured error handling, and secure configuration management.

This project strengthened my understanding of working with external services and building scalable, maintainable applications using industry-relevant tools and techniques.


---



