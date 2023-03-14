from pdsc_iter import PDSCIterator
from vtkmodules.vtkRenderingOpenGL2 import vtkCompositePolyDataMapper2
from vtkmodules.vtkIOXML import vtkXMLPartitionedDataSetCollectionReader
from vtkmodules.vtkRenderingCore import (vtkActor, vtkRenderer, vtkRenderWindow, vtkRenderWindowInteractor)
import sys

if __name__ == "__main__":
    reader = vtkXMLPartitionedDataSetCollectionReader()
    mapper = vtkCompositePolyDataMapper2()
    actor = vtkActor()
    renderer = vtkRenderer()
    win = vtkRenderWindow()
    iren = vtkRenderWindowInteractor()

    renderer.AddActor(actor)
    win.AddRenderer(renderer)
    iren.SetRenderWindow(win)
    iren.UpdateSize(600, 600)

    reader.SetFileName(sys.argv[1])
    mapper.SetInputConnection(reader.GetOutputPort())
    mapper.Update()
    pdsc = reader.GetOutput()
    numObjects = 0
    numPoints = 0
    numTris = 0

    for mesh in PDSCIterator(pdsc):
        numObjects += 1
        numPoints += mesh.GetNumberOfPoints()
        numTris += mesh.GetNumberOfPolys()

    print(f"Dataset size: {pdsc.GetActualMemorySize()} KB")
    print(f"# objects: {pdsc.GetNumberOfPartitionedDataSets()}")
    print(f"# points: {numPoints}")
    print(f"# cells: {numTris}")

    actor.SetMapper(mapper)
    iren.Start()
