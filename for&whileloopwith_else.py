'''Here the 'else' will be excecuted'''
# for i in range(6):
    # print(i)
    # 
# else:
    # print("sorry no i")



'''when we 'Break' the loop ends and the 'else' isnt excecuted. '''

# for i in range(6):
    # print(i)
    # if i == 4:
        # break  # At i == 4 the loop ends 
# else:
    # print("sorry no i") 


'''Can be done with 'while loop' '''
i = 0
while i<7: 
    print(i)
    if i == 4:
        break       # With break placed before the range ends.. the 'else' will not be excecuted.
    i = i + 1

else:
    print("exceeding limit")
