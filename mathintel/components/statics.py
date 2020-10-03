from mathintel.settings import BASE_DIR
import os

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_common')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = (
    # os.path.join(BASE_DIR, 'node/dist'),
    os.path.join(BASE_DIR, 'static'),
)

VERSATILEIMAGEFIELD_SETTINGS = {
    'cache_length': 2592000,  # 30
    'cache_name': 'versatileimagefield_cache',
    'jpeg_resize_quality': 70,
    'sized_directory_name': '__sized__',
    'filtered_directory_name': '__filtered__',
    'placeholder_directory_name': '__placeholder__',
    'create_images_on_demand': True,
    'image_key_post_processor': None,
    'progressive_jpeg': False
}

CKEDITOR_UPLOAD_PATH = 'ckeditor/'
