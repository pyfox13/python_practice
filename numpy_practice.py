

# ------------------------------
# ✅ Import NumPy
# ------------------------------
import numpy as np

# ------------------------------
# ✅ Creating 1D and 2D Arrays
# ------------------------------

# Creating a 1D array (like a Python list)
arr1 = np.array([1, 2, 3])
print("1D Array:", arr1)

# Display properties
print("Shape:", arr1.shape)     # Tuple of dimensions (3,)
print("Dimensions:", arr1.ndim) # Number of dimensions: 1
print("Size:", arr1.size)       # Total number of elements: 3

# Creating a 2D array (like a matrix)
arr2 = np.array([[1, 2], [3, 4]])
print("2D Array:\n", arr2)
print("Shape:", arr2.shape)     # (2 rows, 2 columns)
print("Dimensions:", arr2.ndim) # 2D
print("Size:", arr2.size)       # 4 elements total

# ------------------------------
# ✅ More Practice Arrays
# ------------------------------

# A 3x3 matrix
data = np.array([[1, 3, 5], [2, 4, 6], [7, 8, 9]])
print("3x3 Matrix:\n", data)

# Float array
floats = np.array([0.1, 0.2, 0.3])
print("Float Array:", floats)

# Mixed types: will auto-convert to float
mixed = np.array([1, 2.5, 3])
print("Mixed Array:", mixed)

# Convert Python list to NumPy array
nums = [1, 2, 3, 4]
np_nums = np.array(nums)
print("Double the array:", np_nums * 2)

# ------------------------------
# ✅ Special Arrays
# ------------------------------

zeros_array = np.zeros((2, 3))         # 2x3 matrix filled with 0s
ones_array = np.ones((3, 3))           # 3x3 matrix filled with 1s
identity_matrix = np.eye(3)            # 3x3 identity matrix
arange_array = np.arange(0, 10, 2)     # [0, 2, 4, 6, 8]
linspace_array = np.linspace(0, 1, 5)  # 5 evenly spaced values from 0 to 1

print("Zeros:\n", zeros_array)
print("Ones:\n", ones_array)
print("Identity:\n", identity_matrix)
print("Arange:\n", arange_array)
print("Linspace:\n", linspace_array)

# ------------------------------
# ✅ Math & Broadcasting
# ------------------------------

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print("a + b =", a + b)     # Add element-wise
print("a * 2 =", a * 2)     # Multiply every element by 2
print("b - a =", b - a)     # Subtract element-wise

# Broadcasting: Add 1D array to each row of 2D array
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("matrix + a =\n", matrix + a)

# ------------------------------
# ✅ Indexing & Slicing
# ------------------------------

arr = np.array([[10, 20, 30], [40, 50, 60]])
print("First row:", arr[0])          # Access first row
print("Second column:", arr[:, 1])   # All rows, second column
print("Element (1,2):", arr[1, 2])   # Value at row 1, col 2
print("Slice:", arr[0:2, 1:])        # Subarray of rows 0-1, cols 1-end

# ------------------------------
# ✅ Boolean Indexing
# ------------------------------

x = np.array([1, 2, 3, 4, 5])
print("x > 3:", x > 3)               # Boolean array
print("Filtered x[x > 3]:", x[x > 3]) # Filtered result
x[x % 2 == 0] = 0                    # Replace even numbers with 0
print("After replacing evens:", x)

# ------------------------------
# ✅ Fake Image Simulation
# ------------------------------

image = np.random.randint(0, 255, (5, 5))  # Random pixel values in 5x5 grid
print("Image:\n", image)
print("Mean:", np.mean(image))            # Average pixel value
print("Max:", np.max(image))              # Brightest pixel
print("Argmax:", np.argmax(image))        # Index of brightest pixel (flattened)

# ------------------------------
# ✅ Quick Practice
# ------------------------------

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix = matrix * 5                       # Multiply all by 5
matrix[matrix > 20] = 0                   # Set values > 20 to 0
print("Modified matrix:\n", matrix)
print("Row means:", np.mean(matrix, axis=1))  # Mean across each row

# ------------------------------
# ✅ Student Grades Project
# ------------------------------

grades = np.random.randint(50, 100, size=(10, 5))  # 10 students × 5 subjects
student_averages = np.mean(grades, axis=1)         # Avg per student

print("Grades:\n", grades)
print("Avg per student:", student_averages)
print("Pass status (>= 60):", student_averages >= 60)
print("Top scorer index:", np.argmax(student_averages))
print("Subject averages:", np.mean(grades, axis=0))

