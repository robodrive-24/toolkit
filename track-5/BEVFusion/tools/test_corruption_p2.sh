torchpack dist-run -np 2 python tools/test.py \
    configs/robodrive_p2/det/transfusion/secfpn/camera+lidar/swint_v0p075/convfuser.yaml \
    pretrained/bevfusion-det.pth \
    --eval bbox