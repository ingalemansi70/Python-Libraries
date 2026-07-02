import numpy as np
#Question 1)
arr_2D = np.random.randint(10,100,(5,6))
print("2D Array of shape (5,6) with random integer values : \n",arr_2D)
print("Shape of above array is : ",arr_2D.shape)
print("Total number of elements in the array : ",arr_2D.size)
print("Data type of the array : ",arr_2D.dtype)

#Question 2)
arr_1D = np.random.randint(1,50,20)
print("The 1D array : \n",arr_1D)
print("Minimum value : ",np.min(arr_1D)," and its index is : ",np.argmin(arr_1D))
print("Miximum value : ",np.max(arr_1D)," and its index is : ",np.argmax(arr_1D))
print("The mean value of array is : ",np.mean(arr_1D))
print("Sum of all elements of array : ",np.sum(arr_1D))
print("The Standard Deviation of array is : ",np.std(arr_1D))

#Question 3)

arr = np.random.randint(20,80,(4,5))
print("The 4*5 matrix : \n",arr)
print("The minimum value in the array : ",np.min(arr))
print("The miximum value in the array : ",np.max(arr))
print("Sum of all elements of array : ",np.sum(arr))
print("The mean value of array is : ",np.mean(arr))
print("The Standard Deviation of array is : ",np.std(arr))
print("The sum of each row : ",arr.sum(axis =1))
print("The sum of each column : ",arr.sum(axis =0))


