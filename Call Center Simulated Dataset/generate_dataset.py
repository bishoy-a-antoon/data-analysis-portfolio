import pandas as pd
import random
import numpy as np
from datetime import datetime, timedelta

# Generate synthetic call center dataset
np.random.seed(42)
num_rows = 2000

agents = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eli', 'John', 'Anna', 'Michael', 'James']
departments = ['Billing', 'Shipping', 'Technical Support', 'Sales']
sentiments = ['Very Negative', 'Negative', 'Neutral', 'Positive', 'Very Positive']

start_date = datetime.today() - timedelta(days=14)

data = {
            'Timestamp': [(start_date + timedelta(minutes=random.randint(0, 20160))).strftime('%Y-%m-%d %H:%M:%S') for _ in range(num_rows)],
                'Agent': [random.choice(agents) for _ in range(num_rows)],
                    'Department': [random.choice(departments) for _ in range(num_rows)],
                        'Call Duration (mins)': [round(random.uniform(2, 15), 1) for _ in range(num_rows)],
                            'Resolved': [random.choice(['Yes', 'No']) for _ in range(num_rows)],
                                'CSAT Score': [random.choice([1, 2, 3, 4, 5]) for _ in range(num_rows)],
                                    'Sentiment': [random.choice(sentiments) for _ in range(num_rows)],
                                        'Escalated': [random.choice(['Yes', 'No']) for _ in range(num_rows)]
                                        }

df = pd.DataFrame(data)

# Save to CSV
csv_path = './call_center_dataset.csv'
df.to_csv(csv_path, index=False)

