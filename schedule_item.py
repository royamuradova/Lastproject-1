from dataclasses import dataclass

@dataclass
class ScheduleItem:
    subject: str
    catalog: str
    section: str
    title: str
    instructor: str

    @property
    def key(self) -> str:
        """
        Unique key used for trees.
        Example: 'CSC-223-01'
        """
        return f"{self.subject}-{self.catalog}-{self.section}"
