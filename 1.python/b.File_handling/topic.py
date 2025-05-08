# f = open(r"D:\CODE_BASICS\1.python\b.File_handling\sample.txt","r")
# for line in f:
#     print(line)
# f.close()

# with open(r"D:\CODE_BASICS\1.python\b.File_handling\sample.txt", "r") as f:
#     for line in f:
#         print(line)

d = {}

with open("D:/CODE_BASICS/1.python/b.File_handling/scores.csv", "r") as f:
    
    for line in f:
        player,score = line.split(',')
        score = int(score)
        if player in d:
            d[player].append(score)   
        else:
            d[player] = [score]
    print(d)
for i,j in d.items():
    print(f'{i} - Maxi {max(j)}')
    print(f'    - total {sum(j)}')
    print(f'    - average {(sum(j)/len(j))}')
        
        
