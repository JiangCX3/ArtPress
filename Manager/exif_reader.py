import base64

import os
import random
import shutil
import string

import piexif

from ArtPress import settings


class MediaLibraryExif:
    def __init__(self, **kwargs):
        """
        About the operation of the media library EXIF.

        :param kwargs filename, exif_data:
        """

        self.mediadir_path = settings.STATIC_URL + settings.MEDIA_LIBRATY_DIR + "/"
        self.kwargs = kwargs

    def read(self):
        """ Read EXIF of pictures in media library """
        return piexif.load(self.mediadir_path + self.kwargs["filename"])

    def write(self):
        """ Write EXIF of pictures in media library """
        img_file = self.mediadir_path + self.kwargs["filename"]
        d = piexif.dump(self.kwargs["exif_data"])
        piexif.insert(d, img_file)
        return img_file

    def create_temp_noexif(self):
        """
        Delete the EXIF of the picture and place it in the TEMP STATIC directory
        
        :return: object_filepath
        """""
        scoure_filepath = "./ArtPress" + self.mediadir_path + self.kwargs["filename"]
        extension = os.path.splitext(scoure_filepath)[-1]

        object_filename = ''.join([random.choice(string.hexdigits) for i in range(16)]) + extension
        object_filepath = "./ArtPress" + settings.TEMP_STATIC_DIR + object_filename

        # Copy ImageFile to staticTemp directory
        shutil.copy(scoure_filepath, object_filepath)

        # Delete the EXIF info
        piexif.remove(object_filepath)

        return object_filepath


if __name__ == '__main__':
    ml_exif = MediaLibraryExif(
        filename="exif-test.jpg",
    )

    print(ml_exif.create_temp_noexif())
