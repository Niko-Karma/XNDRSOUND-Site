document.addEventListener('DOMContentLoaded', () => {
    console.log('XNDRSOUND Gallery Loaded');
    fetchMedia();
});

async function fetchMedia() {
    try {
        const response = await fetch('/api/gallery');
        const mediaItems = await response.json();
        renderGallery(mediaItems);
    } catch (error) {
        console.error('Error fetching media:', error);
        document.getElementById('gallery-grid').innerHTML = '<p>Error loading media.</p>';
    }
}

function renderGallery(items) {
    const grid = document.getElementById('gallery-grid');
    grid.innerHTML = ''; // Clear placeholders

    if (items.length === 0) {
        grid.innerHTML = '<p style="text-align:center; width:100%; color:#666;">No media found.</p>';
        return;
    }

    items.forEach(item => {
        const div = document.createElement('div');
        div.className = 'gallery-item';

        // Handle Video vs Image
        let mediaContent = '';
        if (item.type === 'VIDEO') {
            mediaContent = `
                <video src="${item.url}" muted loop playsinline onmouseover="this.play()" onmouseout="this.pause()"></video>
                <div class="gallery-overlay">
                    <i class="fas fa-play play-icon"></i>
                </div>
            `;
        } else {
            mediaContent = `<img src="${item.url}" alt="${item.caption || 'Instagram Post'}">`;
        }

        div.innerHTML = mediaContent;

        // Add click listener (opens permalink)
        div.addEventListener('click', () => {
            if (item.permalink) window.open(item.permalink, '_blank');
        });

        grid.appendChild(div);
    });
}
