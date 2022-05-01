import argparse
import os
import sys

parser = argparse.ArgumentParser(prog='ascii-renderer', description='Render ASCII art from source[camera, image, video] and output it[text, stdout].')

parser.add_argument('-s', '--source', help='Source to be rendered. [camera, image, video]', required=True, type=str)
parser.add_argument('-o', '--output', help='Output format of ASCII rendered image', required=True, type=str)