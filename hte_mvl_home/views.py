from django.core.urlresolvers import reverse
from django.shortcuts import render


def scope(request):
    """ Display the last HOMEPAGE_NB_LAST_TEMPLATES templates.
    Args:
        request:

    Returns:

    """
    return render(request, "hte_mvl_home/scope.html")


def tiles(request):
    """

    :param request:
    :return:
    """
    from django.conf import settings
    installed_apps = settings.INSTALLED_APPS

    context = {
        "tiles": []
    }

    if "core_explore_example_app" in installed_apps:
        explore_tile = {
            "logo": "fa-search",
            "link":  reverse("core_explore_example_index"),
            "title": "Explore the repository and registry",
            "text": "Click here to search for high-throughput experimental data and resources in the repository using "
                    "flexible queries."
        }

        context["tiles"].append(explore_tile)

    if "core_curate_app" in installed_apps:
        curate_tile = {
            "logo": "fa-edit",
            "link": reverse("core_curate_index"),
            "title": "Contribute your data and resources",
            "text": "Click here to select a form template and then fill out the corresponding form."
        }

        context["tiles"].append(curate_tile)

    return render(request, "hte_mvl_home/tiles.html", context)
