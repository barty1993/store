from django.db import connection, reset_queries
import time
import functools


def query_debugger(func):
    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        reset_queries()

        start_queries = len(connection.queries)

        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        end_queries = len(connection.queries)

        print(f"Function : {func.__name__}")
        print(f"Number of Queries : {end_queries - start_queries}")
        print(f"Finished in : {(end - start):.2f}s")
        return result

    return inner_func


def select_related_decorator(func):
    def select_related_wrapper(objects, **kwargs):
        param = kwargs.get('select_related')
        if param is None:
            return func(objects, **kwargs)
        return func(objects).select_related(*param)

    return select_related_wrapper


def prefetch_related_decorator(func):
    def prefetch_related_wrapper(objects, **kwargs):
        param = kwargs.get('prefetch_related')
        if param is None:
            return func(objects, **kwargs)
        return func(objects).prefetch_related(*param)

    return prefetch_related_wrapper


@prefetch_related_decorator
@select_related_decorator
def all_objects(objects, **kwargs):
    return objects.all()
