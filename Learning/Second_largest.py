# Function to print the second largest elements
def print2largest(arr, arr_size):
    # There should be atleast two elements
    if (arr_size < 2):
        print(" Invalid Input ")
        return
    # Sort the array
    arr.sort

    for i in range(arr_size - 2, -1, -1):

      if arr[i] != arr[arr_size - 1]:
            print("The second largest element is",arr[i])
            return


    print("There is no second largest element")

# Driver code
arr = [12, 35, 1, 10, 34, 1]
n = len(arr)
print2largest(arr, n)
