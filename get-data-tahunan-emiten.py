import cloudscraper, json
import pandas as pd
from time import sleep

# length 365 untuk 1 tahun
# karena kita mau setahun
# well actually 1 tahun kerja
length = 365

# list emiten
emiten = pd.read_csv('data/List Emiten/all.csv')
lq45 = pd.read_csv('data/List Emiten/LQ45.csv')

# get kode-kode emiten
emiten = emiten['code'].values
lq45 = lq45['code'].values

# http client
http = cloudscraper.CloudScraper()

for code in emiten:
	# link
	link = f"https://idx.co.id/umbraco/Surface/ListedCompany/GetTradingInfoSS?code={code}&length={length}"

	# send request
	# always try to repeat
	# request whenever failed
	while True:
		try:
			# send request
			result = http.get(link).text
			result = json.loads(result)

			# success, we brake the while loop
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
	history = pd.DataFrame({
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

	# simpan
	history.to_csv(f"data/Saham/Semua/{code}.csv", index=False)

	# Saham LQ45?
	if code in lq45:
		history.to_csv(f"data/Saham/LQ45/{code}.csv", index=False)

	# bobo dulu biar ga kena ban
	sleep(15)