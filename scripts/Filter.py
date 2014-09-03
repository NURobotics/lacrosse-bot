#!/usr/bin/env python

import cv2
import numpy as np


class Filter(object):
  
  def __init__(self):
    pass
  
  def filter(self, image):
    pass
  
  def __call__(self, image):
    return self.filter(image)


class ThresholdFilter(Filter):
  
  modes = ('RANGE', 'TARGET')
  
  def __init__(self, lower_bound=np.array([0, 0, 0], np.uint8), upper_bound=np.array([0, 0, 0], np.uint8),  target=np.array([0, 0, 0], np.uint8), mode='RANGE', tolerance=0.0):
    # Just a formality
    super(ThresholdFilter, self).__init__()
    if mode not in ThresholdFilter.modes:
      self.mode = 'RANGE'
    else:
      self.mode = mode
    self.lower_bound = lower_bound
    self.upper_bound = upper_bound      
    self.target = target
    self.tolerance = tolerance if tolerance >= 0.0 else 0.0
  
  def filter(self, image):
    if self.mode == 'RANGE':
      return cv2.inRange(image, self.lower_bound, self.upper_bound)
    elif self.mode == 'TARGET':
      pass

class KalmanFilter(Filter):
  
  def __init__(self):
    pass


if __name__ == '__main__':
  # ThresholdFilter Main Tests
  tf = ThresholdFilter()  
