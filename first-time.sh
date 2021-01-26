# make folder
mkdir -p "data/List Emiten"
mkdir -p "data/Saham/Semua"
mkdir -p "data/Saham/LQ45"

# install requirements
pip3 install -r requirements.txt

# kaggle env
export KAGGLE_USERNAME=tiwill
export KAGGLE_KEY=bb4949730775b129ad28e8f01aa862d2

# get metadata
kaggle datasets metadata -p data tiwill/saham-lq45-idx

# start script
python3 get-list-emiten.py
python3 get-data-tahunan-emiten.py
