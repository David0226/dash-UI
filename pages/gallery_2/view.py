import dash_bootstrap_components as dbc
from dash import dcc 
from dash import html 
import dash_admin_components as dac

from pages.gallery_2.model import dataframe

content = dac.TabItem(
    [
        html.H1("GDP viewer"),
        html.Hr(),
        dcc.Graph(id='graph-with-slider'),
        dcc.Slider(
            id='year-slider',
            min=dataframe()['year'].min(),
            max=dataframe()['year'].max(),
            value=dataframe()['year'].min(),
            marks={str(year): str(year) for year in dataframe()['year'].unique()},
            step=None
        )
    ],
    id='content_gallery_2',
)
