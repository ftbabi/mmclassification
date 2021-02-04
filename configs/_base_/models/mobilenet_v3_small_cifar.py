# model settings
model = dict(
    type='ImageClassifier',
    backbone=dict(type='MobileNetv3', arch='small'),
    neck=dict(type='GlobalAveragePooling'),
    head=dict(
        type='LinearClsHead',
        # TODO: cls num
        num_classes=10,
        in_channels=96,
        loss=dict(type='CrossEntropyLoss', loss_weight=1.0),
        topk=(1, 5),
    ))
