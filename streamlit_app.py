import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set up page
st.set_page_config(page_title="AI Energy Demand Dashboard", layout="wide")
st.title("🔋 AI Energy Demand vs Clean Power Availability")

# Select region
region = st.selectbox("Select Region", ["Global", "USA", "New York State"])

# Demand baselines
baselines = {
    "Global": 30000,
    "USA": 4300,
    "New York State": 150
}

# Generate data
years = np.arange(2026, 2041)
ai_percent = np.linspace(0.24, 10, len(years))
base = baselines[region]

ai_demand = (ai_percent / 100) * base
clean = ai_demand * 0.3
unmet = ai_demand - clean
investment = unmet * 150_000_000 / 1e9  # in billion USD

df = pd.DataFrame({
    "Year": years,
    "AI_Demand_TWh": ai_demand,
    "Clean_Energy_TWh": clean,
    "Unmet_Energy_TWh": unmet,
    "Investment_BillionUSD": investment
})

# Line chart: Demand
st.subheader(f"📈 Projected AI Electricity Demand in {region}")
st.line_chart(df.set_index("Year")[["AI_Demand_TWh"]])

# Bar chart: Clean vs Unmet
st.subheader("📊 Clean Energy vs Unmet AI Demand")
fig, ax = plt.subplots()
ax.bar(df["Year"], df["Clean_Energy_TWh"], label="Clean Energy", color="green")
ax.bar(df["Year"], df["Unmet_Energy_TWh"], bottom=df["Clean_Energy_TWh"], label="Unmet Energy", color="red")
ax.set_xlabel("Year")
ax.set_ylabel("TWh")
ax.set_title(f"{region}: Energy Supply Stack")
ax.legend()
st.pyplot(fig)

# Investment
st.subheader("💵 Annual Investment Needed to Close Gap")
st.bar_chart(df.set_index("Year")[["Investment_BillionUSD"]])

# Raw Data
st.subheader("📄 Raw Data Table")
st.dataframe(df)
