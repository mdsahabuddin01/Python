"""
Importing different datatypes
The file seaslug.txt

has a text header, consisting of strings
is tab-delimited.
These data consists of percentage of sea slug larvae that had metamorphosed in a given time period. Read more here.

Due to the header, if you tried to import it as-is using np.loadtxt(), Python would throw you a ValueError and tell you that it could not convert string to float. There are two ways to deal with this: firstly, you can set the data type argument dtype equal to str (for string).

Alternatively, you can skip the first row as we have seen before, using the skiprows argument.

Instructions
100 XP
Complete the first call to np.loadtxt() by passing file as the first argument.
Execute print(data[0]) to print the first element of data.
Complete the second call to np.loadtxt(). The file you're importing is tab-delimited, the datatype is float, and you want to skip the first row.
Print the 10th element of data_float by completing the print() command. Be guided by the previous print() call.
Execute the rest of the code to visualize the data.


"""

