import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI Energy Demand Dashboard", layout="wide")
st.title("🔋 AI Energy Demand vs Clean Power Availability")

# Region selector
region = st.selectbox("Select Region", ["Global", "USA", "New York State"])

# Electricity baselines (TWh/year)
baselines = {
    "Global": 30000,
    "USA": 4300,
    "New York State": 150
}

# AI demand percentages over time
years = np.arange(2026, 2041)
ai_percent = np.linspace(0.24, 10, len(years))
baseline = baselines[region]

# Calculations
ai_demand = (ai_percent / 100) * baseline
clean_energy = ai_demand * 0.3
unmet_energy = ai_demand - clean_energy
investment_billion = unmet_energy * 150_000_000 / 1e9  # convert to billions

# Build DataFrame
df = pd.DataFrame({
    "Year": years,
    "AI_Demand_TWh": ai_demand,
    "Clean_Energy_TWh": clean_energy,
    "Unmet_Energy_TWh": unmet_energy,
    "Investment_Billion_USD": investment_billion
})

# Chart: AI demand
st.subheader(f"📈 Projected AI Electricity Demand in {region}")
st.line_chart(df.set_index("Year")[["AI_Demand_TWh"]])

# Chart: Clean vs Unmet Energy
st.subheader("📊 Clean Energy vs Unmet AI Demand")
fig, ax = plt.subplots(figsize=(10, 4))
ax.bar(df["Year"], df["Clean_Energy_TWh"], color="green", label="Clean Energy")
ax.bar(df["Year"], df["Unmet_Energy_TWh"], bottom=df["Clean_Energy_TWh"], color="red", label="Unmet Energy")
ax.set_ylabel("TWh")
ax.set_xlabel("Year")
ax.set_title(f"{region}: Energy Supply Stack")
ax.legend()
st.pyplot(fig)

# Chart: Investment Required
st.subheader("💵 Investment Needed to Close the Gap")
st.bar_chart(df.set_index("Year")[["Investment_Billion_USD"]])

# Raw table
st.subheader("📄 Underlying Data")
st.dataframe(df)
