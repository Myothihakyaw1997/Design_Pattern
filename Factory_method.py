from abc import ABC, abstractmethod

class WineCreator(ABC):

    @abstractmethod
    def produce_wine(self):
        pass

    def analyze_wine(self):

        wine = self.produce_wine()

        result = wine.operation()

        return result

class AppleWineCreator(WineCreator):

    def produce_wine(self):
        return AppleWine()

class GrapeWineCreator(WineCreator):

    def produce_wine(self):
        return GrapeWine()


class WineProduct(ABC):

    @abstractmethod
    def operation(self):
        pass

    
class AppleWine(WineProduct):
    
    def operation(self):
        return "AppleWine"


class GrapeWine(WineProduct):

    def operation(self):
        return "GrapeWine"

def client_code(wineCreator):

    print(f"This is the {wineCreator.analyze_wine()}")

if __name__=="__main__":

    print("First Client Request")
    client_code(wineCreator=AppleWineCreator())
    print("\n")
    print("Second Client Request")
    client_code(wineCreator=GrapeWineCreator())