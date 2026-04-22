#Given an array of integers arr[] of size n, the task is to rotate the array elements to the left by d positions.
# this function will rotate (shift) the list to the left
def rotate_arr(arr, rotate):
    # get length of list
    n = len(arr)

    # we will repeat rotation 'rotate' times
    for i in range(rotate):

        # save first element (because it will be lost)
        first = arr[0]

        # shift all elements one step to left
        for j in range(n - 1):
            arr[j] = arr[j + 1]

        # put first element at the end
        arr[n - 1] = first


# this part will run only when we run this file directly
if __name__ == "__main__":

    # create a list
    arr = [1, 2, 3, 4, 5, 6]

    # how many times we want to rotate
    rotate = 2

    # call function to rotate list
    rotate_arr(arr, rotate)

    # print the final list
    for k in range(len(arr)):
        print(arr[k], end=" ")
