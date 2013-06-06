api_table = {
    'auth_user': {
        'url': '/api/auth_user',
        'method': 'GET',
    },
    'author_list': {
        'url': '/author/list/{{id}}.xml',
        'method': 'GET',
    },
    'author_show': {
        'url': '/author/show/{{id}}.xml',
        'method': 'GET',
    },
    'book_isbn_to_id': {
        'url': '/book/isbn_to_id/{{id}}?key={{key}}',
        'method': 'GET',
    },
    'book_review_counts': {
        'url': '/book/review_counts.json?isbns={{isbns}}',
        'method': 'GET',
    },
    'book_show': {
        'url': '/book/show/{{id}}?format=xml',
        'method': 'GET',
    },
    'book_isbn': {
        'url': '/book/isbn?isbn={{isbn}}&format=xml&key={{key}}&user_id={{user_id}}&rating={{rating}}',
        'method': 'GET',
    },
    'book_title': {
        'url': '/book/title.xml?author={{author}}&key={{key}}&title={{title}}&format=xml&rating={{rating}}',
        'method': 'GET',
    },
    'owned_books': {
        'url': '/owned_books/user?format=xml&id={{id}}',
        'method': 'GET',
    },
    'owned_books_show': {
        'url': '/owned_books/show.xml?id={{id}}',
        'method': 'GET',
    },
    'review_list': {
        'url': '/review/list/{{id}}.xml?key={{key}}&v=2&shelf={{shelf}}&sort={{sort}}&search={{search}}&order={{order}}&page={{page}}&per_page={{per_page}}',
        'method': 'GET',
    },
    'review_recent_reviews': {
        'url': '/review/recent_reviews.xml?key={{key}}',
        'method': 'GET',
    },
    'review_show_by_user_and_book': {
        'url': '/review/show_by_user_and_book.xml?book_id={{book_id}}&key={{key}}&user_id={{user_id}}&include_review_on_work={{include_review_on_work}}',
        'method': 'GET',
    },
    'author_url': {
        'url': '/api/author_url/{{id}}?key={{key}}',
        'method': 'GET',
    },
    'search': {
        'url': '/search.xml?key={{key}}&q={{q}}',
        'method': 'GET',
    },
    'shelf_list': {
        'url': '/shelf/list.xml?key={{key}}&user_id={{user_id}}&page={{page}}',
        'method': 'GET',
    },
}
