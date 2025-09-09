def calculate_average(score_list):
    if len(score_list) == 0:
       return 0
    total = sum(score_list)
    average = total / len(score_list)
    return average


def find_max(score_list):
    if len(score_list) == 0:
       return None
    max_score = score_list[0]
    for score in score_list:
        if score in score_list:
            max_score = score
    return max_score


def find_min(score_list):
    if len(score_list) == 0:
        return None
    
    min_score = score_list[0]
    for score in score_list:
        if score < min_score:
            min_score = score
    return min_score


def count_passed(score_list):
    count = 0
    for score in score_list:
        if score >= 50:
            count += 1
    return count


def get_grades(score_list):
    grades = []
    for score in score_list:
        if score >= 80:
            grades.append('A')
        elif score >= 75:
            grades.append('B+')
        elif score >= 70:
            grades.append('B')
        elif score >= 60:
            grades.append('C')
        elif score >= 50:
            grades.append('D')
        else:
            grades.append('F')
    return grades


 
scores = [88, 92, 75, 68, 95, 80]


avg = calculate_average(scores)
highest = find_max(scores)
lowest = find_min(scores)
passed = count_passed(scores)
grades = get_grades(scores)

print(f"Scores: {scores}")
print(f"Average: {avg:.2f}")
print(f"Highest Score: {highest}")
print(f"Lowest Score: {lowest}")
print("-"*30)
print(f"passed: {passed}")
print(f"grades: {grades}")