import pymongo
import plotly
import plotly.graph_objects as go

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["armageddon"]

mapbox_access_token = "pk.eyJ1IjoiZW1tYW51ZWwwOTA5IiwiYSI6ImNrM3hwbXZwYTA3cnUzbG5vMWZxc2p0aTUifQ.lvLd1wk5areFsQ3t_uYgcA"
mapbox_style = "mapbox://styles/emmanuel0909/ck41idou40px81co820zpvcxd"

crashes = db["plane_crashes"]

Latitude_1 = []
Latitude__2 = []
Latitude__3 = []
Latitude__4 = []

Longitude_1 = []
Longitude__2 = []
Longitude__3 = []
Longitude__4 = []

for obj in crashes.find():
    if obj["TotalFatalInjuries"] != '  ' and obj["TotalFatalInjuries"] is not None:
        if int(obj["TotalFatalInjuries"]) >= 300:
            Latitude_1.append(obj["Latitude"])
            Longitude_1.append(obj["Longitude"])
        elif int(obj["TotalFatalInjuries"]) <300 and int(obj["TotalFatalInjuries"]) >= 200:
            Latitude__2.append(obj["Latitude"])
            Longitude__2.append(obj["Longitude"])
        elif int(obj["TotalFatalInjuries"]) <200 and int(obj["TotalFatalInjuries"]) >= 100:
            Latitude__3.append(obj["Latitude"])
            Longitude__3.append(obj["Longitude"])
        else:
            Latitude__4.append(obj["Latitude"])
            Longitude__4.append(obj["Longitude"])
    else:
        Latitude__4.append(obj["Latitude"])
        Longitude__4.append(obj["Longitude"])

L4 = [go.Scattermapbox(
        lat=Latitude_1,
        lon =Longitude_1,
        mode = 'markers',
        marker=dict(
            size=20,
            color='red',
            opacity = 1,
        ),
        name="Greater than 300"
    )]

L3 = [go.Scattermapbox(
        lat=Latitude__2,
        lon =Longitude__2,
        mode = 'markers',
        marker=dict(
            size=15,
            color='orange',
            opacity = 1,
        ),
        name="300-200"
    )]

L2 = [go.Scattermapbox(
        lat=Latitude__3,
        lon =Longitude__3,
        mode = 'markers',
        marker=dict(
            size=10,
            color='yellow',
            opacity = 1,
        ),
        name="200-100"
    )]

L1 = [go.Scattermapbox(
        lat=Latitude__4,
        lon =Longitude__4,
        mode = 'markers',
        marker=dict(
            size=5,
            color='blue',
            opacity = 1,
        ),
        name="Below 100"
    )]

layout = go.Layout(autosize=True,
    mapbox = dict(accesstoken= mapbox_access_token,
    bearing=0,
    pitch=0,
    zoom=5,
    center=dict(lat=0,lon=0),
    style=mapbox_style),
    width=1500,
    height=1080,
    title = "Armageddon3")

output = dict(data=L1+L2+L3+L4, layout=layout)
plotly.offline.plot(output, filename='Arm3.html')