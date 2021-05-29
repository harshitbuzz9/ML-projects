import numpy as np
import matplotlib.pyplot as plt
import openpyxl

def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)

    # mean of x and y vector
    m_x = np.mean(x)
    m_y = np.mean(y)

    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y * x) - n * m_y * m_x
    SS_xx = np.sum(x * x) - n * m_x * m_x

    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 * m_x

    return (b_0, b_1)


def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color="m",
                marker="o", s=30)

    # predicted response vector
    y_pred = b[0] + b[1] * x

    # plotting the regression line
    plt.plot(x, y_pred, color="g")

    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')

    # function to show plot
    plt.show()


def main():
    wb = openpyxl.load_workbook("E:\minor 2 data set\msp, gdp year.xlsx")

    ws = wb.active
    first_column = ws['A']

    X = []  # storing data from database into list of column Aq12
    Y = []  # # storing data from database into list of column B
    Z = []

    print("Column A is year from 2010 - 2019")
    for x in range(len(first_column)):
        a = first_column[x].value
        X.append(a)

    year_X = np.array(X)
    print(year_X)

    print("Column B is MSP from 2010 - 2019")
    ws2 = wb.active
    second_column = ws2['B']
    for x in range(len(second_column)):
        a = second_column[x].value
        Y.append(a)

    msp_Y = np.array(Y)
    print(msp_Y)

    print("Column C is GDP from 2010 - 2019")
    ws3 = wb.active
    third_column = ws3['C']  # column refference
    for x in range(len(third_column)):
        a = third_column[x].value
        Z.append(a)

    gdp_Z = np.array(Z)
    print(gdp_Z)

    # estimating coefficients
    print("To calculate GDP vs MSP Regression graph")


    b = estimate_coef(gdp_Z,msp_Y)
    print("Estimated coefficients:\nb_0 = {}  \nb_1 = {}".format(b[0], b[1]))

    # plotting regression line
    plot_regression_line(gdp_Z,msp_Y, b)



if __name__ == "__main__":
    main()