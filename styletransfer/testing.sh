cd ~/joliGEN/scripts
python3 gen_single_image.py\
     --model_in_file PATHTO/joliGEN/checkpoints/latest_net_G_A.pth\
     --img_in PATHTO/edgeAI/data/deepdrive/images/test/cae4f10f-e5906613.jpg\
     --img_out output.png\
     --img-width 1280\
     --img-height 720