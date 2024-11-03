import qrcode, webbrowser, sys

sys.stdout.write("Press q and Enter for quit.\n")
choice = ["y", "n", "q"]
while True:
	try:
		qr_addr = input("Medication: ")
		my_qr = qrcode.make(qr_addr)

		if(qr_addr == choice[-1]):
			sys.exit()

		qr_save = input("Patient ID: ")
		my_qr.save(qr_save)

		my_qr.show()

		#For Linux users
		if sys.platform.startswith('linux'):
			choose = input("Do you want to check your address of QR code? (y / n) > ")
			if(choose == choice[0]):
				webbrowser.open(qr_addr)
				sys.exit()
			elif(choose == choice[1]):
				sys.exit()
			else:
				print("Error: Invalid input.\n")
		#For Linux users

	except SyntaxError:
		sys.stderr.write("Error: If you are a Linux user, you should use the python3.\n")
		sys.stderr.flush()
		sys.exit()
	except KeyboardInterrupt:
		sys.exit()
		data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASQAAAEkCAYAAACG+UzsAAAAAklEQVR4AewaftIAABT+SURBVO3BQW7g2rLgQFLw/rfMrmGODiBI9tX7nRH2D2ut9QEXa631ERdrrfURF2ut9REXa631ERdrrfURF2ut9REXa631ERdrrfURF2ut9REXa631ERdrrfURF2ut9REXa631ERdrrfURF2ut9RE/PKTylyqeUJkqJpWTijtUpooTlaniROWk4kTlL1VMKndUTCpTxaRyR8WkMlVMKlPFpDJVTConFZPKVHGi8pcqnrhYa62PuFhrrY+4WGutj/jhZRVvUjlRmSomlTepTBWTylQxqfwllanipOJEZaqYVKaKOyreVHGiMqn8lypOKiaVqeKk4k0qb7pYa62PuFhrrY+4WGutj/jhl6ncUfGEyh0qU8WJyknFScWk8kTFicpJxYnKVPGEyhMqU8WJylTxpopJZaqYVO5QmSrepHJHxW+6WGutj7hYa62PuFhrrY/44f8zFZPKpPImld+kclLxJpWpYqqYVO5QmSqmikllqpgqfpPKVDGp3KFyojJV/F9ysdZaH3Gx1lofcbHWWh/xw/+4ihOVSeU3qUwVf6niRGWqeELlL6mcqJxUnFS8qWJSmSomlaniRGWq+F92sdZaH3Gx1lofcbHWWh/xwy+r+EsqU8WkMlWcqNxRcaJyUnFHxaQyVbyp4g6VqeJEZVKZKiaVN6m8SeWOikllqpgqnqj4kou11vqIi7XW+oiLtdb6iB9epvKXVKaKSWWqmFSmipOKSWWqmFSmiknlRGWqmFSmikllqphUpoo7VKaKO1SmiknljopJ5Y6KSWWqmFTuqJhUpoo7VKaKE5Uvu1hrrY+4WGutj7hYa62PsH/4H6YyVUwqJxWTyh0Vk8pUcaIyVfwmlaliUjmpuEPlpGJSOal4k8pUMamcVEwqJxUnKndU/F9ysdZaH3Gx1lofcbHWWh/xw0MqU8WbVKaKE5X/UsWJylQxqUwVJyonFScqU8WkMqm8SeWkYlKZKiaVOyomlTtUpooTlanijooTlZOKE5U7Kt50sdZaH3Gx1lofcbHWWh/xwy9TeaLipOIJlZOKE5WTijsqJpU7Kp5QOak4UXmiYlI5UbmjYlJ5k8odKk+o3KFyUjGpTBW/6WKttT7iYq21PuJirbU+4oc/VnGiMqlMFZPKVPGbVKaKSWVSmSreVDGpnFRMKlPFpDKpPFHxmyp+U8UdKndUnKhMFScqU8WkclLxly7WWusjLtZa6yMu1lrrI354qGJSmSruqHhCZaqYVJ6oeELlpGKqOFGZKu6omFROKiaVqWJS+S+pTBUnFZPKicpJxYnKHRWTylQxVUwqU8WkMlVMKlPFmy7WWusjLtZa6yMu1lrrI354WcWkclJxonJHxaQyVUwqU8UdKicVJyqTylRxh8odFVPFicqbVKaKk4pJZVKZKu5QmSomlTtUpoo7VE4q7qiYVL7kYq21PuJirbU+4mKttT7ih49RmSomlROVN6lMFXeoTBVTxaRyojJVnKg8oTJVTConFU9UTCpTxaQyqZxU/KaKSWWqmFROKn5TxUnFpDJVPHGx1lofcbHWWh9xsdZaH/HDQyp3VEwqJypTxYnKVPFExaTyhMpUMVVMKlPFpDJVTBUnKlPFHRWTypdUnKicVEwVJyqTyh0VT6icVNyhclLxpou11vqIi7XW+oiLtdb6CPuHF6lMFZPKHRUnKndUTConFZPKScWJym+qmFSmiknliYpJZaqYVKaKSWWq+EsqU8UTKlPFicpJxR0qU8WJyhMVT1ystdZHXKy11kdcrLXWR/zwkModFZPKVDGpTBUnFZPKEypPqJxU3KEyVUwqU8WkckfFpHJSMamcqLxJ5aTiDpUnKn6TyhMqJxV/6WKttT7iYq21PuJirbU+4oeHKu5QuaPipOJNFU+onFRMKlPFHSpTxaQyVZyo3KFyUjGpPKEyVUwVk8qJylRxojJVTConKm+quENlqrhD5aTiiYu11vqIi7XW+oiLtdb6iB9epnJSMamcqEwVk8odKicqJxWTyknFScWk8qaKE5WpYlKZKk5Unqh4QuVE5YmKk4o3VZyonFTcoTJVTBWTypsu1lrrIy7WWusjLtZa6yN+eEjlpGJSmSomlaliUpkq7lCZKk5UJpUnVO6oOFGZVH6TyknFb6o4qThRuUPlpGJSmSpOKk5U7qiYVKaKL7tYa62PuFhrrY+4WGutj/jhoYo3VUwqU8UdKneoTBWTylQxqUwqU8Wk8psqJpUTlaniDpU3qZxUTCp3VEwqJxWTylRxUnGi8oTKicodKlPFb7pYa62PuFhrrY+4WGutj7B/eJHKVHGiclIxqUwVJypTxR0qU8WJylQxqZxUnKicVNyhMlVMKlPFpDJVTCpTxYnKScWJyknFpDJVTCpvqphUvqRiUjmpeNPFWmt9xMVaa33ExVprfYT9wwMqJxUnKk9U/CWVqeJE5aRiUnmiYlJ5ouIOlZOKSeWkYlI5qThRmSomlaliUjmpmFROKiaVqeIJlaliUpkq/ksXa631ERdrrfURF2ut9RH2D79IZao4UZkqJpW/VDGpTBV3qJxUTCp3VDyhclIxqZxUTCpTxYnKHRV3qEwVd6hMFZPKScUTKlPFpDJVnKhMFScqU8UTF2ut9REXa631ERdrrfURPzykMlVMFU+oTBWTyh0Vv0nlTRVPqEwVd1RMKneoTBWTyknFpHKHylTxhMoTFZPKVDGpnFRMKicqT6j8pou11vqIi7XW+oiLtdb6iB8eqphU7qg4qTipOFGZVE4q3lQxqUwVJyp3VJyoTBVPVEwqU8VJxR0VJyonKn+p4i9V3KEyVZxUTCpvulhrrY+4WGutj7hYa62P+OEhlTsqJpWpYlKZKp6omFTuqDipmFR+U8VJxaQyqUwVd6hMFZPKVDGpTBUnKlPFScWkcqJyUvGbVKaKSeVE5QmVqWJSmSredLHWWh9xsdZaH3Gx1lof8cPLKiaVk4pJZaqYVKaKk4pJZaqYVKaKSeWJiknlpGJSuUPlpGJSOal4U8WbKiaVqeIOlTepTBUnKndU3KEyVUwqU8VvulhrrY+4WGutj7hYa62PsH94QOWkYlI5qZhU7qi4Q2WqmFROKiaVOyomlZOKSWWqeEJlqphUpoonVE4qnlCZKk5UpopJ5Y6K36QyVUwqU8WkMlVMKicVb7pYa62PuFhrrY+4WGutj/jhoYpJZVKZKu6ouEPljoo7KiaVqWJSmSomlaniCZWTipOKSWWqOFGZKiaVk4oTlaniL1WcqJyoTBWTyh0Vk8pUMancUTGp/KaLtdb6iIu11vqIi7XW+gj7h/+Qypsq/pLKVHGHyknFicpUMalMFZPK/5KKSeWkYlKZKiaVN1WcqEwVk8r/koonLtZa6yMu1lrrIy7WWusj7B9+kcodFXeoTBWTyknFicpvqjhRmSomlZOKO1ROKu5QmSomlTsqJpWTihOVqeJEZaqYVE4q3qQyVdyhclIxqUwVb7pYa62PuFhrrY+4WGutj/jhZSpTxYnKicpU8ZtUTiomlaniDpWp4kTlpOIOlaliUjlRmSpOVKaKE5VJZaqYVE5UpopJ5Q6Vk4pJZar4TSpTxR0qf+lirbU+4mKttT7iYq21PuKHh1SmiknliYo7VE4qnlA5UZkqTiomlaliUpkq7lB5U8UdFScqU8WJyonKHRWTyknFpDKpnKhMFZPKExVPVEwqv+lirbU+4mKttT7iYq21PsL+4QGVk4pJ5X9JxYnKVDGpnFScqEwVk8pU8SaV31Rxh8odFXeo3FExqTxRMan8pYpJZar4TRdrrfURF2ut9REXa631ET+8rOKJijepPKEyVUwVf0llqphUpoonKiaVqWJS+U0Vd6g8UTGp/CaVJyomlZOKSWWqmFSmijddrLXWR1ystdZHXKy11kf88McqJpVJ5aRiUjmpOFG5Q2WqOKl4U8UdKicVk8oTFXeoTBUnKn9JZaqYVE4qTlSeqDip+E0qU8UTF2ut9REXa631ERdrrfURPzxUMamcVEwVk8pUMalMFZPKicpJxaQyVUwqd1RMKlPFVPFExaRyUjGpTBUnKn+pYlI5qThRmSpOKiaVE5WpYlI5qThRmSomlZOKk4pJ5U0Xa631ERdrrfURF2ut9RE/vKziROUOld9U8UTFHSonKlPFHRWTyonKVDFV3FFxojJVnKicqJxUTCpTxYnKScWJyh0Vd6g8UTGp3FHxpou11vqIi7XW+oiLtdb6iB9epnJSMamcVEwqJxVvqjhROamYKu5QOan4TSonFZPKVDFVTCpTxUnFHSp3VEwqT1ScqEwVJypTxaTyl1Smiicu1lrrIy7WWusjLtZa6yN+eFnFicpJxaQyVUwqU8UdKlPFExUnKndUnKicVEwqJyonFZPKVDGpTBV3VEwqU8WkMlVMKm9SmSomlZOKSeWkYlKZKp6omFSmiknlTRdrrfURF2ut9REXa631ET/8xypOKu5QmSrepHKiMlVMFXeonFRMKpPKScWJyqQyVdyhcqIyVUwVd6jcoTJVTCpTxUnFicodKlPFpDJVnKhMFf+li7XW+oiLtdb6iIu11vqIH/5YxaQyVUwqU8VUMalMKlPFpDKpnFRMKicqT1RMKicVJyqTylQxVUwqd1RMKlPFicpJxUnFicoTKicVk8pUcYfKpDJVTCpTxaTyJRdrrfURF2ut9REXa631EfYPv0jljoo7VKaKE5U7Kp5QOamYVKaKJ1SmijtU7qh4k8odFW9SmSrepHJSMalMFZPKScWJylQxqZxUPHGx1lofcbHWWh9xsdZaH2H/8IDKHRUnKndUTConFXeoTBWTyknFpHJSMamcVEwqf6liUpkqJpU7Ku5QOak4UTmpmFSmikllqrhDZaqYVKaKN6lMFZPKVPHExVprfcTFWmt9xMVaa32E/cMDKlPFHSonFXeonFRMKlPFHSpTxYnKVDGpPFExqdxRMalMFZPKX6qYVKaKSeWOikllqjhRuaNiUjmpeELljoq/dLHWWh9xsdZaH3Gx1lofYf/wYSonFZPKVDGpnFRMKicVd6icVEwqJxV3qLyp4gmV31RxonJScaJyR8WkMlX8JpWpYlI5qfhNF2ut9REXa631ERdrrfUR9g8PqEwVJypTxR0qb6qYVE4qJpWpYlI5qZhUTir+kspUcYfKScWJylTxJpWpYlKZKk5UpooTlScqTlSmiknlpOIvXay11kdcrLXWR1ystdZH2D/8IpWpYlK5o+JE5Y6KJ1TeVDGpTBWTylQxqUwVJyonFScqJxWTylQxqTxRMancUXGickfFpPKmir+kMlU8cbHWWh9xsdZaH3Gx1lofYf/wgMoTFZPKVHGHylQxqZxUTCp3VEwqT1RMKlPFX1KZKk5UTiomlaliUpkqTlSmiidU7qiYVKaKSeWkYlKZKiaVOyruUJkqnrhYa62PuFhrrY+4WGutj/jhZRWTylQxqZyo3FExqZxUPFExqZxU3KFyojJVTConFZPKVHGHylQxqbxJZap4QuWk4g6VE5Wp4k0Vd6icVEwVb7pYa62PuFhrrY+4WGutj7B/+EMqU8WkMlVMKndUTCpPVEwqU8WJyh0Vk8pUMalMFScqJxUnKlPFicpUMalMFScqT1S8SeWk4g6VqeJEZaqYVKaKSeWJiicu1lrrIy7WWusjLtZa6yPsHx5QmSqeUDmpuEPlpGJSmSpOVJ6o+EsqJxUnKlPFpDJVTCpvqrhDZaqYVJ6oOFGZKp5QOamYVH5TxRMXa631ERdrrfURF2ut9RE/PFTxmyomlaliUpkq7qiYVKaKOyomlUnliYoTlanif0nFicpUMancUXGicqIyVdyhclIxVfymihOVN12stdZHXKy11kdcrLXWR/zwy1ROKk5UpopJ5UTljoo7KiaVOyomlZOKSeWkYlKZKk5U7qiYVN6kMlVMKlPFpHKiclIxqUwVJxWTylQxqUwqJxWTylQxqdyh8psu1lrrIy7WWusjLtZa6yN+eEhlqpgqJpWTijsqJpWTikllUrlD5QmVO1ROKu5QmSpOKp6ouENlqphUTlSmiknliYoTlanijopJZaqYVE5Unqj4TRdrrfURF2ut9REXa631EfYPL1I5qZhUpopJ5Y6KSeU3VUwqJxWTylQxqUwVd6jcUTGpvKliUpkqJpWTihOVk4pJ5aRiUjmpmFSmiidU3lQxqZxUvOlirbU+4mKttT7iYq21PuKHl1XcUXFScaIyqUwVJyonFZPKScWkMqk8oTJVnFRMKk9U3KEyqUwVT6hMFScVk8oTFZPKpDJVTCpTxaRyR8UdKl9ysdZaH3Gx1lofcbHWWh/xw0Mqf6liqphUJpWp4qRiUjlRmSruqDipmFQmlZOKqeJE5Q6VqeKk4o6KJyp+k8oTFXdUTConKlPFExW/6WKttT7iYq21PuJirbU+4oeXVbxJ5Y6KJ1TuqDipmFQmlaniiYoTlaliqphUTiruUJkqTlSmikllqphUpoqTikllUpkqJpWpYlI5qThRuaPiDpWpYlKZKt50sdZaH3Gx1lofcbHWWh/xwy9TuaPiTSpTxVTxhMpJxVQxqUwqJxWTyonKicpUcaLyRMWkMlU8oTJVTCpPVEwqU8WkMlVMKpPKEypPVEwqU8WkMlU8cbHWWh9xsdZaH3Gx1lof8cP/cRVPqEwVU8WJyh0V/yWVqeJEZap4QmWquKNiUjmpmFSmikllqphUpopJ5YmKE5Wp4g6VqeKk4k0Xa631ERdrrfURF2ut9RE//B+jckfFpDJVTCpTxaQyVUwqU8WJyknFScWkclIxqUwVU8WkMlXcUTGpnFScVEwqb1KZKiaVqWJSmSpOVKaKqWJSeZPKVPGmi7XW+oiLtdb6iIu11vqIH35ZxV+qmFROVKaKSeVEZaqYVKaKSeWk4kTlpOKkYlKZKu6omFTeVHGi8iUVb6o4UXmTylQxqUwVT1ystdZHXKy11kdcrLXWR/zwMpW/pDJVnFScqJxU3FHxX1I5UTlRmSqeqJhUJpWpYlKZKk4qJpU7VO5QmSomlaniv1QxqdxR8aaLtdb6iIu11vqIi7XW+gj7h7XW+oCLtdb6iIu11vqIi7XW+oiLtdb6iIu11vqIi7XW+oiLtdb6iIu11vqIi7XW+oiLtdb6iIu11vqIi7XW+oiLtdb6iIu11vqIi7XW+oj/B4M2SuFGcouiAAAAAElFTkSuQmCC