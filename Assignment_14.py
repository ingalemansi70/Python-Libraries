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


#Question 4)
arr = np.arange(1,25)
arr1 = arr.reshape(4,6)
arr2 = arr.reshape(3,8)
arr3D = arr.reshape(2,3,4)
print("Original array : \n",arr)
print("Array with 4 rows and 6 columns : \n",arr1," Its shape : : ",arr1.shape)
print("Array with 3 rows and 8 columns : \n",arr2," Its shape : ",arr2.shape)
print("The 3D array : \n",arr3D," and its shape : ",arr3D.shape)

#Question 5)

arr = np.array([[10, 20, 30, 40],
[50, 60, 70, 80],
[90, 100, 110, 120]])
print("The array : ",arr)
print("The first row : ",arr[0])
print("The first column : ",arr[:,0])
print("The center 2*2 : \n",(arr[1:3][1:3]).reshape(2,2))
even_array = arr[arr%2 == 0]  
print("Even numbers array : ",even_array)


#Question 6)

arr = np.random.randint(1,100,(5,5))
print("The 5*5 array : \n",arr)
print("Diagonal elements : \n")
for i in range(min(arr.shape)):
    print("arr[", i, ",",i,"]=",arr[i,i])
arr_50 = arr[arr>50]
print("Array containing elements greater than 50 : \n",arr_50)
print("Array after Replacing all elements less than 30 with 0 : \n")
for i in range(min(arr.shape)):
    arr[arr<30]=0
print(arr)

print("The final modified array : \n",arr)
