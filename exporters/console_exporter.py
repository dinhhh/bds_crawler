from abc import ABC

from object.objs import Bds
from exporters import abstract_exporter


class ConsoleExporter(abstract_exporter.AbstractExporter, ABC):
    def export(self, bds: Bds):
        print(f"Start export {bds.title}")
