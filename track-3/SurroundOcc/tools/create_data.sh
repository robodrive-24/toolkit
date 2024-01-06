cp -r ./data/robodrive-release/robodrive-v1.0-test ./data/nuscenes

python tools/create_data.py \
    nuscenes \
    --root-path ./data/nuscenes \
    --out-dir ./data \
    --extra-tag robodrive \
    --version robodrive-v1.0 \
    --canbus ./data/nuscenes