#!/usr/bin/env python
# stdlib imports
import sys
import time
import mylog
import logging
import gc3libs
from gc3libs.workflow import StopOnError


logger = logging.getLogger(__name__)
mylog.setup_logging('console')
# gc3libs.configure_logger(logging.DEBUG, "gdemo")


class CommandApp(gc3libs.Application, StopOnError):

    def __init__(self, args):
        if isinstance(args, basestring):
            args = [args]
        assert type(args) == list
        # No full path, then assume it's a bash command
        if not args[0].startswith('/'):
            args = ['/bin/bash'] + args
        gc3libs.Application.__init__(
            self,
            # the following arguments are mandatory:
            arguments=args,
            inputs=[],
            outputs=[],
            output_dir=self.__class__.__name__,
            # the rest is optional and has reasonable defaults:
            stdout="stdout.txt",)

    def terminated(self):
        logger.info('program was terminated')
        print self.execution.state
        print self.execution.returncode
        self.execution.returncode = 1


app = CommandApp('/bin/hostname')
engine = gc3libs.create_engine()
engine.add(app)

if len(sys.argv) > 1:
    engine.select_resource(sys.argv[1])


while app.execution.state != gc3libs.Run.State.TERMINATED:
    print "Job in status %s " % app.execution.state
    engine.progress()
    time.sleep(1)

print("Job is now terminated.")
print("The output of the application is in `%s`." % app.output_dir)
