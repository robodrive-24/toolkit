cp -r ./data/robodrive-sensor/robodrive-v1.0-test ./data/nuscenes

python tools/create_data.py nuscenes \
    --root-path ./data/nuscenes \
    --out-dir ./data/nuscenes \
    --version robodrive-v1.0 \
    --extra-tag robodrive
