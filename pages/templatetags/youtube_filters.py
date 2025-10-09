import re
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def youtube_embed(content):
    """
    Find YouTube URLs in content and convert them to embed codes
    """
    # Regex to find YouTube URLs in various formats
    youtube_regex = r'(https?://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})(?:&\S+)?)'
    
    def replace_youtube_url(match):
        url = match.group(1)
        video_id = match.group(2)
        
        embed_html = f'''
        <div class="youtube-embed-container">
            <div class="youtube-embed">
                <iframe 
                    src="https://www.youtube.com/embed/{video_id}" 
                    frameborder="0" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                    allowfullscreen
                    loading="lazy">
                </iframe>
            </div>
        </div>
        '''
        return embed_html
    
    # Replace YouTube URLs with embed codes
    content = re.sub(youtube_regex, replace_youtube_url, content)
    return mark_safe(content)