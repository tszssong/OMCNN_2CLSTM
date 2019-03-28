import sys,os
import cv2
import numpy as np
saveDir = '/Users/momo/wkspace/salient/OMCNN_2CLSTM/omcnnResults/'
videoDir = '/Users/momo/wkspace/salient/OMCNN_2CLSTM/omcnnResults/'
videoName = 'findx2'
saveDir = saveDir + videoName + '/'
if not os.path.isdir(saveDir):
    os.makedirs(saveDir)
videoCap = cv2.VideoCapture(videoDir + videoName + '_out.avi')
success, im = videoCap.read()
numFrame = 0
while success:
    picname = videoName + '_s' + str(numFrame) + '.bmp'
    txtname = videoName + '_' + str(numFrame) + '.txt'
    cv2.imwrite(saveDir+picname, im)
    b,g,r = cv2.split(im)
    print im.shape, b.shape
    np.savetxt(saveDir+txtname, b, fmt="%d")
    numFrame += 1
    success, im = videoCap.read()
print "total frame:", numFrame
