import cv2
import dropbox
import time
import random
import pyautogui
import numpy as np

# myScreenshot=pyautogui.screenshot()
# myScreenshot = cv2.cvtColor(np.array(myScreenshot),cv2.COLOR_RGB2BGR)
# cv2.imwrite("image1.png", myScreenshot)


startTime=time.time()
def takeScreenShot():
    number=random.randint(0,100)
    myScreenshot=pyautogui.screenshot()
    myScreenshot = cv2.cvtColor(np.array(myScreenshot),cv2.COLOR_RGB2BGR)
    result=True
    while(result):
        # ret,frame=myScreenshot.read()
        imageName="img"+str(number)+".png"
        cv2.imwrite(imageName,myScreenshot)
        startTime=time.time
        result=False
    return imageName
    print("ScreenShot taken")
    myScreenshot.release()
    cv2.destroyAllWindows()

def uploadFile(imageName):
    accessToken='yxo9223fN44AAAAAAAAAAWet25GZ_EodYFikHJdgc-8yrt6yaiAC0mAVDR4g5weU'
    file=imageName
    filefrom=file
    fileto="/newFolderSS/"+(imageName)
    dbx=dropbox.Dropbox(accessToken)
    with open(filefrom,'rb') as f:
        dbx.files_upload(f.read(),fileto,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while(True):
        if((time.time()-startTime)>=100):
            name=takeScreenShot()
            uploadFile(name)

main()

