from lens_regression import LensRegression

def main():
    lens_regression = LensRegression("./doc/Asphaere_Rohdaten_Only-0-Grad.xlsx")
    lens_regression.rotate_points(180)
    #for i in range(20):
    #    lens_regression.rotate_points(0.1)
    #    lens_regression.shift_min_to_origin()
    #    lens_regression.do_iterative_regression()
    #    lens_regression.render()
    lens_regression.shift_min_to_origin()
    lens_regression.do_analytical_regression()
    lens_regression.render()

if __name__ == "__main__":
    main()