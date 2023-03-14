from pdsc_iter import PDSCIterator
from vtkmodules.vtkRenderingCore import vtkPolyDataMapper
from vtkmodules.vtkIOXML import vtkXMLPartitionedDataSetCollectionReader
from vtkmodules.vtkRenderingCore import (vtkActor, vtkRenderer, vtkRenderWindow, vtkRenderWindowInteractor)
import vtkmodules.vtkRenderingOpenGL2 # for OpenGL factory overrides
import sys

if __name__ == "__main__":
    renderer = vtkRenderer()
    win = vtkRenderWindow()
    iren = vtkRenderWindowInteractor()

    win.AddRenderer(renderer)
    iren.SetRenderWindow(win)
    iren.UpdateSize(600, 600)

    reader = vtkXMLPartitionedDataSetCollectionReader()
    reader.SetFileName(sys.argv[1])
    reader.Update()
    pdsc = reader.GetOutput()
    numObjects = 0
    numPoints = 0
    numTris = 0

    for mesh in PDSCIterator(pdsc):
        actor = vtkActor()
        mapper = vtkPolyDataMapper()
        mapper.SetInputData(mesh)
        actor.SetMapper(mapper)
        renderer.AddActor(actor)

        numObjects += 1
        numPoints += mesh.GetNumberOfPoints()
        numTris += mesh.GetNumberOfPolys()

    print(f"Dataset size: {pdsc.GetActualMemorySize()} KB")
    print(f"# objects: {pdsc.GetNumberOfPartitionedDataSets()}")
    print(f"# points: {numPoints}")
    print(f"# cells: {numTris}")

    iren.Start()
