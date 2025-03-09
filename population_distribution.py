import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#load dataset
data_url = "https://datahub.io/core/population/r/population.csv"
df = pd.read_csv(data_url)

# Filter data for the latest available year
latest_year = df['Year'].max()
df_latest = df[df['Year'] == latest_year]

# Selection of top 10 most populous countries
df_top10 = df_latest.sort_values(by='Value', ascending=False).head(10)

# Plot bar chart with enhanced visualization
plt.figure(figsize=(14, 7))
sns.barplot(x='Country Name', y='Value', data=df_top10, palette='coolwarm', edgecolor='black')

# Add value labels on top of bars
for index, value in enumerate(df_top10['Value']):
    plt.text(index, value + (value * 0.02), f'{int(value):,}', ha='center', fontsize=12, fontweight='bold')

# Add gridlines and styling
plt.xlabel("Country", fontsize=14, fontweight='bold', color='darkred')
plt.ylabel("Population", fontsize=14, fontweight='bold', color='darkred')
plt.title(f" Top 10 Most Populous Countries in {latest_year} 📊", fontsize=18, fontweight='bold', color='darkblue')
plt.xticks(rotation=45, fontsize=12, color='darkgreen')
plt.yticks(fontsize=12, color='darkgreen')
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Improve layout and save the figure
plt.tight_layout()
plt.savefig("population_distribution.png", dpi=300, bbox_inches='tight', facecolor='white')
plt.show()

# Save dataset for reference
df_top10.to_csv("top10_population.csv", index=False)
