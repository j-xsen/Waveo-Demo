import os

from django.shortcuts import render
from django.template.response import TemplateResponse
from PIL import Image, ImageDraw
from random import randrange
# from google.cloud import storage
import io

from WebProject import settings

max_length = 12


# Create your views here.
def home(request):
    args = {'notes': ['a', 'b', 'c', 'd', 'e', 'f', 'g'], 'length': range(1, max_length + 1)}
    return TemplateResponse(request, "waveo/home.html", args)


def get_repeats(split_notes, note):
    """
    Gets how many times repeated.
    :param note - What note to check for
    """
    times = 0
    for index in range(0,len(split_notes)-1):
        if note in split_notes[index+1]:
            times += 1
        else:
            return times
    return times


def create(request, notes):
    # TODO // Check for existing
    img = Image.new('RGB', (1200, 350), color='white')
    draw = ImageDraw.Draw(img, "RGBA")

    split_notes = notes.split("-")

    # variable of how many times to ignore each number
    ignore = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}

    for index in range(0, len(split_notes)):

        start_x = (100 * index)
        end_x = 100+(100 * index)

        for note in split_notes[index]:
            if ignore[note] == 0:
                size = get_repeats(split_notes[index:], note)

                if size != 0:
                    ignore[note] = size

                size_change = 25*size

                start = None
                end = None
                if note == "a":
                    start = (start_x-size_change, 0-size_change)
                    end = (end_x+size_change, 75+size_change)
                elif note == "b":
                    start = (start_x-size_change, 50-size_change)
                    end = (end_x+size_change, 125+size_change)
                elif note == "c":
                    start = (start_x-size_change, 100-size_change)
                    end = (end_x+size_change, 175+size_change)
                elif note == "d":
                    start = (start_x-size_change, 150-size_change)
                    end = (end_x+size_change, 225+size_change)
                elif note == "e":
                    start = (start_x-size_change, 200-size_change)
                    end = (end_x+size_change, 275+size_change)
                elif note == "f":
                    start = (start_x-size_change, 250-size_change)
                    end = (end_x+size_change, 325+size_change)
                elif note == "g":
                    start = (start_x-size_change, 300-size_change)
                    end = (end_x+size_change, 375+size_change)
                draw.ellipse((start, end), fill=(randrange(0, 255), randrange(0, 255), randrange(0, 255), 125+(5*size)))
            else:
                ignore[note] -= 1
    name = notes + '--' + str(randrange(0, 50000))

    # in production, you should change this

    output_dir = os.path.join(settings.MEDIA_ROOT, 'generated')
    os.makedirs(output_dir, exist_ok=True)

    saveloc = os.path.join(output_dir, name + '.png')
    url = settings.MEDIA_URL + "/generated/" + name + ".png"
    img.save(saveloc)

    # Google Cloud code
    # storage_client = storage.Client()
    # bucket = storage_client.bucket("waveo")
    # blob = bucket.blob(name)
    # img_byte_array = io.BytesIO()
    # img.save(img_byte_array,format='png')
    # blob.upload_from_string(img_byte_array.getvalue(), content_type="image/jpeg")
    #
    # url = 'https://storage.googleapis.com/waveo/' + name

    return TemplateResponse(request, "waveo/create.html", {'url': url, 'name': name})


def recall(request, name):
    url = settings.MEDIA_URL + "/generated/" + name + ".png"
    return TemplateResponse(request, "waveo/create.html", {'url': url})
