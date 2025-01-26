# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate
from config import Config
from models import db, Link

import re
import urllib.request

def get_youtube_info(url):
    try:
        html = urllib.request.urlopen(url).read().decode('utf-8', errors='ignore')
    except HTTPError:
        return None, None
    
    # Extract title from meta tags
    title_match = re.search(
        r'<meta[^>]+property="og:title"[^>]+content="([^"]+)"',
        html
    )
    title = title_match.group(1) if title_match else None
    
    # Extract thumbnail from meta tags
    thumb_match = re.search(
        r'<meta[^>]+property="og:image"[^>]+content="([^"]+)"',
        html
    )
    thumbnail = thumb_match.group(1) if thumb_match else None
    
    return title, thumbnail

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate = Migrate(app, db)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        # CREATE
        if request.method == 'POST':
            url = request.form.get('url')
            tags = request.form.get('tags')

            video_title, thumbnail_url = get_youtube_info(url)
            if video_title and thumbnail_url:
                new_link = Link(url=url, tags=tags, thumbnail=thumbnail_url, title=video_title)
                db.session.add(new_link)
                db.session.commit()
                return redirect(url_for('index'))

        # READ (list all) with search
        search_query = request.args.get('q', '')
        if search_query:
            links = Link.query.filter(
                db.or_(
                    Link.url.ilike(f'%{search_query}%'),
                    Link.tags.ilike(f'%{search_query}%')
                )
            ).all()
        else:
            links = Link.query.all()
            
        return render_template('index.html', links=links)

    @app.route('/delete/<int:link_id>', methods=['GET'])
    def delete_link(link_id):
        # DELETE
        link_to_delete = Link.query.get_or_404(link_id)
        db.session.delete(link_to_delete)
        db.session.commit()
        return redirect(url_for('index'))

    @app.route('/update/<int:link_id>', methods=['POST'])
    def update_link(link_id):
        # UPDATE
        link_to_update = Link.query.get_or_404(link_id)
        url = request.form.get('url')
        tags = request.form.get('tags')
        if url:
            link_to_update.url = url
            link_to_update.tags = tags
            db.session.commit()
        return redirect(url_for('index'))

    return app

# For direct "python app.py" usage:
if __name__ == "__main__":
    flask_app = create_app()
    flask_app.run(debug=True)
