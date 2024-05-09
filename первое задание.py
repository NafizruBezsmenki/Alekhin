def x2(x):
    return x**2
    
def y2(x):
    return 5+3/2

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
if __name__ == "__main__":    
    drawSymbolPlot(x2,-5,5,15)
