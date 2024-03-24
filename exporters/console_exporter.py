from abc import ABC

from abstract_exporter import AbstractExporter
from object.objs import Bds


class ConsoleExporter(AbstractExporter, ABC):
    def export(self, bds: Bds):
        print(f"Start export {bds.title}")
