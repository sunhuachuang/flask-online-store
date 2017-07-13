def register_processors(app):
    @app.context_processor
    def utility_processor():
        def zip(list1, list2):
            return list(zip(list1, list2))
        return dict(zip=zip)


def register_filters(app):
    @app.template_filter('reverse')
    def reverse_filter(s):
        return s[::-1]
