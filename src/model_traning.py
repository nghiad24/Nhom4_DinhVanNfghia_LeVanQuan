# Huấn luyện mô hình
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import xgboost as xgb

models = {
    'Linear Regression': LinearRegression(),
    'Decision Tree': DecisionTreeRegressor(max_depth=20, random_state=42),
    'Random Forest': RandomForestRegressor(n_estimators=100, max_depth=20, n_jobs=-1, random_state=42),
    'XGBoost': xgb.XGBRegressor(n_estimators=300, learning_rate=0.1, max_depth=6, random_state=42),
}

from sklearn.metrics import mean_squared_error, r2_score
import math

results = []
predictions = {}

for name, model in models.items():
    print(f"Training {name}...")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    rmse = math.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    results.append({'Model': name, 'RMSE': rmse, 'R2': r2})
    predictions[name] = y_pred
    print(f"Done: RMSE={rmse:.2f}, R2={r2:.3f}")

results_df = pd.DataFrame(results).sort_values('RMSE')
results_df