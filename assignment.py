class Math:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):a
        return a / b

    def remainder(self, a, b):
        return a % b


class Physics:
    def velocity(self, distance, time):
        return distance / time

    def acceleration(self, initial_velocity, final_velocity, time):
        return (final_velocity - initial_velocity) / time

    def force(self, mass, acceleration):
        return mass * acceleration

    def work(self, force, distance):
        return force * distance

    def power(self, work, time):
        return work / time



course = input("Do you want to calculate Math or Physics? ")
if course.lower() == "math":
    answer = Math()
elif course.lower() == "physics":
    answer = Physics()
else:
    print("Not part of courses")
    exit()


operation = input( "Which operation do you want to perform? ")
if operation.lower() == "add":
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    result = answer.add(a, b)
elif operation.lower() == "subtract":
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    result = answer.subtract(a, b)
elif operation.lower() == "multiply":
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    result = answer.multiply(a, b)
elif operation.lower() == "divide":
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    result = answer.divide(a, b)
elif operation.lower() == "remainder":
    a = float(input("Enter the numerator: "))
    b = float(input("Enter the denominator "))
    result = answer.remainder(a, b)
elif operation.lower() == "velocity":
    d = float(input("Enter the distance traveled: "))
    t = float(input("Enter the time taken: "))
    result = answer.velocity(d, t)
elif operation.lower() == "acceleration":
    v1 = float(input("Enter the initial velocity: "))
    v2 = float(input("Enter the final velocity: "))
    t = float(input("Enter the time taken: "))
    result = answer.acceleration(v1, v2, t)
elif operation.lower() == "force":
    m = float(input("Enter the mass: "))
    a = float(input("Enter the acceleration: "))
    result = answer.force(m, a)
elif operation.lower() == "work":
    f = float(input("Enter the force: "))
    d = float(input("Enter the distance: "))
    result = answer.work(f, d)
elif operation.lower() == "power":
    w = float(input("Enter the work done: "))
    t = float(input("Enter the time taken: "))
    result = answer.power(w, t)
else:
    print("Invalid operation.")
    exit()


print("The answer is:", result)
