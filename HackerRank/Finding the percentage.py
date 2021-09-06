"""
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

print(student_marks)
total = 0

for x,y in student_marks.items():
    if x == query_name:
        lent = len(y)
        for i in y :
            total = total +i 


mean = total/lent
mean = "{:.2f}".format(mean)
print(mean)


