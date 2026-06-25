ports = {
    "Mumbai": (18.943, 72.839),
    "Goa": (15.2993, 74.1240),
    "Kochi": (9.9312, 76.2673),
    "Chennai": (13.0827, 80.2707),
    "Kolkata": (22.5726, 88.3639)
}

graph = {
    "Mumbai": {"Goa": 10, "Kochi": 25},
    "Goa": {"Mumbai": 10, "Kochi": 12, "Chennai": 18},
    "Kochi": {"Mumbai": 25, "Goa": 12, "Chennai": 10},
    "Chennai": {"Goa": 18, "Kochi": 10, "Kolkata": 15},
    "Kolkata": {"Chennai": 15}
}