from data import *
from datetime import datetime
from database import *


# import models.database as db


class ManagerControl:
    def __init__(self):
        pass

    def makeDict(self, dataObj):
        print(provDirPath)
        dataDict = dict(name=dataObj.name, Id=dataObj.Id, address=dataObj.address,
                        city=dataObj.city, state=dataObj.state, zipcode=dataObj.zipcode)
        return dataDict

    def addProvider(self, providerObj):
        providerDict = self.makeDict(providerObj)
        addProvider(providerDict)

    # this obj will have things like name, number etc..
    def addMember(self, memberObj):
        # call the data base class funtion to do the ading
        return database.add(memberObj)

    def editMember(self, memberId, memberObj):
        memDict = getJSONListOfDicts(memRegPath)
        for mem in memDict:
            if (mem['Id'] == memberId):
                mem.update(memberObj)
        createJSONListFile(provRegPath, memDict)

    def editProvider(self, providerId, providerObj):
        print(provRegPath)
        provDict = getJSONListOfDicts(provRegPath)
        for prov in provDict:
            if (prov['Id'] == providerId):
                prov.update(providerObj)
        createJSONListFile(provRegPath, provDict)

    def removeProvider():
        pass

    def removeMember():
        pass

    def viewMemberReport(memberFile):
        return database.memberReport(memberId)

    def viewProviderReport(providerFile):
        return database.providerReport(providerId)
