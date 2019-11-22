import pygame


source_dir = os.path.abspath(os.path.dirname(__file__))
root_dir = os.path.normpath(os.path.join(source_dir, '..',))
pics = os.path.join(os.path.join(root_dir, 'pics'), '')
seq = os.path.join(os.path.join(root_dir, 'seq'), '')
sound_dir = os.path.join(os.path.join(root_dir, 'sounds'), '')
map_dir = os.path.join(os.path.join(root_dir, 'maps'), '')
music_dir = os.path.join(os.path.join(root_dir, 'music'), '')
root_dir = os.path.join(root_dir, '')
source_dir = os.path.join(source_dir, '')

def load_image(image_path):
    actual_path = os.path.join(pics, image_path)
    return pygame.image.load(actual_path)