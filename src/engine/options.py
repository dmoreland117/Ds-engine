import argparse
import pygame

class Options:
    full_screen:bool
    
    def __init__(self):
        pass
    
    @staticmethod
    def get_from_args():
        options = Options()
        
        parser = argparse.ArgumentParser(description='add description')
        #parser.add_argument('file', type=str, help='The path to a Rom File.')
        #parser.add_argument('-s', '--slow_mode', action='store_true', help='Start Emulator in Slow Mode.')
        parser.add_argument('-f, --full_screen', action='store_true', help='Start in Fullscreen Mode.', dest='full_screen')
        
        args = parser.parse_args()
        
        #options.file_path = args.file
        #options.slow_mode = args.slow_mode
        options.full_screen = args.full_screen
        
        return options
