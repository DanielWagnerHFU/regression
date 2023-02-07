from lens_regression import LensRegression
from math_utility import MathUtility
def main():
    lens_regression = LensRegression("./doc/Asphaere_Rohdaten_Only-0-Grad.xlsx")
    lens_regression.shift_min_to_origin()
    lens_regression.render()



if __name__ == "__main__":
    main()