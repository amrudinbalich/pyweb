def view(name):
    with open(f'resources/views/{name}.html') as f:
        return f.read().encode('utf-8')