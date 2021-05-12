# importing numpy module
# it is equivalent to "import numpy"
# np = __import__('numpy', globals(), locals(), [], 0)

# # arrya from numpy
# a = np.array([1, 2, 3])

# # prints the type
# print(type(a))

# Both the following statements has same meaning
# and does the same work.

# from numpy import complex as comp, array as arr
np = __import__('numpy', globals(), locals(), ['complex'], 0)
  
comp = np.complex
arr = np.array