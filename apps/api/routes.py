import json
import math
import random
from datetime import datetime
from PIL import Image, ImageFilter
from apps.models.data import Data
from flask import jsonify, current_app
from apps.api import blueprint
import matplotlib.pyplot as plt
import os
from apps.config import Config
import numpy as np
import cv2
import matplotlib
from orangepi.pi3 import BOARD
import OPi.GPIO as GPIO
from time import sleep 

matplotlib.use('agg')
today = datetime.now()


@blueprint.route('/api/test')
def route_default():
    data = Data().find({})
    dt_string = today.strftime("%d-%m-%Y_%H-%M")
    img_1 = Image.open(
        Config.ASSETS_PATH + '/images/matahari4-min.jpg')

    fig_1, axes_1 = plt.subplots(nrows=1, ncols=1, figsize=(15, 15))
    axes_1.imshow(rgb2gray(img_1), cmap='gray')
    axes_1.axis('off')
    plt.savefig(Config.ASSETS_PATH + '/images/report-grayscale/' +
                dt_string + '.png', format='png', bbox_inches='tight', pad_inches=0)
    plt.cla()
    plt.clf()

    img_2 = Image.open(
        Config.ASSETS_PATH + '/images/report-grayscale/' +
        dt_string + '.png')
    blurred_image_1 = img_2.filter(ImageFilter.GaussianBlur(radius=15))
    plt_array_1 = np.asarray(blurred_image_1)
    img_grey = cv2.cvtColor(plt_array_1, cv2.COLOR_BGR2GRAY)
    thresh, threshed1 = cv2.threshold(
        img_grey, 250, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(
        threshed1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # print('contours', contours)
    # print('hierarchy', hierarchy)
    if contours and hierarchy is not None:
        # # img_countour = cv2.drawContours(plt_array_1, contours, -1, (0, 255, 0), 3)

        # # figContour, axesContour = plt.subplots(nrows=1, ncols=1, figsize=(15, 15))
        # # axesContour.imshow(img_countour)
        # # axesContour.axis('off')
        # # plt.savefig(Config.ASSETS_PATH + '/images/report-contour/' +
        # #             dt_string + '.png', format='png', bbox_inches='tight', pad_inches=0)
        # # plt.cla()
        # # plt.clf()

        # fig1, axes1 = plt.subplots(nrows=1, ncols=1, figsize=(15, 15))
        # axes1.imshow(threshed1)
        # axes1.axis('off')
        # plt.savefig(Config.ASSETS_PATH + '/images/report-threshed/' +
        #             dt_string + '.png', format='png', bbox_inches='tight', pad_inches=0)
        # plt.cla()
        # plt.clf()

        # img_8bit = Image.open(
        #     Config.ASSETS_PATH + '/images/report-threshed/' +
        #     dt_string + '.png')
        # img_8bit = img_8bit.convert('RGB').convert(
        #     'P', palette=Image.ADAPTIVE, colors=8)
        # img_8bit.save(Config.ASSETS_PATH + '/images/report-threshed/' +
        #               dt_string + '.png')

        # img_3 = Image.open(
        #     Config.ASSETS_PATH + '/images/report-threshed/' +
        #     dt_string + '.png')
        # image_data_3 = np.asarray(img_3)
        # edges = cv2.Canny(image_data_3, 0, 5)
        # plt.subplots(nrows=1, ncols=1, figsize=(15, 15))
        # plt.imshow(edges, cmap='gray')
        # plt.axis('off')
        # plt.savefig(Config.ASSETS_PATH + '/images/report-canny-edge/' +
        #             dt_string + '.png', format='png', bbox_inches='tight', pad_inches=0)
        # plt.cla()
        # plt.clf()

        # img_8bit = Image.open(
        #     Config.ASSETS_PATH + '/images/report-canny-edge/' +
        #     dt_string + '.png')
        # img_8bit = img_8bit.convert('RGB').convert(
        #     'P', palette=Image.ADAPTIVE, colors=8)
        # img_8bit.save(Config.ASSETS_PATH + '/images/report-canny-edge/' +
        #               dt_string + '.png')

        # img_4 = Image.open(
        #     Config.ASSETS_PATH + '/images/report-canny-edge/' +
        #     dt_string + '.png')
        # img_4 = img_4.convert('RGB')

        # image_data_4 = np.asarray(img_4)
        # cimg = cv2.cvtColor(image_data_4[:, :, 0], cv2.COLOR_GRAY2BGR)
        # gray_blurred = cv2.blur(cimg, (3, 3))
        # circles = cv2.HoughCircles(
        #     gray_blurred[:, :, 0], cv2.HOUGH_GRADIENT, 1, 20,
        #     param1=40,
        #     param2=25,
        #     minRadius=0,
        #     maxRadius=0)
        # circles = np.uint16(np.around(circles))

        # for idx, i in enumerate(circles[0, :]):
        #     print('idx->', idx)
        #     print('i->', i)
        #     if (idx == 0):
        #         # draw the outer circle
        #         cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
        #         # draw the center of the circle
        #         cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)
        #         break

        # plt.subplots(nrows=1, ncols=1, figsize=(15, 15))
        # plt.imshow(cimg)
        # plt.axis('off')
        # plt.savefig(Config.ASSETS_PATH + '/images/report-hough-circle-transform/' +
        #             dt_string + '.png', format='png', bbox_inches='tight', pad_inches=0)

        # # kernel1 = np.ones((5, 5), np.float32)/30
        # # img_filtered = cv2.filter2D(cimg, cv2.CV_8U, kernel=kernel1)
        # # moments = cv2.moments(img_filtered)
        # # print('moments', moments)

        # plt.cla()
        # plt.clf()
        # plt.close()

        img_4 = Image.open(
            Config.ASSETS_PATH + '/images/report-canny-edge/15-01-2023_18-37.png')
        img_4 = img_4.convert('RGB')

        image_data_4 = np.asarray(img_4)
        cimg = cv2.cvtColor(image_data_4[:, :, 0], cv2.COLOR_GRAY2BGR)
        gray_blurred = cv2.blur(cimg, (3, 3))
        circles = cv2.HoughCircles(
            gray_blurred[:, :, 0], cv2.HOUGH_GRADIENT, 1, 20,
            param1=40,
            param2=25,
            minRadius=0,
            maxRadius=0)
        circles = np.uint16(np.around(circles))

        x_circle = circles[0][0][0]
        y_circle = circles[0][0][1]

        img_5 = Image.open(
            Config.ASSETS_PATH + '/images/report-hough-circle-transform/15-01-2023_18-37.png')
        img_5 = img_5.convert('RGB')
        height, width = img_5.size
        x_center = (width/2)
        y_center = (height/2)
        c1 = (x_circle, y_circle)
        c2 = (x_center, y_center)
        d = calculate_diagonal(c1, c2)
        print('height', height)
        print('width', width)
        print('x_center', x_center)
        print('y_center', y_center)
        print('x_circle', x_circle)
        print('y_circle', y_circle)
        print('diagonal', d['diagonal'])
        print('x_dari_pusat', d['width'])
        print('y_dari_pusat', d['height'])
    else:
        os.remove(Config.ASSETS_PATH + '/images/report-grayscale/' +
                  dt_string + '.png')
        print("kosong isi nya")
        GPIO.setmode(BOARD)
    return jsonify({'result': data})


def rgb2gray(img):
    "Convert RGB image to grayscale."
    img = img.convert('RGB')
    img_array = np.asarray(img)
    return cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)


def rgb2rgb(img):
    "Convert RGB image to rgb."
    img = img.convert('RGB')
    img_array = np.asarray(img)
    return cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)


def calculate_diagonal(c1, c2):
    x1, y1 = c1
    x2, y2 = c2

    if x1 < x2:
        width = x2 - x1
    elif x1 == x2:
        width = 0
    else:
        width = x1 - x2

    if y1 < y2:
        height = y2 - y1
    elif y1 == y2:
        height = 0
    else:
        height = y1 - y2

    if height == 0:
        return width
    elif width == 0:
        return height

    diagonal = np.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

    data = {
        'width': width,
        'height': height,
        'diagonal': diagonal
    }

    return data
