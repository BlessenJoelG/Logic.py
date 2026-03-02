user_name = input()
user_name = {user_name[_]for _ in range(len(user_name))}
if (len(user_name))%2 != 0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")
