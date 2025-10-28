import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
# Tắt các cảnh báo không quan trọng trong notebook
warnings.filterwarnings('ignore')

plt.style.use('default')
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (15, 10)

# 1. Doanh thu theo thời gian
plt.figure(figsize=(15, 6))
plt.plot(merged_df['Date'], merged_df['Sales'])
plt.title('Doanh thu theo các mốc thời gian')
plt.xlabel('Mốc thời gian')
plt.ylabel('Doanh thu')
plt.show()

# 2️. Xử lý các giá trị bị thiếu
merged_df['CompetitionDistance'].fillna(merged_df['CompetitionDistance'].mean(), inplace=True)
merged_df['CompetitionOpenSinceMonth'].fillna(0, inplace=True)

# 3️. Doanh thu trung bình theo loại cửa hàng
# Truy cập vào các cột one-hot encoded được tạo ra trước đó
store_type_sales = merged_df.melt(
    id_vars=['Sales'],
    value_vars=[col for col in merged_df.columns if col.startswith('StoreType_')],
    var_name='StoreType_Encoded',
    value_name='IsActive'
)
store_type_sales = store_type_sales[store_type_sales['IsActive'] == True]

plt.figure(figsize=(10, 6))
sns.barplot(
    x='StoreType_Encoded',
    y='Sales',
    data=store_type_sales.groupby('StoreType_Encoded')['Sales'].mean().reset_index()
)
plt.title('Doanh thu trung bình theo loại cửa hàng')
plt.xlabel('Loại cửa hàng')
plt.ylabel('Doanh thu trung bình')
plt.show()

# 4️. Doanh thu trung bình theo thứ trong tuần
plt.figure(figsize=(10, 6))
sns.barplot(x='DayOfWeek', y='Sales', data=merged_df.groupby('DayOfWeek')['Sales'].mean().reset_index())
plt.title('Doanh thu trung bình theo ngày trong tuần')
plt.xlabel('Ngày trong tuần')
plt.ylabel('Doanh thu trung bình')
plt.show()

# 5️. Ảnh hưởng của khuyến mãi đến doanh thu
plt.figure(figsize=(10, 6))
sns.barplot(x='Promo', y='Sales', data=merged_df.groupby('Promo')['Sales'].mean().reset_index())
plt.title('Doanh thu trung bình theo khuyến mãi')
plt.xlabel('Khuyến mãi (0: Không, 1: Có)')
plt.ylabel('Doanh thu trung bình')
plt.show()

# 6️. Doanh thu theo các ngày lễ (StateHoliday)
holiday_value_vars = [col for col in merged_df.columns if col.startswith('StateHoliday_')]
if 'StateHoliday_0' in holiday_value_vars:
    holiday_value_vars.remove('StateHoliday_0') # Xóa danh mục '0' nếu nó tồn tại và được mã hóa

state_holiday_sales = merged_df.melt(
    id_vars=['Sales'],
    value_vars=holiday_value_vars,
    var_name='StateHoliday_Encoded',
    value_name='IsActive'
)
state_holiday_sales = state_holiday_sales[state_holiday_sales['IsActive'] == True]

plt.figure(figsize=(10, 6))
sns.barplot(
    x='StateHoliday_Encoded',
    y='Sales',
    data=state_holiday_sales.groupby('StateHoliday_Encoded')['Sales'].mean().reset_index()
)
plt.title('Doanh thu trung bình theo State Holiday')
plt.xlabel('State Holiday')
plt.ylabel('Doanh thu trung bình')
plt.show()


# 7. Phân bố doanh thu và ngoại lệ
plt.figure(figsize=(10, 6))
sns.boxplot(y='Sales', data=merged_df)
plt.title('Phân bố doanh thu và ngoại lệ')
plt.ylabel('Doanh thu')
plt.show()

# 8. Xu hướng doanh thu theo năm
merged_df['Date'] = pd.to_datetime(merged_df['Date'], errors='coerce')
merged_df.dropna(subset=['Date'], inplace=True)
merged_df['Year'] = merged_df['Date'].dt.year

plt.figure(figsize=(15, 6))
sns.lineplot(x='Date', y='Sales', hue='Year', data=merged_df)
plt.title('Xu hướng doanh thu theo các mốc thời gian')
plt.xlabel('Mốc thời gian')
plt.ylabel('Doanh thu')
plt.show()