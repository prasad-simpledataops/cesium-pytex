from concurrent.futures import TimeoutError
from google.cloud import pubsub_v1


def extract_subscription_name(qualified_subscription):
    return qualified_subscription.split('/')[-1]


class PubSubConsumer:

    def __init__(self, project_id: str, subscription_id: str) -> object:
        self.project_id = project_id
        self.subscription_id = extract_subscription_name(subscription_id)
        self.subscriber = pubsub_v1.SubscriberClient()
        # The `subscription_path` method creates a fully qualified identifier
        # in the form `projects/{project_id}/subscriptions/{subscription_id}`
        self.subscription_path = self.subscriber.subscription_path(self.project_id, self.subscription_id)

# Number of seconds the subscriber should listen for messages
# timeout = 5.0
    def callback(self, message):
        print(f"Received {message}.")
        if message.attributes:
            print("Attributes:")
            for key in message.attributes:
                value = message.attributes.get(key)
                print(f"{key}: {value}")
        message.ack()

    def start_listener(self):
        streaming_pull_future = self.subscriber.subscribe(self.subscription_path, callback=self.callback)
        print(f"Listening for messages on {self.subscription_path}..\n")

        # Wrap subscriber in a 'with' block to automatically call close() when done.
        with self.subscriber:
            try:
                # When `timeout` is not set, result() will block indefinitely,
                # unless an exception is encountered first.
                streaming_pull_future.result()
            except TimeoutError:
                streaming_pull_future.cancel()