#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def sq_err(colors, v_val):
    '''
    colors: List of input R value
    v_val:  Integer
    returns List of (R[i]-x)**2
    '''
    err_list = [None]

    for col in colors:
        err_list.append(((col[0] - v_val) ** 2) * col[1])

    # print('sq_err:', v_val, err_list, file=sys.stderr)
    return err_list  # contains error ** 2 of number of color 


def min_acc_error(colors, sq_err_list):
    '''
    colors: List of input R value
    sq_err_list: List of (R[i]-x)**2
    returns 2D_list[Start][End]. Total of error for optimized V_VAL
    '''

    def range_sum(sq_err_list, start, end):
        min_total = None
        for sq_err in sq_err_list:
            sub_total = 0
            for i in range(start, end+1):
                sub_total += sq_err[i]
            if min_total == None or sub_total < min_total:
                min_total = sub_total

        #print('range_sum', start, end, min_total)
        return min_total

    opt_error = [[None for i in range(NUM_R_COL+1)] for j in range(NUM_R_COL+1)]

    for start in range(1, NUM_R_COL+1):
        for end in range(start, NUM_R_COL+1):
            opt_error[start][end] = range_sum(sq_err_list, start, end)

    return opt_error


NUM_R_COL, NUM_V_COL = map(int, sys.stdin.readline().split())
colors = list()

for i in range(NUM_R_COL):
    r, p = map(int, sys.stdin.readline().split())
    colors.append((r, p))

colors.sort()  # Sort by color value(0-255)

C_RANGE_LOW = colors[0][0]
C_RANGE_HIGH = colors[-1][0]

sq_err_list = list()
for v_val in range(C_RANGE_LOW, C_RANGE_HIGH+1):  # Lowest R val to Highest
    sq_err_list.append(sq_err(colors, v_val))    # 2d list

# opt_error[a][b]: minimum accumulated error of range a-b by 1 pallete
opt_error = min_acc_error(colors, sq_err_list)
#print('opt error', opt_error)

INF = 2**63

# min_err[r][v]: Minimum error of original number of color:v and pallete:v
min_err = [[0 if r==0 or r<=v else INF for v in range(NUM_V_COL+1)] for r in range(NUM_R_COL+1)]
# for r in range(NUM_R_COL):
#    min_err[r][0] = opt_error[r][r+1]

#print('min_err', min_err)

for r in range(1, NUM_R_COL+1):
    for v in range(1, NUM_V_COL+1):
        min_val = INF
        for rx in range(r):
            val = min_err[rx][v-1] + opt_error[rx+1][r]
            #print('xxx', r,v,rx, min_val, val)
            min_val = min(min_val, val)
        min_err[r][v] = min_val

#print(min_err)
print(min_err[NUM_R_COL][NUM_V_COL])
