import pandas as pd
import plotly.figure_factory as ff
from statistics import *

df = pd.read_csv("StudentsPerformance.csv")
math_marks = df["math score"].tolist()
writing_marks = df["writing score"].tolist()
reading_marks = df["reading score"].tolist()

Mean1 = mean(math_marks)
print("The mean of students marks in maths is :",+Mean1)

Meadian1 = median(math_marks)
print("The median of the students marks in maths is :",+Meadian1)

mode1 = mode(math_marks)
print("The mode of the students marks in maths is :",+mode1)