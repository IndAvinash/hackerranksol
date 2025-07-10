data_size = list(map(int,input().split(" "))) # 5 3
student_data = list()
for i in range(data_size[1]):
    subject_data = list(map(float,input().split(" ")))
    student_data.append(subject_data)
avg_data = list()
for i in range(data_size[0]):
    sums = 0
    for j in student_data:
        sums += j[i]
    avg_data.append(sums/data_size[1])
for i in avg_data:
    print(i)

