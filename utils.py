import requests
import time
import os
import sys
import tensorflow as tf

#function to make REST requests with status checking
def try_request(link, iter = 10):
    
    while iter > 0:
        resp = requests.get(link)
        if resp.status_code == 200:
            return resp
        time.sleep(1)
        iter -= 1
    sys.exit('Server not responding correctly')

#function to create windowed datasets
def windowed_dataset(series, window_size, batch_size, shuffle_buffer):
  dataset = tf.data.Dataset.from_tensor_slices(series)
  dataset = dataset.window(window_size + 1, shift=1, drop_remainder=True)
  dataset = dataset.flat_map(lambda window: window.batch(window_size + 1))
  dataset = dataset.shuffle(shuffle_buffer).map(lambda window: (window[:-1], window[-1][1]))
  dataset = dataset.batch(batch_size).prefetch(1)
  return dataset