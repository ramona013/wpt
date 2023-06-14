# Return a 404 error, but with an ORB-compatible MIME type.
# (Otherwise, ORB may block the error response.)
def main(request, response):
  return 404, [(b'Content-Type', b'image/png')], b'Page not found'

