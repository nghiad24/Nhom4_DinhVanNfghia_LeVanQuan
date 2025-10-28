# Dự báo doanh thu trung bình theo ngày và đưa ra đề xuất tồn kho sau khi chạy mô hình XGBoost
forecast_mean = y_pred_best.mean()
safety_stock = forecast_mean * 0.1  # dự trữ an toàn 10%
inventory_needed = forecast_mean + safety_stock

print(f"- Dự báo trung bình doanh số/ngày: {forecast_mean:,.0f}")
print(f"- Đề xuất tồn kho (bao gồm 10% dự trữ): {inventory_needed:,.0f}")