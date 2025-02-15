# Mnist手写数字识别不同超参数的训练效果

[toc]

基于mnist手写数字识别

## 首先保持batch-size=100, lr=0.001

改变epoch分别为100, 300, 500

做三组实验看效果

### epoch=100, batch_size=100

```cmd
epoch=  1, train_loss=3.5159, train_acc=0.5327, val_loss=3.4972, val_acc=0.5368
epoch=  2, train_loss=1.5739, train_acc=0.6771, val_loss=1.5750, val_acc=0.6833
epoch=  3, train_loss=1.3046, train_acc=0.7158, val_loss=1.3286, val_acc=0.7181
epoch=  4, train_loss=1.1556, train_acc=0.7387, val_loss=1.1919, val_acc=0.7412
epoch=  5, train_loss=1.0565, train_acc=0.7556, val_loss=1.0998, val_acc=0.7539
epoch=  6, train_loss=0.9829, train_acc=0.7678, val_loss=1.0304, val_acc=0.7650
epoch=  7, train_loss=0.9250, train_acc=0.7767, val_loss=0.9760, val_acc=0.7742
epoch=  8, train_loss=0.8778, train_acc=0.7838, val_loss=0.9314, val_acc=0.7797
epoch=  9, train_loss=0.8387, train_acc=0.7896, val_loss=0.8942, val_acc=0.7863
epoch= 10, train_loss=0.8053, train_acc=0.7941, val_loss=0.8624, val_acc=0.7908
epoch= 11, train_loss=0.7765, train_acc=0.7990, val_loss=0.8350, val_acc=0.7952
epoch= 12, train_loss=0.7515, train_acc=0.8025, val_loss=0.8113, val_acc=0.7980
epoch= 13, train_loss=0.7291, train_acc=0.8056, val_loss=0.7903, val_acc=0.8011
epoch= 14, train_loss=0.7092, train_acc=0.8086, val_loss=0.7717, val_acc=0.8034
epoch= 15, train_loss=0.6912, train_acc=0.8114, val_loss=0.7547, val_acc=0.8041
epoch= 16, train_loss=0.6751, train_acc=0.8137, val_loss=0.7396, val_acc=0.8061
epoch= 17, train_loss=0.6604, train_acc=0.8162, val_loss=0.7258, val_acc=0.8088
epoch= 18, train_loss=0.6470, train_acc=0.8183, val_loss=0.7132, val_acc=0.8110
epoch= 19, train_loss=0.6344, train_acc=0.8199, val_loss=0.7015, val_acc=0.8123
epoch= 20, train_loss=0.6229, train_acc=0.8222, val_loss=0.6908, val_acc=0.8138
epoch= 21, train_loss=0.6124, train_acc=0.8238, val_loss=0.6812, val_acc=0.8148
epoch= 22, train_loss=0.6024, train_acc=0.8257, val_loss=0.6721, val_acc=0.8163
epoch= 23, train_loss=0.5931, train_acc=0.8275, val_loss=0.6635, val_acc=0.8180
epoch= 24, train_loss=0.5842, train_acc=0.8290, val_loss=0.6554, val_acc=0.8185
epoch= 25, train_loss=0.5760, train_acc=0.8305, val_loss=0.6479, val_acc=0.8191
epoch= 26, train_loss=0.5682, train_acc=0.8318, val_loss=0.6409, val_acc=0.8202
epoch= 27, train_loss=0.5611, train_acc=0.8327, val_loss=0.6345, val_acc=0.8212
epoch= 28, train_loss=0.5542, train_acc=0.8341, val_loss=0.6283, val_acc=0.8224
epoch= 29, train_loss=0.5480, train_acc=0.8350, val_loss=0.6228, val_acc=0.8229
epoch= 30, train_loss=0.5417, train_acc=0.8360, val_loss=0.6174, val_acc=0.8231
epoch= 31, train_loss=0.5359, train_acc=0.8370, val_loss=0.6122, val_acc=0.8242
epoch= 32, train_loss=0.5302, train_acc=0.8381, val_loss=0.6073, val_acc=0.8246
epoch= 33, train_loss=0.5249, train_acc=0.8386, val_loss=0.6027, val_acc=0.8254
epoch= 34, train_loss=0.5198, train_acc=0.8398, val_loss=0.5983, val_acc=0.8261
epoch= 35, train_loss=0.5149, train_acc=0.8403, val_loss=0.5941, val_acc=0.8262
epoch= 36, train_loss=0.5103, train_acc=0.8406, val_loss=0.5902, val_acc=0.8264
epoch= 37, train_loss=0.5058, train_acc=0.8416, val_loss=0.5864, val_acc=0.8268
epoch= 38, train_loss=0.5015, train_acc=0.8426, val_loss=0.5828, val_acc=0.8267
epoch= 39, train_loss=0.4974, train_acc=0.8433, val_loss=0.5794, val_acc=0.8273
epoch= 40, train_loss=0.4935, train_acc=0.8440, val_loss=0.5761, val_acc=0.8278
epoch= 41, train_loss=0.4898, train_acc=0.8446, val_loss=0.5730, val_acc=0.8284
epoch= 42, train_loss=0.4864, train_acc=0.8453, val_loss=0.5701, val_acc=0.8283
epoch= 43, train_loss=0.4829, train_acc=0.8462, val_loss=0.5672, val_acc=0.8294
epoch= 44, train_loss=0.4795, train_acc=0.8469, val_loss=0.5644, val_acc=0.8295
epoch= 45, train_loss=0.4763, train_acc=0.8476, val_loss=0.5617, val_acc=0.8299
epoch= 46, train_loss=0.4732, train_acc=0.8481, val_loss=0.5592, val_acc=0.8306
epoch= 47, train_loss=0.4701, train_acc=0.8487, val_loss=0.5567, val_acc=0.8313
epoch= 48, train_loss=0.4672, train_acc=0.8493, val_loss=0.5543, val_acc=0.8316
epoch= 49, train_loss=0.4644, train_acc=0.8500, val_loss=0.5520, val_acc=0.8317
epoch= 50, train_loss=0.4617, train_acc=0.8505, val_loss=0.5499, val_acc=0.8317
epoch= 51, train_loss=0.4591, train_acc=0.8512, val_loss=0.5477, val_acc=0.8322
epoch= 52, train_loss=0.4565, train_acc=0.8517, val_loss=0.5457, val_acc=0.8328
epoch= 53, train_loss=0.4540, train_acc=0.8521, val_loss=0.5438, val_acc=0.8330
epoch= 54, train_loss=0.4517, train_acc=0.8528, val_loss=0.5419, val_acc=0.8341
epoch= 55, train_loss=0.4493, train_acc=0.8533, val_loss=0.5400, val_acc=0.8346
epoch= 56, train_loss=0.4475, train_acc=0.8536, val_loss=0.5388, val_acc=0.8347
epoch= 57, train_loss=0.4453, train_acc=0.8541, val_loss=0.5371, val_acc=0.8354
epoch= 58, train_loss=0.4432, train_acc=0.8548, val_loss=0.5355, val_acc=0.8357
epoch= 59, train_loss=0.4411, train_acc=0.8551, val_loss=0.5339, val_acc=0.8363
epoch= 60, train_loss=0.4391, train_acc=0.8553, val_loss=0.5323, val_acc=0.8364
epoch= 61, train_loss=0.4371, train_acc=0.8557, val_loss=0.5308, val_acc=0.8370
epoch= 62, train_loss=0.4352, train_acc=0.8559, val_loss=0.5293, val_acc=0.8373
epoch= 63, train_loss=0.4332, train_acc=0.8565, val_loss=0.5279, val_acc=0.8373
epoch= 64, train_loss=0.4314, train_acc=0.8567, val_loss=0.5265, val_acc=0.8381
epoch= 65, train_loss=0.4296, train_acc=0.8570, val_loss=0.5252, val_acc=0.8383
epoch= 66, train_loss=0.4279, train_acc=0.8574, val_loss=0.5239, val_acc=0.8382
epoch= 67, train_loss=0.4262, train_acc=0.8580, val_loss=0.5226, val_acc=0.8385
epoch= 68, train_loss=0.4248, train_acc=0.8581, val_loss=0.5215, val_acc=0.8388
epoch= 69, train_loss=0.4232, train_acc=0.8586, val_loss=0.5203, val_acc=0.8395
epoch= 70, train_loss=0.4216, train_acc=0.8590, val_loss=0.5191, val_acc=0.8397
epoch= 71, train_loss=0.4201, train_acc=0.8594, val_loss=0.5180, val_acc=0.8402
epoch= 72, train_loss=0.4186, train_acc=0.8600, val_loss=0.5169, val_acc=0.8404
^CTraceback (most recent call last):
  File "/home/slx/lc/fashion_minist_cls.py", line 90, in <module>
    grads = grad(xs, ys, W, B)
  File "/home/slx/lc/fashion_minist_cls.py", line 60, in grad
    return tape.gradient(loss_, [w, b])
  File "/home/slx/anaconda3/lib/python3.9/site-packages/tensorflow/python/eager/backprop.py", line 1113, in gradient
epoch= 82, train_loss=0.4117, train_acc=0.8609, val_loss=0.5088, val_acc=0.8359
epoch= 83, train_loss=0.4105, train_acc=0.8613, val_loss=0.5079, val_acc=0.8366
epoch= 84, train_loss=0.4093, train_acc=0.8614, val_loss=0.5070, val_acc=0.8365
epoch= 85, train_loss=0.4082, train_acc=0.8618, val_loss=0.5062, val_acc=0.8367
epoch= 86, train_loss=0.4070, train_acc=0.8621, val_loss=0.5053, val_acc=0.8368
epoch= 87, train_loss=0.4059, train_acc=0.8622, val_loss=0.5045, val_acc=0.8370
epoch= 88, train_loss=0.4048, train_acc=0.8626, val_loss=0.5037, val_acc=0.8372
epoch= 89, train_loss=0.4038, train_acc=0.8627, val_loss=0.5029, val_acc=0.8372
epoch= 90, train_loss=0.4027, train_acc=0.8629, val_loss=0.5021, val_acc=0.8372
epoch= 91, train_loss=0.4017, train_acc=0.8631, val_loss=0.5014, val_acc=0.8372
epoch= 92, train_loss=0.4006, train_acc=0.8634, val_loss=0.5009, val_acc=0.8377
epoch= 93, train_loss=0.3996, train_acc=0.8636, val_loss=0.5002, val_acc=0.8379
epoch= 94, train_loss=0.3986, train_acc=0.8639, val_loss=0.4995, val_acc=0.8377
epoch= 95, train_loss=0.3977, train_acc=0.8640, val_loss=0.4988, val_acc=0.8374
epoch= 96, train_loss=0.3967, train_acc=0.8643, val_loss=0.4982, val_acc=0.8375
epoch= 97, train_loss=0.3958, train_acc=0.8645, val_loss=0.4976, val_acc=0.8376
epoch= 98, train_loss=0.3949, train_acc=0.8648, val_loss=0.4970, val_acc=0.8378
epoch= 99, train_loss=0.3940, train_acc=0.8650, val_loss=0.4964, val_acc=0.8378
epoch=100, train_loss=0.3931, train_acc=0.8654, val_loss=0.4958, val_acc=0.8378
test accuracy: 0.8306
```

