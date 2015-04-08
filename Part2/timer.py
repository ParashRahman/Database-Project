from timeit import Timer

# The Timer Function
# Inputs:
    # methods=[method 1,method 2,.....,method n]
    # names=[name of method 1, name of method 2, .......n]
    # no_times=[# of times to execute method 1, ...................... n]
# Outputs the time needed to execute each methods
def timer(functions, names, no_times):
    timer_objs=[] #a list of Timer object
    execution_time=[] #a list of execution time corresponding to each methods

    for function in functions:
        timer_objs.append(Timer(function))

    for index in range(len(no_times)):
        repeat_number=no_times[index] #repeat_number represents number of times to run the function
        execution_time.append( timer_objs[index](repeat_number) )
        print names[index]+" took "+execution_time[index]+" seconds to run "+repeat_number+" times"

    return
