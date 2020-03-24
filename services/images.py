import requests

USER_AGENT = 'Create Flask Api 1.0'

def get_reddit_images(subreddit):
    response = requests.get("https://reddit.com/r/{}.json".format(subreddit),
                            headers={'User-agent': USER_AGENT}).json()
    if 'error' in response:
        return []
    posts = response["data"]["children"]
    posts_with_image = [p["data"] for p in posts
                        if p["data"].get("post_hint") == "image"]
    return [{
        'url': p['url'],
        'title': p['title'],
        'source': "https://reddit.com{}".format(p['permalink']),
        'author': {
            'name': 'Reddit',
            'description': subreddit,
            'profile_pic': '',
            'link': "https://reddit.com/r/{}".format(subreddit),
        }
    } for p in posts_with_image if p and not p['over_18']]

def format_unsplash_image(p):
    return {
        'url': p['urls']['raw'],
        'title': p['description'] or p['alt_description'],
        'source': p['links']['html'],
        'author': {
            'name': p['user']['name'],
            'description': p['user']['bio'],
            'profile_pic': p['user']['profile_image'].get('medium'),
            'link': p['user']['links']['html'],
        }
    }

def get_unsplash_collection(collection_id=3330448, page=1):
    endpoint_url = 'https://unsplash.com/napi/collections/{}/photos'.format(
        collection_id
    )
    photos = requests.get(endpoint_url, {'page': page},
                          headers={'User-agent': USER_AGENT}).json()

    return [format_unsplash_image(p) for p in photos if p]

def search_unsplash(search_term, page=1):
    response = requests.get('https://unsplash.com/napi/search/photos', {
        'query': search_term,
        'per_page': 25,
        'page': page,
    }, headers={'User-agent': USER_AGENT})
    results = response.json().get('results', [])
    return [format_unsplash_image(p) for p in results]
