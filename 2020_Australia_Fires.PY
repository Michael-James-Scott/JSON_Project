#PROGRAM:   2020 Australian Fires 
#PURPOSE:   To plot data about 2020 Australian fires on a colored graph 
#DATE:      2/12/2020
#AUTHOR:    Mike Scott

from plotly.graph_objs import scattergeo,Layout
from plotly import offline


#CREATE THE LISTS TO STORE THE DATA
temps,lons,lats,hover_texts = [],[],[],[]

#OPEN THE TXT FILE 
with open('MODIS_C6_Australia_NewZealand_MCD14DL_NRT_2020026.txt','r') as txt_file:

    #SKIP THE FIRST HEADER ROW
    next(txt_file)

    #ITERATE THROUGH THE ROWS, COLLECT AND STORE DATA
    for row in txt_file:

        #SPLIT THE FIELDS IN THE ROW BY COMMAS
        field = row.split(",")

        #GRAB DATA
        lat = field[0]
        lon = field[1]
        temp = float(field[2])
        hover_text= field[5]

        #STORE DATA IN LISTS
        temps.append(temp)
        lons.append(lon)
        lats.append(lat)
        hover_texts.append(hover_text)

    #CREATE DATA LIST FOR THE PLOTLY GRAPH
    data = [{ 
                'type':'scattergeo',
                'lon':lons,
                'lat':lats,
                'text':hover_texts,
                'marker':{
                    'size':[temp/15 for temp in temps],
                    'color': temps,
                    'colorscale':'Viridis',
                    'reversescale':True,
                    'colorbar':{'title':'Brightness'}
                },
    }]

#CREATE LAYOUT
fires_2020_layout = Layout(title="Australian Fires - January 2020")

#CREATE THE GRAPH
fig = {'data':data,'layout':fires_2020_layout}

#SAVE THE HTML FILE
offline.plot(fig,filename='australia_fires_2020.html')