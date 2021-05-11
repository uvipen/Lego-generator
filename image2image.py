"""
@author: Viet Nguyen <nhviet1009@gmail.com>
"""
import argparse
import cv2
import numpy as np
from math import ceil


def get_args():
    parser = argparse.ArgumentParser("Lego-generator")
    parser.add_argument("--input", type=str, default="data/input.jpg", help="Path to input image")
    parser.add_argument("--output", type=str, default="data/output.jpg", help="Path to output image")
    parser.add_argument("--stride", type=int, default=15, help="size of each lego brick")
    parser.add_argument("--overlay_ratio", type=float, default=0.2, help="Overlay width ratio")
    args = parser.parse_args()
    return args


def main(opt):
    lego_brick = cv2.imread("data/1x1.png", cv2.IMREAD_COLOR)
    lego_brick = cv2.resize(lego_brick, (opt.stride, opt.stride)).astype(np.int64)
    lego_brick[lego_brick < 33] = -100
    lego_brick[(33 <= lego_brick) & (lego_brick <= 233)] -= 133
    lego_brick[lego_brick > 233] = 100

    image = cv2.imread(opt.input, cv2.IMREAD_COLOR)
    nh, nw = ceil(image.shape[0] / opt.stride), ceil(image.shape[1] / opt.stride),
    image = cv2.resize(image, (nw*opt.stride, nh*opt.stride))
    height, width, num_channels = image.shape
    avg_colors = image.reshape(nh , opt.stride, nw, opt.stride, -1).swapaxes(1, 2).mean(axis=(2, 3))
    avg_colors = avg_colors.reshape(nh, nw, 1, 1, num_channels)
    lego_image = np.clip(avg_colors + lego_brick, 0, 255).astype(np.uint8)
    lego_image = lego_image.swapaxes(1, 2).reshape(*image.shape)
    # h,w,c -> nh,s,nw,s,c (reshape) -> nh,nw,s,s,c (swapaxes)
    # -> nh,nw,c (mean) -> nh,nw,1,1,c (reshape) 
    # -> nh,nw,s,s,c (broad-casting add with lego_brick)

    if opt.overlay_ratio:
        height, width, _ = lego_image.shape
        overlay = cv2.resize(image, (int(width * opt.overlay_ratio), int(height * opt.overlay_ratio)))
        lego_image[height - int(height * opt.overlay_ratio):, width - int(width * opt.overlay_ratio):, :] = overlay
    cv2.imwrite(opt.output, lego_image)


if __name__ == '__main__':
    opt = get_args()
    main(opt)
