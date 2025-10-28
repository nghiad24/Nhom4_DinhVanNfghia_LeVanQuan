# ============================================================================
# BIỂU ĐỒ 1: DỰ ĐOÁN DOANH THU THEO THỜI GIAN (Biểu đồ LINE)
# ============================================================================

def plot_forecast_trends(forecast_6m, forecast_12m):
    fig = make_subplots(
        rows=2, cols=1,
        subplot_titles=('Dự doán 6 tháng', 'Dự đoán 12 tháng'),
        vertical_spacing=0.08,
        row_heights=[0.6, 0.4]
    )

    # Dự đoán 6 tháng
    monthly_6m = forecast_6m.groupby([forecast_6m['Date'].dt.to_period('M')])['Forecast'].sum()
    fig.add_trace(
        go.Scatter(x=monthly_6m.index.astype(str), y=monthly_6m.values,
                  mode='lines+markers', name='Dự doán 6 tháng',
                  line=dict(color='#1f77b4', width=3)),
        row=1, col=1
    )

    # Dự đoán 12 tháng
    monthly_12m = forecast_12m.groupby([forecast_12m['Date'].dt.to_period('M')])['Forecast'].sum()
    fig.add_trace(
        go.Scatter(x=monthly_12m.index.astype(str), y=monthly_12m.values,
                  mode='lines+markers', name='Dự đoán 12 tháng',
                  line=dict(color='#ff7f0e', width=3)),
        row=2, col=1
    )

    fig.update_layout(height=800, title_text="DỰ ĐOÁN TỔNG DOANH THU THEO THÁNG",
                     showlegend=True, template='plotly_white')
    fig.update_yaxes(title_text="Tổng doanh thu ($)", row=1, col=1)
    fig.update_yaxes(title_text="Tổng doanh thu ($)", row=2, col=1)
    fig.show()

forecast_6m = merged_df.copy()
forecast_6m['Forecast'] = merged_df['Sales']
forecast_12m = merged_df.copy()
forecast_12m['Forecast'] = merged_df['Sales']


plot_forecast_trends(forecast_6m, forecast_12m)

# ============================================================================
# BIỂU ĐỒ 2: CÁC CỬA HÀNG CÓ DOANH THU CAO NHẤT (BIỂU ĐỒ CỘT)
# ============================================================================

def plot_top_stores(inv_6m, inv_12m):
    fig = make_subplots(rows=1, cols=2, subplot_titles=('Top 10 - Doanh thu 6 tháng', 'Top 10 - Doanh thu 12 tháng'))

    # Doanh thu 6 tháng cao nhất
    top6 = inv_6m.nlargest(10, 'Forecast')
    fig.add_trace(
        go.Bar(x=top6['Store'], y=top6['Forecast'], name='6M',
               marker_color=px.colors.sequential.Blues),
        row=1, col=1
    )

    # Doanh thu 12 tháng cao nhất
    top12 = inv_12m.nlargest(10, 'Forecast')
    fig.add_trace(
        go.Bar(x=top12['Store'], y=top12['Forecast'], name='12M',
               marker_color=px.colors.sequential.Oranges),
        row=1, col=2
    )

    fig.update_layout(height=500, title_text="TOP 10 STORES CÓ TỔNG DOANH THU CAO NHẤT",
                     showlegend=False, template='plotly_white')
    fig.update_xaxes(title_text="Store ID", row=1, col=1)
    fig.update_xaxes(title_text="Store ID", row=1, col=2)
    fig.update_yaxes(title_text="Doanh thu ($)", row=1, col=1)
    fig.update_yaxes(title_text="Doanh thu ($)", row=1, col=2)
    fig.show()

inv_6m = merged_df.groupby('Store')['Sales'].sum().reset_index().rename(columns={'Sales': 'Forecast'})
inv_12m = merged_df.groupby('Store')['Sales'].sum().reset_index().rename(columns={'Sales': 'Forecast'})


plot_top_stores(inv_6m, inv_12m)