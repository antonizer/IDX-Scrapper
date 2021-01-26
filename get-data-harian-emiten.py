import urllib3, json
import pandas as pd
from time import sleep

# length 1 untuk 1 hari kerja
# karena kita mau ambil sehari aja
length = 1

# list emiten
emiten = pd.read_csv('data/List Emiten/all.csv')
lq45 = pd.read_csv('data/List Emiten/LQ45.csv')

# get kode-kode emiten
kode_emiten = emiten['code'].values
kode_lq45 = lq45['code'].values

# http client
http = urllib3.PoolManager()

for code in kode_emiten:
	# link
	link = f"https://idx.co.id/umbraco/Surface/ListedCompany/GetTradingInfoSS?code={code}&length={length}"

	# send request
	# always try to repeat
	# request whenever failed
	while True:
		try:
			result = http.request('GET', link)
			result = json.loads(result.data.decode('utf-8'))

			# success, we stop the while loop
			break
		except:
			# error, we sleep for 2 minutes
			sleep(2*60)

	# ada isinya?
	if result["replies"] == []:
		# tidak ada, print
		print(f"Tidak ada emiten dengan kode {code}")

		# loop diloncati
		continue
	else:
		# load data lama
		history = pd.read_csv(f"data/Saham/Semua/{code}.csv")

		# hk -> hari kerja
		hk_terakhir = history.tail(1)
		hk_terakhir = hk_terakhir['date'].values

	# data-data
	date = []
	previous = []
	openPrice = []
	firstTrade = []
	high = []
	low = []
	close = []
	change = []
	volume = []
	value = []
	frequency = []
	indexIndividual = []
	offer = []
	offerVolume = []
	bid = []
	bidVolume = []
	listedShares = []
	tradebleShares = []
	weightForIndex = []
	foreignSell = []
	foreignBuy = []
	delistingDate = []
	nonRegularVolume = []
	nonRegularValue = []
	nonRegularFrequency = []

	# simpan data-data
	for data in result["replies"][::-1]:
		# hari kerja?
		if data['Date'] != hk_terakhir:
			# ya
			date.append(data['Date'])
			previous.append(data['Previous'])
			openPrice.append(data['OpenPrice'])
			firstTrade.append(data['FirstTrade'])
			high.append(data['High'])
			low.append(data['Low'])
			close.append(data['Close'])
			change.append(data['Change'])
			volume.append(data['Volume'])
			value.append(data['Value'])
			frequency.append(data['Frequency'])
			indexIndividual.append(data['IndexIndividual'])
			offer.append(data['Offer'])
			offerVolume.append(data['OfferVolume'])
			bid.append(data['Bid'])
			bidVolume.append(data['BidVolume'])
			listedShares.append(data['ListedShares'])
			tradebleShares.append(data['TradebleShares'])
			weightForIndex.append(data['WeightForIndex'])
			foreignSell.append(data['ForeignSell'])
			foreignBuy.append(data['ForeignBuy'])
			delistingDate.append(data['DelistingDate'])
			nonRegularVolume.append(data['NonRegularVolume'])
			nonRegularValue.append(data['NonRegularValue'])
			nonRegularFrequency.append(data['NonRegularFrequency'])

	# data beres, simpan dalam CSV
	hari_ini = pd.DataFrame({
			'date': date,
			'previous': previous,
			'open_price': openPrice,
			'first_trade': firstTrade,
			'high': high,
			'low': low,
			'close': close,
			'change': change,
			'volume': volume,
			'value': value,
			'frequency': frequency,
			'index_individual': indexIndividual,
			'offer': offer,
			'offer_volume': offerVolume,
			'bid': bid,
			'bid_volume': bidVolume,
			'listed_shares': listedShares,
			'tradeble_shares': tradebleShares,
			'weight_for_index': weightForIndex,
			'foreign_sell': foreignSell,
			'foreign_buy': foreignBuy,
			'delisting_date': delistingDate,
			'non_regular_volume': nonRegularVolume,
			'non_regular_value': nonRegularValue,
			'non_regular_frequency': nonRegularFrequency,
		})

	# jadikan satu dgn yang lama
	new_data = pd.concat([history, hari_ini], ignore_index=True)

	# simpan
	new_data.to_csv(f"data/Saham/Semua/{code}.csv", index=False)

	# Saham LQ45?
	if code in kode_lq45:
		new_data.to_csv(f"data/Saham/LQ45/{code}.csv", index=False)

	# bobo dulu biar ga kena ban
	sleep(15)