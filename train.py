from data_preprocessing import preprocess_data\nfrom ml_model import create_model\n\n# Training Script\ndef train_model(data_path):\n    data = preprocess_data(data_path)\n    model = create_model()\n    X, y = data.iloc[:, :-1], data.iloc[:, -1]\n    model.fit(X, y)\n    return model\n\nif __name__ == '__main__':\n    model = train_model('data.csv')\n    print('Model trained successfully')
\n\n# Updated training script with train_model function\n    model = train_model(model, X, y)
\n    data = engineer_features(data)
\n    model = tune_model(model, X, y)
from decision_tree_model import create_decision_tree\n\n# Training script update to include Decision Tree model\n    model = create_decision_tree()
\n    import joblib\n    joblib.dump(model, 'model.pkl')\n    print('Model saved as model.pkl')
\nfrom sklearn.model_selection import cross_val_score\n\n# Cross-Validation\n    scores = cross_val_score(model, X, y, cv=5)\n    print(f'Cross-Validation Scores: {scores}')\n    print(f'Average CV Score: {scores.mean()}')
from random_forest_model import create_random_forest\n\n# Training script update to include Random Forest model\n    model = create_random_forest()
\n    model = tune_random_forest(model, X, y)
