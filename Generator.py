def krange():
    yield "Python"
    yield "Django"
    yield "Data Science"
    yield "Machine Learning"

obj=krange()
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))