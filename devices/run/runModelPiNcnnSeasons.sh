#!/bin/bash

echo "Running model..."
source base/bin/activate
cd $HOME/Documents/edgeAI/yolov8/

timeout 5m python3 app.py best_ncnn_model/ ../videos/videos-seasons/wenig.mp4 > pi_bestPt_seasons-wenig.txt
timeout 5m python3 app.py best_ncnn_model/ ../videos/videos-seasons/wenig-nacht.mp4 > pi_bestPt_seasons-wenig-nacht.txt
timeout 5m python3 app.py best_ncnn_model/ ../videos/videos-seasons/viel.mp4 > pi_bestPt_seasons-viel.txt
timeout 5m python3 app.py best_ncnn_model/ ../videos/videos-seasons/viel_nacht.mp4 > pi_bestPt_seasons-viel-nacht.txt
timeout 5m python3 app.py best_ncnn_model/ ../videos/videos-seasons/tunnel.mp4 > pi_bestPt_seasons-tunnel.txt
timeout 5m python3 app.py best_ncnn_model/ ../videos/videos-seasons/mittel_2.mp4 > pi_bestPt_seasons-mittel2.txt
timeout 5m python3 app.py best_ncnn_model/ ../videos/videos-seasons/mittel_2.mp4 > pi_bestPt_seasons-mittel2.txt
timeout 5m python3 app.py best_ncnn_model/ ../videos/videos-seasons/mittel_nacht.mp4 > pi_bestPt_seasons-mittel-nacht.txt
timeout 5m python3 app.py best_ncnn_model/ ../videos/videos-seasons/Herbst_wenig.mp4 > pi_bestPt_seasons-herbst-wenig.txt
timeout 5m python3 app.py best_ncnn_model/ ../videos/videos-seasons/Herbst_Polizei.mp4 > pi_bestPt_seasons-herbst-polizei.txt
    

echo "Model run complete!"
