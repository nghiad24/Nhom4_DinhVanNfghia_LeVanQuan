# Nhom4_DinhVanNfghia_LeVanQuan
# HƯỚNG DẪN CÀI ĐẶT VÀ CÀI PROJECT
1. Môi trường phát triển

Project được thực hiện và kiểm thử trên nền tảng Google Colab và Jupyter Notebook, sử dụng ngôn ngữ Python 3.10+.
Các phần mềm và công cụ cần thiết bao gồm:

Thành phần	Phiên bản đề xuất	Chức năng
Python	3.9 hoặc cao hơn	Ngôn ngữ chính của project
Jupyter Notebook / Google Colab	Mới nhất	Môi trường chạy mã và hiển thị biểu đồ
Anaconda (tuỳ chọn)	2023+	Hỗ trợ quản lý thư viện dễ dàng
Plotly, Matplotlib, Seaborn	Latest	Trực quan hóa dữ liệu và dự báo
Pandas, NumPy	Latest	Xử lý và tính toán dữ liệu
Scikit-learn	Latest	Huấn luyện và đánh giá mô hình Machine Learning
XGBoost	Latest	Thuật toán dự báo chính trong project
Joblib / Pickle	Latest	Lưu trữ mô hình sau khi huấn luyện (tuỳ chọn)
2. Cài đặt môi trường
Dùng Google Colab:
- Truy cập địa chỉ: https://colab.research.google.com
- Đăng nhập bằng tài khoản Google.
- Tải file notebook của project lên 
- Tải các file dữ liệu cần thiết lên thư mục làm việc (train.csv, store.csv).

Kết nối với Google Drive nếu cần truy cập dữ liệu lớn hơn:

# from google.colab import drive
# drive.mount('/content/drive')


Chạy tuần tự từng cell từ đầu đến cuối để huấn luyện mô hình và tạo kết quả dự báo.
Chạy project:

Mở terminal tại thư mục chứa file notebook.

Gõ lệnh:

# jupyter notebook

Sau đó mở file Rossmann_Sales_Prediction.ipynb và chạy các cell theo thứ tự.
# Hướng dẫn chạy project

4. Các bước thực hiện chính khi chạy project

Nhập dữ liệu (train.csv, store.csv)

Kết hợp dữ liệu bằng pd.merge() để tạo bảng tổng hợp.

Tiền xử lý dữ liệu

Làm sạch dữ liệu, xử lý giá trị thiếu, mã hóa biến phân loại (One-hot Encoding).

Phân tích EDA (Exploratory Data Analysis)

Trực quan hóa doanh thu theo thời gian, ngày lễ, loại cửa hàng, chương trình khuyến mãi,…

Chia dữ liệu huấn luyện – kiểm tra (train/test split)

Sử dụng train_test_split() của scikit-learn.

Huấn luyện mô hình Machine Learning (XGBoost, Random Forest, …)

So sánh kết quả RMSE, R² để chọn mô hình tối ưu.

Dự báo và trực quan hóa kết quả bằng Plotly

Hiển thị xu hướng doanh thu 6 tháng và 12 tháng.

Tính toán tồn kho gợi ý và xuất kết quả

Áp dụng mức dự trữ an toàn 10% để đề xuất kế hoạch tồn kho hợp lý.
