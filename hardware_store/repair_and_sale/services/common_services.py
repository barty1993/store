def select_related_decorator(func):
    def select_related_wrapper(*args, **kwargs):
        param = kwargs.get('select_related')
        if param is None:
            return func(*args, **kwargs)
        return func(*args).select_related(*param)

    return select_related_wrapper


def prefetch_related_decorator(func):
    def prefetch_related_wrapper(*args, **kwargs):
        param = kwargs.get('prefetch_related')
        if param is None:
            return func(*args, **kwargs)
        return func(*args).prefetch_related(*param)

    return prefetch_related_wrapper


@prefetch_related_decorator
@select_related_decorator
def all_objects(objects, **kwargs):
    return objects.all()


@prefetch_related_decorator
@select_related_decorator
def repairs_filter_by_id(objects, category_id: int, **kwargs):
    return objects.filter(category_id=category_id)
