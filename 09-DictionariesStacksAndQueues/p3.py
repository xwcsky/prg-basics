Hotels_in_Krakow = [   {"name":"Sky","price":320.00},   {"name":"Metropol","price":480.00},   {"name":"New Port","price":420.00},   {"name":"Aparthotel","price":390.00} ]

hotels_in_Sopot = [   {"name":"Focus","price":510.00},   {"name":"Aqua","price":345.00},   {"name":"La Boutique","price":390.00},   {"name":"Marina","price":410.00} ]

def averagePrice(hotels):
    totalPrice = sum(hotel["price"] for hotel in hotels)
    average = totalPrice / len(hotels)
    return average
    

Krakow = averagePrice(Hotels_in_Krakow)
Sopot = averagePrice(hotels_in_Sopot)

print(f'Średni koszt hotelu w Krakowie to {Krakow}')
print(f'Średni koszt hotelu w Sopocie to {Sopot}')

if Krakow < Sopot:
    print("Hotele w Krakowie są tańsze")
elif Krakow > Sopot:
    print("Hotele w Sopocie są tańsze")

