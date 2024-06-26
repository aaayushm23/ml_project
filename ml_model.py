from sklearn.linear_model import LinearRegression\n\n# Machine Learning Model Script\ndef create_model():\n    model = LinearRegression()\n    return model
\ndef train_model(model, X, y):\n    model.fit(X, y)\n    return model
\nfrom sklearn.model_selection import GridSearchCV\n\ndef tune_model(model, X, y):\n    parameters = {'fit_intercept': [True, False], 'normalize': [True, False]}\n    grid_search = GridSearchCV(model, parameters)\n    grid_search.fit(X, y)\n    return grid_search.best_estimator_
