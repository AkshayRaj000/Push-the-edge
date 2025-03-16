import gspread
import pandas as pd
import plotly.graph_objects as go
from oauth2client.service_account import ServiceAccountCredentials

# ---- Google Sheets API Setup ----
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("mythical-way-453915-n9-f1c19f0ed37b.json", scope)
client = gspread.authorize(creds)

# ---- Fetch Data from Google Sheets ----
sheet = client.open("bodylog").worksheet("Sheet1")  # Change to your actual sheet name
data = pd.DataFrame(sheet.get_all_records())

# Convert Date column to datetime format
data["Date"] = pd.to_datetime(data["Date"], errors="coerce")

# ---- Create Plotly Graph ----
fig = go.Figure()
fig.add_trace(go.Scatter(x=data['Date'], y=pd.to_numeric(data['Pushups max'], errors='coerce'), mode='lines', name='Pushups max', fill='tozeroy'))
fig.add_trace(go.Scatter(x=data['Date'], y=pd.to_numeric(data['Squats max'], errors='coerce'), mode='lines', name='Squats max', fill='tozeroy'))
fig.add_trace(go.Scatter(x=data['Date'], y=pd.to_numeric(data['Hollow body hold'], errors='coerce'), mode='lines', name='Hollow body hold', fill='tozeroy'))
fig.add_trace(go.Scatter(x=data['Date'], y=pd.to_numeric(data['Leg raises max'], errors='coerce'), mode='lines', name='Leg raises max', fill='tozeroy'))

# Update layout
fig.update_layout(title='PUSH THE EDGE', xaxis_title='Date', yaxis_title='Count')
fig.update_layout(title={'text': 'PUSH THE EDGE', 'x': 0.5, 'font': {'family':'Times New Roman', 'size': 24}})

# ---- Save as an HTML File for GitHub Pages ----
fig.write_html("index.html")
print("✅ Graph saved as 'index.html' - Ready for GitHub Pages!")
