from sklearn.ensemble import RandomForestRegressor\n\ndef create_random_forest():\n    model = RandomForestRegressor(n_estimators=100)\n    return model
\ndef tune_random_forest(model, X, y):\n    from sklearn.model_selection import RandomizedSearchCV\n    parameters = {'n_estimators': [50, 100, 200], 'max_features': ['auto', 'sqrt', 'log2']}\n    rand_search = RandomizedSearchCV(model, parameters)\n    rand_search.fit(X, y)\n    return rand_search.best_estimator_
