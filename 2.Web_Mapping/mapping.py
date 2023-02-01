#!/usr/bin/env python3

"""
Developed by adejonghm
----------

Tiles for Map: "Stamen Terrain", "Stamen Watercolor", "OpenStreetMap"

CircleMarker:
    It has several optional parameters "color" is used to define the color (outline by default), if the parameter "fill" is True, the mark will be filled.
    The "opacity" parameter allows you to control the transparency of the outline, and "fill_opacity" the transparency of the fill. There is another
    parameter "fill_color" which is used to define the fill color, so you can define one color for the fill and another for the outline. With this combination
    of parameters, "fill=True/False" is not used.
"""

import folium
import pandas


def color_icon(elevation):
    if elevation < 1500:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


if __name__ == "__main__":
    volcanoes = pandas.read_csv("datasources/Volcanoes.txt")
    lat = volcanoes["LAT"]
    lon = volcanoes["LON"]
    elev = volcanoes["ELEV"]

    html = """
    <b>Volcano information:</b><hr>
    Height: %s m
    """

    map = folium.Map(location=[38.58, -99.09],
                     zoom_start=5, tiles="OpenStreetMap")

    fgp = folium.FeatureGroup(name="World Population")
    fgp.add_child(folium.GeoJson(data=open('datasources/world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {
                  'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
    map.add_child(fgp)

    fgv = folium.FeatureGroup(name="Volcanous")
    for lt, ln, el in zip(lat, lon, elev):
        iframe = folium.IFrame(html=html % str(el), width=170, height=90)
        # fgv.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color=color_icon(el))))
        fgv.add_child(folium.CircleMarker(location=[lt, ln], popup=folium.Popup(
            iframe), radius=5, color=color_icon(el), fill=True, opacity=0.4, fill_opacity=0.7))
    map.add_child(fgv)

    map.add_child(folium.LayerControl())
    map.save("demo_map.html")
