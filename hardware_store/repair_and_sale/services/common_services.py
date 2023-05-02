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
