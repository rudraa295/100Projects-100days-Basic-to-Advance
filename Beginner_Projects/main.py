# numbers = [
#     1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#     11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
#     21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
#     31, 32, 33, 341, 35, 36, 37, 38, 39, 40,
#     41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
#     51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
#     61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
#     71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
#     81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
#     91, 92, 93, 94, 95, 96, 97, 98, 99, 100
# ]
#
# max = 0
#
# for number in numbers:
#     if number > max:
#         max = number
# print(max)



# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }
# student_grades ={}
#
# for key in student_scores:
#
#     if student_scores[key] > 90:
#         student_grades[key] = "Outstanding"
#     elif student_scores[key] > 80:
#         student_grades[key] = "Exceeds Expectations"
#     elif student_scores[key] > 70:
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Fail"
#
# print(student_grades)

# global lohbs = 1
# def main():
#     return lohbs
# print(main())
a = {"name": 'Royal Challengers Bengaluru', "follower_count": 20, "description": 'Cricket team', "country": 'India'}
b = {}
b = a
print(a)
print(b)