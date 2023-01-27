#-------------------------------------------------------------
# Statistical Analysis
#-------Basics of machine learning----------------------------
# The basis of machine learning
# The use of statisticl tools and analysis to generate algorithms
# to predict outcomes. One basic example of this is
# linear regression - whihc wil be covered in this lesson.

# -----import numpy---------
import numpy as np
import matplotlib.pyplot as py
#----------------------------

# -------Let's look at different types of data and datatypes-----

# ---Uniform distribution

# using fake (randomized data) data:
x = np.random.uniform(0,10,250) # (min, max, #)
#print(x)
py.hist(x,10)
py.show()

# big data
del x
x = np.random.uniform(0,100,100000)
py.hist(x,100)
py.show()

#----Normal distributions----

del x
x = np.random.normal(5,1, 100000) #(average, stdev, n points)
py.hist(x, 100)
py.show()

#----Scatter Plot-------------
del x
x = [6,11,30,2,5,17,21,19,5,12,15,8,6]
y = [99,91,87,88,111,86,104,78,100,12,70,91,86]

py.scatter(x,y)
py.show()

del x,y # making another set of data
x = np.random.normal(10,2.5,1000)
y = np.random.normal(16,5,1000)
py.scatter(x,y)
py.show()

#----------Linear regression------------------
# Using a linear model, one can try to estimate,
# while usning the values of slope and intercept,
# what a future or preducted value would be based on
# already existing data.

# However, we do need to import a new package: scipy (a stats package)

from spicy import stats # terminal: pip3 install spicy

#Example:

#Using the same data as before:
#del x,y
x = [6,11,30,2,5,17,21,19,5,12,15,8,6]
y = [99,91,87,88,111,86,104,78,100,12,70,91,86]

# this next line is a method, there I asking python to determine the:
# -slope
# -y-intercept
# - r, a value whihc when squared offers a "fit" value of the regression
# - p, a value for a null hypothesis (which assumes slope to be 0. Don't worry about it for now
# - std_err, the standard error of the estimated slope value.

slope, intercept, r, p, std_err = stats.linregress(x, y)

def linreg(x):
  return slope * x + intercept

# This line of code reates a list of values for y, the output of the function and maps them.
# List is the "listing of the values" while map generates an array which tabulates
# ( think of a matrix) whihc mapes the values of (in this case) the linreg function output
# to the value of x, the input.

model = list(map(linreg, x))

py.scatter(x, y) # plot a scatter of the original data
py.plot(x, model)# plot the linar regression model
py.show() # show the plot with the combined data and model

print(r) # pearson correlation coefficint. The sign of the value
# is indicative of the slope of the model while the value (absolute value
#of which is between 0 and 1) identifies how well the data fit on the line
# the closer to 1, the better: suggesting a 1 to 1 corespondance between
#model and data.

#--------------Using the model-----------------------
# keeping the values of x and y we've already established:

value = linreg(14)
print(value)
# when x=14, the model predicts the value to be 84. Is that a trustworthy estimate?

# to check:
value2 = linreg(15)
print(value2)
# the value is ~83, which is not the actual value of y when x is 15. This illustrates
# how well the model actually fits the obeserved data.

