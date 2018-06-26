import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as tri


def solver(x_start, x_stop, x_step, x_coef, y_start, y_stop, y_step, y_coef, fx, fy):
    if x_start > x_stop:  # x flippy flippy if need
        temp = x_stop
        x_stop = x_start
        x_start = temp
    if y_start > y_stop:  # y flippy flippy
        temp = y_stop
        y_stop = y_start
        y_start = temp
    bx = -x_coef / x_step - .5
    ax = x_coef / x_step - .5
    by = -y_coef / y_step - .5
    ay = y_coef / y_step - .5
    x_number = int((x_stop - x_start) / x_step)  # number of iterations / rows/ columns
    y_number = int((x_stop - x_start) / x_step)  # number of iterations / rows/ columns

    # x matrix making here

    to_be_matrix_x = []
    for i in range(0, x_number * x_number):
        to_be_matrix_x.append([0.0] * x_number * x_number)  # puts a row full of 0s there
        if i % x_number != 0:
            to_be_matrix_x[i][i] = ax
            to_be_matrix_x[i][i - 1] = bx
        else:
            to_be_matrix_x[i][i] = 1

    to_be_matrix_x2 = []
    for i in range(0, x_number * x_number):
        if i % x_number != 0:
            to_be_matrix_x2.append(0)
        else:
            to_be_matrix_x2.append(fx(i / x_number))
    matx = np.matrix(to_be_matrix_x)
    matx2 = np.matrix(to_be_matrix_x2)

    # y matrix creation hereio cheerio
    to_be_matrix_y = np.zeros((y_number * y_number, y_number * y_number))
    for i in range(0, y_number * y_number):
        if i % y_number != 0:
            to_be_matrix_y[i][i] = ay
            to_be_matrix_y[i][i - 1] = by
        else:
            to_be_matrix_y[i][i] = 1
    to_be_matrix_y2 = np.zeros(y_number * y_number)
    for i in range(0, y_number * y_number):
        if i % y_number != 0:
            to_be_matrix_y2[i] = 0
        else:
            to_be_matrix_y2[i] = fy(i / y_number)
    maty = np.matrix(to_be_matrix_y)
    maty2 = np.matrix(to_be_matrix_y2)
    y_ans = np.matmul(maty.getI(), maty2.getT())
    x_ans = np.matmul(matx.getI(), matx2.getT())
    x_grid, y_grid = np.meshgrid(np.linspace(x_start, x_stop, x_number), np.linspace(y_start, y_stop, y_number))

    ans = np.zeros(len(y_ans))
    for i in range(0, len(y_ans)):
        ans[i] = np.sqrt(y_ans[i] ** 2 + x_ans[i] ** 2)

    triang = tri.Triangulation(x_grid.flatten(), y_grid.flatten())

    cmap = plt.get_cmap("terrain")

    plt.tricontourf(triang, ans, cmap=cmap)

    plt.show()


solver(0, 5, .1, 1, 0, 5, .1, 1, lambda x: np.sin(x), lambda y: np.sin(y))
