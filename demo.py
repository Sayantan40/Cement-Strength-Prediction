from sklearn import pipeline
from cement.pipeline.pipeline import Pipeline
from cement.exception import CementException
from cement.logger import logging



def main():
    try:
        
        pipeline = Pipeline()
        
        pipeline.run_pipeline()

    except Exception as e:

        logging.error(f"{e}")
        print(e)
        



if __name__ == "__main__":
    main()
