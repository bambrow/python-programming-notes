#!/usr/bin/env python
# coding:utf-8

import sys

from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.commons.utils import JsCode


if __name__ == '__main__':

    input_file = sys.argv[1] if len(sys.argv) > 1 else 'map_locations.txt'

    locations = []

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            if line.strip():
                locations.append(line.strip())

    map_title = locations[0]
    locations = locations[1:]

    data = [0] * len(locations)
    loc_data_pair = [[locations[i], data[i]] for i in range(len(locations))]

    m = Geo(init_opts=opts.InitOpts(width='1440px', height='1080px'))
    m.set_global_opts(
        title_opts=opts.TitleOpts(
            title=map_title,
            title_textstyle_opts=opts.TextStyleOpts(
                font_size=30
            )
        ),
        toolbox_opts=opts.ToolboxOpts(
            is_show=True,
            feature=opts.ToolBoxFeatureOpts(
                save_as_image=opts.ToolBoxFeatureSaveAsImageOpts(
                    background_color='white'
                )
            )
        ),
    )
    m.add_schema(maptype='china')
    m.add(
        series_name='',
        data_pair=loc_data_pair,
        color="red",
        label_opts=opts.LabelOpts(
            is_show=True,
            position='top',
            formatter=JsCode(
                "function (params) {return params.name;}"
            ),
            color='red',
            font_size=15,
            font_weight='bold'
        )
    )
    m.render('pyecharts_china.html')
