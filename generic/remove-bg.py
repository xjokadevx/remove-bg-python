

def remove_background_img(image_path, output_path, size=None, bg_color=None, format=None):
  """
  Remove background from image
  :param image_path: Path to image
  :param output_path: Path to save image
  :param size: Size of image
  :param bg_color: Background color
  :param format: Format of image
  :return: True if success
  """
  try:
    from rembg import remove 
    from PIL import Image 
  except ImportError:
    raise ImportError("removebg module not found. Please install it with 'pip install removebg'.")

  input_img = Image.open(image_path) 
  output = remove(input_img) 
  output.save(output_path) 


import os

list_imgs = os.listdir('../static/imgs_in')
for img in list_imgs:
  if '.jpg' in img:
    remove_background_img('../static/imgs_in/' + img, '../static/imgs_out/' + img.replace('.jpg', '.png'))
