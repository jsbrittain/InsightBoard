import dash
from dash import html
import dash_bootstrap_components as dbc

# Register the page
dash.register_page(__name__, path="/")


# Layout for the Home Page with Markdown
def layout():
    button_style = {
        'font-size': '25px',
        'padding': '10px 20px',
    }
    return html.Div([
        html.H1("Welcome to InsightBoard"),
        html.P("This dashboard allows you to upload and manage data and generate reports."),
        html.Div([
            dbc.Button("Upload", href="/uploads", style=button_style),
            dbc.Button("Data", href="/data", style=button_style),
            dbc.Button("Reports", href="/reports", style=button_style),
        ], style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'gap': '20px', 'margin-top': '60px'})
    ])
