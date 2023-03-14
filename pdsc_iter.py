from vtkmodules.vtkCommonDataModel import vtkDataObjectTreeIterator, vtkPartitionedDataSetCollection

class PDSCIterator:
    def __init__(self, pdsc: vtkPartitionedDataSetCollection):
        self._iterator = vtkDataObjectTreeIterator()
        self._iterator.SetDataSet(pdsc)
        self._iterator.InitTraversal()
        self._iterator.GoToFirstItem()
        self._data = self._iterator.GetCurrentDataObject()
    
    def __iter__(self):
        while not self._iterator.IsDoneWithTraversal():
            yield self._data
            self._iterator.GoToNextItem()
            self._data = self._iterator.GetCurrentDataObject()
