#!/usr/bin/env python
import os
from pprint import pprint
from subprocess import call

from appiumparser import AppiumParser
from appiumtest import run_tests, AppiumTest


if __name__ == '__main__':
    p = AppiumParser()
    args = p.parse()
    appium_args = p.to_appium_args(args)

    print ("Running Appium with the following desired capabilities:")
    pprint(appium_args)

    device = str(appium_args['device']).lower()

    test = None
    if device in ['android', 'selendroid']:
        pass
        # test = CustomAndroidTest()
    elif device in ['iphone', 'ipad', 'mock_ios']:
        pass
        # test = CustomIosTest()
    else:
        raise ValueError("Device " + device + " is not supported")

    tests = args['tests']
    tests = tests.split(":") if tests else None

    files = [f for f in tests if f.endswith(".py") and os.path.exists(f)]
    folders = [f for f in tests if f not in files and os.path.isdir(f)]

    AppiumTest.overridden_capabilities = appium_args
    for folder in folders:
        run_tests(folder, args['tests_pattern'])

    for file in files:
        raise NotImplementedError()
#       call(["python", file])