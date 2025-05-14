
import pandas as pd
import numpy as np

def get_energy_projection_data(region):
    years = np.arange(2026, 2041)
    ai_percent = np.linspace(0.24, 10, len(years))

    baselines = {
        "Global": 30000,
        "USA": 4300,
        "New York State": 150
    }

    base = baselines[region]
    ai_demand = (ai_percent / 100) * base
    clean = ai_demand * 0.3
    unmet = ai_demand - clean
    invest = unmet * 150_000_000 / 1e9  # Convert to billion USD

    return pd.DataFrame({
        'Year': years,
        'AI_Demand_TWh': ai_demand,
        'Clean_Energy_TWh': clean,
        'Unmet_Energy_TWh': unmet,
        'Investment_Needed_BillionUSD': invest
    })
