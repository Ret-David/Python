# David Martinez

# 1) Make a list that includes at least three people you'd like to invite to
#     dinner. Include the following in your code.
#
# 2) print the list with at least three people
# 3) Modify your list, replacing the name of one the guest who can't make it
#     with the name #     of the new person you are inviting. Then print the
#     new list.
# 4) Use insert() to add one new guest to the beginning of your list.
# 5) Use insert() to add one new guest to the middle of your list.
# 6) Use append() to add one new guest to the end of your list.
# 7) Print the new list
# 8) Use pop() to remove guests from your list one at a time until only two
#    names remain in your list. Each time you pop a name from your list, print
#    a message to that person letting them know you're sorry you can't invite
#    them to dinner.

dinner_invites = ["Stephen", "Albert", "Nikola"]    # 1
print("Dinner Invitaion List: ", dinner_invites)    # 2

dinner_invites[2] = "Annie"                         # 3
print("Dinner Invitaion List: ", dinner_invites)

dinner_invites.insert(0, "Michio")                  # 4
dinner_invites.insert(2, "Linus")                   # 5
dinner_invites.append("Phineas")                    # 6
print("Dinner Invitaion List: ", dinner_invites)    # 7

for i in range(2, len(dinner_invites)):             # 8
    popped_invitees = dinner_invites.pop()
    print("I'm sorry " + popped_invitees + ", but I can't invite you to dinner.")

print("Final Dinner Invitaion List: ", dinner_invites)
