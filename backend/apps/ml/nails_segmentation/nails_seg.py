import joblib
import pandas as pd

class NailsSegmenter:
    def __init__(self):
        path_to_artifacts = "../research/"
        self.model = joblib.load(path_to_artifacts + "seg.joblib")
        self.x_test = joblib.load(path_to_artifacts + "x_test.joblib")

    def preprocessing(self, input_data):
        # JSON to pandas DataFrame
        input_data = self.x_test
        rand_image = np.random.randint(seg.X_test.__len__())

        return rand_image

    def predict(self, x_test):
        return self.model.predict()[rand_image,:,:,0]

    '''def postprocessing(self, input_data):
        label = "<=50K"
        if input_data[1] > 0.5:
            label = ">50K"
        return {"probability": input_data[1], "label": label, "status": "OK"}'''

    def compute_prediction(self, input_data):
        try:
            input_data = self.preprocessing(input_data)
            prediction = self.predict(input_data)#[0]  # only one sample
            #prediction = self.postprocessing(prediction)
        except Exception as e:
            return {"status": "Error", "message": str(e)}

        return prediction