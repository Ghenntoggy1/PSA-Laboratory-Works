# 3. Counting
import random

iterations = int(input("Input number of iterations: "))
wc = 0
for i in range(1, iterations + 1):
    seats = [0 for x in range(1, 101)]
    p_lost = random.randint(0, 99)
    seats[p_lost] = 1
    for pers in range(1, 99):
        hasSeat = False
        while not hasSeat:
            if seats[pers] == 0:
                seats[pers] = 1
                hasSeat = True
            else:
                p_replace = random.randint(0, 99)
                if seats[p_replace] == 0:
                    seats[p_replace] = 1
                    hasSeat = True
    if seats[99] == 0:
        wc += 1
print("Probability:", wc/iterations)





# # 3. Counting
# import random
#
# iterations = int(input("Input number of iterations: "))
# wc = 0
# for i in range(1, iterations + 1):
#     seats = []
#     for seat in range(1, 101):
#         seats.append(seat)
#     # print(seats)
#     p_lost = random.randint(1, 100)
#     print("Lost =", p_lost)
#     seats.remove(p_lost)
#     print(seats)
#     for person in range(2, 101):
#         print("Person =", person)
#         print(seats)
#         p_seat = random.choice(seats)
#         print("Assigned =", p_seat)
#         if p_seat not in seats:
#             print("UNASSIGNED TAKEN")
#             p_seat_repl = random.choice(seats)
#             seats.remove(p_seat_repl)
#         elif p_seat in seats:
#             print("ASSIGNED FOUND")
#             seats.remove(p_seat)
#         if person == 100 and p_seat in seats:
#             wc += 1
#         print("Seats replaced =", seats)
# print("Probability:", wc/iterations)