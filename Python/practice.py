# student_tuples = [
#   ('john', 'A', 15),
#   ('jane', 'B', 12),
#   ('dave', 'B', 10),
# ]

# print(student_tuples)
# student_tuples.sort(reverse=True, key=lambda student: student[2])
# print(student_tuples)

# data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
# print(data)
# data.sort(reverse=True, key=lambda a: a[0])
# print(data)

# for i in enumerate(data):
#   print(i)

# print("I eat %d apples" % 3)
# print("{0:!^20}".format("hi"))
# print("\n".join("mushmom").split("\n"))
# print("mushmom".upper())

# a = [(1,2), (3,4), (5,6)]
# for (first, last) in a:
#   print(first, last)

# asd = list()
# asd.append(["frodo", "neo"])
# print(["frodo", "neo"] in asd)

# a = {"muzi": "frodo"}
# print(a)
# a["muzi"] = "neo"
# print(a)

# mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(mylist)
# new_list = list(map(list, zip(*mylist)))
# print(new_list)


# def cs(s):
#     _c = ""
#     cnt = 0
#     result = ""
#     for c in s:
#         if c != _c:
#             _c = c
#             if cnt:
#                 result += str(cnt)
#             result += c
#             cnt = 1
#         else:
#             cnt += 1
#     if cnt:
#         result += str(cnt)
#     return result


# print(cs("aaabbcccccccca"))

# nlist = [[0 for i in range(10)] for i in range(10)]
# plist = [a[:] for a in nlist]

# print(nlist)
# print(plist)

# nlist = ["a", "b", "c"]
# print(nlist.index("b"))
# print(nlist.index("c"))

# test = [[0] * 3 for i in range(5)]
# print(test)

# q = dict()
# q[1] = 6
# q[2] = 7
# q[3] = 8
# print(q)
# print(1 in q)
# print(6 in q)

# import heapq
# heap = []
# heapq.heappush(heap, 1)
# heap.append(2)
# heap.append(6)
# heapq.heappush(heap, 3)
# print(heap)

form = []
# for i in "(2*((2)+(3*(3))))+(2*((3)))":
# for i in "2*((2)+(3*((3)))+(2*((3)))":
for i in "2*((2))+(3*((3))))+(2*((3)))":
    form.append(i)
print(form)
formula = "".join(form)
print(formula)
# formula = "(2*((2)+(3*(3))))+(2*((3)))"
print(eval(formula))
form.clear()
print(form)
form.append(0)
print(form)
