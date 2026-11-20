from sklearn.metrics import make_scorer, f1_score, recall_score, precision_score, accuracy_score
from sklearn.model_selection import cross_validate
from imblearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
import pandas as pd


scoring = {
            "F1" : make_scorer(f1_score),
            "Accuracy" : make_scorer(accuracy_score),
            "Recall" : make_scorer(recall_score),
            "Precision" : make_scorer(precision_score)
        }


models = [
    ('Logistic Regression', LogisticRegression(random_state=42, n_jobs=-1)),
    ('Knn', KNeighborsClassifier()),
    ('Gaussian Naive Bayes', GaussianNB()),
    ('Decision Tree', DecisionTreeClassifier(random_state=42)),
    ('Random Forest', RandomForestClassifier(random_state=42, n_jobs=-1)),
    ('Xgboost', XGBClassifier()),
]


def train_model(x, y, preprocessing_pipeline):

    results = []

    for name, model in models :
            
            pipeline = Pipeline([
            ('Preprocessing', preprocessing_pipeline),
            ('Model', model)
                ])
            
            result = cross_validate(pipeline,
                            x, y,
                            cv=5,
                            scoring=scoring,
                            return_train_score=True,
                            n_jobs=-1
                )
    
            model_results = {
            'Model': name,
            'Train_F1': result['train_F1'].mean().round(3),
            'Test_F1': result['test_F1'].mean().round(3),
            'Train_Recall': result['train_Recall'].mean().round(3),
            'Test_Recall': result['test_Recall'].mean().round(3),
            'Train_Precision': result['train_Precision'].mean().round(3),
            'Test_Precision': result['test_Precision'].mean().round(3),
            'Train_Accuracy': result['train_Accuracy'].mean().round(3),
            'Test_Accuracy': result['test_Accuracy'].mean().round(3),
            'Fit_Time': result['fit_time'].sum().round(2)
        }
            results.append(model_results)
    
    return pd.DataFrame(results)



    