### epoch=300, batch_size=100

其实这个可以看出来在二百二三十步的时候就已经收敛了

```cmd
epoch=  1, train_loss=3.5159, train_acc=0.5327, val_loss=3.4972, val_acc=0.5368
epoch=  2, train_loss=1.5739, train_acc=0.6771, val_loss=1.5750, val_acc=0.6833
epoch=  3, train_loss=1.3046, train_acc=0.7158, val_loss=1.3286, val_acc=0.7181
epoch=  4, train_loss=1.1556, train_acc=0.7387, val_loss=1.1919, val_acc=0.7412
epoch=  5, train_loss=1.0565, train_acc=0.7556, val_loss=1.0998, val_acc=0.7539
epoch=  6, train_loss=0.9829, train_acc=0.7678, val_loss=1.0304, val_acc=0.7650
epoch=  7, train_loss=0.9250, train_acc=0.7767, val_loss=0.9760, val_acc=0.7742
epoch=  8, train_loss=0.8778, train_acc=0.7838, val_loss=0.9314, val_acc=0.7797
epoch=  9, train_loss=0.8387, train_acc=0.7896, val_loss=0.8942, val_acc=0.7863
epoch= 10, train_loss=0.8053, train_acc=0.7941, val_loss=0.8624, val_acc=0.7908
epoch= 11, train_loss=0.7765, train_acc=0.7990, val_loss=0.8350, val_acc=0.7952
epoch= 12, train_loss=0.7515, train_acc=0.8025, val_loss=0.8113, val_acc=0.7980
epoch= 13, train_loss=0.7291, train_acc=0.8056, val_loss=0.7903, val_acc=0.8011
epoch= 14, train_loss=0.7092, train_acc=0.8086, val_loss=0.7717, val_acc=0.8034
epoch= 15, train_loss=0.6912, train_acc=0.8114, val_loss=0.7547, val_acc=0.8041
epoch= 16, train_loss=0.6751, train_acc=0.8137, val_loss=0.7396, val_acc=0.8061
epoch= 17, train_loss=0.6604, train_acc=0.8162, val_loss=0.7258, val_acc=0.8088
epoch= 18, train_loss=0.6470, train_acc=0.8183, val_loss=0.7132, val_acc=0.8110
epoch= 19, train_loss=0.6344, train_acc=0.8199, val_loss=0.7015, val_acc=0.8123
epoch= 20, train_loss=0.6229, train_acc=0.8222, val_loss=0.6908, val_acc=0.8138
epoch= 21, train_loss=0.6124, train_acc=0.8238, val_loss=0.6812, val_acc=0.8148
epoch= 22, train_loss=0.6024, train_acc=0.8257, val_loss=0.6721, val_acc=0.8163
epoch= 23, train_loss=0.5931, train_acc=0.8275, val_loss=0.6635, val_acc=0.8180
epoch= 24, train_loss=0.5842, train_acc=0.8290, val_loss=0.6554, val_acc=0.8185
epoch= 25, train_loss=0.5760, train_acc=0.8305, val_loss=0.6479, val_acc=0.8191
epoch= 26, train_loss=0.5682, train_acc=0.8318, val_loss=0.6409, val_acc=0.8202
epoch= 27, train_loss=0.5611, train_acc=0.8327, val_loss=0.6345, val_acc=0.8212
epoch= 28, train_loss=0.5542, train_acc=0.8341, val_loss=0.6283, val_acc=0.8224
epoch= 29, train_loss=0.5480, train_acc=0.8350, val_loss=0.6228, val_acc=0.8229
epoch= 30, train_loss=0.5417, train_acc=0.8360, val_loss=0.6174, val_acc=0.8231
epoch= 31, train_loss=0.5359, train_acc=0.8370, val_loss=0.6122, val_acc=0.8242
epoch= 32, train_loss=0.5302, train_acc=0.8381, val_loss=0.6073, val_acc=0.8246
epoch= 33, train_loss=0.5249, train_acc=0.8386, val_loss=0.6027, val_acc=0.8254
epoch= 34, train_loss=0.5198, train_acc=0.8398, val_loss=0.5983, val_acc=0.8261
epoch= 35, train_loss=0.5149, train_acc=0.8403, val_loss=0.5941, val_acc=0.8262
epoch= 36, train_loss=0.5103, train_acc=0.8406, val_loss=0.5902, val_acc=0.8264
epoch= 37, train_loss=0.5058, train_acc=0.8416, val_loss=0.5864, val_acc=0.8268
epoch= 38, train_loss=0.5015, train_acc=0.8426, val_loss=0.5828, val_acc=0.8267
epoch= 39, train_loss=0.4974, train_acc=0.8433, val_loss=0.5794, val_acc=0.8273
epoch= 40, train_loss=0.4935, train_acc=0.8440, val_loss=0.5761, val_acc=0.8278
epoch= 41, train_loss=0.4898, train_acc=0.8446, val_loss=0.5730, val_acc=0.8284
epoch= 42, train_loss=0.4864, train_acc=0.8453, val_loss=0.5701, val_acc=0.8283
epoch= 43, train_loss=0.4829, train_acc=0.8462, val_loss=0.5672, val_acc=0.8294
epoch= 44, train_loss=0.4795, train_acc=0.8469, val_loss=0.5644, val_acc=0.8295
epoch= 45, train_loss=0.4763, train_acc=0.8476, val_loss=0.5617, val_acc=0.8299
epoch= 46, train_loss=0.4732, train_acc=0.8481, val_loss=0.5592, val_acc=0.8306
epoch= 47, train_loss=0.4701, train_acc=0.8487, val_loss=0.5567, val_acc=0.8313
epoch= 48, train_loss=0.4672, train_acc=0.8493, val_loss=0.5543, val_acc=0.8316
epoch= 49, train_loss=0.4644, train_acc=0.8500, val_loss=0.5520, val_acc=0.8317
epoch= 50, train_loss=0.4617, train_acc=0.8505, val_loss=0.5499, val_acc=0.8317
epoch= 51, train_loss=0.4591, train_acc=0.8512, val_loss=0.5477, val_acc=0.8322
epoch= 52, train_loss=0.4565, train_acc=0.8517, val_loss=0.5457, val_acc=0.8328
epoch= 53, train_loss=0.4540, train_acc=0.8521, val_loss=0.5438, val_acc=0.8330
epoch= 54, train_loss=0.4517, train_acc=0.8528, val_loss=0.5419, val_acc=0.8341
epoch= 55, train_loss=0.4493, train_acc=0.8533, val_loss=0.5400, val_acc=0.8346
epoch= 56, train_loss=0.4475, train_acc=0.8536, val_loss=0.5388, val_acc=0.8347
epoch= 57, train_loss=0.4453, train_acc=0.8541, val_loss=0.5371, val_acc=0.8354
epoch= 58, train_loss=0.4432, train_acc=0.8548, val_loss=0.5355, val_acc=0.8357
epoch= 59, train_loss=0.4411, train_acc=0.8551, val_loss=0.5339, val_acc=0.8363
epoch= 60, train_loss=0.4391, train_acc=0.8553, val_loss=0.5323, val_acc=0.8364
epoch= 61, train_loss=0.4371, train_acc=0.8557, val_loss=0.5308, val_acc=0.8370
epoch= 62, train_loss=0.4352, train_acc=0.8559, val_loss=0.5293, val_acc=0.8373
epoch= 63, train_loss=0.4332, train_acc=0.8565, val_loss=0.5279, val_acc=0.8373
epoch= 64, train_loss=0.4314, train_acc=0.8567, val_loss=0.5265, val_acc=0.8381
epoch= 65, train_loss=0.4296, train_acc=0.8570, val_loss=0.5252, val_acc=0.8383
epoch= 66, train_loss=0.4279, train_acc=0.8574, val_loss=0.5239, val_acc=0.8382
epoch= 67, train_loss=0.4262, train_acc=0.8580, val_loss=0.5226, val_acc=0.8385
epoch= 68, train_loss=0.4248, train_acc=0.8581, val_loss=0.5215, val_acc=0.8388
epoch= 69, train_loss=0.4232, train_acc=0.8586, val_loss=0.5203, val_acc=0.8395
epoch= 70, train_loss=0.4216, train_acc=0.8590, val_loss=0.5191, val_acc=0.8397
epoch= 71, train_loss=0.4201, train_acc=0.8594, val_loss=0.5180, val_acc=0.8402
epoch= 72, train_loss=0.4186, train_acc=0.8600, val_loss=0.5169, val_acc=0.8404
^CTraceback (most recent call last):
  File "/home/slx/lc/fashion_minist_cls.py", line 90, in <module>
    grads = grad(xs, ys, W, B)
  File "/home/slx/lc/fashion_minist_cls.py", line 60, in grad
    return tape.gradient(loss_, [w, b])
  File "/home/slx/anaconda3/lib/python3.9/site-packages/tensorflow/python/eager/backprop.py", line 1113, in gradient
epoch=232, train_loss=0.3421, train_acc=0.8797, val_loss=0.4696, val_acc=0.8445
epoch=233, train_loss=0.3419, train_acc=0.8797, val_loss=0.4696, val_acc=0.8446
epoch=234, train_loss=0.3417, train_acc=0.8797, val_loss=0.4696, val_acc=0.8447
epoch=235, train_loss=0.3416, train_acc=0.8797, val_loss=0.4697, val_acc=0.8446
epoch=236, train_loss=0.3414, train_acc=0.8797, val_loss=0.4697, val_acc=0.8446
epoch=237, train_loss=0.3413, train_acc=0.8797, val_loss=0.4697, val_acc=0.8443
epoch=238, train_loss=0.3411, train_acc=0.8797, val_loss=0.4697, val_acc=0.8443
epoch=239, train_loss=0.3410, train_acc=0.8798, val_loss=0.4697, val_acc=0.8444
epoch=240, train_loss=0.3408, train_acc=0.8798, val_loss=0.4698, val_acc=0.8443
epoch=241, train_loss=0.3407, train_acc=0.8798, val_loss=0.4698, val_acc=0.8443
epoch=242, train_loss=0.3406, train_acc=0.8798, val_loss=0.4698, val_acc=0.8445
epoch=243, train_loss=0.3404, train_acc=0.8799, val_loss=0.4698, val_acc=0.8446
epoch=244, train_loss=0.3403, train_acc=0.8800, val_loss=0.4698, val_acc=0.8447
epoch=245, train_loss=0.3401, train_acc=0.8800, val_loss=0.4699, val_acc=0.8447
epoch=246, train_loss=0.3400, train_acc=0.8799, val_loss=0.4699, val_acc=0.8447
epoch=247, train_loss=0.3398, train_acc=0.8800, val_loss=0.4699, val_acc=0.8448
epoch=248, train_loss=0.3397, train_acc=0.8800, val_loss=0.4700, val_acc=0.8449
epoch=249, train_loss=0.3396, train_acc=0.8800, val_loss=0.4700, val_acc=0.8450
epoch=250, train_loss=0.3394, train_acc=0.8800, val_loss=0.4700, val_acc=0.8450
epoch=251, train_loss=0.3393, train_acc=0.8801, val_loss=0.4700, val_acc=0.8450
epoch=252, train_loss=0.3392, train_acc=0.8801, val_loss=0.4701, val_acc=0.8449
epoch=253, train_loss=0.3390, train_acc=0.8802, val_loss=0.4701, val_acc=0.8448
epoch=254, train_loss=0.3389, train_acc=0.8802, val_loss=0.4701, val_acc=0.8448
epoch=255, train_loss=0.3388, train_acc=0.8802, val_loss=0.4702, val_acc=0.8449
epoch=256, train_loss=0.3386, train_acc=0.8803, val_loss=0.4702, val_acc=0.8449
epoch=257, train_loss=0.3385, train_acc=0.8804, val_loss=0.4702, val_acc=0.8448
epoch=258, train_loss=0.3384, train_acc=0.8804, val_loss=0.4703, val_acc=0.8448
epoch=259, train_loss=0.3383, train_acc=0.8804, val_loss=0.4703, val_acc=0.8448
epoch=260, train_loss=0.3381, train_acc=0.8804, val_loss=0.4703, val_acc=0.8447
epoch=261, train_loss=0.3380, train_acc=0.8805, val_loss=0.4704, val_acc=0.8447
epoch=262, train_loss=0.3379, train_acc=0.8805, val_loss=0.4704, val_acc=0.8447
epoch=263, train_loss=0.3378, train_acc=0.8805, val_loss=0.4704, val_acc=0.8448
epoch=264, train_loss=0.3376, train_acc=0.8805, val_loss=0.4705, val_acc=0.8449
epoch=265, train_loss=0.3375, train_acc=0.8805, val_loss=0.4705, val_acc=0.8448
```

