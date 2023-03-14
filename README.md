This repository provides some auto generated `.vtpc` files in the `data` directory and two python scripts which render the data files with one or many actors.

Usage:

1. Install VTK python
```bash
$ python3 -m venv .
$ pip install -U pip
$ python3 -m pip install vtk
```

Alternatively, compile VTK from source and use `vtkpython` to run the scripts.

2. Run the scripts and observe memory usage from `nvtop` or `intel_gpu_top`

```bash
$ python3 RenderComposite1Actor.py <path to .vtpc>
$ python3 RenderCompositeManyActors.py <path to .vtpc>
```

Here are the memory profiles for desktop GL and GLES polydata mapper.

1. [Desktop GL memory profile](https://plotly.com/~jspanchu/3/)
2. [GLES memory profile](https://plotly.com/~jspanchu/1/)
