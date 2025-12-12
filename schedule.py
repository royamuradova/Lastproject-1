import csv
from schedule_item import ScheduleItem
from search_trees import BSTMap, AVLTreeMap

class Schedule:
    def __init__(self, use_avl: bool = False):
        """
        If use_avl is True, use AVLTreeMap as backend.
        Otherwise, use BSTMap.
        """
        if use_avl:
            self._items = AVLTreeMap()
        else:
            self._items = BSTMap()

    def load_from_csv(self, filename: str):
        """Load courses from a CSV file into the tree."""
        with open(filename, newline="", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Safely get fields from CSV (strip spaces)
                subject = row.get("Subject", "").strip()
                catalog = row.get("Catalog", "").strip()
                section = row.get("Section", "").strip()
                instructor = row.get("Instructor", "").strip()

                # Some CSVs do NOT have a 'Title' column.
                # Try to get it; if missing or empty, fabricate a simple title.
                title = row.get("Title", "").strip()
                if not title:
                    # Fallback title, e.g. "CSC 223"
                    title = f"{subject} {catalog}".strip()

                item = ScheduleItem(
                    subject=subject,
                    catalog=catalog,
                    section=section,
                    title=title,
                    instructor=instructor
                )

                # Insert into the underlying tree (BST or AVL)
                self._items.insert(item.key, item)

    def tree_height(self) -> int:
        """Return height of the underlying tree."""
        return self._items.height()

    def list_all_courses(self):
        """Return a list of all ScheduleItem objects in sorted order."""
        result = []
        for key, item in self._items.inorder_items():
            result.append(item)
        return result

    def search_by_subject(self, subject: str):
        """Return list of courses matching a given subject."""
        subject = subject.upper()
        result = []
        for key, item in self._items.inorder_items():
            if item.subject.upper() == subject:
                result.append(item)
        return result

    def search_by_subject_catalog(self, subject: str, catalog: str):
        """Return list of courses matching subject + catalog."""
        subject = subject.upper()
        catalog = catalog.upper()
        result = []
        for key, item in self._items.inorder_items():
            if item.subject.upper() == subject and item.catalog.upper() == catalog:
                result.append(item)
        return result

    def search_by_instructor(self, instructor_substring: str):
        """Return list of courses where instructor name contains the substring."""
        instructor_substring = instructor_substring.lower()
        result = []
        for key, item in self._items.inorder_items():
            if instructor_substring in item.instructor.lower():
                result.append(item)
        return result
