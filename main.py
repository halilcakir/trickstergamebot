import pyautogui
import time
import win32api, win32con
import keyboard
import pyscreenshot
import cv2 as cv
import easyocr
import numpy as np
from torchvision import models
model = models.resnet50(pretrained=True)
from matplotlib import pyplot as plt
import warnings

Positions = []
item_values =[]
value = []

class Maidenstaff():
    def __init__(self):
        self.MA = 86 
        self.LK = 46
class MaidenDagger():
    def __init__(self):
        self.AP = 1392 
        self.DA = 86
        self.HV = 86
class MaidenHat():
    def __init__(self):
        self.AC = 46
        self.MD = 742
        self.DP = 742
        self.LK = 46
class MaidenGun():
    def __init__(self):
        self.AP = 1392
        self.LK = 46
        self.AC = 46
class MaidenShield():
    def __init__(self):
        self.MD = 1021 
        self.HP = 2598
        self.DP = 1021  
class MaidenRing():
    def __init__(self):
        self.AP = 557 
        self.AC = 34
        self.MP = 1949
        self.MA = 34
        self.DA = 34
        self.LK = 34
        self.HP = 1949
        self.HV = 34



for page in range(7):
    def leftClick():
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        pyautogui.moveTo(700,500)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        
    

    def get_item_value_image(i,j):
        path= ".\equips\item{}{}.png".format(i,j)
        img = cv.imread(path)

        #convert the BGR image to HSV colour space
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

        #set the lower and upper bounds for the white hue
        lower_white = np.array([40,60,168],dtype=np.uint8)
        upper_white = np.array([80,255,255],dtype=np.uint8)

        #create a mask for white colour using inRange function
        mask = cv.inRange(hsv, lower_white, upper_white)


        def cropimage():

            isim = path.split('item')
            
            if isim[1].find('2')== 0:
                cropped_image = mask[10:160, 20:150]
                cv.imwrite("filtered_image{}{}.png".format(i,j),cropped_image)
        
            elif isim[1].find('0')==0:
                cropped_image = mask[5:160, 30:150]
                cv.imwrite("filtered_image{}{}.png".format(i,j),cropped_image)
            

            else:
                cropped_image = mask[10:160, 30:150]
                cv.imwrite("filtered_image{}{}.png".format(i,j),cropped_image)

        cropimage()

    last_values=[]
    def check_values(i,j,last_values=[]):
        warnings.filterwarnings("ignore", category=UserWarning) 

        image = 'filtered_image{}{}.png'.format(i,j)
        reader = easyocr.Reader(['en'])
        result =reader.readtext(image)
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        pointer = []  
        cumle= ""
        value = []
        string_values = []
        for i in range(len(result)):
            for j in range(len(result[i])):
                
                if type(result[i][j])==str:
                        sayac=0
                        string_values.append(result[i][j])

                        for k in range(len(numbers)):
                            
                            if str(result[i][j]).find(numbers[k]) != -1 and str(result[i][j])!='':
                                #print(numbers[k],"index:",str(result[i][j]).find(numbers[k]))
                                pointer.append(str(result[i][j]).find(numbers[k]))
                                sayac = sayac + 1
        
        #print(pointer, sayac,i)
            
            value.append(pointer[-sayac:])
            value[i].sort()
            string_values[i] = ''.join(f for f in str(string_values[i]) if f.isdigit())
            try:
                x=int(string_values[0])

                if x > 2000:
                    string_values[0] = string_values[0][-3:]


                b=int(string_values[i])
                if b > 3500:
                    string_values[i] = string_values[i][-3:]
                elif b==0:
                    string_values[i] = 8

            except:
                pass
        
            print(string_values[i])
            last_values.append(string_values)


    
    def getss(i,j,x,y,w,h):
        
        pic = pyscreenshot.grab(bbox=(x,y,w,h))
        pic.save(".\equips\item{}{}.png".format(i,j))
        get_item_value_image(i,j)
        Positions.append("{},{}".format(pyautogui.position().x, pyautogui.position().y))
        check_values(i,j,last_values)
        time.sleep(0.1)
        
    def getnames(i,j,x,y,w,h):
        
        pic = pyscreenshot.grab(bbox=(x,y-175,w,h-130))
        pic.save(".\\names\item{}{}.png".format(i,j)) 
        time.sleep(0.3)

    item_class=[]
    def get_item_names(img):

        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        lower_purple = np.array([130,10,0],dtype=np.uint8)
        upper_purple = np.array([150,255,255],dtype=np.uint8)
        mask = cv.inRange(hsv, lower_purple, upper_purple)
        res = cv.bitwise_and(img, img, mask=mask)
        items=['Tiara','Gun','Helm','Hem','Shot','Gur'
        'Ring','Helmet','Bracelet','Shield','Crossbow','hel'
        'QueenStaff','Mace', 'Sword',
        'QueenMace','Queen Mace','SpiritualStaff','sta','staff'
        'Spiritual Staff', 'dagger']

        reader = easyocr.Reader(['en'])
        cropped = mask[0:130, 0:220]
        result =reader.readtext(cropped)
        
        time.sleep(0.1)
        print(result)
        for s in range(len(result)):
            cumle=str(result[s][1]).split(' ') 
            for i in range(len(items)):  
                for j in range(len(cumle)):
                    if items[i].lower() in cumle[j].lower():
                        if items[i] == 'Hem' or items[i] == 'Helrn' or items[i] == 'Helr' or items[i] == 'Helmn' or items[i] == 'Helmi':
                            print('Helm')
                            item_info = 'Helm'
                            item_class.append(item_info)
                        elif items[i] == 'SpiritualGun' or items[i] == 'gur' or items[i] == 'Shot' or items[i] == 'Crossbow' or 'dagger':
                            print('Gun')
                            item_info = 'Gun'
                            item_class.append(item_info)
                        
                        else:
                            print(items[i])
                            item_info= items[i]
                            item_class.append(item_info)
                    else:
                        pass       
        time.sleep(0.1)
                        

    def find_item():

        try:
            win_loc = pyautogui.locateOnScreen(r".\images\item1.png")
            if win_loc is not None:
                print("Item Window Loc: ", win_loc)
            else:
                print("Item window1 could not be found")
        except:
            pass

        try:
            win_loc2 = pyautogui.locateOnScreen(r".\images\item2.png")
        
            if win_loc2 is not None:
                print("Item Window loc: ", win_loc2)
            else:
                print("Item window2 could not be found")
                
        except:
            pass

            

        for k in range(3):
                
                for x in range(7):
                       
                            
                        if win_loc is not None:
                            print("position:",pyautogui.position())
                            pyautogui.moveTo(win_loc[0]+(x*40),win_loc[1]+(k*40)+80)
                            getnames(k,x,win_loc[0]+(x*40)-10,win_loc[1]-50+(k*40),win_loc[0]+(x*40)+220,win_loc[1]+150+(k*40))
                        
                            path= r".\names\item{}{}.png".format(k,x)
                            img = cv.imread(path)
                            get_item_names(img)
                        
                            getss(k,x,win_loc[0]+(x*40)-10,win_loc[1]-50+(k*40),win_loc[0]+(x*40)+220,win_loc[1]+150+(k*40))
        
                        
                        else:
                            
                            
                            print("position:",pyautogui.position())
                            pyautogui.moveTo(win_loc2[0]+(x*40),win_loc2[1]+(k*40)+80)
                            getnames(k,x,win_loc2[0]+(x*40)-5,win_loc2[1]-50+(k*40),win_loc2[0]+(x*40)+220,win_loc2[1]+150+(k*40))
                        
                            path= r".\names\item{}{}.png".format(k,x)
                            img = cv.imread(path)
                            get_item_names(img)
                    
                            getss(k,x,win_loc2[0]+(x*40)-5,win_loc2[1]-50+(k*40),win_loc2[0]+(x*40)+220,win_loc2[1]+150+(k*40),)

                            
                        time.sleep(0.3)



    def find_store():

        try:
            store_location = pyautogui.locateOnScreen(r".\images\store1.png")
            if store_location is not None:
                print("Window Location: ",store_location)
                pyautogui.moveTo(store_location[0], store_location[1])
        except:
            pass   
        
        try:
            store_location2 = pyautogui.locateOnScreen(r".\images\store2.png")
            if store_location2 is not None:
                print("Window Location: ",store_location2)
                pyautogui.moveTo(store_location2[0], store_location2[1])
        except:
            print("Store window could not be found")   



    time.sleep(1)
    find_item()
    # scan_item_names()
    time.sleep(1)   
    find_store() 
    print(Positions)
    print(value)


    properties=[]

    for i in range(len(last_values)):
        if last_values[i] not in properties:
            properties.append(last_values[i])


    for j in range(len(properties)):
        for i in range(len(properties[j])):
            if properties[j][i]== '':
                properties[j][i] ='1'


    for j in range(len(properties)):
                properties[j] = [int(i) for i in properties[j]]



    if len(item_class)<len(properties):
        for i in range(len(item_class)):
                if 'sta'in item_class[i]:
                    if max(properties[i])>400:
                        x= str(max(properties[i]))[-2:]
                        value = int(x)
                        if Maidenstaff().MA <= value:
                            
                            print(Positions[i],item_class[i],max(properties[i]),properties[i],value)
                            pyautogui.moveTo(int(Positions[i][:3]),int(Positions[i][-3:]))
                            leftClick()
                            time.sleep(1)
                    elif Maidenstaff().MA <= max(properties[i]):
                            print(Positions[i],item_class[i],max(properties[i]),properties[i],value)
                            pyautogui.moveTo(int(Positions[i][:3]),int(Positions[i][-3:]))
                            leftClick()
                            time.sleep(1)

                elif 'swo'in item_class[i] or 'mace'in item_class[i] :
                    if max(properties[i])>10000:
                        x= str(max(properties[i]))[-2:]
                        value = int(x)
                        if MaidenGun().AP <= value:
                            
                            print(Positions[i],item_class[i],max(properties[i]),properties[i],value)
                            pyautogui.moveTo(int(Positions[i][:3]),int(Positions[i][-3:]))
                            leftClick()
                            time.sleep(1)
                    elif MaidenGun().AP <= max(properties[i]):
                            print(Positions[i],item_class[i],max(properties[i]),properties[i],value)
                            pyautogui.moveTo(int(Positions[i][:3]),int(Positions[i][-3:]))
                            leftClick()
                            time.sleep(1)
                elif 'Helm'in item_class[i]:
                    if max(properties[i])>2000:
                        x= str(max(properties[i]))[-2:]
                        value = int(x)
                        if MaidenHat().MD <= value:
                            
                            print(Positions[i],item_class[i],max(properties[i]),properties[i],value)
                            pyautogui.moveTo(int(Positions[i][:3]),int(Positions[i][-3:]))
                            leftClick()
                            time.sleep(1)
                    elif  MaidenHat().MD <= max(properties[i]):
                            print(Positions[i],item_class[i],max(properties[i]),properties[i],value)
                            pyautogui.moveTo(int(Positions[i][:3]),int(Positions[i][-3:]))
                            leftClick()
                            time.sleep(1)

                elif 'Gun'in item_class[i]:
                    if max(properties[i])>5000:
                        x= str(max(properties[i]))[-2:]
                        value = int(x)
                        if MaidenGun().AP <= value:
                            
                            print(Positions[i],item_class[i],max(properties[i]),properties[i],value)
                            pyautogui.moveTo(int(Positions[i][:3]),int(Positions[i][-3:]))
                            leftClick()
                            time.sleep(1)
                    elif MaidenGun().AP <= max(properties[i]):
                            print(Positions[i],item_class[i],max(properties[i]),properties[i],value)
                            pyautogui.moveTo(int(Positions[i][:3]),int(Positions[i][-3:]))
                            leftClick()
                            time.sleep(1)

                    elif 'ring'in item_class[i]:
                        if max(properties[i])>10000:
                            x= str(max(properties[i]))[-2:]
                            value = int(x)  
                            if MaidenRing().AC <= value:
                            
                                print(Positions[i],item_class[i],max(properties[i]),properties[i],value)
                                pyautogui.moveTo(int(Positions[i][:3]),int(Positions[i][-3:]))
                                leftClick()
                                time.sleep(1)
                        elif MaidenRing().AC <= max(properties[i]):
                            print(Positions[i],item_class[i],max(properties[i]),properties[i],value)
                            pyautogui.moveTo(int(Positions[i][:3]),int(Positions[i][-3:]))
                            leftClick()
                            time.sleep(1)
                            
                    elif 'shield'in item_class[i]:
                        if max(properties[i])>10000:
                            x= str(max(properties[i]))[-2:]
                            value = int(x)  
                            if MaidenShield().HP <= value:
                            
                                print(Positions[i],item_class[i],max(properties[i]),properties[i],value)
                                pyautogui.moveTo(int(Positions[i][:3]),int(Positions[i][-3:]))
                                leftClick()
                                time.sleep(1)
                        elif MaidenShield().HP <= max(properties[i]):
                            print(Positions[i],item_class[i],max(properties[i]),properties[i],value)
                            pyautogui.moveTo(int(Positions[i][:3]),int(Positions[i][-3:]))
                            leftClick()
                            time.sleep(1)



    else:

        for i in range(len(properties)):
            if 'sta'in item_class[i]:
                    if max(properties[i])>400:
                        x= str(max(properties[i]))[-2:]
                        value = int(x)
                        if Maidenstaff().MA <= value:
                            
                            print(Positions[i],item_class[i],max(properties[i]),properties[i],value)
                            pyautogui.moveTo(int(Positions[i][:3]),int(Positions[i][-3:]))
                            leftClick()
                            time.sleep(1)
                    elif Maidenstaff().MA <= max(properties[i]):
                            print(Positions[i],item_class[i],max(properties[i]),properties[i],value)
                            pyautogui.moveTo(int(Positions[i][:3]),int(Positions[i][-3:]))
                            leftClick()
                            time.sleep(1)

            elif 'swo'in item_class[i] or 'mace'in item_class[i] :
                if max(properties[i])>10000:
                    x= str(max(properties[i]))[-2:]
                    value = int(x)
                    if MaidenGun().AP <= value:
                        
                        print(Positions[i],item_class[i],max(properties[i]),properties[i],value)
                        pyautogui.moveTo(int(Positions[i][:3]),int(Positions[i][-3:]))
                        leftClick()
                        time.sleep(1)
                elif MaidenGun().AP <= max(properties[i]):
                        print(Positions[i],item_class[i],max(properties[i]),properties[i],value)
                        pyautogui.moveTo(int(Positions[i][:3]),int(Positions[i][-3:]))
                        leftClick()
                        time.sleep(1)
            elif 'Helm'in item_class[i]:
                if max(properties[i])>2000:
                    x= str(max(properties[i]))[-2:]
                    value = int(x)
                    if MaidenHat().MD <= value:
                        
                        print(Positions[i],item_class[i],max(properties[i]),properties[i],value)
                        pyautogui.moveTo(int(Positions[i][:3]),int(Positions[i][-3:]))
                        leftClick()
                        time.sleep(1)
                elif  MaidenHat().MD <= max(properties[i]):
                        print(Positions[i],item_class[i],max(properties[i]),properties[i],value)
                        pyautogui.moveTo(int(Positions[i][:3]),int(Positions[i][-3:]))
                        leftClick()
                        time.sleep(1)

            elif 'Gun'in item_class[i]:
                if max(properties[i])>5000:
                    x= str(max(properties[i]))[-2:]
                    value = int(x)
                    if MaidenGun().AP <= value:
                        
                        print(Positions[i],item_class[i],max(properties[i]),properties[i],value)
                        pyautogui.moveTo(int(Positions[i][:3]),int(Positions[i][-3:]))
                        leftClick()
                        time.sleep(1)
                elif MaidenGun().AP <= max(properties[i]):
                        print(Positions[i],item_class[i],max(properties[i]),properties[i],value)
                        pyautogui.moveTo(int(Positions[i][:3]),int(Positions[i][-3:]))
                        leftClick()
                        time.sleep(1)

                elif 'ring'in item_class[i]:
                    if max(properties[i])>10000:
                        x= str(max(properties[i]))[-2:]
                        value = int(x)  
                        if MaidenRing().AC <= value:
                        
                            print(Positions[i],item_class[i],max(properties[i]),properties[i],value)
                            pyautogui.moveTo(int(Positions[i][:3]),int(Positions[i][-3:]))
                            leftClick()
                            time.sleep(1)
                    elif MaidenRing().AC <= max(properties[i]):
                        print(Positions[i],item_class[i],max(properties[i]),properties[i],value)
                        pyautogui.moveTo(int(Positions[i][:3]),int(Positions[i][-3:]))
                        leftClick()
                        time.sleep(1)
                        
                elif 'shield'in item_class[i]:
                    if max(properties[i])>10000:
                        x= str(max(properties[i]))[-2:]
                        value = int(x)  
                        if MaidenShield().HP <= value:
                        
                            print(Positions[i],item_class[i],max(properties[i]),properties[i],value)
                            pyautogui.moveTo(int(Positions[i][:3]),int(Positions[i][-3:]))
                            leftClick()
                            time.sleep(1)
                    elif MaidenShield().HP <= max(properties[i]):
                        print(Positions[i],item_class[i],max(properties[i]),properties[i],value)
                        pyautogui.moveTo(int(Positions[i][:3]),int(Positions[i][-3:]))
                        leftClick()
                        time.sleep(1)



    
    
    win=pyautogui.locateOnScreen(r".\images\down.png")

    pyautogui.moveTo(win[0]-15,win[1]+5)
    
    for i in range (3):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


