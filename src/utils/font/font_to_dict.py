from utils.image_editors import clip


def clip_font_to_dict(fontset, order, separator_color=(255, 0, 0, 255)):
    characters = {}
    character_wd = 0
    idx = 0

    # Loop over every top pixel in the given fontset
    for x in range(fontset.get_width()):
        pixel = fontset.get_at((x, 0))

        # A separator has been found
        if pixel == separator_color:
            # Get letter image
            img = clip(
                fontset,
                (x - character_wd, 0),
                (character_wd, fontset.get_height())
            )

            # Append letter image to characters dictionary
            characters[order[idx]] = img

            # Update variables
            character_wd = 0
            idx += 1
        else:
            # Update variables
            character_wd += 1
    
    # Return
    return characters
