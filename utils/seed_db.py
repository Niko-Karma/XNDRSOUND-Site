from app import app
from models import db, MediaItem

def seed_data():
    with app.app_context():
        # Check if data exists
        if MediaItem.query.first():
            print("Database already has data. Skipping seed.")
            return

        print("Seeding database with placeholder data...")
        
        items = [
            MediaItem(
                instagram_id="mock_1",
                media_type="IMAGE",
                media_url="https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?auto=format&fit=crop&w=800&q=80",
                permalink="https://instagram.com",
                caption="Studio Vibes \U0001f399\ufe0f"
            ),
            MediaItem(
                instagram_id="mock_2",
                media_type="IMAGE",
                media_url="https://images.unsplash.com/photo-1493225255756-d9584f8606e9?auto=format&fit=crop&w=800&q=80",
                permalink="https://instagram.com",
                caption="New Gear Alert"
            ),
             MediaItem(
                instagram_id="mock_3",
                media_type="VIDEO",
                media_url="https://images.unsplash.com/photo-1470225620780-dba8ba36b745?auto=format&fit=crop&w=800&q=80",
                permalink="https://instagram.com",
                caption="Snippet from the latest track \U0001f525"
            ),
             MediaItem(
                instagram_id="mock_4",
                media_type="IMAGE",
                media_url="https://images.unsplash.com/photo-1514525253440-b393452e8d26?auto=format&fit=crop&w=800&q=80",
                permalink="https://instagram.com",
                caption="Late night mixing"
            ),
        ]

        db.session.add_all(items)
        db.session.commit()
        print(f"Added {len(items)} mock items.")

if __name__ == "__main__":
    seed_data()
