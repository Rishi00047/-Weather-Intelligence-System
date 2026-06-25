# Smart Maritime Navigation & Weather Intelligence System

## Overview
This project is a Python-based intelligent maritime navigation system that finds optimal sea routes between ports using Dijkstra’s algorithm and enhances decision-making using real-time weather data analysis. It also visualizes routes on interactive maps.

---

## Features
- Shortest path calculation using optimized Dijkstra’s Algorithm
- Real-time weather data integration (OpenWeather API)
- Weather-based risk analysis (Low / Moderate / High)
- Interactive route visualization using Folium
- Modular and scalable system design
- REST-based Flask web interface

---

## Tech Stack
- Python 3
- Flask
- Folium
- Requests
- OpenWeather API
- Graph Algorithms

---

## Project Structure
- app.py → Main Flask application
- routing.py → Optimized shortest path logic
- graph.py → Port network data
- weather_service.py → Weather API + risk analysis
- map_service.py → Map generation
- config.py → API key configuration

---

## How It Works
1. User selects start and destination ports
2. System calculates shortest route using Dijkstra’s algorithm
3. Weather data is fetched for destination port
4. Risk level is analyzed based on weather conditions
5. Route is visualized on an interactive map
6. Results are displayed via Flask API

---

## Output
- Optimal maritime route
- Distance between ports
- Weather conditions at destination
- Risk level assessment
- Interactive map file (route_map.html)