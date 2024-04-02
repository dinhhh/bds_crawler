from abc import ABC

from object.objs import Bds
from exporters import abstract_exporter
import json
from object import objs
from utils import logger
import codecs


class JsonExporter(abstract_exporter.AbstractExporter, ABC):
    output_folder_path: str

    def __init__(self, output_folder_path=r"C:\Users\dinh\PycharmProjects\bds_scrapy\output"):
        self.output_folder_path = output_folder_path

    def export(self, bds: Bds):
        try:
            with open(rf'{self.output_folder_path}\{bds.id}.json', 'w', encoding='utf-8') as f:
                json.dump(bds.reprJSON(), f, cls=objs.ComplexEncoder, ensure_ascii=False)
            f.close()
            logger.get_logger().info(rf"Start export {bds.title} into folder {self.output_folder_path}\{bds.id}.json")
        except:
            logger.get_logger().error(rf"Fail to export to json {self.output_folder_path}\{bds.id}.json")


if __name__ == '__main__':
    bds = Bds()
    bds.link = "link với mã utf8"
    bds.title = "title test bds"
    bds.project = "project bds description"
    add = objs.Address()
    add.full_add = "Hà Nội"
    bds.address = add
    # print(json.dumps(bds.reprJSON(), cls=objs.ComplexEncoder))
    with open(r'C:\Users\dinh\PycharmProjects\bds_scrapy\output\test.json', 'w', encoding='utf-8') as f:
        json.dump(bds.reprJSON(), f, cls=objs.ComplexEncoder, ensure_ascii=False)
    f.close()

    # file = codecs.open(r'C:\Users\dinh\PycharmProjects\bds_scrapy\output\test.json', "w", "utf-8-sig")
    # print(f"{json.dumps(bds.reprJSON(), cls=objs.ComplexEncoder).encode('utf8')}")
    # file.write(f'{json.dumps(bds.reprJSON(), cls=objs.ComplexEncoder)}')
    # file.close()
    logger.get_logger().info("Hix")
