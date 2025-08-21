🔹 Is the code enough for analysis?

✅ Yes — because you’ve got:

Granular data: every call has wait time, handle time, sentiment, CSAT, abandoned flag, etc.

Relational-friendly schema: calls table is already in Postgres.

Flexibility: you can group by queue, interval, agent, date to get metrics.

⚠️ What’s missing (but you can add later):

Agent shift data (for occupancy/coverage analysis).

Shrinkage (breaks, absence, training).

Scheduled vs actual calls handled (for forecasting accuracy checks).

🔹 Key Metrics to Start With

These are the “RTA dashboard basics” you should calculate:

Call Volume

Calls offered (total calls).

Calls answered vs abandoned.

Abandon rate (%).

Service Level (SLA)

% of calls answered within SLA (e.g., 80% within 20s).

Agent Productivity

Calls handled per agent per day.

Average Handle Time (AHT).

Occupancy = handle_time / (shift_time × agents).

Resolution & Quality

% Resolved calls.

First Call Resolution (FCR %).

CSAT average & distribution.

Sentiment distribution.

Interval Metrics

Calls per 30-min interval.

SLA per interval.

Abandon rate per interval.

🔹 How to Calculate in Pandas (example functions)

Here’s a starting point:

# Basic KPIs
def calculate_metrics(df, sla_seconds=20):
    metrics = {}
    metrics['total_calls'] = len(df)
    metrics['answered_calls'] = len(df[~df['abandoned']])
    metrics['abandoned_calls'] = len(df[df['abandoned']])
    metrics['abandon_rate'] = metrics['abandoned_calls'] / metrics['total_calls']

    metrics['sla'] = (
        len(df[(df['wait_time'] <= sla_seconds) & (~df['abandoned'])]) 
        / metrics['answered_calls']
    )

    metrics['aht'] = df.loc[~df['abandoned'], 'handle_time'].mean()
    metrics['fcr'] = df.loc[~df['abandoned'], 'fcr'].mean()
    metrics['csat'] = df.loc[df['csat_score'].notna(), 'csat_score'].mean()
    metrics['resolved'] = df.loc[~df['abandoned'], 'resolved'].mean()
    
    return metrics

kpis = calculate_metrics(df)
print(kpis)

🔹 Pivot Tables for RTA

You’ll want interval-level pivot tables like:

# Calls per interval
interval_stats = df.groupby(['date', 'interval_num']).agg({
    'call_id': 'count',
    'abandoned': 'mean',
    'wait_time': 'mean',
    'handle_time': 'mean'
}).reset_index()

# Calls per agent
agent_stats = df.groupby(['agent_id', 'date']).agg({
    'call_id': 'count',
    'handle_time': 'mean',
    'resolved': 'mean',
    'csat_score': 'mean'
}).reset_index()


These pivot tables let you build SLA charts, heatmaps, and per-agent dashboards.

🔹 Suggested Next Step

Since you already export to Postgres, I’d suggest:

Run SQL queries (same KPIs above, but in SQL) → shows SQL skill.

Validate realism → compare outputs to industry benchmarks (SLA ~80%, abandon <5%, AHT 6–8 min).

Save results → export summaries (CSV/Excel or straight into dashboards).

👉 Question for you:
Do you want me to draft a metrics module (a Python file with functions that compute all the above KPIs from your Postgres calls table), or would you prefer SQL views so the metrics live inside the database? Both are useful for RTA.
