#  Ma trận tương quan giữa các biến số
plt.figure(figsize=(12, 8))
sns.heatmap(merged_df.select_dtypes(include=np.number).corr(), annot=True, cmap='coolwarm')
plt.title('Ma trận tương quan giữa các biến số')
plt.show()