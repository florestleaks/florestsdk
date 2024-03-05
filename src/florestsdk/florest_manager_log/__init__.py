import logging
from enum import Enum, auto
from typing import Any

import sentry_sdk


class Category(Enum):
    CRAWLER = auto()


class TaskState(Enum):
    NONE = auto()
    SCHEDULED = auto()
    QUEUED = auto()
    SUCCESS = auto()
    RUNNING = auto()
    RESTARTING = auto()
    FAILED = auto()
    SKIPPED = auto()
    UPSTREAM_FAILED = auto()
    UP_FOR_RETRY = auto()
    UP_FOR_RESCHEDULE = auto()
    DEFERRED = auto()
    REMOVED = auto()


class LogManager:
    def __init__(self, log_level: int = logging.DEBUG, sentry_dsn: str = ""):
        self.sentry_dsn = sentry_dsn
        if self.sentry_dsn:
            sentry_sdk.init(dsn=self.sentry_dsn)
        logging.basicConfig(
            level=log_level,
            format="%(asctime)s - [%(levelname)s] - [%(name)s] - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

    def _validate_category(self, category):
        if isinstance(category, Enum):
            return category
        else:
            try:
                return Category[category.upper()]
            except KeyError as err:
                allowed_categories = [cat.name.lower() for cat in Category]
                msg = f"Invalid category: {category}. Allowed categories are: {allowed_categories}"
                raise ValueError(msg) from err

    def _validate_task_state(self, state):
        if isinstance(state, Enum):
            return state
        else:
            try:
                return TaskState[state.upper()]
            except KeyError as err:
                allowed_states = [state.name.lower() for state in TaskState]
                msg = f"Invalid task state: {state}. Allowed states are: {allowed_states}"
                raise ValueError(msg) from err

    def log(
        self,
        level: str,
        message: str,
        category: Enum,
        task_state: Enum,
        exc_info: Any = None,
        tags: dict = None,
    ):
        if tags is None:
            tags = {}
        if self.sentry_dsn:
            for tag, value in tags.items():
                sentry_sdk.set_tag(tag, value)

        category_str = category.name.lower()
        task_state_str = task_state.name.upper()

        formatted_message = f"[{task_state_str}] - {message}"
        logger = logging.getLogger(category_str)

        if level == "error" and exc_info is not None:
            logger.error(formatted_message, exc_info=exc_info)
            if self.sentry_dsn:
                sentry_sdk.capture_exception(exc_info)
        else:
            getattr(logger, level)(formatted_message)

    # Removed the expression identified as useless (B018) since it wasn't provided in the initial code snippet.
    # Please review your original code for the specific expression mentioned by B018 and either assign it to a variable or remove it.

    def add_breadcrumb(
        self, category: Enum, message: str, level: str = "info", gas: float | None = None
    ):
        breadcrumb_category = category.name.lower()
        breadcrumb_data = {"message": message, "category": breadcrumb_category}
        if gas is not None:
            breadcrumb_data["gas"] = gas

        sentry_sdk.add_breadcrumb(
            category=breadcrumb_category, message=message, level=level, data=breadcrumb_data
        )

    def capture_exception(
        self, exception: Exception, message: str = "Exception captured", category: str = "crawler"
    ):
        self._validate_category(category)
        sentry_sdk.set_tag("category", category)
        sentry_sdk.capture_exception(exception)
        self.log("error", message, exc_info=exception, category=category)
