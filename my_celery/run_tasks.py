from .tasks import vminspect_scan 
import time
import argparse

def run(images, redis_addr):
    for image in images:
        vminspect_scan.delay(image.strip(), redis_addr)

