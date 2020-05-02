# from colorama import Fore
import sys

def empty_name():
  print('Creation of directory failed: \n')
  sys.exit(1)

def failure_msg(app_name):
  print('Creation of directory failed: ' + app_name + '\n')
  sys.exit(1)

def success_msg(app_name):
  print('Creation of directory success: ' + app_name + '\n')