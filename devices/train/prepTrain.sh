cd $HOME
echo "preparing device for training"
source base/bin/activate
cd $HOME/Documents/edgeAI/datasets/citypersons/
unzip archive(1).zip
echo "Cloning dataset..."
#git close "https://github.com/CharlesShang/Detectron-PYTORCH/tree/master/data/citypersons/annotations" annotations
echo "Dataset cloned!"
echo "Running setup..."
python3 setup.py
echo "Setup complete!"