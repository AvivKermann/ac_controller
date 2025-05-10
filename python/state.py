from typing import Dict

import boto3

from .secrets import AWS_ACCESS_KEY_ID, AWS_DEFAULT_REGION, AWS_SECRET_ACCESS_KEY


class AcState:
    def __init__(self, current_state: Dict):
        self.status = current_state["Item"]["status"]
        """ if the ac is on or off """

        self.temp = current_state["Item"]["temperature"]
        """ Current ac temp """

        self.fan = current_state["Item"]["fan_level"]
        """ Current fan level """

        self.mode = current_state["Item"]["mode"]
        """ Current ac mode, (hot, cold, air)."""

        """ Remove the current state from memory once assained"""
        del current_state

    def __str__(self):
        return str([self.status, self.temp])


class AcStater:
    def __init__(self):
        self.dynamo = boto3.resource(
            "dynamodb",
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_DEFAULT_REGION,
        ).Table("ac_state")

    def get_current_state(self):
        return AcState(self.dynamo.get_item(Key={"state_id": "ac_unit"}))


def main():
    stater = AcStater()
    state = stater.get_current_state()

    print(f"current state is: {state}")


main()
