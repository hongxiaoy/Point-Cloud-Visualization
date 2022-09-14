# README

The `point_cloud_frames` directory contains several point cloud frames in one `tfrecord` file. Those `bin` file are generated from `MMDetection3D`, and the point cloud file are kitti format.

Each point has 6 attributes, the first three are $(x,y,z)$, while the last 3 you should refer to related code in the `MMDetection3D` where the Waymo format data is transformed into the KITTI format.

The `0000024.bin` is an example file for visualizing single point cloud frame.

Both the python script `multi_frame` and `single_frame` are based on Open3d.

You can run commands below to show help for visualizing single frame or a stream of frames:

```bash
python multi_frame.py -h
```

```bash
python single_frame.py -h
```

