from typing import Any


class StackOverflowError(Exception):
    """Raises then trying to push over max size to the stack."""
    def __init__(self):
        super().__init__('Can\'t push more elements to the '
                         'stack - maximum size is reached.')


class StackEmptyError(Exception):
    """Raises then trying to get or pop element from the empty stack."""
    def __init__(self):
        super().__init__('Can\'t get or pop element - the stack is empty.')


class Stack(object):
    def __init__(self, size=float('inf')) -> None:
        """
        Init stack.
        :param size: int maximum size of the stack (default: infinite)
        """
        self.__stack = []
        self.__max_size = size

    def push(self, element: Any) -> None:
        """
        Push element to the top.
        :param element: Any new element
        :return: None
        """
        if self.size() > self.__max_size:
            raise StackOverflowError()
        self.__stack.append(element)

    def pop(self) -> None:
        """
        Pop the top element.
        :return: None
        """
        if self.is_empty():
            raise StackEmptyError()
        self.__stack.pop()

    @property
    def top(self) -> Any:
        """
        Get the top element.
        :return: Any
        """
        if self.is_empty():
            raise StackEmptyError()
        return self.__stack[-1]

    @property
    def empty(self) -> bool:
        """
        Check if the stack is currently empty.
        :return: bool
        """
        return not len(self.__stack)

    @property
    def size(self) -> int:
        """
        Get current size of the stack.
        :return: int
        """
        return len(self.__stack)
