import cfscrape, json
import pandas as pd

# mulai dari 0
start = 0

# supported length -> under 150
length = 150

# emiten lq45
lq45 = pd.read_csv('List Emiten LQ45.csv')
lq45 = lq45['code'].values

# data-data
stock_code = []
stock_name = []
stock_listingDate = []
stock_shares = []
stock_listingBoard = []

# data-data lq45
lq45_code = []
lq45_name = []
lq45_listingDate = []
lq45_shares = []
lq45_listingBoard = []

# http client
http = cfscrape.create_scraper()

while True:
	# buat link
	link = f"https://idx.co.id/umbraco/Surface/StockData/GetSecuritiesStock?code=&sector=&board=&start={start}&length={length}"

	# send request
	result = http.get(link).text
	result = json.loads(result)

	# result empty?
	# kalo iya, berarti daftar
	# emitennya sudah habis
	if result["data"] == []:
		break
	else:
		# loop data
		for data in result["data"]:
			# simpan semuanya
			stock_code.append(data["Code"])
			stock_name.append(data["Name"])
			stock_listingDate.append(data["ListingDate"])
			stock_shares.append(data["Shares"])
			stock_listingBoard.append(data["ListingBoard"])

			# merupakan LQ45?
			if data["Code"] in lq45:
				lq45_code.append(data["Code"])
				lq45_name.append(data["Name"])
				lq45_listingDate.append(data["ListingDate"])
				lq45_shares.append(data["Shares"])
				lq45_listingBoard.append(data["ListingBoard"])

	# start ditambah
	start += length

# uda beres ambil semua
# skrg tinggal convert ke
# bentuk dataframe
emiten = pd.DataFrame({ 'code': stock_code,
						'name': stock_name,
						'listing_date': stock_listingDate,
						'shares': stock_shares,
						'listing_board': stock_listingBoard
					})

emiten_lq45 = pd.DataFrame({'code': lq45_code,
							'name': lq45_name,
							'listing_date': lq45_listingDate,
							'shares': lq45_shares,
							'listing_board': lq45_listingBoard
						})

# save as csv
emiten.to_csv('data/List Emiten/all.csv', index=False)
emiten_lq45.to_csv('data/List Emiten/LQ45.csv', index=False)