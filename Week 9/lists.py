friends = []
new_friend = ''
while new_friend != "end":
    new_friend = input("Type the name of a friend: ")
    friends.append(new_friend)


print(f"Your friends are: ")
for friend in friends:
    if friend != "end":
        print(friend)


