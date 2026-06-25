import folium
from graph import ports

def create_map(path):
    if not path:
        return

    m = folium.Map(location=ports[path[0]], zoom_start=5)

    # ports
    for name, coord in ports.items():
        folium.Marker(coord, tooltip=name).add_to(m)

    # route
    route = [ports[p] for p in path]
    folium.PolyLine(route, color="blue", weight=4).add_to(m)

    m.save("route_map.html")