# cd dulu
cd ~/idx-scrapper

# hapus saham-saham LQ45
# agar listnya selalu update
# hanya dgn mengupdate LQ45.csv
rm data/Saham/LQ45/*

# jalanin script
# utk update emiten
# dan data emiten
python3 get-list-emiten.py
python3 get-data-harian-emiten.py

# jalanin daily.sh dalam folder data
# untuk ngepush ke github dan kaggle
cd data
sh daily.sh
