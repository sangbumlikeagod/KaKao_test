dic = {}
# 합집합 개념을 사용해야 하기 때문에 어떤요소가 배열 안에 있는지 알 수 없는 리스트보다는
# 알 수 있는 집합이나, 딕셔너리를 사용

'''
주어진 4개의 1 * 1 의 1칸들을 차지하는 것으로 보이는데 그것을 1개의 좌표로 치환할 필요가 있음
(i+1, j) (i+1, j+1)
(i,j) (i+1, j)
이렇게 칸이 주어졌을때 하나의 좌표만으로 한칸을 대표할 수 있기 때문에
나머지는 4개의 사각형에 대해서 중복을 제외한 영역을 추가한다.
'''
for i in range(4):
    ix,iy,jx,jy = map(int,input().split())
    for x_cord in range(ix, jx):
        for y_cord in range(iy, jy):
            if (x_cord,y_cord) in dic:
                continue
            dic[(x_cord,y_cord)] = True
print(len(dic))