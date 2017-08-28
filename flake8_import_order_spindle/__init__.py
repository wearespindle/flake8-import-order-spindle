from flake8_import_order.styles import Google


class SpindleOrder(Google):
    """
    Custom import order. We use Google as a base with the addition
    that app imports and relative imports should be in a seperate section.
    """
    @staticmethod
    def same_section(previous, current):
        """
        Make sure all types of imports should be in a different section.
        """
        return current.type == previous.type
