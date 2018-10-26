import requests
import xmltodict


def leavingTrains():
    'asks for station and outputs all the leaving trains on time and destination'
    vraag = str(input("Vul een station in: "))

    # making contact with the API
    auth_details = ('pixelpulp4@gmail.com', 'zdRThsCcDsXBFsIxycTU2uWcctPd1W_50xRICdSN6vZUIfAm987U5g')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station={0}'.format(vraag)
    response = requests.get(api_url, auth=auth_details)

    # saves the response in 'vertrekXML'
    vertrekXML = xmltodict.parse(response.text)
    print("Dit zijn de vertrekkende treinen:")

    # Iterate over the data and print the needed information
    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        eindBestemming = vertrek['EindBestemming']

        vertrekTijd = vertrek['VertrekTijd']
        vertrekTijd = vertrekTijd[11:16]

        print("Om {0} vertrekt een trein naar {1}".format(vertrekTijd, eindBestemming))


leavingTrains()