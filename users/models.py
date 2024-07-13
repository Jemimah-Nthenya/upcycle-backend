from django.db import models
# from users.models import Users

class Users(models.Model):
    email = models.EmailField()
    user_name = models.CharField(max_length= 40)
    password = models.CharField(max_length= 20)
    # game_id = models.ForeignKey(Users, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.full_name} {self.email}"



