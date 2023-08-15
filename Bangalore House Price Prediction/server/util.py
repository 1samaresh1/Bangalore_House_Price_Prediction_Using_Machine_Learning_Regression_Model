import json
import joblib
import numpy as np

class HousePricePredictor:
    def __init__(self, model_path='./artifacts/Bangalore_House_Price_Predication.pkl',
                 columns_path='./artifacts/columns.json'):
        self.load_saved_artifacts(model_path, columns_path)
    
    def load_saved_artifacts(self, model_path, columns_path):
        print("Loading saved artifacts...")
        with open(columns_path, 'r') as f:
            data = json.load(f)
            self.__data_columns = data['data_columns']
            self.__locations = self.__data_columns[3:]

        self.__model = joblib.load(model_path)

    def get_location_names(self):
        return self.__locations

    def get_estimated_price(self, location, sqft, bhk, bath):
        try:
            loc_index = self.__data_columns.index(location.lower())
        except ValueError:
            loc_index = -1

        x = np.zeros(len(self.__data_columns))
        x[0] = sqft
        x[1] = bath
        x[2] = bhk
        if loc_index >= 0:
            x[loc_index] = 1
        
        return round(self.__model.predict([x])[0], 2)

# Example usage
if __name__ == '__main__':
    predictor = HousePricePredictor()
    print(predictor.get_estimated_price("1st block jayanagar", 1000,2,2))
    print(predictor.get_location_names())
