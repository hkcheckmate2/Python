"""
[0][1] => 2
[0][2] => 4
[1][2] => 1
[1][3] => 7
[2][4] => 3
[3][5] => 1
[4][3] => 2
[4][5] => 5

END
5 0 0 0 1 5 0
4 0 0 3 0 0 0
3 0 7 0 0 2 0
2 4 1 0 0 0 0
1 2 0 0 0 0 0
0 0 0 0 0 0 0
  0 1 2 3 4 5
          START  ====> CORRECT FORMAT
//start = x end = y
path = []
start = 0
past = 0
path.append(start)
while(start != END):
    for num in DIST_MATRIX[start]:
        num += past
    past = min(DIST_MATRIX[start])
    start = DIST_MATRIX[start].index(past)
    path.append(start)
TOTAL_WEIGHT = past

MAX_VAL = sys.maxsize
L = len(graph)
row = [MAX_VAL]*L
DIST_MATRIX = row*L
L = len(graph)
PARAMETER = min(DIST_MATRIX[i])
covered = [False]*L
start = 0

"""

def djikstra(graph,START,END):
    

"""
START
5 0 0 0 0 0 0
4 0 0 0 2 0 5
3 0 0 0 0 0 1
2 0 0 0 0 3 0
1 0 0 1 7 0 0
0 0 2 4 0 0 0
  0 1 2 3 4 5
           END
"""
