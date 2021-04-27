from pymobiledevice3.services.dvt.structs import MessageAux


class ApplicationListing:
    IDENTIFIER = 'com.apple.instruments.server.services.device.applictionListing'

    def __init__(self, dvt):
        self._channel = dvt.make_channel(self.IDENTIFIER)

    def applist(self) -> list[dict]:
        """
        Get the applications list from the device.
        :return: List of applications and their attributes.
        """
        self._channel.installedApplicationsMatching_registerUpdateToken_(
            MessageAux().append_obj({}).append_obj(''))
        result = self._channel.receive()
        assert isinstance(result, list)
        return result
