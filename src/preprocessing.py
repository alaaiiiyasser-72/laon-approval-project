import pandas as pd
from sklearn.preprocessing import StandardScaler,RobustScaler,OneHotEncoder,LabelEncoder
from imblearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from imblearn.over_sampling import SMOTE





def load_data(file_path:str = r"D:/loan approval/Data/Loan_approval_data_2025.csv"):
    return pd.read_csv(file_path)





def create_preprocessing_pipeline(config):

    # standard scaler 
    st_pipe = Pipeline(steps=[
                    ("st_scaler",StandardScaler())
                    ])
    
    # robust scaler
    ro_pipe = Pipeline(steps=[
                    ("ro_scaler",RobustScaler()) 
                    ])
    
    # ohe pipeline
    ohe_pipe = Pipeline(steps=[
    ("ohe_encoder",OneHotEncoder(drop="first",sparse_output=False))
                    ])


    preprocessing_pipeline = ColumnTransformer(transformers=[
    ("st_pipe",st_pipe, config["preprocessing"]["st_cols"]),
    ("ro_pipe",ro_pipe, config["preprocessing"]["ro_cols"]),
    ("ohe_pipe",ohe_pipe, config["preprocessing"]["ohe_cols"]),
    ("ready_pipe", "passthrough", config["preprocessing"]["ready_cols"])
    ])

    return preprocessing_pipeline


def preparing_features_target(df , target_col = "loan_status"):

    x = df.drop(columns =['customer_id',"loan_status"])
    y = df["loan_status"]


    return x, y
