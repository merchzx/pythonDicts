# t = input("Enter a string: ")
# w = t.split()
# wc = {}
#
# for wd in w:
#     wc[wd] = wc.get(wd, 0) + 1
#
# print(wc)



# l1 = list(map(int, input("Enter numbers for the 1 list nigga: ").split()))
# l2 = list(map(int, input("Enter numbers for the 2 list nigga: ").split()))
#
# s1 = set(l1)
# s2 = set(l2)
#
# u = s1 | s2
# i = s1 & s2
#
# print("United:", u)
# print("Intersection:", i)



# def g_a(w):
#     a = {}
#     for wd in w:
#         k = ''.join(sorted(wd))
#         if k not in a:
#             a[k] = []
#         a[k].append(wd)
#     return a
#
# w = ["eat", "tea", "tan", "ate", "nat", "bat"]
# print(g_a(w))



# from collections import defaultdict
#
# def g_a(w):
#     r = defaultdict(list)
#     for wd in w:
#         k = ''.join(sorted(wd))
#         r[k].append(wd)
#     return dict(r)
#
# w = ["listen", "silent", "enlist", "google", "gooegl", "abc", "cab"]
# print(g_a(w))



l1 = list(map(int, input("Enter the first list: ").split()))
l2 = list(map(int, input("Enter the second list: ").split()))

s1 = set(l1)
s2 = set(l2)

u = s1 ^ s2

print("Unique elements:", u)
