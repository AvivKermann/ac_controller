import boto3

from .secrets import (AWS_ACCESS_KEY_ID, AWS_DEFAULT_REGION,
                      AWS_SECRET_ACCESS_KEY)


class AcState:
    def __init__(self):
        self.dynamo = boto3.resource(
            "dynamodb",
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_DEFAULT_REGION,
        ).Table("ac_state")
        self.status = None
        self.temp = None
        self.mode = None
        self.fan = None

    @classmethod
    def get_state(cls) -> "AcState":
        state = cls()
        dynamo_state = state.dynamo.get_item(Key={"state_id": "ac_unit"})
        state.status = dynamo_state["Item"]["status"]
        state.temp = dynamo_state["Item"]["temperature"]
        state.fan = dynamo_state["Item"]["fan_level"]
        state.mode = dynamo_state["Item"]["mode"]
        return state

    def set_state(self):
        return self.dynamo.put_item(
            Item={
                "state_id": "ac_unit",
                "status": self.status,
                "temperature": self.temp,
                "fan_level": self.fan,
                "mode": self.mode,
            }
        )

    def __str__(self) -> str:
        return f"Status is: {self.status} | Temp is: {self.temp} | Fan is: {self.fan} | Mode is: {self.mode}"


def main():
    state = AcState.get_state()
    print(state)


main()
