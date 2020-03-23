#!/usr/bin/env python
# coding:utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import sys


if __name__ == "__main__":

    # map shapefile download
    # https://gadm.org/download_country_v3.html
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'map_data.csv'
    map_title = sys.argv[2] if len(sys.argv) > 2 else ''
    df = pd.read_csv(input_file, names=['lat', 'lon'])

    land_color = '#f5f5f3'
    water_color = '#cdd2d4'
    coastline_color = '#f5f5f3'
    border_color = '#cccccc'
    state_color = '#999999'
    meridian_color = '#eaeaea'
    marker_fill_color = '#df2d2d'
    marker_edge_color = 'None'

    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot(111, facecolor='#ffffff', frame_on=False)
    ax.set_title(map_title, fontsize=18, color='#333333')

    m = Basemap(projection='mill', resolution='i', llcrnrlat=14, urcrnrlat=55, llcrnrlon=70, urcrnrlon=140)
    m.drawmapboundary(color=border_color, fill_color=water_color)
    m.drawcoastlines(color=coastline_color)
    m.drawstates(color=state_color)
    m.drawcountries(color=border_color)
    m.readshapefile('resources/gadm36_CHN_shp/gadm36_CHN_1', 'provinces', drawbounds=True, color=state_color, linewidth=0.8)
    m.readshapefile('resources/gadm36_TWN_shp/gadm36_TWN_0', 'taiwan', drawbounds=True, color=state_color, linewidth=0.8)
    m.fillcontinents(color=land_color, lake_color=water_color)
    m.drawparallels(np.arange(-90., 90., 10.), labels=[1, 0, 0, 0], color=meridian_color, fontsize=10)
    m.drawmeridians(np.arange(0., 360., 10.), labels=[0, 0, 0, 1], color=meridian_color, fontsize=10)

    x, y = m(df['lon'].values, df['lat'].values)
    m.scatter(x, y, s=90, marker='o', color=marker_fill_color, edgecolor=marker_edge_color, alpha=1, zorder=3)

    plt.savefig('basemap_china.png', dpi=300, bbox_inches='tight', pad_inches=0.1)
    plt.show()