两个实验共同的epoch=500, batch_size=100

```cmd
epoch=  1, train_loss=3.5159, train_acc=0.5327, val_loss=3.4972, val_acc=0.5368
epoch=  2, train_loss=1.5739, train_acc=0.6771, val_loss=1.5750, val_acc=0.6833
epoch=  3, train_loss=1.3046, train_acc=0.7158, val_loss=1.3286, val_acc=0.7181
epoch=  4, train_loss=1.1556, train_acc=0.7387, val_loss=1.1919, val_acc=0.7412
epoch=  5, train_loss=1.0565, train_acc=0.7556, val_loss=1.0998, val_acc=0.7539
epoch=  6, train_loss=0.9829, train_acc=0.7678, val_loss=1.0304, val_acc=0.7650
epoch=  7, train_loss=0.9250, train_acc=0.7767, val_loss=0.9760, val_acc=0.7742
epoch=  8, train_loss=0.8778, train_acc=0.7838, val_loss=0.9314, val_acc=0.7797
epoch=  9, train_loss=0.8387, train_acc=0.7896, val_loss=0.8942, val_acc=0.7863
epoch= 10, train_loss=0.8053, train_acc=0.7941, val_loss=0.8624, val_acc=0.7908
epoch= 11, train_loss=0.7765, train_acc=0.7990, val_loss=0.8350, val_acc=0.7952
epoch= 12, train_loss=0.7515, train_acc=0.8025, val_loss=0.8113, val_acc=0.7980
epoch= 13, train_loss=0.7291, train_acc=0.8056, val_loss=0.7903, val_acc=0.8011
epoch= 14, train_loss=0.7092, train_acc=0.8086, val_loss=0.7717, val_acc=0.8034
epoch= 15, train_loss=0.6912, train_acc=0.8114, val_loss=0.7547, val_acc=0.8041
epoch= 16, train_loss=0.6751, train_acc=0.8137, val_loss=0.7396, val_acc=0.8061
epoch= 17, train_loss=0.6604, train_acc=0.8162, val_loss=0.7258, val_acc=0.8088
epoch= 18, train_loss=0.6470, train_acc=0.8183, val_loss=0.7132, val_acc=0.8110
epoch= 19, train_loss=0.6344, train_acc=0.8199, val_loss=0.7015, val_acc=0.8123
epoch= 20, train_loss=0.6229, train_acc=0.8222, val_loss=0.6908, val_acc=0.8138
epoch= 21, train_loss=0.6124, train_acc=0.8238, val_loss=0.6812, val_acc=0.8148
epoch= 22, train_loss=0.6024, train_acc=0.8257, val_loss=0.6721, val_acc=0.8163
epoch= 23, train_loss=0.5931, train_acc=0.8275, val_loss=0.6635, val_acc=0.8180
epoch= 24, train_loss=0.5842, train_acc=0.8290, val_loss=0.6554, val_acc=0.8185
epoch= 25, train_loss=0.5760, train_acc=0.8305, val_loss=0.6479, val_acc=0.8191
epoch= 26, train_loss=0.5682, train_acc=0.8318, val_loss=0.6409, val_acc=0.8202
epoch= 27, train_loss=0.5611, train_acc=0.8327, val_loss=0.6345, val_acc=0.8212
epoch= 28, train_loss=0.5542, train_acc=0.8341, val_loss=0.6283, val_acc=0.8224
epoch= 29, train_loss=0.5480, train_acc=0.8350, val_loss=0.6228, val_acc=0.8229
epoch= 30, train_loss=0.5417, train_acc=0.8360, val_loss=0.6174, val_acc=0.8231
epoch= 31, train_loss=0.5359, train_acc=0.8370, val_loss=0.6122, val_acc=0.8242
epoch= 32, train_loss=0.5302, train_acc=0.8381, val_loss=0.6073, val_acc=0.8246
epoch= 33, train_loss=0.5249, train_acc=0.8386, val_loss=0.6027, val_acc=0.8254
epoch= 34, train_loss=0.5198, train_acc=0.8398, val_loss=0.5983, val_acc=0.8261
epoch= 35, train_loss=0.5149, train_acc=0.8403, val_loss=0.5941, val_acc=0.8262
epoch= 36, train_loss=0.5103, train_acc=0.8406, val_loss=0.5902, val_acc=0.8264
epoch= 37, train_loss=0.5058, train_acc=0.8416, val_loss=0.5864, val_acc=0.8268
epoch= 38, train_loss=0.5015, train_acc=0.8426, val_loss=0.5828, val_acc=0.8267
epoch= 39, train_loss=0.4974, train_acc=0.8433, val_loss=0.5794, val_acc=0.8273
epoch= 40, train_loss=0.4935, train_acc=0.8440, val_loss=0.5761, val_acc=0.8278
epoch= 41, train_loss=0.4898, train_acc=0.8446, val_loss=0.5730, val_acc=0.8284
epoch= 42, train_loss=0.4864, train_acc=0.8453, val_loss=0.5701, val_acc=0.8283
epoch= 43, train_loss=0.4829, train_acc=0.8462, val_loss=0.5672, val_acc=0.8294
epoch= 44, train_loss=0.4795, train_acc=0.8469, val_loss=0.5644, val_acc=0.8295
epoch= 45, train_loss=0.4763, train_acc=0.8476, val_loss=0.5617, val_acc=0.8299
epoch= 46, train_loss=0.4732, train_acc=0.8481, val_loss=0.5592, val_acc=0.8306
epoch= 47, train_loss=0.4701, train_acc=0.8487, val_loss=0.5567, val_acc=0.8313
epoch= 48, train_loss=0.4672, train_acc=0.8493, val_loss=0.5543, val_acc=0.8316
epoch= 49, train_loss=0.4644, train_acc=0.8500, val_loss=0.5520, val_acc=0.8317
epoch= 50, train_loss=0.4617, train_acc=0.8505, val_loss=0.5499, val_acc=0.8317
epoch= 51, train_loss=0.4591, train_acc=0.8512, val_loss=0.5477, val_acc=0.8322
epoch= 52, train_loss=0.4565, train_acc=0.8517, val_loss=0.5457, val_acc=0.8328
epoch= 53, train_loss=0.4540, train_acc=0.8521, val_loss=0.5438, val_acc=0.8330
epoch= 54, train_loss=0.4517, train_acc=0.8528, val_loss=0.5419, val_acc=0.8341
epoch= 55, train_loss=0.4493, train_acc=0.8533, val_loss=0.5400, val_acc=0.8346
epoch= 56, train_loss=0.4475, train_acc=0.8536, val_loss=0.5388, val_acc=0.8347
epoch= 57, train_loss=0.4453, train_acc=0.8541, val_loss=0.5371, val_acc=0.8354
epoch= 58, train_loss=0.4432, train_acc=0.8548, val_loss=0.5355, val_acc=0.8357
epoch= 59, train_loss=0.4411, train_acc=0.8551, val_loss=0.5339, val_acc=0.8363
epoch= 60, train_loss=0.4391, train_acc=0.8553, val_loss=0.5323, val_acc=0.8364
epoch= 61, train_loss=0.4371, train_acc=0.8557, val_loss=0.5308, val_acc=0.8370
epoch= 62, train_loss=0.4352, train_acc=0.8559, val_loss=0.5293, val_acc=0.8373
epoch= 63, train_loss=0.4332, train_acc=0.8565, val_loss=0.5279, val_acc=0.8373
epoch= 64, train_loss=0.4314, train_acc=0.8567, val_loss=0.5265, val_acc=0.8381
epoch= 65, train_loss=0.4296, train_acc=0.8570, val_loss=0.5252, val_acc=0.8383
epoch= 66, train_loss=0.4279, train_acc=0.8574, val_loss=0.5239, val_acc=0.8382
epoch= 67, train_loss=0.4262, train_acc=0.8580, val_loss=0.5226, val_acc=0.8385
epoch= 68, train_loss=0.4248, train_acc=0.8581, val_loss=0.5215, val_acc=0.8388
epoch= 69, train_loss=0.4232, train_acc=0.8586, val_loss=0.5203, val_acc=0.8395
epoch= 70, train_loss=0.4216, train_acc=0.8590, val_loss=0.5191, val_acc=0.8397
epoch= 71, train_loss=0.4201, train_acc=0.8594, val_loss=0.5180, val_acc=0.8402
epoch= 72, train_loss=0.4186, train_acc=0.8600, val_loss=0.5169, val_acc=0.8404
^CTraceback (most recent call last):
  File "/home/slx/lc/fashion_minist_cls.py", line 90, in <module>
    grads = grad(xs, ys, W, B)
  File "/home/slx/lc/fashion_minist_cls.py", line 60, in grad
    return tape.gradient(loss_, [w, b])
  File "/home/slx/anaconda3/lib/python3.9/site-packages/tensorflow/python/eager/backprop.py", line 1113, in gradient
epoch=482, train_loss=0.3221, train_acc=0.8851, val_loss=0.4888, val_acc=0.8441
epoch=483, train_loss=0.3220, train_acc=0.8851, val_loss=0.4889, val_acc=0.8441
epoch=484, train_loss=0.3220, train_acc=0.8851, val_loss=0.4890, val_acc=0.8441
epoch=485, train_loss=0.3220, train_acc=0.8851, val_loss=0.4890, val_acc=0.8439
epoch=486, train_loss=0.3220, train_acc=0.8851, val_loss=0.4891, val_acc=0.8440
epoch=487, train_loss=0.3219, train_acc=0.8852, val_loss=0.4892, val_acc=0.8439
epoch=488, train_loss=0.3219, train_acc=0.8852, val_loss=0.4892, val_acc=0.8438
epoch=489, train_loss=0.3219, train_acc=0.8853, val_loss=0.4893, val_acc=0.8438
epoch=490, train_loss=0.3218, train_acc=0.8853, val_loss=0.4894, val_acc=0.8438
epoch=491, train_loss=0.3218, train_acc=0.8853, val_loss=0.4894, val_acc=0.8438
epoch=492, train_loss=0.3218, train_acc=0.8853, val_loss=0.4895, val_acc=0.8439
epoch=493, train_loss=0.3217, train_acc=0.8853, val_loss=0.4896, val_acc=0.8439
epoch=494, train_loss=0.3217, train_acc=0.8853, val_loss=0.4897, val_acc=0.8439
epoch=495, train_loss=0.3217, train_acc=0.8853, val_loss=0.4897, val_acc=0.8439
epoch=496, train_loss=0.3216, train_acc=0.8853, val_loss=0.4898, val_acc=0.8439
epoch=497, train_loss=0.3216, train_acc=0.8853, val_loss=0.4899, val_acc=0.8439
epoch=498, train_loss=0.3216, train_acc=0.8853, val_loss=0.4899, val_acc=0.8438
epoch=499, train_loss=0.3215, train_acc=0.8853, val_loss=0.4900, val_acc=0.8438
epoch=500, train_loss=0.3215, train_acc=0.8854, val_loss=0.4901, val_acc=0.8438
test accuracy: 0.8333
```



