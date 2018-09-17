n=int(input())
grades=[]
result=[]

if 1<=n<=60:
    for _ in range(n):
        grades_item=int(input())
        grades.append(grades_item)

def grading(grades):
    for val in grades:
        if 0<=val<=100:
            if val >=38:
                if val % 5 != 0:
                    
                    for k in range(1,3):
                        if (val+k)%5==0:
                            val=val+k
                            break
                        else:
                            k+=1
                else:
                    val=val
            else:
                val=val
            result.append(val)
    return result
            
result=grading(grades)

for val in result:
    print(val,end='\n')

