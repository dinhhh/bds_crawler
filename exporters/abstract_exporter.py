from abc import ABC, abstractmethod
from object.objs import Bds

class AbstractExporter(ABC):

    @abstractmethod
    def export(self, bds: Bds):
        pass
