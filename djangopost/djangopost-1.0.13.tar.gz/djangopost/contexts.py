from djangopost.models import CategoryModel


def CategoryUniversalContext(request):
    djangopost_category = CategoryModel.objects.filter_publish()
    return {"djangopost_category": djangopost_category}
