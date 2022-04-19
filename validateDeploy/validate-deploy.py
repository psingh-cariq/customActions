#!/usr/bin/python3
import os
import time
from pprint import pprint

import envoy
import logging

logging.basicConfig(level=logging.INFO)

logging.basicConfig(level=logging.INFO)
app = os.environ['INPUT_APP']
expectedSha = os.environ['INPUT_GITSHA']
maxAttempt = os.environ['INPUT_MAXATTEMPT']
sleepDuration = os.environ['INPUT_SLEEPDURATION']
counter = 1

logging.info(f"App: {app}")
logging.info(f"Expected Sha: {expectedSha}")


json_path1 = "{.items[?(@.metadata.labels.app=='%s')].status}" % app
command2 = 'kubectl get pods -o=jsonpath="{0}"'.format(json_path1)
result = envoy.run(command2)
pprint(result.std_out)

while counter <= int(maxAttempt):
    logging.info(f"Validate sha {expectedSha} for app {app} attempt {counter}")
    json_path = "{.items[?(@.metadata.labels.app=='%s')].status.containerStatuses[0].image}" % app
    # command = 'kubectl get pods -o=jsonpath="{0}"'.format(json_path)
    command = 'kubectl get pods -o json'
    print(f"command == {command}")
    r = envoy.run(command)
    print(f"Line 32 {r.std_out}")
    list_of_images = r.std_out.split(",")
    if len(list_of_images) < 1:
        logging.warning(f"No images found for app: {app}")
        break
    candidatesCount = len(list_of_images)
    matchCount: int = 0
    logging.info("Found {0} images for app {1} to validate".format(candidatesCount, app))
    for image in list_of_images:
        logging.info(f"Image name before split: {image}")
        try:
            actualSha = image.split(":")[1].split(" ")[0]
            if expectedSha == actualSha:
                print("Actual Sha:{0} and Expected Sha:{1} are matched for app {2}".format(actualSha, expectedSha, app))
                matchCount += 1
            else:
                print("Actual Sha:{0} and Expected Sha:{1} are not matched".format(actualSha, expectedSha))
        except:
            logging.error(f"Failed to extract sha from image name: {image}")
    if matchCount == candidatesCount:
        print(f"All images are matched with expected sha {expectedSha} for app {app} validated total of {candidatesCount}")
        break
    else:
        errorMessage = f"{matchCount} matched against {candidatesCount} candidates"
        assert False, errorMessage
    time.sleep(int(sleepDuration))
    counter += 1
