#!/usr/bin/env python36
from collections import deque

# not very scary third iteration of algorithm
def cube_pillar3(que):
    lastInPillar = (max(que[0], que[-1]))
    while len(que) > 0:
        element = (max(que[0], que[-1]))
        if que[0] > que[-1]:
            que.popleft()
        else:
            que.pop()
        if element > lastInPillar:
            return('No')
    else:
        return 'Yes'
    return 'Something went wrong'


# scary second iteration of algorithm
# def cube_pillar2(que):
#     starter = True
#     lastInPillar = 0
#     while len(que) >= 1:
#         element = (max(que[0], que[-1]))
#         if que[0] > que[-1]:
#             que.popleft()
#         else:
#             que.pop()
#         if starter:
#             lastInPillar = element
#             starter = False
#         elif element > lastInPillar:
#             return('No')
#     else:
#         return 'Yes'
#     return 'Something gone wrong'

# scary first iteration of algorithm
# def cube_pillar(que):
#     starter = True
#     lastInPillar = 0
#     while len(que) >= 1:
#         leftElement = que.popleft()
#         if len(que) > 0:
#             rightElement = que.pop()
#         else:
#             rightElement = False
        
#         if rightElement and rightElement >= leftElement:
#             que.appendleft(leftElement)
#             workingelement = rightElement
#         elif rightElement and leftElement > rightElement:
#             que.append(rightElement)
#             workingelement = leftElement
#         else:
#             workingelement = leftElement

#         if starter:
#             lastInPillar = workingelement
#             starter = False
#             continue

#         if workingelement > lastInPillar:
#             return 'No'

#     return 'Yes'
        
listsCount = int(input())
for _ in range(listsCount):
    listLen = int(input())
    cubesList = map (int, input().split())
    quene = deque()
    quene.extendleft(cubesList)
    print(cube_pillar3(quene))
