# hapus saham-saham LQ45
# agar listnya selalu update
# hanya dgn mengupdate LQ45.csv
rm data/saham/LQ45/*

# date hari ini
date_today=$(date +'%d %B %Y')

# jalanin script
# utk update emiten
# dan data emiten
python3 get-list-emiten.py
python3 get-data-harian-emiten.py