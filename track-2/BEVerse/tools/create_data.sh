#!/usr/bin/env bash

# cp -r ./data/robodrive-release/robodrive-v1.0-test ./data/nuscenes

python tools/create_data.py \
    nuscenes \
    --root-path ./data/nuscenes \
    --out-dir ./data/nuscenes_infos \
    --extra-tag robodrive \
    --version robodrive-v1.0 \