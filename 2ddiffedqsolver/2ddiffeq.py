import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as tri

def solver(x_start, x_stop, x_step, x_coef, y_start, y_stop, y_step, y_coef, fx, fy):
    if x_start > x_stop:  # x flippy flippy if need
        x_stop, x_start = x_start, x_stop
    if y_start > y_stop:  # y flippy flippy
        y_stop, y_start = y_start, y_stop

    bx = -x_coef / x_step - .5
    ax = +x_coef / x_step - .5
    by = -y_coef / y_step - .5
    ay = +y_coef / y_step - .5
    x_number = (x_stop - x_start) // x_step  # number of iterations / rows / columns
    y_number = (x_stop - x_start) // x_step  # number of iterations / rows / columns

    # x matrix making here

    to_be_matrix_x = []
    for i in range(x_number ** 2):
        to_be_matrix_x.append([0.0] * x_number ** 2)  # puts a row full of 0s there
        if i % x_number != 0:
            to_be_matrix_x[i][i] = ax
            to_be_matrix_x[i][i - 1] = bx
        else:
            to_be_matrix_x[i][i] = 1

    to_be_matrix_x2 = []
    for i in range(x_number ** 2):
        if i % x_number != 0:
            to_be_matrix_x2.append(0)
        else:
            to_be_matrix_x2.append(fx(i / x_number))

    matx  = np.matrix(to_be_matrix_x)
    matx2 = np.matrix(to_be_matrix_x2)

    # y matrix creation hereio cheerio  `
     
    to_be_matrix_y = np.zeros((y_number ** 2, y_number ** 2))
    for i in range(y_number ** 2):
        if i % y_number != 0:
            to_be_matrix_y[i][i] = ay
            to_be_matrix_y[i][i - 1] = by
        else:
            to_be_matrix_y[i][i] = 1

    to_be_matrix_y2 = np.zeros(y_number ** 2)
    for i in range(y_number ** 2):
        if i % y_number != 0:
            to_be_matrix_y2[i] = 0
        else:
            to_be_matrix_y2[i] = fy(i / y_number)

    maty  = np.matrix(to_be_matrix_y)
    maty2 = np.matrix(to_be_matrix_y2)

    y_ans = np.matmul(maty.getI(), maty2.getT())
    x_ans = np.matmul(matx.getI(), matx2.getT())
    x_grid, y_grid = np.meshgrid(np.linspace(x_start, x_stop, x_number), np.linspace(y_start, y_stop, y_number))
    y_ans_transform = np.zeros(y_number*x_number)

    for i in range(y_number * x_number):
        y_ans_transform[(i % y_number) * y_number + i // y_number] = y_ans[i]

    ans = np.zeros(y_number * x_number)

    for i in range(x_number * y_number):
        ans[i] = np.sqrt((x_ans[i]**2) + (y_ans_transform[i]**2))

    triang = tri.Triangulation(x_grid.flatten(), y_grid.flatten())
    cmap = plt.get_cmap("hot")
    plt.tricontourf(triang, ans, cmap=cmap)
    plt.show()

# start, stop, step, a
solver(0, 5, .1, 1, 0, 5, .1, -1, lambda x: 1, lambda y: 130)

