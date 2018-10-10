class Camping(object):
    id = None
    documentname = None
    templatetype = None
    turismdescription = None
    address = None
    marks = None
    web = None
    lodgingtype = None
    category = None
    capacity = None
    postalcode = None
    municipality = None
    municipalitycode = None
    country = None
    countrycode = None

    def __init__(self):
        self.coordinates = []

    def setId(self, id):
        self.id = id

    def setDocumentname(self, documentname):
        self.documentname = documentname

    def setTemplatetype(self, templatetype):
        self.templatetype = templatetype

    def setTurismdescription(self, turismdescription):
        self.turismdescription = turismdescription

    def setAddress(self, address):
        self.address = address

    def setMarks(self, marks):
        self.marks = marks

    def setWeb(self, web):
        self.web = web

    def setLodgingtype(self, lodgingtype):
        self.lodgingtype = lodgingtype

    def setCategory(self, category):
        self.category = category

    def setCapacity(self, capacity):
        self.capacity = capacity

    def setPostalcode(self, postalcode):
        self.postalcode = postalcode

    def setMunicipality(self, municipality):
        self.municipality = municipality

    def setMunicipalitycode(self, municipalitycode):
        self.municipalitycode = municipalitycode

    def setCountry(self, country):
        self.country = country

    def setCountrycode(self, countrycode):
        self.countrycode = countrycode

    def setCoordinates(self, coordinates):
        self.coordinates.append(coordinates[1])
        self.coordinates.append(coordinates[0])

    # No toma capacity, postalcode ni marks. RE MISTERIOSO!
    def deserializar(self, dict):
        self.setId(dict["id"])
        self.setDocumentname(dict["properties"]["documentname"])
        self.setTemplatetype(dict["properties"]["templatetype"])
        self.setTurismdescription(dict["properties"]["turismdescription"])
        self.setAddress(dict["properties"]["address"])
        if "marks" in dict["properties"]:
            self.setMarks(dict["properties"]["marks"])
        self.setWeb(dict["properties"]["web"])
        self.setLodgingtype(dict["properties"]["lodgingtype"])
        self.setCategory(dict["properties"]["category"])
        if "capacity" in dict["properties"]:
            self.setCapacity(dict["properties"]["capacity"])
        if "postalcode" in dict["properties"]:
            self.setPostalcode(dict["properties"]["postalcode"])
        self.setMunicipality(dict["properties"]["municipality"])
        self.setMunicipalitycode(dict["properties"]["municipalitycode"])
        self.setCountry(dict["properties"]["country"])
        self.setCountrycode(dict["properties"]["countrycode"])
        # Coordenadas
        self.setCoordinates(dict["geometry"]["coordinates"])

    @staticmethod
    def getListaFromMongo(campings):
        dict = campings.find_one({}, {"features": 1})
        listaCampings = []
        for item in dict["features"]:
            camping = Camping()
            camping.deserializar(item)
            listaCampings.append(camping)
        return listaCampings

    @staticmethod
    def getAllCampings(collection):
        dict = collection.find_one({}, {"features": 1})
        Lista = Camping.getListaFromMongo(dict)
        return Lista

    @staticmethod
    def getCamping(collection, campingId):
        dict = collection.find_one({"features}":{"properites": {"id":campingId}}}, {"features": 1})
        camping = Camping()
        camping.deserializar(dict)
        return camping


