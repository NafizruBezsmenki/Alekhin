

def drawSymbolPlot(func,topEdge,bottomEdge,stringCount):

    x_step = ( topEdge - bottomEdge) / stringCount
    x_list = []
    for i in range(stringCount+1):
        x = bottomEdge + x_step*i
        x_list.append(x)
    # print(x_list)
    y_list = []
    for x in x_list:
        y = func(x)
        y_list.append(y)
        print(int(y)*"  ", "*")
        print()
    # print(y_list)
    
    return