class RichPresenceStatus:

    # Normal details
    state: str = None
    details: str = None

    # Time details
    start_timestamp: int = None
    end_timestamp: int = None

    # Images
    large_image_key: str = None
    large_image_text: str = None
    small_image_key: str = None
    small_image_text: str = None

    def remove_none(self, dictionary: dict):
        for key, value in list(dictionary.items()):
            if value is None:
                del dictionary[key]
            elif isinstance(value, dict):
                self.remove_none(value)

    def to_dict(self) -> dict:
        timestamps, assets = None, None
        if self.start_timestamp or self.end_timestamp:
            timestamps = {
                "start": self.start_timestamp,
                "end": self.end_timestamp
            }

        if self.large_image_text or self.large_image_key or self.small_image_text or self.small_image_key:
            assets = {
                "large_image": self.large_image_key,
                "large_text": self.large_image_text,
                "small_image": self.small_image_key,
                "small_text": self.small_image_text
            }

        state = {
            "state": self.state,
            "details": self.details,
            "timestamps": timestamps,
            "assets": assets
        }
        self.remove_none(state)

        return state
