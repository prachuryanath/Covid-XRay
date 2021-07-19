import splitfolders as sf

def divide_folder(input_folder, output_folder):
  sf.ratio(input_folder, output=output_folder, seed=1337, ratio=(.8, .2), group_prefix=None)

divide_folder("data", "data1")