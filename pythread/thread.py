#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

######  #######
#     #    #     #    #  #####   ######    ##    #####
#     #    #     #    #  #    #  #        #  #   #    #
######     #     ######  #    #  #####   #    #  #    #
#          #     #    #  #####   #       ######  #    #
#          #     #    #  #   #   #       #    #  #    #
#          #     #    #  #    #  ######  #    #  #####

"""

from threading import Thread, Timer


class PThread(Thread):
    """
    A class that represents a thread of control.
    This class subclassed Thread class :
        class Thread(builtins.object)

    We specify the activity by passing a callable object to the constructor.

    Why:
        - clean the main code
        - dedicate import Thread
        - simplify multithreading use with generic objectives

    Why we will never use it:
        - all the code use multithreading
        - we use complex mecanisme between object: sync between object or
          data issue

        +----------+
        |          |   define with func & elapse
      -->   INIT   +-------------------+----------------------+
        |          |                   |                      |
        +----------+                   |                      |
                                       |                      |
             +----------------------------------------------+ |
             |                         |                    | |
             |               +-----------------------------------------+
             |               | RUN     |                    | |        |
        +----v-----+         |    +----v-----+          +---+-v---+    |
        |          |         |    |          |          |         |    |
      -->  START   +-------------->   TASK   +---------->  TIMER  |    |
        |          |         |    |          |          |         |    |
        +----------+         |    +----^-----+          +----^----+    |
                             |         |                     |         |
                             +-----------------------------------------+
                                       |                     |
        +----------+     disable       |                     |
        |          +-------------------+         cancel      |
      -->   STOP   +-----------------------------------------+
        |          +--------------------+
        +----------+                    |
                                  +-----v-----+
                                  |           |
                                  |JOIN Thread|
                                  |           |
                                  +-----------+

    Use:
        >>> # Import the module :
        >>> from pythread import PThread
        >>> import time
        >>> # define a task
        >>> def mytask(): print("lorem ipsum dolor sit amet consectetur")
        >>> # We want to run "mytask" in a thread and repeat the task:
        >>> mthr = PThread(mytask, 0.1)
        >>> mthr.start() ; print("other task");time.sleep(0.3) ; mthr.stop()
        lorem ipsum dolor sit amet consectetur
        other task
        lorem ipsum dolor sit amet consectetur
        lorem ipsum dolor sit amet consectetur
        >>> # We want to run "mytask" in a thread one time:
        >>> mthr = PThread(mytask).start() ; print("other task")
        lorem ipsum dolor sit amet consectetur
        other task
        >>> # oups - start issue:
        >>> mthr = PThread(mytask, 0.1)
        >>> mthr.start() ; mthr.start()
        Traceback (most recent call last):
        ...
        RuntimeError: threads can only be started once
        >>> # Stop a not repeatable task:
        >>> mthr = PThread(mytask)
        >>> mthr.start() ; print("other task")
        lorem ipsum dolor sit amet consectetur
        other task
        >>> mthr.stop()
        >>> # a test avoid the AttributeError exception

    """
    def __init__(self, func, elapse=0):
        Thread.__init__(self)

        self.__repeat = True
        if elapse is 0:
            self.__repeat = False

        self.__running = True
        self.__timer = None
        self.__func = func
        self.__elapse = elapse
        self.setDaemon(True)

    @property
    def func(self):
        """
        Returns the callable object defined by Thread constructor.

        Args:
            None.

        Returns:
            callable object
        """
        return self.__func

    def start(self):
        """
        Start the thread's activity.

        It must be called at most once per thread object. It arranges for the
        object's run() method to be invoked in a separate thread of control.

        This method will raise a RuntimeError if called more than once on the
        same thread object.

        Args:
            None.

        Return:
            None.
        """
        super().start()

    def run(self):
        """
        Method (override) representing the thread's activity.
        This method will raise a RuntimeError if called more than once on the
        same thread object.

        Args:
            None.

        Returns:
            None.
        """
        if not self._initialized:
            raise RuntimeError("thread.__init__() not called")

        self.__func()

        if self.__running and self.__repeat:
            self.__timer = Timer(self.__elapse, self.run)
            self.__timer.start()

    def stop(self):
        """
        Wait until the thread terminates.
        This blocks the calling thread until the thread whose join() method is
        called terminates -- either normally or through an unhandled exception.

        Args:
            None.

        Returns:
            None.
        """
        self.__running = False
        if self.__timer is not None:
            self.__timer.cancel()
        self.join()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
