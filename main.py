# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import configparser
import sys
import getopt
import util.pytexutil
from pubsub.PubSubConsumer import PubSubConsumer
from util import pytexutil


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def get_config_file(argv):
    configfile = None
    try:
        opts, args = getopt.getopt(argv,"hc:",["config="])
    except getopt.GetoptError:
        print("Usage: main.py -c <config_file> or -h for help")
        sys.exit(2)

    for opt, arg in opts:
        print(f'opt={opt}, arg={arg}')
        if opt == '-h':
            print(' -c <config_file>')
        elif opt == '-c':
            configfile = arg

    if(configfile == None):
        print("Usage: main.py -c <config_file> or -h for help")
        sys.exit(2)

    return configfile

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    configfile = 'config.properties';# get_config_file(sys.argv)
    print(f'Config file to use = {configfile}')
    config = configparser.ConfigParser()
    config.read(configfile);
    login_response = pytexutil.login(config.get('cesium','base_url'),
                    config.get('cesium','tex_id'),
                config.get('cesium','tex_password'));

    print(login_response)
    project_id = login_response['toTexTopicInfo']['topicAuthInfo']['authCreds']['PROJECT_ID']
    subscription_id = login_response['toTexTopicInfo']['topicAuthInfo']['authCreds']['SUBSCRIPTION_ID']
    consumer = PubSubConsumer(project_id, subscription_id)
    consumer.start_listener()





# See PyCharm help at https://www.jetbrains.com/help/pycharm/

