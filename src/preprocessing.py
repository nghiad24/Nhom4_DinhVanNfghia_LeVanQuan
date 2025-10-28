import pandas as pd
import numpy as np
from google.colab import drive
drive.mount('/content/drive')

train = pd.read_csv("/content/drive/MyDrive/Bao_cao_KPDL/rossmann-store-sales/train.csv")
store = pd.read_csv("/content/drive/MyDrive/Bao_cao_KPDL/rossmann-store-sales/store.csv")

# Gộp dữ liệu 
merged_df = pd.merge(train, store, how='left', on='Store')

# Loại bỏ các dòng có Sales = 0 (khi cửa hàng đóng cửa)
merged_df = merged_df[merged_df['Sales'] > 0]

# Chuyển đổi ngày tháng
merged_df['Date'] = pd.to_datetime(merged_df['Date'])
merged_df['Year'] = merged_df['Date'].dt.year
merged_df['Month'] = merged_df['Date'].dt.month
merged_df['Day'] = merged_df['Date'].dt.day
merged_df['WeekOfYear'] = merged_df['Date'].dt.isocalendar().week.astype(int)
merged_df['DayOfWeek'] = merged_df['Date'].dt.dayofweek

# Điền missing values
merged_df = merged_df.fillna(0)

# One-hot encode cho các cột phân loại
categorical_cols = ['StoreType', 'Assortment', 'StateHoliday']
merged_df = pd.get_dummies(merged_df, columns=categorical_cols, drop_first=True)

print("Dữ liệu đã sẵn sàng:", merged_df.shape)
merged_df.head()