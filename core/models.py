from django.db import models

# Create your models here.

class ValentineVideo(models.Model):
    """
    Model to store the Valentine's Day video.
    You can upload the video via the Django Admin panel.
    """
    title = models.CharField(max_length=100, default="My Valentine Gift")
    
    # REVERTED: Back to standard FileField
    video_file = models.FileField(upload_to='videos/')
    
    is_active = models.BooleanField(default=True, help_text="Only one video should be active at a time.")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title