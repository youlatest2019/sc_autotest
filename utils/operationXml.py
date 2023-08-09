import os
import xml.dom.minidom


class OperationXml(object):

    def dir_base(self, fileName, filePath='data'):
        '''获取data文件夹下的文件
        '''

        return os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)), filePath, 'data_xml'), fileName)

    def getXmlData(self, fileName, value):
        '''
        获取xml单节点中的数据
        :param value: xml文件中单节点的名称
        :return:
        '''
        dom = xml.dom.minidom.parse(self.dir_base(fileName))
        db = dom.documentElement
        name = db.getElementsByTagName(value)
        nameValue = name[0]
        return nameValue.firstChild.data

    def getXmlUser(self, fileName, parent, child, index=True):
        """
        获取xml子节点中的数据
        :param fileName:xml文件名称
        :param index:索引（bool类型)
        :param parent: 文件中父节点的名称
        :param child: 文件中子节点的名称
        :return:
        """
        dom = xml.dom.minidom.parse(self.dir_base(fileName))
        db = dom.documentElement
        itemlist = db.getElementsByTagName(parent)
        if index is False:
            item = itemlist[0]
            return item.getAttribute(child)
        elif index is True:
            res_list = []
            for item in itemlist:
                res_list.append(item.getAttribute(child))
            return res_list
        else:
            print('index参数错误，只能为True或者False')


if __name__ == '__main__':
    print(OperationXml().getXmlUser('JCXX_YGXX.xml', 'data01', 'code', index=True))
