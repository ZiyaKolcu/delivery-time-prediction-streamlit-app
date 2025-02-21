from src.data_processing.data_processing import DataProcessing
import joblib


class ModelPredictionPipeline:
    def __init__(self):
        pass

    def get_model_prediction(self, data):
        data_processing = DataProcessing()
        df = data_processing.process(data)

        model = joblib.load(filename="final_model/model.joblib")
        prediction = model.predict(df)
        return prediction[0]
