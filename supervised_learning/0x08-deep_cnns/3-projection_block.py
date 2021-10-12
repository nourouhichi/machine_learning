#!/usr/bin/env python3
""" projection Block module"""
import tensorflow.keras as K


def projection_block(A_prev, filters, s=2):
    """ projection block """
    init = K.initializers.he_normal()
    c1 = K.layers.Conv2D(
                        filters[0],
                        (1, 1),
                        strides=s,
                        padding='same',
                        kernel_initializer=init)(A_prev)
    norm1 = K.layers.BatchNormalization()(c1)
    l1 = K.layers.Activation('relu')(norm1)
    c2 = K.layers.Conv2D(
                        filters[1],
                        (3, 3),
                        padding='same',
                        kernel_initializer=init)(l1)
    norm2 = K.layers.BatchNormalization()(c2)
    l2 = K.layers.Activation('relu')(norm2)
    c3 = K.layers.Conv2D(
                        filters[2],
                        (1, 1),
                        padding='same',
                        kernel_initializer=init)(l2)
    norm3 = K.layers.BatchNormalization()(c3)
    c4 = K.layers.Conv2D(
                        filters[2],
                        (1, 1),
                        strides=s,
                        padding='same',
                        kernel_initializer=init)(A_prev)
    norm4 = K.layers.BatchNormalization()(c4)
    output = K.layers.Add()([norm3, norm4])
    output = K.layers.Activation('relu')(output)
    return output
