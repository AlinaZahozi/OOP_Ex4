from graphics import Scale


class Scalable:
    """
        Interface that representing scalable object
    """

    def scale(self, scaler: Scale) -> tuple[float, float]:
        """
            Scales the object according to the scaler.
        """
        raise NotImplementedError

    def get_size(self) -> float:
        """
            Return a float that representing the size of the object.
            For example: for node it is radius.
        """
        raise NotImplementedError

