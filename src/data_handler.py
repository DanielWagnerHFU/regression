import numpy as np
import pandas as pd

class DataHandler:
    def save_data_to_excel(data, filename):
        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)

    def load_data_from_excel(filename):
        df = pd.read_excel(filename)
        data = df.to_numpy()
        return data