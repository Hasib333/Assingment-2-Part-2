print("\nOverall risk rate:", merged['risk'].mean())
print("Overall reward rate:", merged['reward'].mean())

by_season = merged.groupby('season').agg(
    n=('risk','size'),
    risk_rate=('risk','mean'),
    reward_rate=('reward','mean'),
    vigilance=('bat_landing_to_food','mean'),
    rat_minutes=('rat_minutes','mean'),
    rat_arrivals=('rat_arrival_number','mean')
).reset_index()

print("\nRisk/Reward/Vigilance by Season:")
print(by_season)

# Save CSV summary
by_season.to_csv(os.path.join(BASE_DIR, "by_season_summary.csv"), index=False)