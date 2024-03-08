left_jug_capacity = int(input("Enter left jug capacity:"))
right_jug_capacity = int(input("Enter right jug capacity:"))
target_capacity = int(input("Enter target jug capacity:"))
left_jug, right_jug = 0, 0
g = [left_jug, right_jug]
while left_jug != target_capacity and right_jug != target_capacity:
    g = [left_jug, right_jug]
    if right_jug < right_jug_capacity:
        if left_jug != 0:
            if right_jug + left_jug <= right_jug_capacity:
                right_jug += left_jug
                left_jug = 0
                print("Transferring Water:",g,"->",[left_jug,right_jug])
            else:
                n = left_jug + right_jug - right_jug_capacity
                right_jug = right_jug_capacity
                left_jug = n
                print("Transferring Water:",g,"->",[left_jug,right_jug])
        else:
            left_jug = left_jug_capacity
            print("Filling Water:",g,"->",[left_jug,right_jug])
    else:
        right_jug = 0
        print("Emptying Water:",g,"->",[left_jug,right_jug])
print("Solution Found:",[left_jug, right_jug])
