from random import randint

version = "indev-0.0.1"

uuidCounter=0


class expert(): #unemployed
    def __init__(self,name,job,morale):
        self.name=name
        self.job=job
        self.morale=morale

class advisor(expert): #employed
    def __init__(self, name, job, morale, position, modifier):
        super().__init__(name, job, morale)
        self.position=position
        self.modifier=modifier
    def applyBuff(self, factor):
        pass
 
class resource(): #N/A, ore, food, ec, data, morale
    def __init__(self,name,value):
        self.value=value
        self.name=name
    def getValue(self):
        return self.value
    def setValue(self, amount):
        self.value=amount
    def getType(self):
        return self.name
    def addValue(self, amount):
        self.value += amount

"""
class system(): #lifesupport, oreMining, culinary, electricityGen, research, morale
    def __init__(self,name,production:resource):
        self.name=name
        self.production=production
"""

class structure():
    def __init__(self,uuid,production:resource,consumption:resource):
        self.uuid=uuid #TODO: implement a UUID generator (line 3)
        self.production=production
        self.consumption=consumption
    def useStructure(self):
        pass #TODO: Come back to this later.

class modifier():
    def __init__(self,magnitude):
        self.magnitude=magnitude
       # self.system=system
    def applyModifier(self):
        pass

class colony():
    def __init__(self, name:str, colonist:int, lifeSupport:resource, ore:resource, food:resource, power:resource, researchPoints:resource, morale:resource):
        
        return(self.magnitude)