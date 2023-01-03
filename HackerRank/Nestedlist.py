if __name__ == '__main__':
  students = []
  for _ in range(int(input())):
   name = input()
   score = float(input())
   students.append([name, score])
   # sort students by score
students.sort(key=lambda x: x[1])

# find the second lowest score
second_lowest_score = sorted(set(student[1] for student in students))[1]

# filter students by second lowest score and sort them by name
second_lowest_scorers = sorted([student[0] for student in students if student[1] == second_lowest_score])

# print names of second lowest scorers
for name in second_lowest_scorers:
    print(name)



# n = int(input())
# # Create a list to store the scores
# scores = []

# # Loop through each student
# for i in range(n):
#     # Get the name and score of the student
#     name = input()
#     score = float(input())

#     # Add the score to the list
#     scores.append(score)

# # Find the second highest score
# second_highest = sorted(set(scores))[1]

# # Create a list to store the names of the students with the second highest score
# second_highest_names = []

# # Loop through the scores again
# for i in range(n):
#     # If the score of the current student is the second highest
#     if scores[i] == second_highest:
#         # Add the name of the student to the list of names
#         second_highest_names.append(name)

# # Sort the names alphabetically
# second_highest_names.sort()

# # Print each name on a new line
# for name in second_highest_names:
#     print(name)
















