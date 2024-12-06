from SetParam import *
from ProgBar import progress_bar


def get_i_real(uo, i_in):
    return i_in - (uo - up) / (R_leak_L * R_sis)


def calc_ic(u_left, u_right, u_this):
    return (u_left - u_this) / R_sis + (u_right - u_this) / R_sis + (up - u_this) / R_leak

def solve_i():
    i_real = get_i_real(u_n[0], I_in)
    i_n[0] = i_real + calc_ic(u_n[0], u_n[1], u_n[0])
    for i in range(1, n-1):
        i_n[i] = calc_ic(u_n[i-1], u_n[i+1], u_n[i])
    i_n[-1] = calc_ic(u_n[-2], u_n[-1], u_n[-1])

def solve_u():
    for i in range(n):
        u_n[i] += dt * i_n[i] / C




if __name__ == '__main__':
    u_n = [i + 15 for i in range(n)]
    i_n = [0 for i in range(n)]
    if T/dt != int(T/dt):
        print("T/dt must be an integer")
    for itime in range(int(T/dt)):
        solve_i()
        solve_u()
        progress_bar(itime / (T/dt) * 100)
    print()
    print(u_n)
