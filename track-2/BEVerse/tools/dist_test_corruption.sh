#!/usr/bin/env bash

CONFIG=projects/configs/robodrive/beverse_small.py
CHECKPOINT=ckpt/beverse_small.pth
GPUS=2
PORT=${PORT:-29500}

PYTHONPATH="$(dirname $0)/..":$PYTHONPATH \
python -m torch.distributed.launch --nproc_per_node=$GPUS --master_port=$PORT \
    $(dirname "$0")/test_corruption.py $CONFIG $CHECKPOINT --launcher pytorch ${@:4} --eval=bbox --mtl
