from src.preprocessing import load_data, preparing_features_target, create_preprocessing_pipeline
from src.training import train_model
from src.utils import load_config, setup_logging
import pandas as pd

def main():

    config = load_config()
    logger = setup_logging()

    logger.info("loading_data")
    df = load_data()
    logger.info("successfully_loading_data")


    logger.info("starting prepare data")
    x,y = preparing_features_target(df)
    logger.info("successfully preparing data")


    logger.info("creating pipeline")
    preprocessing_pipeline = create_preprocessing_pipeline(config)
    logger.info("successfully creating pipeline")


    # results = train_model(x, y, preprocessing_pipeline)
    results = xgb_model (x, y, preprocessing_pipeline)
    logger.info(f"training completed \n {50 * "----"}")
    print(results)




if __name__ == "__main__":
    main()



 