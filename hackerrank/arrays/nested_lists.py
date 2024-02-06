# https://www.hackerrank.com/challenges/nested-list/problem

import math

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        
    min_score = math.inf
    second_min_score = math.inf
    
    for record in records:
        if record[1] < min_score:
            second_min_score = min_score
            min_score = record[1]
        if record[1] < second_min_score and record[1] != min_score:
            second_min_score = record[1]
    
    second_lowest_students = []
    for record in records:
        if record[1] == second_min_score:
            second_lowest_students.append(record[0])
    
    for student in sorted(second_lowest_students):
        print(student)
