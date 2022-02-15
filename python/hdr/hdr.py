from __future__ import print_function
from __future__ import division
import cv2 as cv
import numpy as np
import argparse
import os

def cargarExposiciones(path) :
    imagenes = []
    tiempos = []
    with open(os.path.join(path, 'list.txt')) as f :
        content = f.readlines()
    for linea in content :
        tokens = linea.split()
        imagenes.append(cv.imread(os.path.join(path, tokens[0])))
        tiempos.append(1 / float(tokens[1]))

    return imagenes, np.asarray(tiempos, dtype=np.float32)

parser = argparse.ArgumentParser(description="Imagenes con HDR")
parser.add_argument('--input', type=str, help="Dirección de la carpeta que contiene las imagenes y el archivo list.txt")
args = parser.parse_args()

if not args.input :
    parser.print_help()
    exit(0)

imagenes, tiempos = cargarExposiciones(args.input)

calibrar = cv.createCalibrateDebevec()
respuesta = calibrar.process(imagenes, tiempos)

merge_devec = cv.createMergeDebevec()
hdr = merge_devec.process(imagenes, tiempos, respuesta)

tono = cv.createTonemap(0.5)
ldr = tono.process(hdr)

merge_mertens = cv.createMergeMertens()
fusion = merge_mertens.process(imagenes)

cv.imwrite('fusion.png', fusion * 255)
cv.imwrite('ldr.png', ldr * 255)
cv.imwrite('hdr.hdr', hdr)
