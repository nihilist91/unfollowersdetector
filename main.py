from flask import Flask, render_template, request
import requests
import requests_cache
app = Flask(__name__)


# Enable requests caching with a time-based expiration of 60 seconds
requests_cache.install_cache('github_api_cache', expire_after=60)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        followers = get_followers(username)
        following = get_following(username)
        unfollowers = get_unfollowers(followers, following)
        return render_template('result.html', username=username, unfollowers=unfollowers)
    return render_template('index.html')

def get_followers(username):
    response = requests.get(f'https://api.github.com/users/{username}/followers')
    followers = [follower['login'] for follower in response.json()]
    return followers

def get_following(username):
    response = requests.get(f'https://api.github.com/users/{username}/following')
    following = [user['login'] for user in response.json()]
    return following

def get_unfollowers(followers, following):
    unfollowers = []
    for user in following:
        if user not in followers:
            response = requests.get(f'https://api.github.com/users/{user}')
            if response.status_code == 200:
                user_info = response.json()
                unfollower = {
                    'login': user_info['login'],
                    'avatar_url': user_info['avatar_url']
                }
                unfollowers.append(unfollower)
    return unfollowers

if __name__ == '__main__':
    app.run(debug=True)
