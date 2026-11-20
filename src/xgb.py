from sklearn.metrics import make_scorer, f1_score, recall_score, precision_score, accuracy_score
from sklearn.model_selection import cross_validate
from imblearn.pipeline import Pipeline
import pandas as pd
from xgboost import XGBClassifier
import joblib
import mlflow
import os


scoring = {
            "F1" : make_scorer(f1_score),
            "Accuracy" : make_scorer(accuracy_score),
            "Recall" : make_scorer(recall_score),
            "Precision" : make_scorer(precision_score)
        }


xgb_params = {
    "n_estimators": 250,
    "max_depth": 35,
    "learning_rate": 0.001,
    "subsample": 1.0,
    "colsample_bytree": 1.0,
    "gamma": 0,
    "n_jobs": 0,              
    "random_state": 0,
}



model = XGBClassifier(**xgb_params)

def xgb_model(x, y, preprocessing_pipeline):

    mlflow.set_experiment("hotel_project")

       with mlflow.start_run() as run :

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

            mlflow.log_params({**xgb_params,
                            "cv":5})
            pipeline.fit(x, y)

            os.makedirs("models", exist_ok=True)
            joblib.dump(pipeline , r"models/xgb_model.pkl" )
            mlflow.sklearn.log_model(
                                        pipeline, 
                                        name="model",
                                        input_example=x.iloc[:5]  
                                    )

            # mlflow.log_artifact("models/xgb_model.pkl")



            model_results = {
                    'Model_name': "xgb_model",
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


            mlflow.log_metrics({
                'train_f1': model_results['Train_F1'],
                'test_f1': model_results['Test_F1'],
                'train_recall': model_results['Train_Recall'],
                'test_recall': model_results['Test_Recall'],
                'train_precision': model_results['Train_Precision'],
                'test_precision': model_results['Test_Precision'],
                'train_accuracy': model_results['Train_Accuracy'],
                'test_accuracy': model_results['Test_Accuracy'],
                'total_fit_time': model_results['Fit_Time']
            })
            
            
            for k, v in model_results.items():
                logger.info(f"{k}: {v}")
            
            
            return model_results