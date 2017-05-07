# Calculating Length

# len() --> returns length

firstName = "John"
print(len(firstName))
lastName = "Doe"
print(len(lastName))
firstName.__len__()

ages = [0, 11, 43, 12, 10]
print(len(ages))
i = 0
for i in range(0, len(ages)):
    print(ages[i])

print(len(["bob", "mary", "sam"]))

candyCollection = {"bob": 10, "mary": 7, "sam": 18}
print(len(candyCollection))

pointInaGame = [0, -10, 15, -2, 1, 12]
sortedGame = sorted(pointInaGame)
print(sortedGame)

children = ["Sue", "jerry", "linda"]
print(sorted(children, key=str.lower))
print(sorted(["Sue", "jerry", "linda"]))

print(sorted("My favorite child is Linda".split(), key=str.upper))
print(sorted(pointInaGame, reverse=True))

leaderBoard = {231: "CKL", 123: "ABC", 432: "JKC"}
print(sorted(leaderBoard, reverse=True))
print(leaderBoard.get(432))
students = [('alice', 'B', 12), ('eliza', 'A', 16), ('tae', 'C', 15)]
print(sorted(students, key=lambda student:students[1]))