import logging


def should_abort_request(req):

    # if req.resource_type != "image":
    #     logging.log(logging.INFO, f"Ignoring Image {req.url}")
    #     return True
    if req.method.lower() == 'post':
        logging.log(logging.INFO, f"Ignoring {req.method} {req.url} ")
        return True
    return False

def should_abort_nonrelated_request(request):
    # Abort requests to .js and .ttf files
    # if (request.url.endswith('.ttf') or request.url.endswith('.css') or request.url.endswith('.svg') or
    #         request.url.endswith('.gif') or request.url.endswith('.pdf')):
    #     return True
    #
    # if (request.resource_type == 'font' or request.resource_type == 'stylesheet' or
    #         request.resource_type == 'video' or request.resource_type == 'audio'):
    #     return True

    if (request.url.endswith('.svg') or
            request.url.endswith('.gif') or request.url.endswith('.pdf')):
        return True

    if request.resource_type == 'video' or request.resource_type == 'audio':
        return True

    # if '/js/' in request.url:
    #     return True
    # Continue with other requests
    return False
