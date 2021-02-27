#This Class has the Function that Creates the USA Board
#Currently, it just returns a list of all nodes, but may later be used for actually modeling Ticket to Ride
#Board Game Scholar Post 2
#Freddy Reiber

from City import City
from Route import Route


def setUpUSABoard():
    listOfCites = []

    Seattle = City("Seattle")
    Route1 = Route("Seattle", "Vancouver", 1)
    Route2 = Route("Seattle", "Calgary", 4)
    Route3 = Route("Seattle", "Helena", 6, "Yellow")
    Route4 = Route("Seattle", "Portland", 1)
    Seattle.addRoute(Route1)
    Seattle.addRoute(Route2)
    Seattle.addRoute(Route3)
    Seattle.addRoute(Route4)
    listOfCites.append(Seattle)

    Vancouver = City("Vancouver")
    Route5 = Route("Vancouver", "Calgary", 3)
    Vancouver.addRoute(Route1)
    Vancouver.addRoute(Route5)
    listOfCites.append(Vancouver)

    Calgary = City("Calgary")
    Route6 = Route("Calgary", "Helena", 4)
    Route7 = Route("Calgary", "Winnipeg", 6, "White")
    Calgary.addRoute(Route5)
    Calgary.addRoute(Route6)
    Calgary.addRoute(Route7)
    Calgary.addRoute(Route2)
    listOfCites.append(Calgary)

    Portland = City("Portland")
    Route8 = Route("Portland", "Salt Lake City", 6, "Blue")
    Route9 = Route("Portland", "San Francisco", 5, ["Green", "Pink"])
    Portland.addRoute(Route4)
    Portland.addRoute(Route8)
    Portland.addRoute(Route9)
    listOfCites.append(Portland)

    SanFran = City("San Francisco")
    Route10 = Route("San Francisco", "Salt Lake City", 5, ["Orange", "White"])
    Route11 = Route("San Francisco", "Los Angeles", 3, ["Yellow", "Pink"])
    SanFran.addRoute(Route10)
    SanFran.addRoute(Route11)
    SanFran.addRoute(Route9)
    listOfCites.append(SanFran)

    LA = City("Los Angeles")
    Route12 = Route("Los Angeles", "Las Vegas", 2)
    Route13 = Route("Los Angeles", "Phoenix", 3, "Blue")
    Route14 = Route("Los Angeles", "El Paso", 6, "Black")
    LA.addRoute(Route12)
    LA.addRoute(Route13)
    LA.addRoute(Route14)
    LA.addRoute(Route11)
    listOfCites.append(LA)

    LV = City("Las Vegas")
    Route15 = Route("Las Vegas", "Salt Lake City", 3, 'Orange')
    LV.addRoute(Route15)
    LV.addRoute(Route12)
    listOfCites.append(LV)

    SLC = City("Salt Lake City")
    route16 = Route("Salt Lake City", "Denver", 3, ["Red", "Yellow"])
    route17 = Route("Salt Lake City", "Helena", 3, "Pink")
    SLC.addRoute(route16)
    SLC.addRoute(route17)
    SLC.addRoute(Route15)
    SLC.addRoute(Route10)
    SLC.addRoute(Route8)
    listOfCites.append(SLC)

    Helena = City("Helena")
    Route18 = Route("Helena", "Winnipeg", 4, "Blue")
    Route19 = Route("Helena", "Duluth", 6, "Orange")
    Route20 = Route("Helena", "Omaha", 5, "Red")
    Route21 = Route("Helena", "Denver", 4, "Green")
    Helena.addRoute(Route18)
    Helena.addRoute(Route19)
    Helena.addRoute(Route20)
    Helena.addRoute(Route21)
    Helena.addRoute(route17)
    Helena.addRoute(Route6)
    listOfCites.append(Helena)

    Denver = City("Denver")
    Route22 = Route("Denver", "Omaha", 4, "Pink")
    Route23 = Route("Kansas City", "Denver", 4, "Orange")
    Route24 = Route("Denver", "Oklahoma City", 4, "Red")
    Route25 = Route("Denver", "Santa Fe", 2)
    RouteOops = Route("Denver", "Phoenix", 5, "White")
    Denver.addRoute(Route22)
    Denver.addRoute(Route23)
    Denver.addRoute(Route24)
    Denver.addRoute(Route25)
    Denver.addRoute(Route21)
    Denver.addRoute(route16)
    listOfCites.append(Denver)

    SantaFe = City("Santa Fe")
    Route26 = Route("Santa Fe", "El Paso", 2)
    Route27 = Route("Santa Fe", "Phoenix", 3)
    Route28 = Route("Santa Fe", "Oklahoma City", 3, "Blue")
    SantaFe.addRoute(Route26)
    SantaFe.addRoute(Route27)
    SantaFe.addRoute(Route28)
    SantaFe.addRoute(Route25)
    listOfCites.append(SantaFe)

    ElPaso = City("El Paso")
    Route29 = Route("El Paso", "Oklahoma City", 5, "Yellow")
    Route30 = Route("El Paso", "Dallas", 4, "Red")
    Route31 = Route("El Paso", "Houston", 6, "Green")
    Route32 = Route("El Paso", "Phoenix", 3)
    ElPaso.addRoute(Route29)
    ElPaso.addRoute(Route30)
    ElPaso.addRoute(Route31)
    ElPaso.addRoute(Route26)
    ElPaso.addRoute(Route14)
    ElPaso.addRoute(Route32)
    listOfCites.append(ElPaso)

    Phoenix = City("Phoenix")
    Phoenix.addRoute(Route32)
    Phoenix.addRoute(Route27)
    Phoenix.addRoute(Route13)
    Phoenix.addRoute(RouteOops)
    listOfCites.append(Phoenix)

    Winni = City("Winnipeg")
    Route33 = Route("Winnipeg", "Sault St.Marie", 6)
    Route34 = Route("Winnipeg", "Duluth", 4, "Black")
    Winni.addRoute(Route33)
    Winni.addRoute(Route34)
    Winni.addRoute(Route18)
    Winni.addRoute(Route7)
    listOfCites.append(Winni)

    Duluth = City("Duluth")
    Route35 = Route("Duluth", "Sault St.Marie", 3)
    Route36 = Route("Duluth", "Toronto", 6, "Pink")
    Route37 = Route("Duluth", "Chicago", 3, "Red")
    Route38 = Route("Duluth", "Omaha", 2)
    Duluth.addRoute(Route35)
    Duluth.addRoute(Route36)
    Duluth.addRoute(Route37)
    Duluth.addRoute(Route38)
    Duluth.addRoute(Route34)
    Duluth.addRoute(Route19)
    listOfCites.append(Duluth)

    Omaha = City("Omaha")
    Route39 = Route("Omaha", "Chicago", 3, "Blue")
    Route40 = Route("Omaha", "Kansas City", 1)
    Omaha.addRoute(Route39)
    Omaha.addRoute(Route40)
    Omaha.addRoute(Route38)
    Omaha.addRoute(Route22)
    Omaha.addRoute(Route20)
    listOfCites.append(Omaha)

    KC = City("Kansas City")
    Route41 = Route("Kansas City", "Saint Louis", 2, ["Blue", "Pink"])
    Route42 = Route("Kansas City", "Oklahoma City", 2)
    KC.addRoute(Route41)
    KC.addRoute(Route42)
    KC.addRoute(Route40)
    KC.addRoute(Route23)
    listOfCites.append(KC)

    OC = City("Oklahoma City")
    Route43 = Route("Oklahoma City", "Little Rock", 2)
    Route44 = Route("Oklahoma City", "Dallas", 2)
    OC.addRoute(Route44)
    OC.addRoute(Route43)
    OC.addRoute(Route42)
    OC.addRoute(Route29)
    OC.addRoute(Route28)
    OC.addRoute(Route24)
    listOfCites.append(OC)

    Dallas = City("Dallas")
    Route45 = Route("Dallas", "Little Rock", 2)
    Route46 = Route("Dallas", "Houston", 1)
    Dallas.addRoute(Route45)
    Dallas.addRoute(Route46)
    Dallas.addRoute(Route44)
    Dallas.addRoute(Route30)
    listOfCites.append(Dallas)

    Houston = City("Houston")
    Route47 = Route("Houston", "New Orleans", 2)
    Houston.addRoute(Route47)
    Houston.addRoute(Route46)
    Houston.addRoute(Route31)
    listOfCites.append(Houston)

    SSM = City("Sault St.Marie")
    Route48 = Route("Sault St.Marie", "Montreal", 5, "Black")
    Route49 = Route("Sault St.Marie", "Toronto", 2)
    SSM.addRoute(Route48)
    SSM.addRoute(Route49)
    SSM.addRoute(Route35)
    SSM.addRoute(Route33)
    listOfCites.append(SSM)

    Chicago = City("Chicago")
    Route50 = Route("Chicago", "Toronto", 4, "White")
    Route51 = Route("Chicago", "Pittsburgh", 3, ["Black", "Orange"])
    Route52 = Route("Chicago", "Saint Louis", 2, ["Green", "White"])
    Chicago.addRoute(Route51)
    Chicago.addRoute(Route50)
    Chicago.addRoute(Route52)
    Chicago.addRoute(Route37)
    Chicago.addRoute(Route39)
    listOfCites.append(Chicago)

    SL = City("Saint Louis")
    Route53 = Route("Saint Louis", "Pittsburgh", 5, "Green")
    Route54 = Route("Saint Louis", "Nashville", 2)
    Route55 = Route("Saint Louis", "Little Rock", 2)
    SL.addRoute(Route53)
    SL.addRoute(Route54)
    SL.addRoute(Route55)
    SL.addRoute(Route52)
    SL.addRoute(Route41)
    listOfCites.append(SL)

    LR = City("Little Rock")
    Route56 = Route("Little Rock", "Nashville", 3, "White")
    Route57 = Route("Little Rock", "New Orleans", 3, "Green")
    LR.addRoute(Route56)
    LR.addRoute(Route57)
    LR.addRoute(Route55)
    LR.addRoute(Route45)
    LR.addRoute(Route43)
    listOfCites.append(LR)

    NO = City("New Orleans")
    Route58 = Route("New Orleans", "Atlanta", 4, ["Yellow", "Orange"])
    Route59 = Route("New Orleans", "Miami", 6, "Red")
    NO.addRoute(Route58)
    NO.addRoute(Route59)
    NO.addRoute(Route57)
    NO.addRoute(Route47)
    listOfCites.append(NO)

    Toronto = City("Toronto")
    Route60 = Route("Toronto", "Montreal", 3)
    Route61 = Route("Toronto", "Pittsburgh", 2)
    Toronto.addRoute(Route60)
    Toronto.addRoute(Route61)
    Toronto.addRoute(Route50)
    Toronto.addRoute(Route49)
    Toronto.addRoute(Route36)
    listOfCites.append(Toronto)

    Pitts = City("Pittsburgh")
    Route62 = Route("Pittsburgh", "New York", 2, ["Green", "White"])
    Route63 = Route("Pittsburgh", "Washington", 2)
    Route64 = Route("Pittsburgh", "Raleigh", 2)
    Route65 = Route("Pittsburgh", "Nashville", 4, "Yellow")
    Pitts.addRoute(Route62)
    Pitts.addRoute(Route63)
    Pitts.addRoute(Route64)
    Pitts.addRoute(Route65)
    Pitts.addRoute(Route61)
    Pitts.addRoute(Route53)
    Pitts.addRoute(Route51)
    listOfCites.append(Pitts)

    Nash = City("Nashville")
    Route66 = Route("Nashville", "Raleigh", 3, "Black")
    Route67 = Route("Nashville", "Atlanta", 1)
    Nash.addRoute(Route66)
    Nash.addRoute(Route67)
    Nash.addRoute(Route65)
    Nash.addRoute(Route56)
    Nash.addRoute(Route54)
    listOfCites.append(Nash)

    Atlanta = City("Atlanta")
    Route68 = Route("Atlanta", "Raleigh", 2, ["Grey", "Grey"])
    Route69 = Route("Atlanta", "Charleston", 2)
    Route70 = Route("Atlanta", "Miami", 5, "Blue")
    Atlanta.addRoute(Route68)
    Atlanta.addRoute(Route69)
    Atlanta.addRoute(Route70)
    Atlanta.addRoute(Route66)
    Atlanta.addRoute(Route64)
    listOfCites.append(Atlanta)

    Miami = City("Miami")
    Route71 = Route("Miami", "Charleston", 4, "Pink")
    Miami.addRoute(Route71)
    Miami.addRoute(Route69)
    Miami.addRoute(Route59)
    listOfCites.append(Miami)

    Charleston = City("Charleston")
    Route72 = Route("Charleston", "Raleigh", 2)
    Charleston.addRoute(Route72)
    Charleston.addRoute(Route71)
    Charleston.addRoute(Route69)
    listOfCites.append(Charleston)

    Raleigh = City("Raleigh")
    Route73 = Route("Raleigh", "Washington", 2)
    Raleigh.addRoute(Route73)
    Raleigh.addRoute(Route72)
    Raleigh.addRoute(Route68)
    Raleigh.addRoute(Route66)
    Raleigh.addRoute(Route64)
    listOfCites.append(Raleigh)

    Washington = City("Washington")
    Route74 = Route("Washington", "New York", 2, ["Orange", "Black"])
    Washington.addRoute(Route74)
    Washington.addRoute(Route73)
    Washington.addRoute(Route63)
    listOfCites.append(Washington)

    NY = City("New York")
    Route75 = Route("New York", "Boston", 2, ["Yellow", "Red"])
    Route76 = Route("New York", "Montreal", 3, "Blue")
    NY.addRoute(Route75)
    NY.addRoute(Route74)
    NY.addRoute(Route76)
    NY.addRoute(Route62)
    listOfCites.append(NY)

    Boston = City("Boston")
    Route78 = Route("Boston", "Montreal", 2, ["Grey", "Grey"])
    Boston.addRoute(Route78)
    Boston.addRoute(Route75)
    listOfCites.append(Boston)

    Montreal = City("Montreal")
    Montreal.addRoute(Route48)
    Montreal.addRoute(Route78)
    Montreal.addRoute(Route76)
    Montreal.addRoute(Route60)
    listOfCites.append(Montreal)

    return listOfCites