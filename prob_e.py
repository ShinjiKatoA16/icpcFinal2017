#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ICPC 2017 Final. Problem-E Need for Speed


import sys

def total_time(c, n, dist, speed):
    total = 0.0
    for i in range(n):
        total += dist[i] / (c+speed[i])
    return total

def search_minmax(t, n, dist, speed):
    min_c = - (min(speed))
    if min_c == 0:
        max_c = 1.0
    elif min_c > 0:
        max_c = min_c * 2
    else:
        max_c = -min_c

    while True:
        travel_time = total_time(max_c, n, dist, speed)
        #print('max_c adjust', max_c, travel_time, file=sys.stderr)
        if travel_time < t:
            break
        min_c = max_c
        max_c *= 2

    return min_c, max_c


MAX_ERROR = 10 ** (-7)

n, t = map(int, sys.stdin.readline().split())
dist = list()
speed = list()

for i in range(n):
    d, s = map(int, sys.stdin.readline().split())
    dist.append(d)
    speed.append(s)

min_c, max_c = search_minmax(t, n, dist, speed)
#print(min_c, max_c, file=sys.stderr)

while True:
    c = (min_c + max_c) / 2
    travel_time = total_time(c, n, dist, speed)
    if abs(travel_time - t) < MAX_ERROR:
        break

    if travel_time < t:
        max_c = c
    else:
        min_c = c

print(c)
