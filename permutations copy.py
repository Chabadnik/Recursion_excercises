# print all permutations of a 3 char string
# x = abc
# abc
# acb
# bac
# bca
# cab
# cba

#
# loop solve
#

# loop 1 0 <= i < 3 (Determine First character)
#   loop 2 0 <= j < 3 (Determine Second character)
#       if j != i:
#           loop 3 0 <= k < 3
#               if k != i and k!= j:
#                   print(x(i) + x(j) + x(k))

x = "abc"
y = ""

# for i in range(0, 3):
#     for j in range(0, 3):
#         if j != i:
#             for k in range(0, 3):
#                 if k != i and k != j:
#                     print(x[i] + x[j] + x[k])


def permutations(unused, developing):
    if len(unused) == 1:
        print(developing + unused)
    else:
        for i in range(0, len(unused)):
            permutations(unused[0:i] + unused[i+1:len(unused)], developing + unused[i])


permutations(x, y)


