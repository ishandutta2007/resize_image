import PIL.Image


def resize_image(image, width, height):
    """Resizes an image to the specified width and height.

  Args:
    image: The image to resize.
    width: The desired width of the resized image.
    height: The desired height of the resized image.

  Returns:
    The resized image.
  """

    # Get the original size of the image.
    original_width, original_height = image.size

    # If the image is smaller than the desired size, upscale it first.
    if original_width < width or original_height < height:
        ratio = max(width / original_width, height / original_height)
        image = image.resize(
            (int(original_width * ratio), int(original_height * ratio))
        )

    # Crop the image to the desired size.
    cropped_image = image.crop(
        (
            (width - original_width) // 2,
            (height - original_height) // 2,
            (width + original_width) // 2,
            (height + original_height) // 2,
        )
    )

    return cropped_image


filename = "pubmed"
desired_width = 1280
desired_height = 800

image = PIL.Image.open(filename + ".png")

# Resize the image to desired_width x desired_height pixels.
resized_image = resize_image(image, desired_width, desired_height)

# Save the resized image to a file.
resized_image.save(
    filename + "_" + str(desired_width) + "x" + str(desired_height) + ".png"
)
