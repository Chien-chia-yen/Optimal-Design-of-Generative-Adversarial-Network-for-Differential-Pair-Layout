import numpy as np
##############假設bump座標########
min_row_temp=24
min_col_temp=25
max_row_temp=39
max_col_temp=38

########起始點############
start_row=28
stat_col=52
##########終點##########
goal_row=26
goal_col=37

import numpy as np
path="./result/final_result9_500.txt"

f = open(path)
idx_x=0
idx_y=0
matrix=np.zeros((64,64))

for line in f.readlines():
    word = line.split()
    for val in word:
        matrix[idx_x][idx_y]=float(val)
        idx_y=idx_y+1
        if idx_y==64:
            idx_y=0
            idx_x=idx_x+1
f.close()

arr = np.zeros((64,64), dtype = float) 
row=0
col=0
path2 = './result_with_die/final_result9_with_die.txt'

##########Draw#####################
#########bump範圍代號9##############
arr[min_row_temp][min_col_temp]=9
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if i>=min_row_temp and i<=max_row_temp and j>=min_col_temp and j<=max_col_temp:
            if matrix[i][j]==0:
                matrix[i][j]=1
#####起終點標好255#####
arr[28][52]=255
arr[26][37]=255
f_result = open(path2, 'w')
for i in range(64):
    for j in range(64):
        f_result.write(str(matrix[i][j])+" ")  
    f_result.write("\n")  
f_result.close()