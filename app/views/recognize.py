# -*- coding:utf-8 -*-
# Rec 车牌预测功能封装及测试

from . import HyperLPRLite as pr  # 引入LPR大类
import cv2
from PIL import ImageFont
import os

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'


class Rec():
    '''预测类，调用HyperLPR'''

    def __init__(self, mod_path='./app/static/recmod/'):  # 部署到服务器要改成绝对路径
        # 初始化，读取模型
        self.mod_path = mod_path
        self.fontC = ImageFont.truetype(
            mod_path + "font/platech.ttf", 14, 0)
        self.model = pr.LPR(mod_path + "model/cascade.xml", mod_path + "model/model12.h5",
                            mod_path + "model/ocr_plate_all_gru.h5")  # 输入之前训练好的目标检测，车牌边界左右回归，车牌文字检测模型

    def getPredict(self, img_path):
        '''获取预测车牌号'''
        cv_img = cv2.imread(img_path)
        os.remove(img_path)
        for pstr, confidence, rect in self.model.SimpleRecognizePlateByE2E(cv_img):
            if confidence > 0.7:  # 若置信度大于0.7，则识别结果可信(最大为1)
                return pstr, confidence
            else:
                return False


# 测试
if __name__ == '__main__':
    mod_path = '../static/recmod/'
    rec = Rec(mod_path=mod_path)
    img_path = '../static/image/demo.jpg'
    cid = rec.getPredict(img_path)
    print(cid)
