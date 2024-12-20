import numpy as np
import matplotlib.pyplot as plt

from SetParam import *
from ProgBar import progress_bar


def get_i_real(uo, i_in):
    return i_in - (uo - up) / (R_leak_L * R_sis)


def calc_ic(u_left, u_right, u_this):
    return (u_left - u_this + u_right - u_this) / R_sis + (up - u_this) / R_leak


def solve_i():
    i_real = get_i_real(u_n[0], I_in)
    i_n[0] = i_real + calc_ic(u_n[0], u_n[1], u_n[0])
    for i in range(1, n - 1):
        i_n[i] = calc_ic(u_n[i - 1], u_n[i + 1], u_n[i])
    i_n[-1] = calc_ic(u_n[-2], u_n[-1], u_n[-1])


def solve_u():
    for i in range(n):
        u_n[i] += dt * i_n[i] / C


def solve_i_np():
    i_real = get_i_real(u_n_np[0], I_in)
    i_n_np[1:-1] = (u_n_np[:-2] - u_n_np[1:-1] + u_n_np[2:] - u_n_np[1:-1]) / R_sis + (up - u_n_np[1:-1]) / R_leak
    i_n_np[0] = i_real + calc_ic(u_n_np[0], u_n_np[1], u_n_np[0])
    i_n_np[-1] = calc_ic(u_n_np[-2], u_n_np[-1], u_n_np[-1])


def solve_u_np():
    for i in range(n):
        u_n_np[i] += dt * i_n_np[i] / C


if __name__ == '__main__':
    if T / dt != int(T / dt):
        print("T/dt must be an integer")
    u_n = [2 * i for i in range(n)]
    i_n = [0 for i in range(n)]
    u_n_np = np.array(u_n, dtype=np.float64)
    result = np.copy(u_n_np)
    if np_mode:
        i_n_np = np.array(i_n, dtype=np.float64)
    for itime in range(int(T / dt)):
        progress_bar(itime / (T / dt) * 100)
        if np_mode:
            solve_i_np()
            solve_u_np()
            if itime % int(T / dt / (n * 4)) == 0:
                result = np.vstack((result, u_n_np))
        else:
            solve_i()
            solve_u()
    print()
    if np_mode:
        print(u_n_np)
    else:
        print(u_n)

    # draw result
    result = result.T
    result = result.copy()
    print(result.shape)
    plt.imshow(result, cmap='plasma')
    plt.show()
