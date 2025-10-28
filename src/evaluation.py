# Đánh giá mô hình
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10,6))
sns.barplot(data=results_df, x='RMSE', y='Model', palette='viridis')
plt.title("So sánh RMSE giữa các mô hình")
plt.show()

# So sánh 200 mẫu đầu tiên
best_model_name = results_df.iloc[0]['Model']
best_model = models[best_model_name]
y_pred_best = predictions[best_model_name]

plt.figure(figsize=(12,5))
plt.plot(y_test.values[:200], label='Thực tế')
plt.plot(y_pred_best[:200], label=f'Dự đoán ({best_model_name})')
plt.title(f"So sánh 200 mẫu đầu tiên - Mô hình: {best_model_name}")
plt.legend()
plt.show()