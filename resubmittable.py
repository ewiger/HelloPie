#!/usr/bin/env python
# stdlib imports
import sys
import time
import gc3libs
import mylog


mylog.setup_logging('console')
# gc3libs.configure_logger(logging.DEBUG, "gdemo")


class CommandApp(gc3libs.Application):

    def __init__(self, args):
        assert type(args) == list
        if args[0].startswith
        gc3libs.Application.__init__(
            self,
            # the following arguments are mandatory:
            arguments=args,
            inputs=[],
            outputs=[],
            output_dir=self.__class__.__name__,
            # the rest is optional and has reasonable defaults:
            stdout="stdout.txt",)

# Create an instance of GdemoSimpleApp
app = GdemoSimpleApp()

engine = gc3libs.create_engine()
engine.add(app)

# in case you want to select a specific resource, call
# `Engine.select_resource(<resource_name>)`
if len(sys.argv)>1:
    engine.select_resource(sys.argv[1])

# Periodically check the status of your application.
while app.execution.state != gc3libs.Run.State.TERMINATED:
    print "Job in status %s " % app.execution.state
    # `Engine.progress()` will do the GC3Pie magic:
    # submit new jobs, update status of submitted jobs, get
    # results of terminating jobs etc...
    engine.progress()

    # Wait a few seconds...
    time.sleep(1)

print "Job is now terminated."
print "The output of the application is in `%s`." %  app.output_dir
