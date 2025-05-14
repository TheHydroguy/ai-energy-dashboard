
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from ai_energy_model import get_energy_projection_data

st.set_page_config(page_title="AI Energy Demand Dashboard", layout="wide")

st.title("🔋 AI Energy Demand vs Clean Power Availability")

region = st.selectbox("Select Region", ["Global", "USA", "New York State"])
data = get_energy_projection_data(region)

st.subheader(f"📈 Projected AI Electricity Demand in {region}")
st.line_chart(data[['AI_Demand_TWh']])

st.subheader("📊 Energy Supply vs Gap")
fig, ax1 = plt.subplots(figsize=(10, 4))
ax1.bar(data['Year'], data['Clean_Energy_TWh'], label='Clean Energy', color='green')
ax1.bar(data['Year'], data['Unmet_Energy_TWh'], bottom=data['Clean_Energy_TWh'], label='Unmet Energy', color='red')
ax1.set_ylabel("TWh")
ax1.set_xlabel("Year")
ax1.legend()
st.pyplot(fig)

st.subheader("💵 Annual Investment Needed to Close the Gap")
st.bar_chart(data.set_index('Year')[['Investment_Needed_BillionUSD']])
