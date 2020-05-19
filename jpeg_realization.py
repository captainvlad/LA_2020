import cv2
import numpy as np
import scipy.fftpack as fftpack
import zlib
prev_16 = lambda x: x >> 4 << 4


def encode_quant(orig, quant):
    return (orig / quant).astype(np.int)


def decode_quant(orig, quant):
    return (orig * quant).astype(float)


def encode_dct(orig, bx, by):
    new_shape = (
        orig.shape[0] // bx * bx,
        orig.shape[1] // by * by,
        3
    )
    new = orig[
        :new_shape[0],
        :new_shape[1]
    ].reshape((
        new_shape[0] // bx,
        bx,
        new_shape[1] // by,
        by,
        3
    ))
    return fftpack.dctn(new, axes=[1,3], norm='ortho')


def decode_dct(orig, bx, by):
    return fftpack.idctn(orig, axes=[1,3], norm='ortho'
    ).reshape((
        orig.shape[0]*bx,
        orig.shape[2]*by,
        3
    ))


def encode_zip(x):
    return zlib.compress(x.astype(np.int8).tobytes())


def decode_zip(orig, shape):
    return np.frombuffer(zlib.decompress(orig), dtype=np.int8).astype(float).reshape(shape)


def jpeg_algorithm(imagename):
    im = cv2.imread(imagename)
    quants = [1, 10]
    blocks = [(16,16)]
    for qscale in quants:
        for bx, by in blocks:

            quant = (
                (np.ones((bx, by)) * (qscale * qscale))
                .clip(-100, 100)  # to prevent clipping
                .reshape((1, bx, 1, by, 1))
            )
            enc = encode_dct(im, bx, by)
            encq = encode_quant(enc, quant)
            encz = encode_zip(encq)
            decz = decode_zip(encz, encq.shape)
            decq = decode_quant(encq, quant)
            dec = decode_dct(decq, bx, by)
            cv2.imwrite("changed_image.png", dec.astype(np.uint8))


# jpeg_algorithm("sample_5.jpg")