## 然后保持epoch=500, lr=0.001

改变batch_size分别为100, 300, 500

做三组实验看效果

这里面跟上面实验有一个组实验重合了, 即epoch=500, batch_size=100

### epoch=500, batch_size=300

```cmd
epoch=  1, train_loss=3.5159, train_acc=0.5327, val_loss=3.4972, val_acc=0.5368
epoch=  2, train_loss=1.5739, train_acc=0.6771, val_loss=1.5750, val_acc=0.6833
epoch=  3, train_loss=1.3046, train_acc=0.7158, val_loss=1.3286, val_acc=0.7181
epoch=  4, train_loss=1.1556, train_acc=0.7387, val_loss=1.1919, val_acc=0.7412
epoch=  5, train_loss=1.0565, train_acc=0.7556, val_loss=1.0998, val_acc=0.7539
epoch=  6, train_loss=0.9829, train_acc=0.7678, val_loss=1.0304, val_acc=0.7650
epoch=  7, train_loss=0.9250, train_acc=0.7767, val_loss=0.9760, val_acc=0.7742
epoch=  8, train_loss=0.8778, train_acc=0.7838, val_loss=0.9314, val_acc=0.7797
epoch=  9, train_loss=0.8387, train_acc=0.7896, val_loss=0.8942, val_acc=0.7863
epoch= 10, train_loss=0.8053, train_acc=0.7941, val_loss=0.8624, val_acc=0.7908
epoch= 11, train_loss=0.7765, train_acc=0.7990, val_loss=0.8350, val_acc=0.7952
epoch= 12, train_loss=0.7515, train_acc=0.8025, val_loss=0.8113, val_acc=0.7980
epoch= 13, train_loss=0.7291, train_acc=0.8056, val_loss=0.7903, val_acc=0.8011
epoch= 14, train_loss=0.7092, train_acc=0.8086, val_loss=0.7717, val_acc=0.8034
epoch= 15, train_loss=0.6912, train_acc=0.8114, val_loss=0.7547, val_acc=0.8041
epoch= 16, train_loss=0.6751, train_acc=0.8137, val_loss=0.7396, val_acc=0.8061
epoch= 17, train_loss=0.6604, train_acc=0.8162, val_loss=0.7258, val_acc=0.8088
epoch= 18, train_loss=0.6470, train_acc=0.8183, val_loss=0.7132, val_acc=0.8110
epoch= 19, train_loss=0.6344, train_acc=0.8199, val_loss=0.7015, val_acc=0.8123
epoch= 20, train_loss=0.6229, train_acc=0.8222, val_loss=0.6908, val_acc=0.8138
epoch= 21, train_loss=0.6124, train_acc=0.8238, val_loss=0.6812, val_acc=0.8148
epoch= 22, train_loss=0.6024, train_acc=0.8257, val_loss=0.6721, val_acc=0.8163
epoch= 23, train_loss=0.5931, train_acc=0.8275, val_loss=0.6635, val_acc=0.8180
epoch= 24, train_loss=0.5842, train_acc=0.8290, val_loss=0.6554, val_acc=0.8185
epoch= 25, train_loss=0.5760, train_acc=0.8305, val_loss=0.6479, val_acc=0.8191
epoch= 26, train_loss=0.5682, train_acc=0.8318, val_loss=0.6409, val_acc=0.8202
epoch= 27, train_loss=0.5611, train_acc=0.8327, val_loss=0.6345, val_acc=0.8212
epoch= 28, train_loss=0.5542, train_acc=0.8341, val_loss=0.6283, val_acc=0.8224
epoch= 29, train_loss=0.5480, train_acc=0.8350, val_loss=0.6228, val_acc=0.8229
epoch= 30, train_loss=0.5417, train_acc=0.8360, val_loss=0.6174, val_acc=0.8231
epoch= 31, train_loss=0.5359, train_acc=0.8370, val_loss=0.6122, val_acc=0.8242
epoch= 32, train_loss=0.5302, train_acc=0.8381, val_loss=0.6073, val_acc=0.8246
epoch= 33, train_loss=0.5249, train_acc=0.8386, val_loss=0.6027, val_acc=0.8254
epoch= 34, train_loss=0.5198, train_acc=0.8398, val_loss=0.5983, val_acc=0.8261
epoch= 35, train_loss=0.5149, train_acc=0.8403, val_loss=0.5941, val_acc=0.8262
epoch= 36, train_loss=0.5103, train_acc=0.8406, val_loss=0.5902, val_acc=0.8264
epoch= 37, train_loss=0.5058, train_acc=0.8416, val_loss=0.5864, val_acc=0.8268
epoch= 38, train_loss=0.5015, train_acc=0.8426, val_loss=0.5828, val_acc=0.8267
epoch= 39, train_loss=0.4974, train_acc=0.8433, val_loss=0.5794, val_acc=0.8273
epoch= 40, train_loss=0.4935, train_acc=0.8440, val_loss=0.5761, val_acc=0.8278
epoch= 41, train_loss=0.4898, train_acc=0.8446, val_loss=0.5730, val_acc=0.8284
epoch= 42, train_loss=0.4864, train_acc=0.8453, val_loss=0.5701, val_acc=0.8283
epoch= 43, train_loss=0.4829, train_acc=0.8462, val_loss=0.5672, val_acc=0.8294
epoch= 44, train_loss=0.4795, train_acc=0.8469, val_loss=0.5644, val_acc=0.8295
epoch= 45, train_loss=0.4763, train_acc=0.8476, val_loss=0.5617, val_acc=0.8299
epoch= 46, train_loss=0.4732, train_acc=0.8481, val_loss=0.5592, val_acc=0.8306
epoch= 47, train_loss=0.4701, train_acc=0.8487, val_loss=0.5567, val_acc=0.8313
epoch= 48, train_loss=0.4672, train_acc=0.8493, val_loss=0.5543, val_acc=0.8316
epoch= 49, train_loss=0.4644, train_acc=0.8500, val_loss=0.5520, val_acc=0.8317
epoch= 50, train_loss=0.4617, train_acc=0.8505, val_loss=0.5499, val_acc=0.8317
epoch= 51, train_loss=0.4591, train_acc=0.8512, val_loss=0.5477, val_acc=0.8322
epoch= 52, train_loss=0.4565, train_acc=0.8517, val_loss=0.5457, val_acc=0.8328
epoch= 53, train_loss=0.4540, train_acc=0.8521, val_loss=0.5438, val_acc=0.8330
epoch= 54, train_loss=0.4517, train_acc=0.8528, val_loss=0.5419, val_acc=0.8341
epoch= 55, train_loss=0.4493, train_acc=0.8533, val_loss=0.5400, val_acc=0.8346
epoch= 56, train_loss=0.4475, train_acc=0.8536, val_loss=0.5388, val_acc=0.8347
epoch= 57, train_loss=0.4453, train_acc=0.8541, val_loss=0.5371, val_acc=0.8354
epoch= 58, train_loss=0.4432, train_acc=0.8548, val_loss=0.5355, val_acc=0.8357
epoch= 59, train_loss=0.4411, train_acc=0.8551, val_loss=0.5339, val_acc=0.8363
epoch= 60, train_loss=0.4391, train_acc=0.8553, val_loss=0.5323, val_acc=0.8364
epoch= 61, train_loss=0.4371, train_acc=0.8557, val_loss=0.5308, val_acc=0.8370
epoch= 62, train_loss=0.4352, train_acc=0.8559, val_loss=0.5293, val_acc=0.8373
epoch= 63, train_loss=0.4332, train_acc=0.8565, val_loss=0.5279, val_acc=0.8373
epoch= 64, train_loss=0.4314, train_acc=0.8567, val_loss=0.5265, val_acc=0.8381
epoch= 65, train_loss=0.4296, train_acc=0.8570, val_loss=0.5252, val_acc=0.8383
epoch= 66, train_loss=0.4279, train_acc=0.8574, val_loss=0.5239, val_acc=0.8382
epoch= 67, train_loss=0.4262, train_acc=0.8580, val_loss=0.5226, val_acc=0.8385
epoch= 68, train_loss=0.4248, train_acc=0.8581, val_loss=0.5215, val_acc=0.8388
epoch= 69, train_loss=0.4232, train_acc=0.8586, val_loss=0.5203, val_acc=0.8395
epoch= 70, train_loss=0.4216, train_acc=0.8590, val_loss=0.5191, val_acc=0.8397
epoch= 71, train_loss=0.4201, train_acc=0.8594, val_loss=0.5180, val_acc=0.8402
epoch= 72, train_loss=0.4186, train_acc=0.8600, val_loss=0.5169, val_acc=0.8404
^CTraceback (most recent call last):
  File "/home/slx/lc/fashion_minist_cls.py", line 90, in <module>
    grads = grad(xs, ys, W, B)
  File "/home/slx/lc/fashion_minist_cls.py", line 60, in grad
    return tape.gradient(loss_, [w, b])
  File "/home/slx/anaconda3/lib/python3.9/site-packages/tensorflow/python/eager/backprop.py", line 1113, in gradient
epoch=482, train_loss=0.3315, train_acc=0.8835, val_loss=0.4659, val_acc=0.8498
epoch=483, train_loss=0.3314, train_acc=0.8835, val_loss=0.4659, val_acc=0.8498
epoch=484, train_loss=0.3314, train_acc=0.8834, val_loss=0.4659, val_acc=0.8497
epoch=485, train_loss=0.3313, train_acc=0.8834, val_loss=0.4659, val_acc=0.8497
epoch=486, train_loss=0.3312, train_acc=0.8834, val_loss=0.4659, val_acc=0.8497
epoch=487, train_loss=0.3312, train_acc=0.8834, val_loss=0.4659, val_acc=0.8497
epoch=488, train_loss=0.3311, train_acc=0.8834, val_loss=0.4659, val_acc=0.8497
epoch=489, train_loss=0.3310, train_acc=0.8834, val_loss=0.4660, val_acc=0.8497
epoch=490, train_loss=0.3310, train_acc=0.8835, val_loss=0.4660, val_acc=0.8496
epoch=491, train_loss=0.3309, train_acc=0.8835, val_loss=0.4660, val_acc=0.8497
epoch=492, train_loss=0.3308, train_acc=0.8836, val_loss=0.4660, val_acc=0.8498
epoch=493, train_loss=0.3308, train_acc=0.8836, val_loss=0.4660, val_acc=0.8498
epoch=494, train_loss=0.3307, train_acc=0.8836, val_loss=0.4661, val_acc=0.8498
epoch=495, train_loss=0.3306, train_acc=0.8836, val_loss=0.4661, val_acc=0.8497
epoch=496, train_loss=0.3306, train_acc=0.8836, val_loss=0.4661, val_acc=0.8497
epoch=497, train_loss=0.3305, train_acc=0.8835, val_loss=0.4661, val_acc=0.8496
epoch=498, train_loss=0.3305, train_acc=0.8836, val_loss=0.4661, val_acc=0.8495
epoch=499, train_loss=0.3304, train_acc=0.8837, val_loss=0.4661, val_acc=0.8494
epoch=500, train_loss=0.3303, train_acc=0.8838, val_loss=0.4662, val_acc=0.8494
test accuracy: 0.8337
```

