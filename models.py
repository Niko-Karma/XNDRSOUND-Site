from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class MediaItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    instagram_id = db.Column(db.String(50), unique=True, nullable=False)
    media_type = db.Column(db.String(20), nullable=False) # IMAGE, CAROUSEL_ALBUM, VIDEO
    media_url = db.Column(db.String(500), nullable=False) # The CDN link
    local_path = db.Column(db.String(200), nullable=True) # Path to saved file
    permalink = db.Column(db.String(200), nullable=False)
    caption = db.Column(db.Text, nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {
            'id': self.id,
            'url': self.local_path if self.local_path else self.media_url,
            'type': self.media_type,
            'caption': self.caption,
            'permalink': self.permalink
        }
