#!/usr/bin/python3
"""tracking the iss using
   api.open-notify.org/astros.json | Alta3 Research"""

import requests

## Define URL
MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    """runtime code"""

    ## Call the webservice
    groundctrl = requests.get(MAJORTOM)
    
    ## Check if the request was successful
    if groundctrl.status_code == 200:
        ## Parse the JSON response
        helmetson = groundctrl.json()

        ## Print the number of people in space
        print("People in space:", helmetson['number'])

        ## Print each astronaut's name and craft
        for person in helmetson['people']:
            print(person['name'], "on the", person['craft'])
    else:
        print("Failed to retrieve data from the API")

if __name__ == "__main__":
    main()