### epoch=500, batch_size=500

```cmd
epoch=  1, train_loss=3.5159, train_acc=0.5327, val_loss=3.4972, val_acc=0.5368
epoch=  2, train_loss=1.5739, train_acc=0.6771, val_loss=1.5750, val_acc=0.6833
epoch=  3, train_loss=1.3046, train_acc=0.7158, val_loss=1.3286, val_acc=0.7181
epoch=  4, train_loss=1.1556, train_acc=0.7387, val_loss=1.1919, val_acc=0.7412
epoch=  5, train_loss=1.0565, train_acc=0.7556, val_loss=1.0998, val_acc=0.7539
epoch=  6, train_loss=0.9829, train_acc=0.7678, val_loss=1.0304, val_acc=0.7650
epoch=  7, train_loss=0.9250, train_acc=0.7767, val_loss=0.9760, val_acc=0.7742
epoch=  8, train_loss=0.8778, train_acc=0.7838, val_loss=0.9314, val_acc=0.7797
epoch=  9, train_loss=0.8387, train_acc=0.7896, val_loss=0.8942, val_acc=0.7863
epoch= 10, train_loss=0.8053, train_acc=0.7941, val_loss=0.8624, val_acc=0.7908
epoch= 11, train_loss=0.7765, train_acc=0.7990, val_loss=0.8350, val_acc=0.7952
epoch= 12, train_loss=0.7515, train_acc=0.8025, val_loss=0.8113, val_acc=0.7980
epoch= 13, train_loss=0.7291, train_acc=0.8056, val_loss=0.7903, val_acc=0.8011
epoch= 14, train_loss=0.7092, train_acc=0.8086, val_loss=0.7717, val_acc=0.8034
epoch= 15, train_loss=0.6912, train_acc=0.8114, val_loss=0.7547, val_acc=0.8041
epoch= 16, train_loss=0.6751, train_acc=0.8137, val_loss=0.7396, val_acc=0.8061
epoch= 17, train_loss=0.6604, train_acc=0.8162, val_loss=0.7258, val_acc=0.8088
epoch= 18, train_loss=0.6470, train_acc=0.8183, val_loss=0.7132, val_acc=0.8110
epoch= 19, train_loss=0.6344, train_acc=0.8199, val_loss=0.7015, val_acc=0.8123
epoch= 20, train_loss=0.6229, train_acc=0.8222, val_loss=0.6908, val_acc=0.8138
epoch= 21, train_loss=0.6124, train_acc=0.8238, val_loss=0.6812, val_acc=0.8148
epoch= 22, train_loss=0.6024, train_acc=0.8257, val_loss=0.6721, val_acc=0.8163
epoch= 23, train_loss=0.5931, train_acc=0.8275, val_loss=0.6635, val_acc=0.8180
epoch= 24, train_loss=0.5842, train_acc=0.8290, val_loss=0.6554, val_acc=0.8185
epoch= 25, train_loss=0.5760, train_acc=0.8305, val_loss=0.6479, val_acc=0.8191
epoch= 26, train_loss=0.5682, train_acc=0.8318, val_loss=0.6409, val_acc=0.8202
epoch= 27, train_loss=0.5611, train_acc=0.8327, val_loss=0.6345, val_acc=0.8212
epoch= 28, train_loss=0.5542, train_acc=0.8341, val_loss=0.6283, val_acc=0.8224
epoch= 29, train_loss=0.5480, train_acc=0.8350, val_loss=0.6228, val_acc=0.8229
epoch= 30, train_loss=0.5417, train_acc=0.8360, val_loss=0.6174, val_acc=0.8231
epoch= 31, train_loss=0.5359, train_acc=0.8370, val_loss=0.6122, val_acc=0.8242
epoch= 32, train_loss=0.5302, train_acc=0.8381, val_loss=0.6073, val_acc=0.8246
epoch= 33, train_loss=0.5249, train_acc=0.8386, val_loss=0.6027, val_acc=0.8254
epoch= 34, train_loss=0.5198, train_acc=0.8398, val_loss=0.5983, val_acc=0.8261
epoch= 35, train_loss=0.5149, train_acc=0.8403, val_loss=0.5941, val_acc=0.8262
epoch= 36, train_loss=0.5103, train_acc=0.8406, val_loss=0.5902, val_acc=0.8264
epoch= 37, train_loss=0.5058, train_acc=0.8416, val_loss=0.5864, val_acc=0.8268
epoch= 38, train_loss=0.5015, train_acc=0.8426, val_loss=0.5828, val_acc=0.8267
epoch= 39, train_loss=0.4974, train_acc=0.8433, val_loss=0.5794, val_acc=0.8273
epoch= 40, train_loss=0.4935, train_acc=0.8440, val_loss=0.5761, val_acc=0.8278
epoch= 41, train_loss=0.4898, train_acc=0.8446, val_loss=0.5730, val_acc=0.8284
epoch= 42, train_loss=0.4864, train_acc=0.8453, val_loss=0.5701, val_acc=0.8283
epoch= 43, train_loss=0.4829, train_acc=0.8462, val_loss=0.5672, val_acc=0.8294
epoch= 44, train_loss=0.4795, train_acc=0.8469, val_loss=0.5644, val_acc=0.8295
epoch= 45, train_loss=0.4763, train_acc=0.8476, val_loss=0.5617, val_acc=0.8299
epoch= 46, train_loss=0.4732, train_acc=0.8481, val_loss=0.5592, val_acc=0.8306
epoch= 47, train_loss=0.4701, train_acc=0.8487, val_loss=0.5567, val_acc=0.8313
epoch= 48, train_loss=0.4672, train_acc=0.8493, val_loss=0.5543, val_acc=0.8316
epoch= 49, train_loss=0.4644, train_acc=0.8500, val_loss=0.5520, val_acc=0.8317
epoch= 50, train_loss=0.4617, train_acc=0.8505, val_loss=0.5499, val_acc=0.8317
epoch= 51, train_loss=0.4591, train_acc=0.8512, val_loss=0.5477, val_acc=0.8322
epoch= 52, train_loss=0.4565, train_acc=0.8517, val_loss=0.5457, val_acc=0.8328
epoch= 53, train_loss=0.4540, train_acc=0.8521, val_loss=0.5438, val_acc=0.8330
epoch= 54, train_loss=0.4517, train_acc=0.8528, val_loss=0.5419, val_acc=0.8341
epoch= 55, train_loss=0.4493, train_acc=0.8533, val_loss=0.5400, val_acc=0.8346
epoch= 56, train_loss=0.4475, train_acc=0.8536, val_loss=0.5388, val_acc=0.8347
epoch= 57, train_loss=0.4453, train_acc=0.8541, val_loss=0.5371, val_acc=0.8354
epoch= 58, train_loss=0.4432, train_acc=0.8548, val_loss=0.5355, val_acc=0.8357
epoch= 59, train_loss=0.4411, train_acc=0.8551, val_loss=0.5339, val_acc=0.8363
epoch= 60, train_loss=0.4391, train_acc=0.8553, val_loss=0.5323, val_acc=0.8364
epoch= 61, train_loss=0.4371, train_acc=0.8557, val_loss=0.5308, val_acc=0.8370
epoch= 62, train_loss=0.4352, train_acc=0.8559, val_loss=0.5293, val_acc=0.8373
epoch= 63, train_loss=0.4332, train_acc=0.8565, val_loss=0.5279, val_acc=0.8373
epoch= 64, train_loss=0.4314, train_acc=0.8567, val_loss=0.5265, val_acc=0.8381
epoch= 65, train_loss=0.4296, train_acc=0.8570, val_loss=0.5252, val_acc=0.8383
epoch= 66, train_loss=0.4279, train_acc=0.8574, val_loss=0.5239, val_acc=0.8382
epoch= 67, train_loss=0.4262, train_acc=0.8580, val_loss=0.5226, val_acc=0.8385
epoch= 68, train_loss=0.4248, train_acc=0.8581, val_loss=0.5215, val_acc=0.8388
epoch= 69, train_loss=0.4232, train_acc=0.8586, val_loss=0.5203, val_acc=0.8395
epoch= 70, train_loss=0.4216, train_acc=0.8590, val_loss=0.5191, val_acc=0.8397
epoch= 71, train_loss=0.4201, train_acc=0.8594, val_loss=0.5180, val_acc=0.8402
epoch= 72, train_loss=0.4186, train_acc=0.8600, val_loss=0.5169, val_acc=0.8404
^CTraceback (most recent call last):
  File "/home/slx/lc/fashion_minist_cls.py", line 90, in <module>
    grads = grad(xs, ys, W, B)
  File "/home/slx/lc/fashion_minist_cls.py", line 60, in grad
    return tape.gradient(loss_, [w, b])
  File "/home/slx/anaconda3/lib/python3.9/site-packages/tensorflow/python/eager/backprop.py", line 1113, in gradient
epoch=482, train_loss=0.3315, train_acc=0.8835, val_loss=0.4659, val_acc=0.8498
epoch=483, train_loss=0.3314, train_acc=0.8835, val_loss=0.4659, val_acc=0.8498
epoch=484, train_loss=0.3314, train_acc=0.8834, val_loss=0.4659, val_acc=0.8497
epoch=485, train_loss=0.3313, train_acc=0.8834, val_loss=0.4659, val_acc=0.8497
epoch=486, train_loss=0.3312, train_acc=0.8834, val_loss=0.4659, val_acc=0.8497
epoch=487, train_loss=0.3312, train_acc=0.8834, val_loss=0.4659, val_acc=0.8497
epoch=488, train_loss=0.3311, train_acc=0.8834, val_loss=0.4659, val_acc=0.8497
epoch=489, train_loss=0.3310, train_acc=0.8834, val_loss=0.4660, val_acc=0.8497
epoch=490, train_loss=0.3310, train_acc=0.8835, val_loss=0.4660, val_acc=0.8496
epoch=491, train_loss=0.3309, train_acc=0.8835, val_loss=0.4660, val_acc=0.8497
epoch=492, train_loss=0.3308, train_acc=0.8836, val_loss=0.4660, val_acc=0.8498
epoch=493, train_loss=0.3308, train_acc=0.8836, val_loss=0.4660, val_acc=0.8498
epoch=494, train_loss=0.3307, train_acc=0.8836, val_loss=0.4661, val_acc=0.8498
epoch=495, train_loss=0.3306, train_acc=0.8836, val_loss=0.4661, val_acc=0.8497
epoch=496, train_loss=0.3306, train_acc=0.8836, val_loss=0.4661, val_acc=0.8497
epoch=497, train_loss=0.3305, train_acc=0.8835, val_loss=0.4661, val_acc=0.8496
epoch=498, train_loss=0.3305, train_acc=0.8836, val_loss=0.4661, val_acc=0.8495
epoch=499, train_loss=0.3304, train_acc=0.8837, val_loss=0.4661, val_acc=0.8494
epoch=500, train_loss=0.3303, train_acc=0.8838, val_loss=0.4662, val_acc=0.8494
test accuracy: 0.8337
```

