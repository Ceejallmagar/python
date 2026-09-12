import numpy as np

# arr=[10,20,30,40]
# num_list=np.array([10,20,30,40])
# print(num_list/2)







#2d array

# list=np.array([
#       [1,3],
#       [2,5],
#       [5,5]
# ])
# print("shape",list.shape)
# print("list",list)
# print(list.ndim)


# matrix= np.array([
#     [1,3],
#     [3,5],
#     [6,4]
# ])
# print(matrix[2,1])


# data = np.array([
#     [10, 20, 30],  # Row 0
#     [40, 50, 60],  # Row 1
#     [70, 80, 90]   # Row 2
# ])

# print(data[2,2])

# print(data[:,1]) # it gives us that the second column of all row like first denotes the row and second is the columns for eg

# print(data[2,1]) # the answer is the 80 means the second index row and 1 indexed column 


# arra=np.array([1, 2, 3, 4, 5, 6, 7, 8])
# reshaped=arra.reshape(4,2)
# print(reshaped)


# scores = np.array([55, 82, 90, 40, 68])

# marks=scores>=70
# print("marks",marks)

# pass_marks=scores[marks]
# print(pass_marks)


# data=np.array([5, 12, 18, 25, 30, 42])


# marks=data>20

# greter_than_20=data[marks]
# print(greter_than_20)

# print(data[data>20])




#axis

# num=np.array([[5,10,50],[3,5,6]])
# #axis one is the row and the axis 0 is the column

# print(np.sum(num, axis=0))
# print(np.sum(num,axis=1))


# grid = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])


# print(np.mean(grid,axis=0))
# print(np.mean(grid,axis=1))


# print(np.arange(10, 30, 5))


# #scalar broadcasting
# matrix = np.array([
#     [10, 20],
#     [30, 40]
# ])

# row=np.array([10,10])
# a_matrix=matrix-row
# print(a_matrix)  #output is [[0,10]
#                            #[20,30]
# print(matrix-10)


# #Q
# #1 Create a 1D array named raw_data containing integers from 1 to 12 using np.arange()

raw_data=np.arange(1, 13,1)
print(raw_data)

print(raw_data.reshape(3,4))

print(raw_data.dtype)
print(raw_data[raw_data>7])


Fahrenheit=np.array([72, 75, 68, 80, 85, 74, 70])
C = (Fahrenheit - 32)*(5/9)
print(C)

grades = np.array([[85, 92, -1],
                   [5,91,47]])
grades[grades < 0]=0
print(grades)

value=np.mean(grades,axis=1)
print(value)
value1=np.max(grades,axis=1)
print(value1)



matrix=np.zeros((8,8),dtype=int)
matrix[::2,::2]=1
matrix[1:2,1:2]=1
print(matrix)


data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
xmin=np.min(data)
print(xmin)
xmax=np.max(data)
print(xmax)

xnorm=(data-xmin)/(xmax-xmin)
print(xnorm)


sijal=np.array([2,5,7,3])
print(sijal)