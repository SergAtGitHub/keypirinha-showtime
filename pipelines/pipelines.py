from typing import Callable, Any
from .on_start import pipeline as start
from .on_suggest import pipeline as suggest


def on_start(plugin):
    run_methods(start.pipeline, plugin)


def on_suggest(args):
    run_methods(suggest.pipeline, args)


def run_methods(pipeline, context):
    for processor in pipeline():
        if context.get('aborted'):
            break
        else:
            processor(context)
