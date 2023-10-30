import random


colorList = ['AliceBlue', 'AntiqueWhite', 'aquamarine', 'beige', 'bisque', 'black', 'BlanchedAlmond', 'blue', 'BlueViolet', 'brown', 'burlywood', 'CadetBlue', 'chartreuse', 'chocolate', 'coral', 'CornflowerBlue', 'cornsilk', 'cyan', 'DarkBlue', 'DarkCyan', 'DarkGoldenrod', 'DarkGray', 'DarkGreen', 'DarkGrey', 'DarkKhaki', 'DarkMagenta', 'DarkOliveGreen', 'DarkOrange', 'DarkOrchid', 'DarkRed', 'DarkSalmon', 'DarkSeaGreen', 'DarkSlateBlue', 'DarkSlateGray', 'DarkSlateGrey', 'DarkTurquoise', 'DarkViolet', 'DeepPink', 'DeepSkyBlue']





def getColorList():
    return colorList

def getlenCL():
    return len(colorList)

def remove(item):
    colorList.remove(item)

def add(item):
    colorList.append(item)


if __name__ == '__main__':
    # print(getlenCL())
    # print(getColorList())
    # remove('DarkSlateGray')
    # print(getlenCL())
    # add("Red")
    # print(getlenCL())
    print(colorList[random.randint(0, len(colorList)-1)])
