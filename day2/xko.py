rozmer = int(input("Zadej rozměr: "))

# 5
# X O X O X
# O X O X O
# O O X O O
# O X O X O
# X O X O X

# [0,0] [0,1] [0,2] [0,3] [0,4]
# [1,0] [1,1] [1,2] [1,3] [1,4]
# [2,0] [2,1] [2,2] [2,3] [2,4]
# [3,0] [3,1] [3,2] [3,3] [3,4]
# [4,0] [4,1] [4,2] [4,3] [4,4]

for i in range(rozmer):
    for j in range(rozmer):
        if i == j or i + j == rozmer - 1:
            print("X ", end="")
        else:
            print("O ", end="")
    print()