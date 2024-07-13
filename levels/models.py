from django.db import models
# from levels.models import Level


class Level(models.Model):
    # game_id = models.ForeignKey(Level, on_delete=models.CASCADE, default=1)
    video_name = models.CharField(max_length= 20)
    video_description = models.TextField()
    level_number = models.PositiveSmallIntegerField()
    level_scores = models.PositiveSmallIntegerField()

    def __self__(self):
        return f"{self.level_number}"

# Create your models here.
