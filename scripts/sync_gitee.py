
import requests
import json
import logging
import os
import sys
import urllib.request
import urllib.error
import urllib.parse
def main():
    print(os.environ['EVENT_NAME'])
    print(os.environ['RUN_ID'])
    print(os.environ['REPOSITORY'])
    print(os.environ['REPOSITORY_URL'])
if __name__ == "__main__":
    main()
