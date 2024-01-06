#!/usr/bin/env bash

CONFIG=projects/configs/surroundocc/surroundocc.py
CHECKPOINT=ckpts/surroundocc.pth
GPUS=2
PORT=${PORT:-29282}

PYTHONPATH="$(dirname $0)/..":$PYTHONPATH \
python -m torch.distributed.launch --nproc_per_node=$GPUS --master_port=$PORT \
    $(dirname "$0")/test.py $CONFIG $CHECKPOINT --launcher pytorch ${@:4} --deterministic --eval bbox
