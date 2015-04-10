import time 
# The Timer Function
# Inputs:
    # functions=[method 1,method 2,.....,method n]
    # names=[name of method 1, name of method 2, .......n]
    # no_times=[# of times to execute method 1, ...................... n]
# Outputs the time needed to execute each methods
def timer(functions, names, no_times):
   
    # timer_objs=[] #a list of Timer object
    execution_time=[] #a list of execution time corresponding to each methods
    for index in xrange(len(functions)):
        print functions[index],names[index],no_times[index]

    for index in xrange(len(no_times)):
    
        repeat_number=no_times[index] #repeat_number represents number of times to run the function

        time_taken=timeit.timeit(functions[index], setup="from startup import *" ,number=repeat_number)
    
        execution_time.append( time_taken*1000000 )
    
        print names[index] + " took " + str(execution_time[index]) + " microseconds to run " + str(repeat_number) + " times"

    return [execution_time,names]


# def timer(functions,names,no_times):

#     temp1=functions[2]
#     functions[2]=functions[0]
#     functions[0]=temp1

#     temp2=names[2]
#     names[2]=names[0]
#     names[0]=temp2

#     for index in xrange(len(functions)):

#         t1=time.time()
#         functions[index]()
#         # print w, "gg"
#         t2=time.time()
#         t3=(t2-t1)*1000000
#         print names[index] + " took " + str(t3)


