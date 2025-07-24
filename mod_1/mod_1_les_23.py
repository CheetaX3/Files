def get_absolute_url(url, *args, **kwargs):
    path = '/'.join(args)
    query = '&'.join(f'{k}={v}' for k, v in kwargs.items())
    return url + ('/' if path else '') + path + ('?' if query else '') + query

print(get_absolute_url('www.yandex.ru'))
print(get_absolute_url('www.google.com', 'images', id='24', category='auto', color='red', size='small'))