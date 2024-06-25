import logging

logger = logging.getLogger(__name__)


class FixtureSet:
    def __init_subclass__(cls, name=None, **kwargs) -> None:
        """
        A special class method that allows customization of class creation when
        a class is subclassed.

        Args:
            name (_type_, optional): _description_. Defaults to None.
        """
        cls.fixtureset_name = name or cls.__name__

    def _install(self, *args, **kwargs):
        logger.info(f"Installing fixtures for {self.fixtureset_name}")
