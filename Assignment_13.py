#Question 1
import numpy as np
# a)
arr_1d = np.array([10,20,30,40,50])
# b) 
arr_2d = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
print("One dimensional Array : ",arr_1d) 
print("The shape of arr_1d : ",arr_1d.shape)
print("The data type of arr_1d : ",arr_1d.dtype)
print("Two dimensional Array(3*3) : ",arr_2d)
print("The shape of arr_2d : ",arr_2d.shape)
print("The data type of arr_2d : ",arr_2d.dtype)



#Question 2)
#a)
zero_arr = np.zeros(8)
print("1 Dimensional array with 8 zeros : ",zero_arr)
#b)
twoD_arr1 = np.ones((4,4))
print("4*4 array with 1 is : ",twoD_arr1)
#c)
twoD_arr2 = np.zeros((3,3))
print("3*3 array with 0 is : ",twoD_arr2)

# Question 3)
#a)
arr = np.arange(0,20)
print("Array with Numbers from 0 to 20 (step 1) : ",arr)
#b)
even_arr = np.arange(10,51,2)
print("Array of Even numbers from 10 to 50 :",even_arr)
#c)
new_arr = np.arange(5,100,5)
print("Array of Numbers from 5 to 100 with step of 5 : ",new_arr)

#Question 4)
#a)
lin_arr1 = np.linspace(0,5,10)
print("10 equally spaced numbers between 0 and 5 : ",lin_arr1,"And its length is : ",len(lin_arr1))

lin_arr2 = np.linspace(-10,10,15)
print("15 equally spaced numbers between -10 and 10 : ",lin_arr2,"And its length is : ",len(lin_arr2))

#Question 5)
#a)
random_array1 = np.random.rand(0,1,10)
print("1D array of 10 random numbers between 0 and 1 is : ",random_array1)
#b)
random_matrix = np.random.randn(3,3)
print("A 3x3 matrix of random numbers : ",random_matrix)
#c)
random_array2 = np.random.randint(10, 51, size=(4, 5))
print("A 2D array (4x5) of random integers between 10 and 50 usingnp.random.randint() : ",random_array2)

#Question 6)
v1 = np.array([2, 4, 6, 8])
v2 = np.array([1, 3, 5, 7])
print("v1 = ",v1)
print("v2 = ",v2)
print("Sum of v1 and v2 : ",v1+v2)
print("Substraction of v1 and v2 : ",v1-v2)
print("Product pf v1 and v2 : ",v1*v2)
print("Dot product of v1 and v2 : ",np.dot(v1,v2))

#Question 7)
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[9,8,7],[6,5,4],[3,2,1]])
print("A = ",A)
print("B = ",B)
print("A+B : \n",A+B)
print("A@B : \n",A@B)
print("A*B : \n",A*B)

#Question 8)
M = np.random.randint(1, 101, size=(4, 4))
print("Matrix:\n",M)
print("Shape:",M.shape)
print("Dimension:",M.ndim)
print("Size:",M.size)
print("Data type:",M.dtype)

#Question 9)
arr = np.random.randint(1, 51, size=20)
matrix = arr.reshape(4, 5)
print("Matrix:\n",matrix)
print("Sum:",matrix.sum())
print("Mean:",matrix.mean())
print("Std:",matrix.std())
print("Max in each row:",matrix.max(axis=1))

#Question 10)

try:
    # Get number of elements
    n = int(input("How many numbers? "))
    
    # Generate array
    arr = np.random.randint(10, 101, size=n)
    
    # Print stats
    print("Array:", arr)
    print("Mean:", arr.mean())
    print("Median:", np.median(arr))
    print("Std:", arr.std())
    print("Min:", arr.min(), "Max:", arr.max())
    
    # Try reshape if possible
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                matrix = arr.reshape(i, n//i)
                print(f"Reshaped {i}*{n//i}:\n{matrix}")
                print("Row sums:", matrix.sum(axis=1))
                break
        else:
            print("Cannot reshape to 2D")
            
except ValueError:
    print("Enter a valid number")