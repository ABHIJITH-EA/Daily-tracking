""" CLI utils """

from base.constants import System

def aligner(text: str) -> int:
    align_size = System.SECONDARY_LEFT_ALIGN.value \
                + System.CONSOLE_MENU_ALIGN_SIZE.value
    if len(text) > align_size:
        align_size = len(text) \
                    + System.CONSOLE_MENU_ALIGN_SIZE.value

    return align_size