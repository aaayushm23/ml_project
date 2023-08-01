from data_preprocessing import preprocess_data\nfrom ml_model import create_model\n\n# Training Script\ndef train_model(data_path):\n    data = preprocess_data(data_path)\n    model = create_model()\n    X, y = data.iloc[:, :-1], data.iloc[:, -1]\n    model.fit(X, y)\n    return model\n\nif __name__ == '__main__':\n    model = train_model('data.csv')\n    print('Model trained successfully')
\n\n# Updated training script with train_model function\n    model = train_model(model, X, y)
\n    data = engineer_features(data)
