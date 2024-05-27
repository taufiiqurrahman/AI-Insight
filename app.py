
from flask import Flask, jsonify
import pandas as pd
import plotly.express as px
import os

app = Flask(__name__)

def process_data_and_generate_plots():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Data boq.csv'), encoding='utf-8')

    vendor_mapping = {
        'PT. Berca Engineering': 'PT Berca Engineering',
        'PT. Fadil Jaya abadi': 'PT Fadil Jaya Abadi',
        'PT. JAYA ABADI': 'PT Jaya Abadi',
        'PT. Kaliraya Sari': 'PT Kaliraya Sari',
        'PT. Yaop yaya op op ': 'PT Yaop Yaya Op Op',
        'Universal export': 'Universal Export',
        'pt yes': 'PT Yes'
    }
    df['vendor_name'] = df['vendor_name'].replace(vendor_mapping)

    boq_df = df.groupby(['vendor_name', 'month']).agg({
        'plan_cost': 'sum',
        'actual_cost': 'sum'
    }).reset_index()
    boq_df['month'] = pd.to_datetime(boq_df['month'])
    boq_df['month'] = boq_df['month'].dt.strftime('%B %Y')

    vendors = [
        'PT Vendor Al Fatih',
        'PT Vendor Sejati',
        'PT Berca Engineering',
        'PT Fadil Jaya Abadi',
        'PT Jaya Abadi',
        'PT Kaliraya Sari',
        'PT Yaop Yaya Op Op',
        'SCM',
        'Universal Export',
        'PT Yes'
    ]

    results = {}
    for vendor_name in vendors:
        vendor_data = boq_df[boq_df['vendor_name'] == vendor_name]
        fig = px.scatter(vendor_data, x='month', y=['plan_cost', 'actual_cost'], 
                         color_discrete_map={'plan_cost': 'blue', 'actual_cost': 'green'},
                         title=f'{vendor_name} Performance Analysis',
                         labels={'month': 'Time', 'value': 'Cost'},
                         hover_name='vendor_name')
        fig.update_yaxes(tickprefix='IDR ')
        fig.add_hline(y=(vendor_data['plan_cost'].max() + vendor_data['actual_cost'].max()) / 2, 
                      line=dict(color='red', dash='dash'), name='Max Threshold')
        results[vendor_name] = fig.to_json()
    
    return results

@app.route('/plot')
def plot():
    plots = process_data_and_generate_plots()
    return jsonify(plots)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
