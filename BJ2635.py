inp = 100

def fibonaci_devide(num1, num2):
    # print(num1, num2)
    if num1 * inp // num2 == num2 * inp // (num1 + num2):
        # print(num1 * inp / num2, num2 * inp / (num1 + num2))
        # return num1 * inp // num2 + 1 if num2 // (num1 * inp // num2) >= 2 else num1 * inp // num2
        return round(min( num1 * inp / num2 , num2 * inp / (num1 + num2)))
        # return num1 * inp // num2 + 1 if num2 // (num1 * inp // num2) < 2 else num1 * inp // num2
    else:
        return fibonaci_devide(num2, num1 + num2)

def fibonaci_devide2(num1, num2):
    # print(num1, num2)
    if num1 * inp // num2 == num2 * inp // (num1 + num2):
        # print(num1 * inp / num2, num2 * inp / (num1 + num2))
        # return num1 * inp // num2 + 1 if num2 // (num1 * inp // num2) >= 2 else num1 * inp // num2
        return round(min( num1 * inp / num2 , num2 * inp / (num1 + num2))) + 1 
        # return num1 * inp // num2 + 1 if num2 // (num1 * inp // num2) < 2 else num1 * inp // num2
    else:
        return fibonaci_devide(num2, num1 + num2)

def fibonaci_devide3(num1, num2):
    # print(num1, num2)
    if num1 * inp // num2 == num2 * inp // (num1 + num2):
        # print(num1 * inp / num2, num2 * inp / (num1 + num2))
        # return num1 * inp // num2 + 1 if num2 // (num1 * inp // num2) >= 2 else num1 * inp // num2
        return round(min( num1 * inp / num2 , num2 * inp / (num1 + num2))) - 1 
        # return num1 * inp // num2 + 1 if num2 // (num1 * inp // num2) < 2 else num1 * inp // num2
    else:
        return fibonaci_devide(num2, num1 + num2)


# print(maxint)

def fibonacci_substract(num1, num2):
    # print(num1, num2)
    if num1 - num2 < 0:
        return [num2, num1]
    else:
        lst1 = fibonacci_substract(num2, num1 - num2)
        lst1 += [num1]
        return lst1
# return_ans = fibonacci_substract(inp, fibonaci_devide(1,1))
# print(len(return_ans))
# print(' '.join(map(str,return_ans[::-1])))

for inp in range(1, 30000):
    return_ans = fibonacci_substract(inp, fibonaci_devide(1,1))
    return_ans2 = fibonacci_substract(inp, fibonaci_devide2(1,1)+1)
    return_ans3 = fibonacci_substract(inp, fibonaci_devide3(1,1)-1)

    if len(return_ans) < len(return_ans2) or len(return_ans) < len(return_ans3):
        print('반례발견')
        print(
            return_ans,
            return_ans2,
            return_ans3,
            sep='\n'
            )
        
else:
    print(inp)
    print('없음')
    
    
'''
아래는 반례를 해결하기 위해서 두가지 경우를 대입해서 큰 수를 찾아내는 방식으로 문제를 풀었다.
'''


inp = int(input())


def fibonaci_devide(num1, num2):
    if num1 * inp // num2 == num2 * inp // (num1 + num2):
        return
    else:
        result = fibonaci_devide(num2, num1 + num2)
        if result != None:
            return result
        else:
            return max(num1 * inp // num2, num2 * inp // (num1 + num2) )

    
def fibonacci_substract(num1, num2):
    # print(num1, num2)
    if num1 - num2 < 0:
        return [num2, num1]
    else:
        lst1 = fibonacci_substract(num2, num1 - num2)
        lst1 += [num1]
        return lst1
    
    
return_ans1 = fibonacci_substract(inp, fibonaci_devide(1,1))
return_ans2 = fibonacci_substract(inp, fibonaci_devide(1,1) - 1)


if len(return_ans2) > len(return_ans1):
    return_ans = return_ans2
else:
    return_ans = return_ans1

print(len(return_ans))
print(' '.join(map(str,return_ans[::-1])))