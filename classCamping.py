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
        self.coordinates = coordinates

    def deserializar(self, dict):
        self.setId(dict["id"])
        self.setDocumentname(dict["propierties"]["documentname"])
        self.setTemplatetype(dict["propierties"]["templatetype"])
        self.setTurismdescription(dict["propierties"]["turismdescription"])
        self.setAddress(dict["properties"]["address"])
        self.setMarks(dict["propierties"]["marks"])
        self.setWeb(dict["propierties"]["web"])
        self.setLodgingtype(dict["propierties"]["lodgingtype"])
        self.setCategory(dict["propierties"]["category"])
        self.setCapacity(dict["propierties"]["capacity"])
        self.setPostalcode(dict["propierties"]["postalcode"])
        self.setMunicipality(dict["propierties"]["municipality"])
        self.setMunicipalitycode(dict["propierties"]["municipalitycode"])
        self.setCountry(dict["propierties"]["country"])
        self.setCountrycode(dict["propierties"]["countrycode"])
        # Coordenadas
        self.setCoordinates(dict["coordinates"])





