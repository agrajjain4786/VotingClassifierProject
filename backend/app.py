
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    data = pd.read_csv(file)

    data_split = data.iloc[:, 0].str.split('|', expand=True)
    data_split.columns = [f'Feature_{i}' for i in range(data_split.shape[1])]
    X = data_split.iloc[:, :-1]
    y = data_split.iloc[:, -1]

    if y.isnull().any():
        y.fillna(0, inplace=True)
    y = y.astype(int)

    non_numeric_columns = X.select_dtypes(include=['object']).columns
    for column in non_numeric_columns:
        le = LabelEncoder()
        X[column] = le.fit_transform(X[column])

    X_numeric = X.apply(pd.to_numeric, errors='coerce')
    X_numeric.fillna(X_numeric.mean(), inplace=True)

    if X_numeric.empty or y.empty:
        return jsonify({'error': 'Feature matrix or target is empty after preprocessing.'}), 400

    X_train, X_test, y_train, y_test = train_test_split(
        X_numeric, y, test_size=0.3, random_state=42, stratify=y)

    model1 = RandomForestClassifier(random_state=42, n_jobs=-1)
    model2 = LogisticRegression()
    model3 = SVC()
    model4 = GradientBoostingClassifier(random_state=42)
    model5 = AdaBoostClassifier(random_state=42)
    model6 = DecisionTreeClassifier(random_state=42)
    model7 = GaussianNB()

    ensemble_model = VotingClassifier(estimators=[
        ('rf', model1), ('lr', model2), ('svc', model3),
        ('gb', model4), ('ab', model5), ('dt', model6), ('gnb', model7)
    ], voting='hard')

    ensemble_model.fit(X_train, y_train)
    y_pred_ensemble = ensemble_model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred_ensemble)
    report = classification_report(y_test, y_pred_ensemble)

    return jsonify({
        'accuracy': accuracy,
        'report': report
    })

if __name__ == '__main__':
    app.run(debug=True)
