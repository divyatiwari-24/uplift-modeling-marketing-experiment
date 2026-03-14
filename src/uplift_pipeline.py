import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklift.models import TwoModels


def load_data(path):
    df = pd.read_csv(path)
    df['treatment'] = df['segment'].apply(lambda x: 0 if x == 'No E-Mail' else 1)
    return df


def train_uplift_model(X, y, treatment):

    X_train, X_test, y_train, y_test, tr_train, tr_test = train_test_split(
        X, y, treatment, test_size=0.3, random_state=42
    )

    uplift_model = TwoModels(
        estimator_trmnt=RandomForestClassifier(n_estimators=100),
        estimator_ctrl=RandomForestClassifier(n_estimators=100)
    )

    uplift_model.fit(X_train, y_train, tr_train)

    return uplift_model